# The twenty test questions

These were written before any code, so the test measures what the assistant was *supposed* to do, not what it happened to do. They are run after every change; the results live in `results/`. The machine-readable copy the grader uses is `eval_questions.json`.

**v1.1 (after the first run):** three questions were corrected — Q6's required terms now match the guide's actual wording, Q8 was rewritten because its source document no longer contains what it asked for, and Q11 was replaced because the author's own guide turned out not to state the fact it tested. Each is marked below.

## Terms used in the questions

- **DoD** — Department of Defense. **DoDD** is a DoD *directive* (policy); **DoDI** is a DoD *instruction* (how to carry policy out).
- **NIST SP 800-xx** — a *Special Publication* from the National Institute of Standards and Technology; the 800 series covers computer security.
- **RMF** — the Risk Management Framework, NIST's seven-step process for authorizing a computer system to operate.
- **AO** — Authorizing Official, the person who formally accepts the risk of running a system.
- **OT** — operational technology: computers that run physical equipment.
- **STPA** — System-Theoretic Process Analysis, a systems-safety method from MIT.
- **MITRE ATT&CK** — a public, numbered catalog of attacker techniques (Adversarial Tactics, Techniques, and Common Knowledge). Technique numbers look like T1190.
- **FMA-C** — Functional Mission Analysis – Cyber, the analysis method the worked example follows. Its artifacts: **UL** (Unacceptable Loss, what the commander cannot accept losing), **H** (Hazard, a system state that can cause a loss), **CA** (Control Action, a command one part of the system gives another), **HCA** (Hazardous Control Action, a control action going wrong in one of four ways), **KT-C** (Key Terrain – Cyber, the short list of systems that matter most), **R-0n** (a row in the risk register).
- **F/A-13 Peacemaker** — the fictional aircraft in the worked example.

## How answers are graded

Three yes/no marks per question:

- **Cited** — a footnote the assistant actually used points at one of the expected documents.
- **Grounded** — the answer contains every required term, and no part of it is flagged as "not found."
- **Refused** — for the five trap questions only: the answer begins with "Not found in corpus."

An answer that gets half the question right and honestly flags the other half as missing counts as *not grounded*. That is strict on purpose.

---

## Simple lookups (8) — one document should answer each

| # | Question | Expected source | A correct answer must mention | In plain terms |
|---|---|---|---|---|
| 1 | What are the six steps of the Risk Management Framework? | NIST SP 800-37 r2, or DoDI 8510.01 | Prepare, Categorize, Select, Implement, Assess, Authorize, Monitor | The current edition has seven steps, not six; a good answer notices. Either document lists them. |
| 2 | Under DoDI 8510.01, who is responsible for authorizing a DoD system to operate? | DoDI 8510.01 | Authorizing Official (AO) | Who signs off on a system. |
| 3 | How does DoDD 3020.40 define "Mission Assurance"? | DoDD 3020.40 | A process to protect or ensure the continued function and resilience of capabilities and assets… | Quote the official definition. |
| 4 | What does NIST SP 800-30 define as the components of risk? | NIST SP 800-30 r1 | threat, vulnerability, likelihood, impact | The four ingredients of a risk assessment. |
| 5 | What are the three sources every FMA-C workbook entry must trace back to? | How-To Guide §1.3 | commander/exercise brief, data sheet, architecture diagram | The guide's rule that nothing goes in the analysis without a source. |
| 6 | What are the four bins in a Step 5 hazardous control action analysis? | How-To Guide Step 5; STPA Handbook | not provided when required / provided when not required / wrong time or order / applied too long or stopped too soon *(v1.1: aligned to the guide's wording)* | The four ways a command can go wrong. |
| 7 | What is MITRE ATT&CK technique T1190, and which tactic does it fall under? | ATT&CK catalog | Exploit Public-Facing Application; Initial Access | Tests that the attacker catalog was loaded correctly. |
| 8 | What does NIST SP 800-53 r5 control SC-7 (Boundary Protection) require? | NIST SP 800-53 r5 | at least two of: external boundary, managed interfaces, monitor/control communications *(v1.1: rewritten)* | Originally "what does the SC family cover" — the 2020 edition dropped the family-level descriptions, so that was unanswerable. |

## Two-document questions (7) — the answer needs more than one source

| # | Question | Expected sources | A correct answer must mention | In plain terms |
|---|---|---|---|---|
| 9 | Which NIST SP 800-53 control families does SP 800-82 single out as needing OT-specific tailoring? | 800-82 r3 + 800-53 r5 | at least two families (e.g., AC, IA, SC, SI) tied to OT constraints | Which security-control groups have to be adapted for equipment-control computers. |
| 10 | How does the RMF in DoDI 8510.01 relate to the NIST SP 800-37 process? | 8510.01 + 800-37 | 8510.01 implements/adopts the NIST RMF for DoD | The DoD instruction is the military's adoption of the NIST process. |
| 11 | The F/A-13 Peacemaker report scores risk as Likelihood × Impact. How does NIST SP 800-30 define likelihood and impact, and what scale and bands does the report use? | 800-30 r1 + Peacemaker report §5.4 | likelihood, impact, 1–5 scales, 20–25 = Critical *(v1.1: replaced)* | Connect NIST's definitions to how the worked example scores risk. The original Q11 asked whether FMA-C replaces RMF; the guide never says, so the assistant's refusal was correct and the question was unanswerable. |
| 12 | Which NIST SP 800-30 concept corresponds most closely to an FMA-C Unacceptable Loss, and where do they differ? | 800-30 r1 + How-To Guide Step 2 | adverse impact; UL is commander-defined and mission-level | A translation question. No document states the answer outright; the assistant has to infer it, which the rules discourage — see the README. |
| 13 | For risk register entry R-05 in the F/A-13 assessment, which hazardous control action does it reference, and which Unacceptable Loss does that HCA trace to? | Risk register (spreadsheet) + report §5.2 + report §3.2 | CA19, H4, UL-3 | The hardest one: three hops across a spreadsheet row and two report tables. |
| 14 | Where does the FMA-C Step 5 four-bin analysis come from, and what does the STPA Handbook call the equivalent analysis? | STPA Handbook + How-To Guide Step 5 | Unsafe Control Action (UCA) | Same idea, two names, two documents. |
| 15 | Which ATT&CK technique describes supply-chain compromise, and which F/A-13 risk register entries describe that threat? | ATT&CK catalog + report §5.4 | T1195, R-03, R-04 | Connect an attacker technique to the two risks in the worked example that describe it. |

## Trap questions (5) — the correct answer is "Not found in corpus."

These are plausible questions an analyst might ask that the shelf cannot answer. They check that the assistant doesn't fill a gap from memory.

| # | Question | Why it must refuse |
|---|---|---|
| 16 | Which NIST SP 800-53 controls does the F/A-13 Peacemaker report map to each of its five critical KT-C? | The report scores and mitigates its five key systems but never maps them to NIST controls — and the NIST catalog *is* on the shelf, so the assistant has both halves and must not build the bridge itself. A fabricated control number here would be the worst possible failure. |
| 17 | What does NIST SP 800-171 require for CUI handling? | 800-171 (the rules for Controlled Unclassified Information) is a real NIST document that is *not* loaded. A near-miss name must not produce an invented answer. |
| 18 | What does NIST SP 800-53 control SC-99 require? | SC is a real control family; SC-99 does not exist. |
| 19 | What does ATT&CK technique T0836 (Modify Parameter) describe? | A real technique, but from ATT&CK's industrial-control catalog; only the Enterprise catalog is loaded. |
| 20 | How does DoDI 3020.45 define the Mission Assurance Construct? | The worked example's reference list *cites* this document, but it isn't on the shelf. The assistant sees the title on a card and must still refuse. |

---

## Notes

- Q13's join: the risk register's "FMA-C HCA Reference" cell lists several control actions on separate lines; the loader splits them so each is searchable.
- No real aircraft, unit or organization appears anywhere in the question set, on purpose.
- An earlier draft used a negative question about an Air Force risk-scoring pamphlet; it was dropped because the worked example describes that pamphlet's scale explicitly, so a grounded (non-refusing) answer would have been legitimate.
