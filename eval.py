"""
eval.py — run the 20-question eval set through the RAG and score it.

Scores three binaries per question:
  cited_correct   at least one expected_sources entry appears among the citations the model used
                  (negatives: true when no citation is used, i.e. the model did not cite anything)
  grounded        every must_contain term appears in the answer (or must_contain_min of must_contain_any);
                  negatives: the answer begins with the refusal string
  refusal_correct negatives only: answer begins with "Not found in corpus."

Usage:
  python eval.py                         # full run, k from .env
  python eval.py --k 8 --no-id-boost     # variant run
  python eval.py --ids 1,13,16           # subset
  python eval.py --label "chunk400"      # tag the results file

Writes:
  results/eval_<label>_<timestamp>.json   full transcript (question, answer, passages, scores)
  results/eval_<label>_<timestamp>.md     README-ready table
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv

from prompts import REFUSAL
from query import Store, answer_question, TOP_K

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

load_dotenv()
ROOT = Path(__file__).resolve().parent
RESULTS = ROOT / "results"
RESULTS.mkdir(exist_ok=True)


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip().lower()


def contains(answer: str, term: str) -> bool:
    return norm(term) in norm(answer)


def source_matches(expected: str, cite: str) -> bool:
    """Loose match: every alnum token of the expected source appears in the citation.
    'NIST SP 800-37 r2' matches '[NIST SP 800-37 r2, pp. 8-9 (doctrine)]';
    'F/A-13 Peacemaker FMA-C Report §5.2' matches a cite from §5.2 but not §5.4."""
    e_tokens = [t for t in re.findall(r"[a-z0-9§.\-/]+", expected.lower()) if t not in {"the", "of", "—", "-"}]
    c = cite.lower()
    return all(t in c for t in e_tokens)


def score(q: dict, res: dict) -> dict:
    answer = res["answer"]
    head = answer.strip().lstrip("*#_ ").lower()
    refused = head.startswith(REFUSAL.lower().rstrip("."))
    partial = (not refused) and bool(re.search(r"not found in corpus", answer, re.I))  # answered some, declared the rest not found
    cited = res["cited"]

    if q["should_refuse"]:
        refusal_correct = refused
        grounded = refused                      # a refusal makes no claims
        cited_correct = len(cited) == 0 or refused
    else:
        refusal_correct = None
        if q.get("must_contain"):
            missing = [t for t in q["must_contain"] if not contains(answer, t)]
            grounded = not missing and not refused and not partial
        else:
            hits = [t for t in q.get("must_contain_any", []) if contains(answer, t)]
            grounded = len(hits) >= q.get("must_contain_min", 1) and not refused and not partial
        cited_correct = any(source_matches(e, c) for e in q["expected_sources"] for c in cited)

    return {
        "cited_correct": bool(cited_correct),
        "grounded": bool(grounded),
        "refusal_correct": refusal_correct,
        "refused": refused,
        "partial": partial,
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--k", type=int, default=TOP_K)
    ap.add_argument("--no-id-boost", action="store_true")
    ap.add_argument("--no-bm25", action="store_true")
    ap.add_argument("--ids", type=str, default="", help="comma-separated question ids")
    ap.add_argument("--label", type=str, default="baseline")
    ap.add_argument("--questions", type=str, default="eval_questions.json")
    ap.add_argument("--rescore", type=str, default="", help="re-grade a saved results JSON (no API calls)")
    args = ap.parse_args()

    questions = json.loads((ROOT / args.questions).read_text(encoding="utf-8"))
    if args.ids:
        want = {int(x) for x in args.ids.split(",")}
        questions = [q for q in questions if q["id"] in want]

    saved = None
    if args.rescore:
        saved = json.loads(Path(args.rescore).read_text(encoding="utf-8"))
        by_id = {r["id"]: r for r in saved["rows"]}
        questions = [q for q in questions if q["id"] in by_id]
        args.k = saved["meta"]["k"]
        id_boost = saved["meta"]["id_boost"]
        bm25 = saved["meta"].get("bm25", False)
        backend = saved["meta"]["backend"]
        args.label = saved["meta"]["label"] + "_rescored"
    else:
        store = Store()
        id_boost = not args.no_id_boost
        bm25 = not args.no_bm25
        backend = store.backend()
    print(f"Eval: {len(questions)} questions | k={args.k} | id_boost={id_boost} | bm25={bm25} | backend={backend} | model={os.getenv('ANTHROPIC_MODEL')}\n")

    rows = []
    t0 = time.time()
    for q in questions:
        if saved:
            r0 = by_id[q["id"]]
            res = {"answer": r0["answer"], "cited": r0["cited"],
                   "passages": [{"cite": c} for c in r0["retrieved"]]}
        else:
            res = answer_question(q["question"], store, k=args.k, id_boost=id_boost, bm25=bm25)
        s = score(q, res)
        rows.append({**q, **s, "answer": res["answer"], "cited": res["cited"],
                     "retrieved": [p["cite"] for p in res["passages"]]})
        flag = "✓" if (s["grounded"] and s["cited_correct"]) or (q["should_refuse"] and s["refusal_correct"]) else "✗"
        print(f"{flag} Q{q['id']:>2} [{q['type']}] cited={int(s['cited_correct'])} grounded={int(s['grounded'])}"
              + (f" refusal={int(s['refusal_correct'])}" if q["should_refuse"] else ""))
        if flag == "✗":
            tag = "PARTIAL " if s["partial"] else ""
            print("     " + tag + res["answer"][:220].replace("\n", " ") + ("…" if len(res["answer"]) > 220 else ""))

    pos = [r for r in rows if not r["should_refuse"]]
    neg = [r for r in rows if r["should_refuse"]]
    cited_n = sum(r["cited_correct"] for r in pos)
    grounded_n = sum(r["grounded"] for r in pos)
    refusal_n = sum(bool(r["refusal_correct"]) for r in neg)
    false_refusals = [r["id"] for r in pos if r["refused"]]
    partials = [r["id"] for r in pos if r["partial"]]

    print(f"\nCited correct : {cited_n}/{len(pos)}")
    print(f"Grounded      : {grounded_n}/{len(pos)}")
    print(f"Refusal correct: {refusal_n}/{len(neg)}")
    if false_refusals:
        print(f"False refusals (positives answered 'Not found'): Q{', Q'.join(map(str, false_refusals))}")
    if partials:
        print(f"Partial answers (part declared not found): Q{', Q'.join(map(str, partials))}")
    print(f"Elapsed: {time.time() - t0:.0f}s")

    stamp = datetime.now().strftime("%Y%m%d_%H%M")
    out = RESULTS / f"eval_{args.label}_{stamp}"
    meta = {"label": args.label, "k": args.k, "id_boost": id_boost, "bm25": bm25, "model": os.getenv("ANTHROPIC_MODEL"),
            "chunk_tokens": os.getenv("CHUNK_TOKENS", "800"), "backend": backend, "timestamp": stamp,
            "cited_correct": f"{cited_n}/{len(pos)}", "grounded": f"{grounded_n}/{len(pos)}",
            "refusal_correct": f"{refusal_n}/{len(neg)}"}
    out.with_suffix(".json").write_text(json.dumps({"meta": meta, "rows": rows}, indent=1, ensure_ascii=False), encoding="utf-8")

    md = [f"## Eval run: {args.label} ({stamp})", "",
          f"k={args.k}, id_boost={id_boost}, bm25={bm25}, chunk≈{meta['chunk_tokens']} tokens, model={meta['model']}", "",
          "| # | Type | Cited | Grounded | Refusal | Note |", "|---|---|---|---|---|---|"]
    for r in rows:
        note = ""
        if r["should_refuse"] and not r["refusal_correct"]:
            note = "answered instead of refusing"
        elif not r["should_refuse"] and r["refused"]:
            note = "false refusal"
        elif not r["should_refuse"] and r["partial"]:
            note = "partial — rest declared not found"
        elif not r["should_refuse"] and not r["grounded"]:
            note = "missing expected terms"
        elif not r["should_refuse"] and not r["cited_correct"]:
            note = "cited wrong source"
        md.append(f"| {r['id']} | {r['type']} | {'Y' if r['cited_correct'] else 'N'} | {'Y' if r['grounded'] else 'N'} | "
                  f"{'-' if r['refusal_correct'] is None else ('Y' if r['refusal_correct'] else 'N')} | {note} |")
    md += ["", f"**Cited correct {cited_n}/{len(pos)} · Grounded {grounded_n}/{len(pos)} · Refusal correct {refusal_n}/{len(neg)}**"]
    out.with_suffix(".md").write_text("\n".join(md), encoding="utf-8")
    print(f"\nWrote {out.with_suffix('.json').relative_to(ROOT)} and .md")


if __name__ == "__main__":
    main()
