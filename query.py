"""
query.py — ask a question against the local index and get a cited answer from Claude.

Usage:
  python query.py "What are the six steps of the Risk Management Framework?"
  python query.py --k 8 --show-context "How does FMA-C relate to RMF?"
  python query.py --no-llm "T1190"            # retrieval only, no API call
  python query.py --no-id-boost "..."         # pure dense retrieval (baseline comparison)

Retrieval = local MiniLM embeddings (chroma if present, else numpy cosine) + an optional
exact-match boost for identifiers in the question (R-05, T1190, CA19, SC-7, UL-3 …), because a
small embedding model does not reliably distinguish "T1190" from "T1195".
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

import numpy as np
from dotenv import load_dotenv

from prompts import SYSTEM_PROMPT, REFUSAL, build_user_message

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

load_dotenv()
ROOT = Path(__file__).resolve().parent
INDEX = ROOT / "data" / "index"
EMBED_MODEL = os.getenv("EMBED_MODEL", "all-MiniLM-L6-v2")
MODEL = os.getenv("ANTHROPIC_MODEL", "claude-sonnet-4-5")
TOP_K = int(os.getenv("TOP_K", "6"))

# Identifier patterns worth an exact-match boost
ID_PATTERNS = [
    r"\bT\d{4}(?:\.\d{3})?\b",            # ATT&CK technique
    r"\b[A-Z]{2}-\d{1,2}(?:\(\d+\))?\b",  # 800-53 control (AC-2, SC-7(5))
    r"\bR-0\d\b",                         # risk register
    r"\bCA-?\d{1,2}\b",                   # control action
    r"\bUL-\d\b", r"\bH\d\b", r"\bC-\d\b",  # FMA-C artifacts
    r"\bKT-C\s?\d{1,2}\b",
    r"\b(?:DoDD|DoDI)\s?\d{4}\.\d{2}\b",
    r"\b800-\d{2,3}\b",
]


# ----------------------------------------------------------------------------
# Index loading
# ----------------------------------------------------------------------------
class Store:
    """Loads chunks.jsonl (+ embeddings.npy). Uses chroma for ANN if the collection exists."""

    def __init__(self) -> None:
        jl = INDEX / "chunks.jsonl"
        if not jl.exists():
            sys.exit("No index found. Run: python ingest.py")
        self.chunks = [json.loads(l) for l in jl.read_text(encoding="utf-8").splitlines() if l.strip()]
        self.by_id = {c["id"]: c for c in self.chunks}
        self.vecs = np.load(INDEX / "embeddings.npy")
        self.col = None
        try:
            import chromadb
            client = chromadb.PersistentClient(path=str(INDEX / "chroma"))
            col = client.get_collection("mission_assurance")
            if col.count() == len(self.chunks):
                self.col = col
        except Exception:  # noqa: BLE001 — numpy fallback is fine
            self.col = None
        from sentence_transformers import SentenceTransformer
        self.model = SentenceTransformer(EMBED_MODEL)

    def backend(self) -> str:
        return "chroma" if self.col is not None else "numpy"

    def embed(self, question: str) -> np.ndarray:
        return self.model.encode([question], normalize_embeddings=True)[0].astype(np.float32)

    def dense(self, question: str, k: int, q: np.ndarray | None = None) -> list[tuple[str, float]]:
        q = self.embed(question) if q is None else q
        if self.col is not None:
            res = self.col.query(query_embeddings=[q.tolist()], n_results=k, include=["distances"])
            return [(i, 1.0 - d) for i, d in zip(res["ids"][0], res["distances"][0])]
        sims = self.vecs @ q
        top = np.argsort(-sims)[:k]
        return [(self.chunks[i]["id"], float(sims[i])) for i in top]

    def id_matches(self, question: str, limit: int, q: np.ndarray | None = None) -> list[str]:
        """Chunks containing identifiers from the question; ranked by (#ids matched, dense similarity)."""
        ids_in_q = set()
        for pat in ID_PATTERNS:
            ids_in_q.update(m.group(0).upper().replace(" ", "") for m in re.finditer(pat, question))
        if not ids_in_q:
            return []
        sims = self.vecs @ (self.embed(question) if q is None else q)
        hits = []
        for i, c in enumerate(self.chunks):
            hay = (c["text"] + " " + c["section"]).upper().replace(" ", "")
            n = sum(1 for t in ids_in_q if t in hay)
            if n:
                hits.append((n, float(sims[i]), c["id"]))
        hits.sort(key=lambda x: (-x[0], -x[1]))
        return [cid for _, _, cid in hits[:limit]]


def retrieve(store: Store, question: str, k: int = TOP_K, id_boost: bool = True) -> list[dict]:
    """Return top-k chunk dicts with a 'score' field. ID-matched chunks are pinned to the top (max k//2)."""
    q = store.embed(question)
    dense = store.dense(question, k * 2, q=q)
    order: list[str] = []
    if id_boost:
        for cid in store.id_matches(question, limit=max(1, k // 2), q=q):
            if cid not in order:
                order.append(cid)
    for cid, _ in dense:
        if cid not in order:
            order.append(cid)
        if len(order) >= k:
            break
    dscore = dict(dense)
    out = []
    for cid in order[:k]:
        c = dict(store.by_id[cid])
        c["score"] = round(dscore.get(cid, 0.0), 3)
        c["boosted"] = cid not in dscore
        out.append(c)
    return out


# ----------------------------------------------------------------------------
# Generation
# ----------------------------------------------------------------------------
def ask_claude(question: str, passages: list[dict]) -> str:
    import anthropic
    if not os.getenv("ANTHROPIC_API_KEY"):
        sys.exit("ANTHROPIC_API_KEY not set. Copy .env.example to .env and add your key.")
    client = anthropic.Anthropic()
    msg = client.messages.create(
        model=MODEL,
        max_tokens=900,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": build_user_message(question, passages)}],
    )
    return "".join(b.text for b in msg.content if getattr(b, "type", "") == "text").strip()


def answer_question(question: str, store: Store | None = None, k: int = TOP_K,
                    id_boost: bool = True, llm: bool = True) -> dict:
    store = store or Store()
    passages = retrieve(store, question, k=k, id_boost=id_boost)
    answer = ask_claude(question, passages) if llm else ""
    cited = [p["cite"] for p in passages if p["cite"] in answer]
    return {
        "question": question,
        "answer": answer,
        "refused": answer.startswith(REFUSAL),
        "passages": passages,
        "cited": cited,
        "model": MODEL,
        "backend": store.backend(),
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("question", nargs="+")
    ap.add_argument("--k", type=int, default=TOP_K)
    ap.add_argument("--show-context", action="store_true", help="print retrieved passages")
    ap.add_argument("--no-llm", action="store_true", help="retrieval only")
    ap.add_argument("--no-id-boost", action="store_true", help="pure dense retrieval")
    args = ap.parse_args()
    question = " ".join(args.question)

    store = Store()
    res = answer_question(question, store, k=args.k, id_boost=not args.no_id_boost, llm=not args.no_llm)

    print(f"\nQ: {question}\n[retrieval: {res['backend']}, k={args.k}, id_boost={not args.no_id_boost}]\n")
    if args.show_context or args.no_llm:
        for i, p in enumerate(res["passages"], 1):
            flag = " *id-match*" if p.get("boosted") else ""
            print(f"[{i}] score={p['score']}{flag} {p['cite']}")
            print("    " + p["text"][:300].replace("\n", " ") + ("…" if len(p["text"]) > 300 else ""))
        print()
    if not args.no_llm:
        print(res["answer"])
        print("\nSources:")
        seen = set()
        for p in res["passages"]:
            if p["cite"] in seen:
                continue
            seen.add(p["cite"])
            mark = "cited" if p["cite"] in res["cited"] else "retrieved"
            print(f"  - {p['cite']}  ({mark})")


if __name__ == "__main__":
    main()
