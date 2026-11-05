# What's on the shelf

Every document the assistant can draw on, where it came from, and what *type* it is. The type matters because every footnote the assistant writes carries it, so a reader can tell whether a claim rests on official policy or on a training example.

**Types**

- **policy** (`doctrine` in the code) — official, public government or standards documents.
- **method** (`methodology`) — the how-to guide for the analysis technique, written by the author.
- **worked example** (`worked_example`) — a complete, fictional analysis of a made-up aircraft, used to show the method in practice.
- **threat data** (`threat_data`) — a public, numbered catalog of how attackers operate.

## Public documents (downloaded, not stored in this repository)

| Document | What it is, in a sentence | Type | Where to get it |
|---|---|---|---|
| DoDD 3020.40, *Mission Assurance* (2016, updated 2018) | The Department of Defense (DoD) directive that defines "mission assurance" and says who is responsible for protecting the things a mission depends on. | policy | https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodd/302040p.pdf |
| DoDI 8510.01, *Risk Management Framework for DoD Systems* (2022) | The DoD instruction that applies the government-wide Risk Management Framework (RMF) to military computer systems, including who may authorize a system to operate. | policy | https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodi/851001p.pdf |
| NIST SP 800-30 rev. 1, *Guide for Conducting Risk Assessments* | The National Institute of Standards and Technology (NIST) guide to assessing risk — how to think about threats, vulnerabilities, likelihood and impact. | policy | https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-30r1.pdf |
| NIST SP 800-37 rev. 2, *Risk Management Framework* | The seven-step RMF process itself (Prepare, Categorize, Select, Implement, Assess, Authorize, Monitor). | policy | https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-37r2.pdf |
| NIST SP 800-53 rev. 5, *Security and Privacy Controls* | The catalog of security controls (roughly a thousand numbered safeguards, grouped into families such as Access Control and System and Communications Protection). | policy | https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf |
| NIST SP 800-82 rev. 3, *Guide to Operational Technology Security* | How to secure operational technology (OT) — the computers that run physical equipment, from factory floors to aircraft data buses — and how the 800-53 controls have to be adapted for it. | policy | https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r3.pdf |
| *STPA Handbook* (Leveson & Thomas, MIT, 2018) | The free handbook for System-Theoretic Process Analysis (STPA), the systems-safety method that the FMA-C technique descends from. | policy | https://psas.scripts.mit.edu/home/get_file.php?name=STPA_handbook.pdf (mirror: https://www.flighttestsafety.org/images/STPA_Handbook.pdf) |
| MITRE ATT&CK Enterprise (STIX 2.1 JSON) | MITRE's public catalog of attacker tactics and techniques, each with a number such as T1190. ATT&CK stands for Adversarial Tactics, Techniques, and Common Knowledge. "Enterprise" is the version covering ordinary computer networks; the industrial-control version is not loaded. | threat data | https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack.json |

`scripts/download.ps1` fetches all of these into `data/raw/`, which is excluded from version control. Two of the DoD files are behind a download filter that blocks scripts; save those from a browser if the script reports an error on them.

## The author's own documents (included in this repository)

All fictional. Written during a training course on a made-up aircraft so the method could be shown end to end without touching anything real.

| Document | What it is, in a sentence | Type | File |
|---|---|---|---|
| FMA-C How-To Guide | A step-by-step guide to Functional Mission Analysis – Cyber (FMA-C): how to go from a commander's mission statement to a prioritized list of the computer systems that mission can't survive losing. | method | `data/corpus/howto_guide.md` |
| F/A-13 Peacemaker FMA-C Report | A complete FMA-C analysis of the fictional F/A-13 — mission, unacceptable losses, hazards, control structure, the fifteen most important systems, risk scores and recommended fixes. | worked example | `data/corpus/peacemaker_report.md` |
| FMAC Tables for the F/A-13 | The analysis spreadsheets behind the report, one row per entry (losses, hazards, constraints, control actions, hazardous control actions, key systems, scenarios). | worked example | `data/corpus/fmac_tables.json` |
| F/A-13 Risk Assessment | The risk register: five risks, each tied to the control actions it involves, the losses it could cause, and a likelihood × impact score. | worked example | `data/corpus/risk_assessment.json` |
| F/A-13 Peacemaker Technical Data Sheet v0.3 | The fictional aircraft's technical description — its computers, data buses, external ports, ground equipment and maintenance tools. Written by the course staff and banner-marked as not real. | worked example | `data/corpus/fa13_datasheet.md` |

The spreadsheets are stored here as JSON (one plain-text record per row) because that is what the assistant indexes; the original Excel files are not committed.
