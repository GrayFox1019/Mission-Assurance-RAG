"""
ingest.py — build the local vector index for the Mission Assurance RAG.

Reads:
  data/raw/*.pdf            doctrine PDFs           -> ~800-token chunks, 100 overlap, page-tracked
  data/raw/enterprise-attack.json  ATT&CK STIX      -> one chunk per technique
  data/corpus/howto_guide.md       methodology      -> split on bold section lines
  data/corpus/peacemaker_report.md worked example   -> split on #/##/### headings
  data/corpus/fa13_datasheet.md    worked example   -> split on headings (or fixed windows)
  data/raw/*.xlsx                  worked example   -> one record per row (sheet + headers)

Writes:
  data/corpus/<workbook>.json      row records (committed; the structured corpus)
  data/index/chunks.jsonl          every chunk + metadata
  data/index/embeddings.npy        float32 matrix aligned with chunks.jsonl
  data/index/chroma/               chromadb collection "mission_assurance" (if chromadb works)

Usage:
  python ingest.py              # full build
  python ingest.py --dry-run    # parse + chunk + print counts, no embedding
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass, asdict, field
from pathlib import Path

import numpy as np
from dotenv import load_dotenv

# Windows consoles choke on em-dashes under cp1252; force UTF-8 output.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

load_dotenv()
ROOT = Path(__file__).resolve().parent
RAW = ROOT / "data" / "raw"
CORPUS = ROOT / "data" / "corpus"
INDEX = ROOT / "data" / "index"
INDEX.mkdir(parents=True, exist_ok=True)

EMBED_MODEL = os.getenv("EMBED_MODEL", "all-MiniLM-L6-v2")
# Chunk sizes are in approximate tokens; we window on whitespace words at ~0.75 words/token.
# No tokenizer download required (tiktoken fetches its BPE file from the internet on first use,
# which breaks the air-gapped deployment story).
CHUNK_TOKENS = int(os.getenv("CHUNK_TOKENS", "800"))
OVERLAP_TOKENS = int(os.getenv("OVERLAP_TOKENS", "100"))
WORDS_PER_TOKEN = 0.75
CHUNK_WORDS = int(CHUNK_TOKENS * WORDS_PER_TOKEN)
OVERLAP_WORDS = int(OVERLAP_TOKENS * WORDS_PER_TOKEN)

# Filename -> (citation name, source_type)
PDF_DOCS = {
    "dodd_3020.40.pdf": "DoDD 3020.40",
    "dodi_8510.01.pdf": "DoDI 8510.01",
    "nist_800-30r1.pdf": "NIST SP 800-30 r1",
    "nist_800-37r2.pdf": "NIST SP 800-37 r2",
    "nist_800-53r5.pdf": "NIST SP 800-53 r5",
    "nist_800-82r3.pdf": "NIST SP 800-82 r3",
    "stpa_handbook.pdf": "STPA Handbook",
}
MD_DOCS = {
    "howto_guide.md": ("FMA-C How-To Guide", "methodology", "bold"),
    "peacemaker_report.md": ("F/A-13 Peacemaker FMA-C Report", "worked_example", "hash"),
    "fa13_datasheet.md": ("F/A-13 Peacemaker Data Sheet", "worked_example", "hash"),
}
XLSX_DOCS = {  # substring of filename -> (citation name, json stem)
    "FMAC Tables": ("FMAC Tables for F/A-13", "fmac_tables"),
    "Risk Assessment": ("F/A-13 Risk Assessment", "risk_assessment"),
}
SKIP_SHEETS = ("instructions", "matrix", "key", "pert")


@dataclass
class Chunk:
    id: str
    text: str
    doc: str
    section: str
    source_type: str
    cite: str
    page_start: int = 0
    page_end: int = 0
    extra: dict = field(default_factory=dict)

    def meta(self) -> dict:
        m = {
            "doc": self.doc,
            "section": self.section,
            "source_type": self.source_type,
            "cite": self.cite,
            "page_start": int(self.page_start),
            "page_end": int(self.page_end),
        }
        for k, v in self.extra.items():  # chroma wants flat scalars
            if isinstance(v, (str, int, float, bool)):
                m[k] = v
        return m


def ntok(s: str) -> int:
    """Approximate token count."""
    return int(len(s.split()) / WORDS_PER_TOKEN)


def clean_md(text: str) -> str:
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", text)            # images
    text = re.sub(r"<img[^>]*>", "", text)
    text = re.sub(r"</?(p|div|span|br)[^>]*>", "", text)         # stray html
    text = re.sub(r"\\([<>#*_|])", r"\1", text)                  # pandoc escapes
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def window_tokens(text: str, size=CHUNK_WORDS, overlap=OVERLAP_WORDS) -> list[str]:
    """Fixed-size word windows with overlap (sizes in words)."""
    words = text.split()
    if len(words) <= size:
        return [text]
    out, start = [], 0
    while start < len(words):
        out.append(" ".join(words[start:start + size]))
        if start + size >= len(words):
            break
        start += size - overlap
    return out


# ----------------------------------------------------------------------------
# PDFs — doctrine
# ----------------------------------------------------------------------------
def read_pdfs() -> list[Chunk]:
    from pypdf import PdfReader

    chunks: list[Chunk] = []
    for fname, doc in PDF_DOCS.items():
        path = RAW / fname
        if not path.exists():
            print(f"  [skip] {fname} not found")
            continue
        reader = PdfReader(str(path))
        words: list[str] = []
        word_page: list[int] = []
        for i, page in enumerate(reader.pages, start=1):
            t = page.extract_text() or ""
            w = t.split()
            words.extend(w)
            word_page.extend([i] * len(w))
        n = len(words)
        start, k = 0, 0
        while start < n:
            end = min(start + CHUNK_WORDS, n)
            text = " ".join(words[start:end]).strip()
            p0, p1 = word_page[start], word_page[end - 1]
            if text:
                sec = f"p. {p0}" if p0 == p1 else f"pp. {p0}-{p1}"
                chunks.append(Chunk(
                    id=f"{path.stem}::{k:04d}", text=text, doc=doc, section=sec,
                    source_type="doctrine", cite=f"[{doc}, {sec} (doctrine)]",
                    page_start=p0, page_end=p1,
                ))
                k += 1
            if end >= n:
                break
            start += CHUNK_WORDS - OVERLAP_WORDS
        print(f"  {doc}: {len(reader.pages)} pages -> {k} chunks")
    return chunks


# ----------------------------------------------------------------------------
# Markdown — methodology + worked example
# ----------------------------------------------------------------------------
BOLD_SEC = re.compile(r"^\*\*((?:Part \d|\d+\.\d+|Step \d(?:\.\d)?|Appendix [A-Z])[^*]*)\*\*\s*$", re.M)
HASH_SEC = re.compile(r"^(#{1,3})\s+(.+?)\s*$", re.M)


def short_label(title: str) -> str:
    """'1.3 The universal 3-source rule' -> '§1.3'; 'Step 5 - ...' -> 'Step 5'; 'Part 2 - ...' -> 'Part 2'."""
    t = title.strip()
    m = re.match(r"^(\d+(?:\.\d+)*)\b", t)
    if m:
        return f"§{m.group(1)}"
    m = re.match(r"^(Step \d(?:\.\d)?|Part \d|Appendix [A-Z]|Scenario \d|Hazard \d|R-0\d)", t)
    if m:
        return m.group(1)
    return t[:40]


def split_sections(text: str, mode: str) -> list[tuple[str, str]]:
    """Return [(title, body)] in document order. Leading text before the first heading is 'Front matter'."""
    pat = BOLD_SEC if mode == "bold" else HASH_SEC
    matches = list(pat.finditer(text))
    if not matches:
        return [("Document", text)]
    out = []
    if matches[0].start() > 0:
        out.append(("Front matter", text[: matches[0].start()]))
    for i, m in enumerate(matches):
        title = m.group(1) if mode == "bold" else m.group(2)
        body_start = m.end()
        body_end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        out.append((title.strip(), text[body_start:body_end]))
    return out


def read_markdown() -> list[Chunk]:
    chunks: list[Chunk] = []
    for fname, (doc, stype, mode) in MD_DOCS.items():
        path = CORPUS / fname
        if not path.exists():
            print(f"  [skip] {fname} not found")
            continue
        text = clean_md(path.read_text(encoding="utf-8"))
        sections = split_sections(text, mode)
        if mode == "hash" and len(sections) <= 1:   # datasheet may have no headings
            sections = [(f"part {i+1}", w) for i, w in enumerate(window_tokens(text))]
        k = 0
        for title, body in sections:
            body = body.strip()
            if not body:
                continue
            label = short_label(title)
            pieces = window_tokens(body)
            for j, piece in enumerate(pieces):
                sec = label if len(pieces) == 1 else f"{label} (part {j+1}/{len(pieces)})"
                full = f"{title}\n\n{piece}" if j == 0 else f"{title} (cont.)\n\n{piece}"
                chunks.append(Chunk(
                    id=f"{path.stem}::{k:04d}", text=full, doc=doc, section=sec,
                    source_type=stype, cite=f"[{doc} {label} ({stype})]",
                    extra={"section_title": title},
                ))
                k += 1
        print(f"  {doc}: {len(sections)} sections -> {k} chunks")
    return chunks


# ----------------------------------------------------------------------------
# XLSX — one record per row
# ----------------------------------------------------------------------------
def cell_str(v) -> str:
    if v is None:
        return ""
    if isinstance(v, float) and v.is_integer():
        v = int(v)
    s = str(v).strip()
    return re.sub(r"\s*\n\s*", "; ", s)


ID_RE = re.compile(r"^(UL-\d|H\d|C-\d)$")
MARK_RE = re.compile(r"^(W\*?|N)$")


def parse_step23(ws) -> list[dict]:
    """Step 2 & 3 sheet: UL table, Hazard table and H/UL crosswalk sit side by side; constraints lower down.
    Anchor on ID cells (UL-n, Hn, C-n) instead of row positions."""
    rows = [[cell_str(c) for c in r] for r in ws.iter_rows(values_only=True)]
    legend = next(("; ".join(x for x in r[1:] if x) for r in rows if r and r[0] == "Legend"), "")
    # column where the crosswalk starts (header cell like "H \ UL"); text left of it never crosses over
    cross_col = next((j for r in rows for j, v in enumerate(r) if re.match(r"^H\s*\\\s*UL$", v)), None)
    recs = []
    for r in rows:
        for j, v in enumerate(r):
            if not ID_RE.match(v):
                continue
            vals = []
            for k in range(j + 1, len(r)):
                if ID_RE.match(r[k]):
                    break
                if cross_col is not None and j < cross_col <= k:
                    break
                if r[k]:
                    vals.append(r[k])
            if not vals:          # header labels like UL-1..UL-5 in the crosswalk header row
                continue
            if v.startswith("H") and vals and all(MARK_RE.match(x) for x in vals):
                fields = {"Table": "Hazard / Loss Crosswalk", "Hazard": v}
                fields.update({f"UL-{n + 1}": x for n, x in enumerate(vals)})
                if legend:
                    fields["Legend"] = legend
                label = f"crosswalk {v}"
            else:
                kind = {"U": "Unacceptable Loss", "H": "Hazard", "C": "Constraint"}[v[0]]
                fields = {"Table": kind, "ID": v}
                if len(vals) >= 2:
                    fields["Source"] = vals[0]
                    fields["Definition"] = " ".join(vals[1:])
                elif vals:
                    fields["Definition"] = vals[0]
                label = v
            text = f"Sheet: {ws.title} | " + " | ".join(f"{h}: {x}" for h, x in fields.items())
            recs.append({"sheet": ws.title, "row": label, "fields": fields, "text": text})
    return recs


def parse_blocks(ws) -> list[dict]:
    """Narrow prose sheets (e.g. Step 6 causal scenarios): one record per blank-line-separated block."""
    recs, block = [], []

    def flush():
        if block:
            label = block[0][:60]
            text = f"Sheet: {ws.title} | {label}\n" + "\n".join(block)
            recs.append({"sheet": ws.title, "row": label, "fields": {"lines": len(block)}, "text": text})
            block.clear()

    for r in ws.iter_rows(values_only=True):
        line = " ".join(cell_str(c) for c in r if cell_str(c))
        if line:
            block.append(line)
        else:
            flush()
    flush()
    return recs


def parse_table(ws) -> list[dict]:
    """Ordinary one-table sheets: header = first row with >= 3 cells, one record per following row."""
    rows = [[cell_str(c) for c in r] for r in ws.iter_rows(values_only=True)]
    hidx = next((i for i, r in enumerate(rows) if sum(1 for c in r if c) >= 3), None)
    if hidx is None:
        return []
    headers, recs = rows[hidx], []
    for r in rows[hidx + 1:]:
        fields = {h: v for h, v in zip(headers, r) if h and v}
        if len(fields) < 2:
            continue
        row_label = next(iter(fields.values()))
        text = f"Sheet: {ws.title} | " + " | ".join(f"{h}: {v}" for h, v in fields.items())
        recs.append({"sheet": ws.title, "row": row_label, "fields": fields, "text": text})
    return recs


def read_xlsx() -> list[Chunk]:
    import openpyxl

    chunks: list[Chunk] = []
    for path in sorted(RAW.glob("*.xlsx")):
        hit = next((v for key, v in XLSX_DOCS.items() if key.lower() in path.name.lower()), None)
        if hit is None:
            print(f"  [skip] {path.name}: not a recognized workbook")
            continue
        doc, stem = hit
        wb = openpyxl.load_workbook(path, data_only=True)
        records = []
        for ws in wb.worksheets:
            title = ws.title.strip().lower()
            if any(s in title for s in SKIP_SHEETS):
                continue
            if title.startswith("step 2"):
                recs = parse_step23(ws)
            elif ws.max_column <= 2:
                recs = parse_blocks(ws)
            else:
                recs = parse_table(ws)
            records.extend(recs)
        out_json = CORPUS / f"{stem}.json"
        out_json.write_text(json.dumps(records, indent=1, ensure_ascii=False), encoding="utf-8")
        per_sheet = {}
        for rec in records:
            per_sheet[rec["sheet"]] = per_sheet.get(rec["sheet"], 0) + 1
        for k, rec in enumerate(records):
            sec = f"{rec['sheet']} row {rec['row']}"
            pieces = window_tokens(rec["text"])
            for j, piece in enumerate(pieces):
                sec_j = sec if len(pieces) == 1 else f"{sec} (part {j + 1})"
                chunks.append(Chunk(
                    id=f"{stem}::{k:04d}" + (f"-{j}" if len(pieces) > 1 else ""), text=piece, doc=doc,
                    section=sec_j, source_type="worked_example",
                    cite=f"[{doc} — {sec_j} (worked_example)]",
                    extra={"sheet": rec["sheet"], "row": str(rec["row"])},
                ))
        print(f"  {doc}: {len(records)} rows -> {out_json.relative_to(ROOT)}  " +
              ", ".join(f"{k}={v}" for k, v in per_sheet.items()))
    return chunks


# ----------------------------------------------------------------------------
# ATT&CK STIX — one chunk per technique
# ----------------------------------------------------------------------------
def read_attack() -> list[Chunk]:
    path = RAW / "enterprise-attack.json"
    if not path.exists():
        print("  [skip] enterprise-attack.json not found")
        return []
    bundle = json.loads(path.read_text(encoding="utf-8"))
    chunks: list[Chunk] = []
    for obj in bundle.get("objects", []):
        if obj.get("type") != "attack-pattern" or obj.get("revoked") or obj.get("x_mitre_deprecated"):
            continue
        ext = next((r for r in obj.get("external_references", []) if r.get("source_name") == "mitre-attack"), None)
        if not ext:
            continue
        tid, name = ext["external_id"], obj.get("name", "")
        tactics = sorted({p["phase_name"].replace("-", " ").title() for p in obj.get("kill_chain_phases", [])})
        platforms = ", ".join(obj.get("x_mitre_platforms", []))
        desc = re.sub(r"\(Citation: [^)]*\)", "", obj.get("description", "")).strip()
        desc = " ".join(desc.split()[:450])
        text = (f"ATT&CK Technique {tid} — {name}\n"
                f"Tactic(s): {', '.join(tactics) or 'n/a'}\n"
                f"Platforms: {platforms or 'n/a'}\n"
                f"Sub-technique: {'yes' if obj.get('x_mitre_is_subtechnique') else 'no'}\n\n{desc}")
        chunks.append(Chunk(
            id=f"attack::{tid}", text=text, doc="MITRE ATT&CK Enterprise", section=tid,
            source_type="threat_data", cite=f"[MITRE ATT&CK {tid} {name} (threat_data)]",
            extra={"technique_id": tid, "technique_name": name, "tactics": "; ".join(tactics)},
        ))
    print(f"  MITRE ATT&CK Enterprise: {len(chunks)} techniques")
    return chunks


# ----------------------------------------------------------------------------
# Embed + store
# ----------------------------------------------------------------------------
def embed(texts: list[str]) -> np.ndarray:
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer(EMBED_MODEL)
    vecs = model.encode(texts, batch_size=64, show_progress_bar=True, normalize_embeddings=True)
    return np.asarray(vecs, dtype=np.float32)


def write_numpy_store(chunks: list[Chunk], vecs: np.ndarray) -> None:
    with (INDEX / "chunks.jsonl").open("w", encoding="utf-8") as f:
        for c in chunks:
            f.write(json.dumps({"id": c.id, "text": c.text, **c.meta()}, ensure_ascii=False) + "\n")
    np.save(INDEX / "embeddings.npy", vecs)
    print(f"  numpy store: {len(chunks)} chunks -> data/index/chunks.jsonl + embeddings.npy")


def write_chroma(chunks: list[Chunk], vecs: np.ndarray) -> None:
    try:
        import chromadb
    except Exception as e:  # noqa: BLE001
        print(f"  chromadb unavailable ({e}); numpy store only")
        return
    client = chromadb.PersistentClient(path=str(INDEX / "chroma"))
    try:
        client.delete_collection("mission_assurance")
    except Exception:  # noqa: BLE001
        pass
    col = client.create_collection("mission_assurance", metadata={"hnsw:space": "cosine"})
    B = 256
    for i in range(0, len(chunks), B):
        batch = chunks[i:i + B]
        col.add(
            ids=[c.id for c in batch],
            documents=[c.text for c in batch],
            metadatas=[c.meta() for c in batch],
            embeddings=vecs[i:i + B].tolist(),
        )
    print(f"  chroma: {col.count()} chunks -> data/index/chroma/")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="parse and chunk only; no embeddings")
    args = ap.parse_args()

    print("Reading sources…")
    chunks: list[Chunk] = []
    chunks += read_pdfs()
    chunks += read_markdown()
    chunks += read_xlsx()
    chunks += read_attack()

    ids = [c.id for c in chunks]
    assert len(ids) == len(set(ids)), "duplicate chunk ids"

    by_type: dict[str, int] = {}
    for c in chunks:
        by_type[c.source_type] = by_type.get(c.source_type, 0) + 1
    print(f"\nTotal chunks: {len(chunks)}  " + "  ".join(f"{k}={v}" for k, v in sorted(by_type.items())))
    toks = [ntok(c.text) for c in chunks]
    print(f"Chunk tokens (approx): min={min(toks)} median={int(np.median(toks))} max={max(toks)}")

    if args.dry_run:
        sample = next((c for c in chunks if c.source_type == "methodology"), chunks[0])
        print(f"\nSample chunk {sample.id} {sample.cite}\n{sample.text[:500]}…")
        return

    print(f"\nEmbedding with {EMBED_MODEL} (local)…")
    vecs = embed([c.text for c in chunks])
    write_numpy_store(chunks, vecs)
    write_chroma(chunks, vecs)
    print("\nDone.")


if __name__ == "__main__":
    main()
