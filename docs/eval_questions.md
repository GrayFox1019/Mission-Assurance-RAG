# Eval Questions — Mission Assurance RAG

All 20 written (2026-11-04). **v1.1** after baseline run: Q6 must-contain aligned to guide wording, Q8 rewritten, Q11 replaced — see notes in each row. Each has: the question, the document(s) that should be cited, and what a correct answer must contain. Score each run on three binaries: **cited correctly**, **grounded** (no claims beyond the context), **refusal correct** (negatives only).

Split: 8 factual lookups, 7 cross-document (2 bridge FMA-C ↔ doctrine/STPA, 1 bridge threat_data ↔ worked_example, 1 structured multi-hop), 5 negatives (correct answer is "Not found in corpus").

Machine-readable copy: `eval_questions.json` (same IDs).

```json
{"id": 1, "type": "factual", "question": "...", "expected_sources": ["DoDI 8510.01"], "must_contain": ["..."], "should_refuse": false}
```

---

## Factual lookups (8)

| # | Question | Expected source | Must contain |
|---|---|---|---|
| 1 | What are the six steps of the Risk Management Framework? | NIST SP 800-37 r2 | Prepare, Categorize, Select, Implement, Assess, Authorize, Monitor (r2 has seven incl. Prepare — a correct answer notes this) |
| 2 | Under DoDI 8510.01, who is responsible for authorizing a DoD system to operate? | DoDI 8510.01 | Authorizing Official (AO) |
| 3 | How does DoDD 3020.40 define "Mission Assurance"? | DoDD 3020.40 | A process to protect or ensure the continued function and resilience of capabilities and assets... (verbatim or near) |
| 4 | What does NIST SP 800-30 define as the components of risk? | NIST SP 800-30 r1 | threat, vulnerability, likelihood, impact |
| 5 | What are the three sources every FMA-C workbook entry must trace back to? | How-To Guide §1.3 | commander/exercise brief, data sheet, architecture diagram |
| 6 | What are the four bins in a Step 5 hazardous control action analysis? | How-To Guide Step 5; STPA Handbook | not provided when required / provided when not required / wrong time or order / applied too long or stopped too soon (guide wording; report's applied-unsafe / not-applied / early-late / short-long also accepted) |
| 7 | What is MITRE ATT&CK technique T1190, and which tactic does it fall under? | ATT&CK Enterprise STIX (threat_data) | Exploit Public-Facing Application; Initial Access. Tests the STIX ingest. |
| 8 | What does NIST SP 800-53 r5 control SC-7 (Boundary Protection) require? | NIST SP 800-53 r5 SC-7 | At least two of: external boundary, managed interfaces, monitor/control communications. *(v1.1: rewritten — r5 has no family-scope prose, so the original 'what does the SC family cover' was unanswerable.)* |

## Cross-document (7)

| # | Question | Expected sources | Must contain |
|---|---|---|---|
| 9 | Which NIST SP 800-53 control families does SP 800-82 single out as needing OT-specific tailoring? | 800-82 r3 + 800-53 r5 | Names at least two families 800-82 discusses (e.g., AC, IA, SC, SI) and ties them to OT constraints |
| 10 | How does the RMF in DoDI 8510.01 relate to the NIST SP 800-37 process? | 8510.01 + 800-37 | States 8510.01 implements/adopts the NIST RMF for DoD |
| 11 | The F/A-13 Peacemaker report scores risk as Likelihood × Impact. How does NIST SP 800-30 define likelihood and impact, and what scale and bands does the report use? | 800-30 r1 + Peacemaker §5.4 | likelihood / adverse impact definitions; 1–5 scales, Score = L×I, 20–25 Critical. *(v1.1: replaced 'does FMA-C replace RMF' — the How-To Guide never states the relationship, so the baseline refusal was correct and the question was unanswerable.)* |
| 12 | Which NIST SP 800-30 concept corresponds most closely to an FMA-C Unacceptable Loss, and where do they differ? | 800-30 r1 + How-To Guide Step 2 | adverse impact; UL is commander-defined and mission-level, not system-level |
| 13 | For risk register entry R-05 in the F/A-13 assessment, which hazardous control action does it reference, and which Unacceptable Loss does that HCA trace to? | Risk Assessment xlsx (Risk Register sheet, `FMA-C HCA Reference` column) + Peacemaker report §5.2 (HCA → hazard) + §3.2 (hazard → UL) | CA19 (GCS_MAM_Any IssueOverride) → H4 → UL-3. Three hops across a JSON-row chunk and two report sections. Partial credit: CA19 + UL-3 without H4. |
| 14 | Where does the FMA-C Step 5 four-bin analysis come from, and what does the STPA Handbook call the equivalent analysis? | STPA Handbook (doctrine) + How-To Guide Step 5 (methodology) | Unsafe Control Action (UCA); the four UCA types; STPA / Leveson. Vocabulary bridge FMA-C ↔ parent discipline. |
| 15 | Which ATT&CK technique describes supply-chain compromise, and which F/A-13 risk register entries describe that threat? | ATT&CK Enterprise STIX (threat_data) + Peacemaker report §5.4 or Risk Register xlsx (worked_example) | T1195 (Supply Chain Compromise); R-03 and R-04. The technique ID must come from a retrieved STIX chunk — positive-direction test of rule 3. |

## Negatives (5)

Correct output is a refusal. Plausible questions a doctrine assistant *might* get asked but the corpus can't answer.

| # | Question | Why it must refuse |
|---|---|---|
| 16 | Which NIST SP 800-53 controls does the F/A-13 Peacemaker report map to each of its five critical KT-C? | **Must refuse.** The report scores and mitigates the five KT-C but never maps them to 800-53 controls, and 800-53 is in the corpus — so the model has both halves of a plausible bridge and must not build it. Tests rule 3 (no fabricated control IDs) and FMA-C ↔ doctrine bridge-refusal. Goes in the README as a deliberate safety test. |
| 17 | What does NIST SP 800-171 require for CUI handling? | 800-171 is not in the corpus; tests that a near-miss document name doesn't produce a fabricated answer |
| 18 | What does NIST SP 800-53 control SC-99 require? | Real family, nonexistent control. Direct test of rule 3 — the model must not invent a control from the SC family's pattern. |
| 19 | What does ATT&CK technique T0836 (Modify Parameter) describe? | Real technique, but in the **ICS** matrix; only Enterprise is ingested. Plausible for an aircraft-bus question; model must not fill the gap from memory. |
| 20 | How does DoDI 3020.45 define the Mission Assurance Construct? | Cited in the Peacemaker report's reference list but not ingested. Tests the "cite it, don't ingest it" rule — the model sees the title in a chunk and must still refuse. |

---

## Notes

- Q13 join key: the Risk Register `FMA-C HCA Reference` cell is multi-line (one CA per line). Ingest splits on newline so each CA name is searchable in the row's text rendering.
- Q16 stays inside the notional F/A-13 universe on purpose — no real platform or unit anywhere in the eval set. Add `eval_questions.json` and `README.md` to the pre-commit grep scope so this file is checked too.
- Q16 partial-credit trap: an answer that names the report's mitigations (two-person integrity, attestation, etc.) *as if* they were 800-53 controls, or that suggests "likely" control IDs, scores as not grounded.
- Avoid an AFPAM 63-128 negative — the report describes its L×I scale explicitly, so a grounded non-refusal is possible.

## Results table (paste into README after each run)

| Run | Chunk size | k | Cited correct | Grounded | Refusal correct | Notes |
|---|---|---|---|---|---|---|
| 1 | section-aware (own docs) + 800/100 (doctrine) | 6 | /15 | /15 | /5 | baseline |
| 2 | | | | | | |
