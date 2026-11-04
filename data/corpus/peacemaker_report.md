**F/A-13 "Peacemaker"**

**Functional Mission Analysis — Cyber (FMA-C) Report**

**91st Fighter Squadron**

**9350th Air Dominance Wing**

McCandles AFB, Durango, New Mexico

Prepared by:

**Cameron Partlow**

Mission Assurance Cyber Coordinator Element (MACCE)

MACCE Capstone Exercise Product

**21 July 2026**

**UNCLASSIFIED // FOR TRAINING ONLY**

*This is all make-believe. All systems, personnel, unit designations, and scenarios are notional and generated for training use only.*

# Executive Summary

The F/A-13 “Peacemaker” is a next-generation multi-role fighter/attack platform operated by the 91st Fighter Squadron in support of the 9350th Air Dominance Wing's air dominance mission from McCandles AFB, Durango, New Mexico. The aircraft's distinguishing feature is a modular autonomy architecture that supports three operating modes — Crewed, Loyal Wingman, and Fully Autonomous — built around the Mission Autonomy Module (MAM), the Collaborative Swarm Pod (CSP), and a Ground Control Station (GCS) that serves as the primary human authority in autonomous mode. Every external cyber pathway onto the aircraft is designed to be mediated by a redundant pair of Security Gateways bridging the MIL-STD-1553B command-and-control backbone, the MIL-STD-1760 weapons interface bus, and the ARINC 664 / AFDX high-bandwidth data network.

This Functional Mission Analysis — Cyber (FMA-C) identifies fifteen Key Terrain — Cyber (KT-C) nodes distributed across the aircraft, ground station, and support infrastructure. Five KT-C are elevated to critical for prioritized risk assessment: the Security Gateway, the Mission Autonomy Module, the DTC/DTU + Type-1 crypto chain, the vendor direct-connect ports (Radar / EW / FADEC), and the Ground Control Station in autonomous mode. Two of those five score at the Critical risk threshold (20/25) when scored under AFPAM 63-128 semi-qualitative L × I methodology, driven primarily by adversary supply-chain opportunity: the DTC/DTU + Type-1 crypto chain, and the vendor direct-connect ports that presently bypass Security Gateway mediation.

Top-line recommendations for the 91 FS Commander (copy to ACC A6/2/3KM): (1) extend Security Gateway mediation to the vendor direct-connect ports as a priority Engineering Change Request to the F/A-13 Program Office; (2) enforce two-person integrity for all Mission Data Load builds at the Mission Planning System enclave and for all MAM Support Kit (MSK) bench loads; (3) implement multi-source AI-model validation and adversarial red-team of the MAM model set prior to every deployment; (4) require hardware attestation of GCS consoles at the start of every mission and multi-console consensus for any autonomous-mode override; (5) require MACCE-witnessed vendor tool connections for every RMT / EST / EFT session on any aircraft. The complete list of prioritized mitigations, the supporting causal scenarios, and the risk register are contained in Sections 5 and 6.

# Scope, Limitations, and Assumptions

## Scope and Limitations

Scope. This analysis addresses the 91st Fighter Squadron's operational employment of the F/A-13 Peacemaker across all three operating modes (Crewed, Loyal Wingman, and Fully Autonomous) for a single-mission cycle. The cyber terrain considered includes:

> **Onboard buses:** MIL-STD-1553B, MIL-STD-1760, and ARINC 664 / AFDX (each dual-redundant).
>
> **Onboard processing nodes:** Mission Computer (MC ×2), Mission Autonomy Module (MAM), Vehicle Management Computer (VMC ×2), Sensor Fusion Engine (SFE ×2), Stores Management System (SMS ×2), Weapon Interface Unit (WIU ×2), Flight Control Computer (FCC ×3), FADEC (×2 per engine), Health Monitoring System (HMS), and the redundant Security Gateway pair.
>
> **External through-the-skin interfaces:** Maintenance Ethernet Port, Secure Data Load Port (SDLP), Weapon Load Interface, Power/BIT Panel, MAM Access Bay, Data Transfer Unit (DTU), and vendor direct-connect ports (Radar Service Port, EW Service Port, FADEC direct interface).
>
> **Ground support:** Portable Maintenance Aid (PMA), Mission Systems Maintenance Terminal (MSMT), Weapons Integration Tool (WIT), Radar Maintenance Tool (RMT), EW Suite Tool (EST), Engine/FADEC Tool (EFT), and the MAM Support Kit (MSK) — both on-aircraft and off-aircraft bench modes.
>
> **Ground control:** Ground Control Station (GCS) comprising Ground Mission Computer Cluster (GMCC), Autonomy Supervisory Module (ASM), and the Communications Segment.
>
> **Mission planning:** Mission Planning System (MPS) classified enclave and the DTC / DTU / Secure Maintenance Laptop (SML) load chain.
>
> **External RF surfaces:** Link-16, ATDL loyal-wingman datalink, SATCOM, LOS HF/VHF/UHF, and the encrypted UAV RF mesh.
>
> **Governance and tool chain:** CROWS validation authority, PMO distribution, and CASU / CTK physical tool control.

Limitations. This analysis is bounded to the information contained in the F/A-13 Peacemaker Technical Data Sheet, Version 0.3 (CAO 4/2/2026, 22 pages), and the commander-provided FMA-C inputs (Mission statement, AST/BMO/IOTCT decomposition, Unacceptable Losses UL-1..5, Hazards H1..5, and Constraints C-1..5) delivered in the 21 July 2026 scenario brief. The analysis does not include a full adversary threat model, formal STRIDE decomposition per interface, penetration test results, or classified detail. Where the data sheet does not name a specific artifact (for example, MPS enclave network naming, presence or absence of SIPR/NIPR/wireless maintenance networks), that gap is treated as an assumption and is documented in the next subsection rather than as fact.

## Assumptions

> **A-1.** The F/A-13 fleet is home-based at McCandles AFB with an adjacent MPS classified enclave and secure network transport between MPS and GCS.
>
> **A-2.** The Cyber Resiliency Office for Weapon Systems (CROWS) and the Program Management Office (PMO) tool-validation chain operates as documented in the F/A-13 Technical Data Sheet, including zero-day exception handling.
>
> **A-3.** Fully Autonomous mode requires an active GCS as the primary human authority in the loop. Loss of GCS authority in that mode is treated as an unacceptable state.
>
> **A-4.** The Type-1 crypto chain for the Data Transfer Cartridge (DTC) is properly implemented at the physical-media layer, with valid COMSEC key management under an accountable custodian.
>
> **A-5.** Vendor direct-connect ports for Radar, EW, and FADEC currently bypass the Security Gateway per the aircraft as-designed. This as-designed bypass is analyzed here as a KT-C exposure, not a defect against the design baseline.
>
> **A-6.** All personnel handling classified media, tools, and mission data are cleared, trained, and named on the Commander-signed CASU access memorandum.
>
> **A-7.** Aircraft operate with both Security Gateways installed. Loss of one is a GO with restrictions per MEL Category B; loss of both is NO-GO.

# 1. System and Mission Context

## 1.1 Detailed System Description

The F/A-13 Peacemaker is a stealth-optimized, multi-role fighter/attack aircraft positioned in capability between the F-22 Raptor and the F-35 Lightning II. It combines a low-observable airframe, internal weapons bays, high-bandwidth sensor fusion, and a modular autonomy architecture that permits operation in Crewed, Loyal Wingman, or Fully Autonomous mode. Its distinguishing operational feature is the internal Mission Autonomy Module (MAM) paired with the external Collaborative Swarm Pod (CSP), enabling coordinated ISR, EW, and strike effects with a mixed manned/unmanned force.

### 1.1.1 Onboard Buses

> **MIL-STD-1553B:** Command-and-control backbone. Dual-redundant (a/b). Carries all safety- and mission-critical device traffic among MC, MAM, VMC, SFE, SMS, WIU, FCC, FADEC, and HMS.
>
> **MIL-STD-1760:** Weapons interface bus. Dual-redundant (a/b). Provides power and data between the aircraft and smart munitions via the Weapon Interface Unit (WIU).
>
> **ARINC 664 / AFDX:** High-bandwidth ethernet bus. Dual-redundant (a/b). Carries sensor fusion, cockpit display, MAM data-plane, and external RF datalink traffic.

### 1.1.2 Key Processing Nodes (LRUs)

| **Node** | **Qty / Required** | **Bus / Path** | **Role** |
|----|----|----|----|
| Mission Computer (MC) | 2 / 1 | 1553 BC + AFDX | Tactical decision-making, sensor-fusion coordination, C2 authority |
| Mission Autonomy Module (MAM) | 1 / mode-dependent | 1553 + AFDX (via Sec GW) | Autonomy engine; CPU + GPU/TPU cluster; holds AI models, ROE, abort criteria; removable LRU (54×30×24 in, 650-900 lb, 30-min rail install) |
| Vehicle Management Computer (VMC) | 2 / 1 | 1553 | Flight control coordination, engine ops, health-monitoring coord |
| Sensor Fusion Engine (SFE) | 2 / 1 | AFDX | Combines radar + EO/IR + EW into unified track files |
| Stores Management System (SMS) | 2 / 1 | 1553 + 1760 (via WIU) | Weapons inventory and launch commands |
| Flight Control Computer (FCC) | 3 / 2 | 1553 | Actuator commands (triple-redundant safety-critical) |
| FADEC | 2 per engine / 1 per | 1553 | Engine control (vendor firmware) |
| Health Monitoring System (HMS) | 1 / 0 | 1553 (all LRUs) + AFDX (MX) | BIT, fault-code aggregation, log dump |
| Weapon Interface Unit (WIU) | 2 / 1 | 1553 + 1760 | Protocol translator between SMS (1553) and munitions (1760) |
| Security Gateway | 2 / 1 (both failed = NO-GO) | Between external ports and internal buses | Authenticates, validates, and cross-domain-partitions every external ingress |

### 1.1.3 External Through-the-Skin Interfaces

All except the vendor direct-connect ports are mediated by the Security Gateway.

| **External Interface** | **Physical Type** | **Function / Tool** |
|----|----|----|
| Maintenance Ethernet Port | Ethernet | Primary MX interface; used by PMA, MSMT, and MSK (limited on-aircraft mode) |
| Secure Data Load Port (SDLP) | Serial / proprietary | Alt MDL load path via SML; also post-mission debrief pull |
| Weapon Load Interface | 1760 | Used by WIT for smart-munition test and validation |
| Power/BIT Panel | Discrete + serial | HMS + VMC diagnostics via the Security Gateway |
| MAM Access Bay | Physical hatch | Physical LRU removal / installation (30 minutes via rail-based quick install) |
| Data Transfer Unit (DTU) | Type-1 encrypted DTC receptacle | Primary MDL ingress point pre-flight |
| Radar Service Port (vendor direct) | Vendor proprietary | RMT direct connect to AESA — BYPASSES Security Gateway |
| EW Service Port (vendor direct) | Vendor proprietary | EST direct connect to EW Suite — BYPASSES Security Gateway |
| FADEC Direct Interface (vendor) | Vendor proprietary | EFT direct connect to FADEC — BYPASSES Security Gateway |

### 1.1.4 Collaborative Swarm Pod (CSP) and UAV Architecture

The CSP is an external smart dock/launch pod carried on a wing or fuselage hardpoint. It interfaces to the aircraft via MIL-STD-1760 (stores management) and ARINC 664 (programming and status). Critically, the CSP does NOT control UAVs post-launch — that authority resides with the MC and MAM. Each UAV (approximately 75 lb, canister-ejected, electric ducted-fan propulsion) carries an EO/IR camera, a SAR sensor, a mini jammer, and up to a 10-lb precision micro-munition. UAV-to-aircraft communications ride an encrypted RF mesh; MC distributes UAV data over ARINC 664. Every UAV has encrypted storage and a Zeroize / Self-wipe capability. UAV recovery disposition ranges from expendable (Strike, EW, Decoy, low-cost ISR) to recoverable (high-value ISR) to persistent (Relay/Network).

### 1.1.5 Ground Control Station (GCS)

The GCS is a distributed mission-control system with three working consoles (Pilot/Operator, Mission Commander, Swarm Control) and three aircraft-interacting components: the Ground Mission Computer Cluster (GMCC), which mirrors the onboard MC; the Autonomy Supervisory Module (ASM), which is the ground-side counterpart to the onboard MAM; and the Communications Segment, providing multi-band SATCOM, LOS datalink, and a tactical-network gateway. In Loyal Wingman mode, the GCS acts as secondary control ready to take over if the primary manned aircraft loses connectivity. In Fully Autonomous mode, the GCS is the primary human authority in the loop and is treated by this analysis as KT-C on par with the onboard MAM.

### 1.1.6 Mission Data Load (MDL) Path

An MDL package built at the MPS classified enclave includes the flight plan, threat library, target packages, weapon profiles, communications plan (frequencies and crypto keys), UAV tasking, and autonomy constraints (ROE, MAM abort criteria). The MDL is written to a Data Transfer Cartridge (DTC), a removable solid-state module protected with Type-1 encryption, and physically transported to the aircraft for insertion into the DTU. An alternative path uses the Secure Maintenance Laptop (SML) connected to the Secure Data Load Port (SDLP). In Fully Autonomous mode, a synchronized copy of the MDL is also pushed from MPS to GCS via a secure network. On the aircraft, the ingress path is: DTU or SDLP → MC → Security Gateway (validation + partitioning) → MAM (autonomy logic) + SFE (threat library) + SMS (weapon profiles) + Datalink (network plan) → onboard mission storage.

### 1.1.7 Maintenance Tool Inventory

| **Tool** | **Full Name** | **Type** | **Connection Path** | **Target Systems** |
|----|----|----|----|----|
| PMA | Portable Maintenance Aid | Gov ruggedized laptop | Maint Ethernet | HMS, MC, VMC, FCC, FADEC, SMS |
| MSMT | Mission Systems Maint Terminal | Gov ruggedized laptop (container apps) | Maint Ethernet + can reach 1553 | Radar diag, EO/IR cal, SFE verify, datalink cfg, MAM operational I/F |
| WIT | Weapons Integration Tool | Gov ruggedized laptop (modernized CMBRE) | Weapon Load Interface or direct 1760 | Smart munitions test/validate |
| RMT | Radar Maintenance Tool | VENDOR ruggedized laptop | Radar Service Port (direct — bypasses Sec GW) | AESA Radar |
| EST | EW Suite Tool | VENDOR ruggedized laptop | EW Service Port (direct — bypasses Sec GW) | EW Suite |
| EFT | Engine/FADEC Tool | VENDOR ruggedized laptop | FADEC direct (bypasses Sec GW) | FADEC |
| MSK | MAM Support Kit | Multi-component secure terminal + bench | On-aircraft = Maint Eth (limited). High-authority ops OFF-AIRCRAFT air-gapped. | MAM SW, AI model, deep diag |

### 1.1.8 Tool Governance and Update Chain (CROWS / PMO)

All specialty tools are stored in Controlled Access Storage Units (CASU) managed by the Central Tool Kit (CTK) — locked racks with visual inventory. Access is serialized and electronically tracked (check-in/check-out); a Commander-signed memorandum names authorized personnel. Every tool runs with secure boot, encrypted onboard storage, AV/malware protection, and digital certificates. The aircraft treats every tool connection as zero-trust: certificates are validated per transaction. No tool update is trusted outright. The update chain is OEM → CROWS validates → PMO distributes → tool. Zero-day exceptions may permit expedited vendor updates, which increases risk and is called out in Section 5.

### 1.1.9 Post-Mission and Diagnostic Egress Paths

Post-mission mission data is collected via the Debrief Exploitation System (DES) in a secure facility. The path is: onboard recorder → MC → Security Gateway (sanitize/export) → DTC or SDLP → DES. In Fully Autonomous mode, a partial data stream flows in real time from the aircraft to GCS via SATCOM/Datalink; full-resolution data is still pulled post-flight. Log and diagnostic data (BIT results, LRU fault codes, HMS logs, FADEC logs, bus traffic, thermal/power logs) are pulled via the PMA over the Maintenance Ethernet Port, through the Security Gateway, and via MC / VMC / HMS to subsystem LRUs and back. Vendor direct-connect ports (FADEC, Radar, EW) provide alternate diagnostic-pull paths that bypass the Security Gateway.

## 1.2 Mission Purpose and Goal

**Commander-provided Mission Statement (91st FS):**

> *"To provide the 9350th Air Dominance Wing and Combatant Commanders with lethal, all-weather Air Dominance and Strategic Precision Strike capabilities. The 91st Fighter Squadron recruits, trains, and maintains a premier force of elite aviators and mission-ready F/A-13 aircraft to penetrate contested environments, neutralize advanced aerial threats, and ensure the freedom of maneuver for joint and coalition forces across the globe."*

**Commander's Intent:**

> *"To operate as the 'first-in' force of the 9350th ADW. We exist to ensure that no adversary can challenge our sovereignty or our allies in the sky. By leveraging the F/A-13's advanced low-observable technology and multi-role versatility, we are the Wing's primary tool for dismantling integrated air defense systems and achieving immediate air superiority."*

**FMA-C Mission Formulation (AST / BMO / IOTCT):**

> *"The 91st Fighter Squadron employs the F/A-13 as a system to maintain air dominance through crewed or uncrewed technologies by means of generating aircraft to perform sensing and strike hostile threats, in order to contribute to ensuring joint force freedom of maneuver."*
>
> **AST (As a System To):** maintain air dominance through crewed or uncrewed technologies.
>
> **BMO (By Means Of):** generating aircraft to perform sensing and strike hostile threats.
>
> **IOTCT (In Order To Contribute To):** ensuring joint force freedom of maneuver.

## 1.3 Key Tasks (KT)

Derived from the BMO. Each Key Task represents a mission-essential function of the 91 FS employment of the F/A-13. These are the tasks whose failure or corruption most directly leads to an Unacceptable Loss.

> **KT-1 Generating:** Generate mission-ready F/A-13 aircraft — including any required manning, weapons, fuel, mission-data load, and configuration — to fly the assigned sortie in the required operating mode (Crewed, Loyal Wingman, or Autonomous).
>
> **KT-2 Sensing:** Aggregate sensor information from the primary aircraft, loyal-wingman aircraft, autonomous aircraft, and deployed UAV swarms into a single Operational Picture usable for tactical decision-making.
>
> **KT-3 Striking (Kinetic):** Employ kinetic munitions — onboard weapons and UAV-mounted micro-munitions — against authorized targets within ROE.
>
> **KT-4 Striking (Electronic Effects):** Disrupt the electromagnetic spectrum — via the onboard EW Suite, HPM pod, and UAV-mounted jammers — against authorized targets within ROE and frequency deconfliction rules.

# 2. High-Level Unacceptable Losses (UL)

Commander-provided list. Each UL represents an outcome that is unacceptable at the mission level. All hazards, control actions, and mitigations in this report are traceable back to one or more of these losses.

> **UL-1 Loss of Life:** Death of a squadron member (aircrew, maintenance, GCS operator) or a civilian non-combatant caused by any 91 FS action or mission failure.
>
> **UL-2 Loss of an Aircraft:** F/A-13 airframe missing, destroyed, or damaged so severely that it is approaching a NO-GO state, whether by kinetic engagement, controlled flight into terrain, engine/flight-control failure, or a maneuver outside envelope.
>
> **UL-3 Loss of MAM Control of an Aircraft or UAV Swarm:** Free-flight of an F/A-13 (in Autonomous or Loyal Wingman mode) or of a UAV swarm — i.e., autonomy operates outside the commanded envelope with no effective supervisory authority.
>
> **UL-4 Loss of the Ability to Generate a Sortie:** Inability to man, crew, or equip an F/A-13 to fly its assigned mission — including autonomous missions where MAM, MDL, or GCS is unavailable.
>
> **UL-5 Unintended Damage to Civilian Infrastructure:** Imprecise fire — from an F/A-13, a loyal-wingman F/A-13, a fully autonomous F/A-13, or a UAV-swarm asset — that damages non-combatant infrastructure.

# 3. Hazards and Constraints

## 3.1 Hazard and Constraint Listing

Hazards are internal system conditions that, under worst-case environmental or adversarial conditions, cause one or more Unacceptable Losses. Constraints are the reciprocal — the rules or design features the system must satisfy to prevent the hazard. Commander convention: an unmarked cell in the crosswalk means the hazard WILL cause the loss; an asterisk means it COULD cause the loss.

> **H1 — Inappropriate Maneuver.** Aircraft or UAV maneuvers outside the safe or intended flight envelope. Can occur from corrupted flight-control inputs, autonomy behaving outside ROE, or a compromised FADEC or FCC input.
>
> **Constraint C-1:** Aircraft and UAVs shall remain within the safe and intended flight envelope at all times.
>
> **H2 — Incorrect Weapons Utilization.** A weapon is armed, selected, programmed, or released against an invalid, misidentified, unauthorized, or mistimed target. Can occur from corrupted target data, altered weapon profile, MAM engaging without positive human authority, or PIC error induced by a compromised sensor picture.
>
> **Constraint C-2:** Weapons shall only be armed, selected, programmed, and released when target validity, authorization, and timing constraints are satisfied.
>
> **H3 — MPS Compromise.** Aircraft or swarm acts on compromised or faulty battlespace data — including a corrupted threat library, target package, or communications plan produced at the Mission Planning System (MPS) enclave, or altered in transit via the DTC / DTU / SML path.
>
> **Constraint C-3:** Aircraft and swarm operations shall only act on validated, current, and sufficiently reliable battlespace and mission data.
>
> **H4 — Autonomy Constraint Violation.** Autonomous behavior occurs outside authorized mission, ROE, or supervisory constraints. Can occur from a poisoned MAM AI model, altered ROE library, compromised GCS override, or corrupted abort criteria loaded from the MDL.
>
> **Constraint C-4:** Autonomous behavior shall remain within authorized mission, rules of engagement (ROE), and supervisory constraints at all times.
>
> **H5 — Invalid or Degraded System State.** The aircraft or a subsystem is in an incorrect, unverified, or degraded state such that (a) required capability is unavailable when needed, (b) system configuration (including stores state) is incorrect, or (c) a maintenance or update action introduces an unsafe or unvalidated condition.
>
> **Constraint C-5:** The aircraft and all subsystems shall operate only in verified, valid, and mission-capable configurations.

## 3.2 Hazard / Unacceptable Loss Cross-Correlation

Legend: W = Will Cause \| W\* = Could Cause \| N = Will Not Cause

| **Hazard** | **UL-1 Life** | **UL-2 Aircraft** | **UL-3 MAM Ctrl** | **UL-4 Sortie** | **UL-5 Civ Infra** |
|----|----|----|----|----|----|
| H1 Inappropriate Maneuver | W | W | W\* | W\* | W\* |
| H2 Incorrect Weapons Utilization | W | W\* | N | W\* | W |
| H3 MPS Compromise | W\* | W\* | W | W | W |
| H4 Autonomy Constraint Violation | W | W | W | W\* | W |
| H5 Invalid/Degraded System State | W | W | W | W | W\* |

## 3.3 Causal Scenarios — Definitions and Findings by Hazard

### Hazard 1: Inappropriate Maneuver

H1 will cause UL-1 (Loss of Life) and UL-2 (Loss of Aircraft) because an envelope excursion in a stealth-optimized fighter operating in a contested environment — whether triggered by corrupted FADEC firmware pushed via the vendor EFT direct-connect port, by an FCC input driven from a compromised MC/VMC channel, or by a MAM autonomy decision that maneuvers the aircraft outside its flight envelope — produces controlled flight into terrain, structural overstress, or a departure that the pilot (or the autonomy) cannot recover from at combat altitudes and airspeeds. H1 could cause UL-3 (loss of MAM control) if the excursion itself was authored by MAM, could cause UL-4 (loss of sortie generation) if the affected aircraft is grounded pending investigation, and could cause UL-5 (civilian infrastructure damage) if an uncommanded departure occurs over populated terrain. The dominant cyber pathway is the vendor direct-connect chain (RMT / EST / EFT) that presently bypasses the Security Gateway.

### Hazard 2: Incorrect Weapons Utilization

H2 will cause UL-1 (Loss of Life) and UL-5 (Civilian Infrastructure) because a weapon released against a misidentified target — the classic fratricide or collateral-damage failure mode — kills people and destroys infrastructure. On the F/A-13 the cyber pathways enabling H2 include: a compromised MDL that alters target packages or weapon profiles (H3 upstream driver); a poisoned SFE that labels a friendly aircraft as hostile; a MAM that authorizes engagement outside ROE (H4 upstream driver); or a corrupted SMS/WIU that releases the wrong store. H2 could cause UL-2 (aircraft loss) via retaliatory engagement, could cause UL-4 (sortie generation loss) if a fratricide investigation grounds the fleet, and will not directly cause UL-3 (MAM control loss) because a single bad release does not imply free-flight of the airframe.

### Hazard 3: MPS Compromise

H3 will cause UL-3 (Loss of MAM control), UL-4 (Loss of sortie generation), and UL-5 (civilian infrastructure damage) because compromised battlespace data delivered via the MDL corrupts every downstream consumer: SFE receives a false threat library, MAM receives altered ROE and abort criteria, SMS receives modified weapon profiles, and the datalink receives a corrupted communications plan. In Autonomous mode the same corrupted MDL is pushed from MPS to GCS via the secure network, so ground-side override authority is also operating on bad data. H3 could cause UL-1 (loss of life) and UL-2 (aircraft loss) as downstream consequences — H3 is often the enabling condition that H2 or H1 then executes on. The dominant cyber pathways are the MPS classified enclave itself, the Type-1 crypto chain that protects the DTC in transit, and the SML alternate loading path via SDLP.

### Hazard 4: Autonomy Constraint Violation

H4 will cause UL-1 (Loss of Life), UL-2 (Aircraft loss), UL-3 (MAM control loss by definition), and UL-5 (civilian infrastructure damage). The condition is specific to Loyal Wingman and Fully Autonomous modes and can be triggered by any of: a poisoned MAM AI model loaded via the MSK bench; an altered ROE library delivered via a compromised MDL; a hijacked GCS console issuing (or blocking) override; or a UAV mesh spoof that redirects swarm tasking. Because Autonomous mode designates GCS as the primary human authority, GCS compromise and MAM compromise are effectively additive: either one is sufficient to violate the constraint. H4 could cause UL-4 (sortie generation loss) if fleet-wide autonomy is grounded pending forensics — a proportionate response given the stakes.

### Hazard 5: Invalid or Degraded System State

H5 will cause UL-1, UL-2, UL-3, and UL-4 because a degraded state is the background condition that all other hazards exploit: a subsystem in an unverified state (e.g., HMS falsely reporting nominal), a stores configuration in error (e.g., SMS believing the wrong munition is loaded), or an update action that left an LRU in an unvalidated state (e.g., a partial firmware push interrupted mid-transaction). H5 could cause UL-5 (civilian infrastructure damage) as a downstream consequence when the degraded state produces an incorrect release or an uncommanded EW effect. The dominant cyber pathways are the entire tool chain — PMA, MSMT, WIT, RMT, EST, EFT, MSK — and any interrupted or partial load through any external port.

# 4. Mission Functional Control Structure

## 4.1 / 4.2 Control Structure and Relationships

The F/A-13 mission control structure follows a three-tier model in which control actions flow downward from higher-level controllers to lower-level components, and feedback flows upward from sensors, physical components, and automated systems to operators and decision-makers. The system boundary encloses the aircraft (with MAM, CSP + UAVs installed), the GCS, the MPS enclave, and the maintenance-tool chain (CROWS/PMO governed) at McCandles AFB. External RF, adversary action, and higher headquarters (ACC A6/2/3KM, Combatant Commander) sit outside the boundary and appear as inputs/outputs.

**Elements — Operator (Persona) tier:**

> Pilot in Command (PIC)
>
> Wingman / Support Aircrew
>
> GCS Operator (Pilot/Operator, Mission Commander, Swarm Control)
>
> Maintenance Crew
>
> MPS Operator (Mission Planner + Intel)
>
> CROWS validator
>
> Vendor Technician (RMT / EST / EFT operator)
>
> MACCE (Mission Assurance Cyber Coordinator Element)
>
> COMSEC Custodian

**Elements — Controller (Logical) tier:**

> Mission Computer (MC)
>
> Mission Autonomy Module (MAM)
>
> Security Gateway
>
> Vehicle Management Computer (VMC)
>
> Sensor Fusion Engine (SFE)
>
> Stores Management System (SMS)
>
> Weapon Interface Unit (WIU)
>
> Flight Control Computer (FCC)
>
> FADEC
>
> Health Monitoring System (HMS)
>
> Ground Mission Computer Cluster (GMCC — ground twin of MC)
>
> Autonomy Supervisory Module (ASM — ground twin of MAM)

**Elements — Physical / Function tier:**

> F/A-13 airframe (control surfaces, engines, weapons bays)
>
> Collaborative Swarm Pod (CSP) and UAVs
>
> Weapons (A/A missiles, A/G missiles, precision bombs, loitering munitions, EW pod, HPM pod, gun)
>
> Data Transfer Cartridge / Data Transfer Unit (DTC / DTU)
>
> Secure Data Load Port (SDLP)
>
> Maintenance Ethernet Port
>
> Vendor direct-connect ports (Radar Service, EW Service, FADEC direct)
>
> MPS classified enclave
>
> GCS Communications Segment (SATCOM, LOS Datalink, tactical net gateway)

Note: A visual rendering of the control structure diagram is contained in the accompanying PowerPoint briefing prepared for the 91 FS Commander. This report presents the structure textually in section 4.3 (Element × Mode responsibilities) and section 4.4 (Control Actions per mode).

## 4.3 Responsibilities

The table below assigns each control-structure element a responsibility summary for each of the five mission modes. Modes are: Ground Ops, Mission Planning, Ingress, Engage, and Egress / Recovery / Debrief.

| **Element** | **Ground Ops** | **Mission Planning** | **Ingress** | **Engage (Sensing + Striking)** | **Egress / Recovery / Debrief** |
|----|----|----|----|----|----|
| PIC | Preflight per MEL; sign AFTO 781A; mode selection | Aircrew brief; accept MDL; verify autonomy constraints | Fly per MDL; monitor MAM authority; monitor sensor picture | Authorize weapon release (crewed); supervise MAM (autonomy) | RTB; sign AFTO; debrief |
| Wingman / Support Aircrew | Preflight; arm stores | Coordinate flight and weapon config | Nav backup; monitor RF mesh with F/A-13 | Execute assigned engagement; coordinate | Post-mission review |
| GCS Operator | GCS BIT; comms check | Accept MDL push from MPS; verify autonomy plan | Monitor F/A-13 telemetry via ATDL / SATCOM | Primary human authority in Autonomous mode; monitor MAM; abort if needed | Command UAV recovery; receive debrief stream |
| Maintenance | Run 781A discrepancies; PMA diagnostics; firmware via PMA/MSMT/WIT | Load DTC into DTU (or SML→SDLP alt); verify tool integrity | Ground role only | Ground role only | Post-flight inspection; extract debrief via SDLP → DES; download logs |
| MPS Operator | (n/a) | Build MDL in classified enclave; write Type-1 encrypted DTC; push MDL to GCS over secure net (autonomous) | (n/a) | (n/a) | Ingest debrief for planning next mission |
| CROWS | Validate tool and firmware updates before distribution | Validate MDL software baseline | (n/a) | (n/a) | Post-incident forensics if compromise suspected |
| Vendor Technician | Push firmware via RMT / EST / EFT (direct-connect, bypasses Security Gateway) | (n/a) | (n/a) | (n/a) | Diagnostic data pull |
| COMSEC Custodian | Key Type-1 DTC crypto; ATDL, Link-16, UAV mesh keys | Zeroize / reload keys per rotation | (n/a) | (n/a) | Key rotation |
| MC | Boot BIT | Accept MDL via DTU/SDLP → Sec GW; distribute to MAM/SFE/SMS/Datalink | Bus arbitration; sensor picture; waypoint nav | Kill-chain mgmt; stores release logic; UAV command distribution | Log to recorder; prep debrief |
| MAM | Standby | Load AI models, ROE, abort criteria from MDL | Initialize per MDL constraints; begin autonomy supervisory | Autonomous: authorize engagement within ROE. Loyal Wingman: coordinate | Command UAV recovery / zeroize |
| Security Gateway | Standby / BIT | Mediate all MDL ingress; validate provenance | Continuous port validation; per-transaction re-auth | Continuous port validation | Sanitize / export debrief data |
| SFE | Standby / BIT | Load threat library from MDL | Provide fused radar + EO/IR + EW picture to MC/MAM | Same, continuously updated | Log fusion data to recorder |
| SMS | Standby / BIT | Load weapon profiles via MC | Track stores and fuel state | Execute release commands; dispense countermeasures | Standby |
| WIU | Standby | Standby | Translate 1553 ↔ 1760 for stores | Same | Standby |
| VMC | Standby / BIT | Standby | Flight control coordination | Same | Same until shutdown |
| FCC | BIT | Standby | Control surface commands | Same | Same |
| FADEC | Standby | Accept updates via vendor EFT direct-connect (Ground Ops only) | Engine control | Engine control | Engine control; shutdown |
| HMS | BIT reporting | Standby | Continuous health telemetry | Same | Fault log dump via PMA |
| GCS (as system) | BIT; comms warm | Receive MDL push | Monitor F/A-13 telemetry | Autonomous: primary human decision authority | UAV recovery command; debrief telemetry ingest |
| CSP + UAV Swarm | Preflight self-check | Programmed via MC on 1760/AFDX | Launch on MC command; establish encrypted RF mesh | Execute per MAM/MC; commanded zeroize on threat | Recovery per type; zeroize if capture imminent |

## 4.4 Control Actions (CA)

CAs are named per school convention: SRC_DST_MODE_FUNCTION_CA#. The full list of 20 CAs spans the five mission modes. Each CA is expanded in Section 4.5/4.6/4.7 with its Process Model Description (PMD), Process Model Variables (PMV), and Process Model Variable Values (PMVV), and re-examined in Section 5.2 for the four bins of hazardous-behavior badness.

### Ground Ops Mode

> **CA1 Vendor_RMT_GroundOps (UpdateRadar)\_CA1: Vendor tech pushes radar firmware to the AESA via the Radar Service Port using the RMT (bypasses Security Gateway).**
>
> **CA2 Vendor_EST_GroundOps (UpdateEW)\_CA2: Vendor tech pushes EW firmware to the EW Suite via the EW Service Port using the EST (bypasses Security Gateway).**
>
> **CA3 Vendor_EFT_GroundOps (UpdateFADEC)\_CA3: Vendor tech pushes FADEC firmware via the FADEC direct interface using the EFT (bypasses Security Gateway).**
>
> **CA4 Maint_PMA_GroundOps (UpdateFirmware)\_CA4: Maintainer runs a general firmware update to MC / VMC / FCC / SMS via the PMA on the Maintenance Ethernet Port, mediated by the Security Gateway.**
>
> **CA5 Maint_MSK_GroundOps (UpdateMAM)\_CA5: Maintainer loads MAM software, an AI model, or performs deep diagnostics using the MSK — high-authority operations off-aircraft air-gapped; limited operations on-aircraft via Maint Ethernet through the Security Gateway.**
>
> **CA20 MC_HMS_Any (QueryHealth)\_CA20: MC continuously polls HMS; any fault code triggers an alert to PIC or GCS. (Applies in all modes; listed here for the ground start-of-mission.)**

### Mission Planning Mode

> **CA6 MPS_DTC_MissionPlan (BuildMDL)\_CA6: MPS operator builds an MDL in the classified enclave and writes it to a Type-1 encrypted DTC.**
>
> **CA7 Maint_DTU_MissionPlan (LoadMDL)\_CA7: Maintainer loads the DTC into the DTU on the aircraft; MC ingests via the Security Gateway.**
>
> **CA8 MPS_GCS_MissionPlan (PushMDLAutonomous)\_CA8: In Autonomous mode, MPS pushes a synchronized MDL copy to the GCS over the secure network.**

### Ingress Mode

> **CA9 MC_MAM_Ingress (InitializeAutonomy)\_CA9: MC initializes MAM per the loaded MDL: AI model loaded, ROE loaded, abort criteria loaded, mode set to Loyal Wingman or Autonomous.**
>
> **CA10 MC_CSPUAV_Ingress (LaunchProgram)\_CA10: MC commands CSP to power, program (via 1760 + AFDX), and launch UAVs; establishes encrypted RF mesh keys.**

### Engage Mode

> **CA11 PIC_MC_Engage (AuthorizeWeaponRelease)\_CA11: In Crewed mode, PIC authorizes weapon release after positive target ID, ROE satisfaction, and friendly-clear.**
>
> **CA12 MAM_MC_Engage (AutonomousEngagement)\_CA12: In Autonomous mode, MAM authorizes engagement within ROE, absent GCS override, on a weapon authorized in the mode.**
>
> **CA13 MAM_CSP_Engage (CommandSwarm)\_CA13: MAM commands the swarm to execute an engagement (kinetic or EW) per MDL tasking.**
>
> **CA14 MC_EWPod_Engage (ActivateJamming)\_CA14: MC activates the EW pod against a designated target after frequency deconfliction.**
>
> **CA15 PIC_MC_Engage (FireGun)\_CA15: PIC fires the internal 25 mm gun — only permitted in Crewed mode; Limited in Loyal Wingman; NOT ALLOWED in Autonomous.**
>
> **CA19 GCS_MAM_Any (IssueOverride)\_CA19: GCS operator issues an override to MAM upon identifying out-of-envelope behavior (applies primarily in Autonomous).**

### Egress / Recovery / Debrief Mode

> **CA16 MAM_UAVs_Egress (RecoverySequence)\_CA16: MAM sequences UAV recovery for the recoverable UAV types (high-value ISR, Relay/Network).**
>
> **CA17 UAVs_Self_Egress (ZeroizeOnCompromise)\_CA17: A UAV self-zeroizes on loss of mesh + geofence violation + timeout, or upon MAM zeroize command.**
>
> **CA18 Maint_SDLP_Debrief (ExtractData)\_CA18: Maintainer extracts debrief data via the Secure Data Load Port (SDLP) using the SML; Security Gateway sanitize/export applies.**

## 4.5 / 4.6 / 4.7 Process Model Description, Variables, and Values

For each CA, the Process Model Description states the precondition (IF/WHEN clause); the Process Model Variables (PMV) list the state variables the controller must know to issue the CA safely; and the Process Model Variable Values (PMVV) enumerate the allowed/observed values for each variable.

| **CA** | **PMD (IF / WHEN)** | **PMV** | **PMVV** |
|----|----|----|----|
| CA1: Vendor_RMT_GroundOps (UpdateRadar)\_CA1 | Begin when RMT cert authenticated AND vendor firmware CROWS-attested AND Radar Service Port authorized | RMT cert · CROWS attestation · Radar port state | authed/unauth · attested/not · authorized/unauthorized |
| CA2: Vendor_EST_GroundOps (UpdateEW)\_CA2 | Begin when EST cert valid AND CROWS-attested AND EW Service Port authorized | EST cert · CROWS attestation · EW port state | authed/unauth · attested/not · authorized/unauthorized |
| CA3: Vendor_EFT_GroundOps (UpdateFADEC)\_CA3 | Begin when EFT cert valid AND CROWS-attested AND FADEC port authorized | EFT cert · CROWS attestation · FADEC port state | authed/unauth · attested/not · authorized/unauthorized |
| CA4: Maint_PMA_GroundOps (UpdateFirmware)\_CA4 | Begin when PMA cert valid AND firmware CROWS-attested AND Maint Eth authorized AND Sec GW online | PMA cert · CROWS attestation · Maint Eth state · Sec GW state | authed/unauth · attested/not · authorized/unauthorized · online/degraded |
| CA5: Maint_MSK_GroundOps (UpdateMAM)\_CA5 | Begin when MSK bench air-gap verified AND cert valid AND CROWS-attested AND MAM off-aircraft OR limited on-aircraft via Sec GW | MSK cert · CROWS attestation · air-gap verify · Sec GW state | authed/unauth · attested/not · verified/breach · online/degraded |
| CA6: MPS_DTC_MissionPlan (BuildMDL)\_CA6 | Begin when MPS enclave verified AND Type-1 keys valid AND MDL components validated (threat lib, ROE, weapon profiles) | Enclave status · crypto keys · MDL validation | verified/breach · valid/expired · pass/fail |
| CA7: Maint_DTU_MissionPlan (LoadMDL)\_CA7 | Begin when DTC chain-of-custody unbroken AND Type-1 decryption succeeds AND MDL signature valid AND Sec GW online | DTC CoC · decryption · MDL sig · Sec GW state | intact/broken · success/fail · valid/invalid · online/degraded |
| CA8: MPS_GCS_MissionPlan (PushMDLAutonomous)\_CA8 | Begin when secure network authenticated AND MDL sig valid AND GCS ready | Secure net auth · MDL sig · GCS state | authed/unauth · valid/invalid · ready/not-ready |
| CA9: MC_MAM_Ingress (InitializeAutonomy)\_CA9 | Begin when MAM BIT pass AND ROE loaded AND abort criteria loaded AND mode = Loyal Wingman or Autonomous | MAM BIT · ROE · abort criteria · mode | pass/fail · loaded/missing · loaded/missing · Crewed/LW/Auto |
| CA10: MC_CSPUAV_Ingress (LaunchProgram)\_CA10 | Begin when CSP present AND UAV BIT pass AND mesh keys loaded AND MDL UAV tasking loaded | CSP state · UAV BIT · mesh keys · UAV tasking | present/absent · pass/fail · loaded/missing · loaded/missing |
| CA11: PIC_MC_Engage (AuthorizeWeaponRelease)\_CA11 | Begin when target identified AND stores armed AND friendly clear AND ROE satisfied | Target ID · stores state · friendly clear · ROE | pos/unknown · armed/safe · clear/not-clear · satisfied/violated |
| CA12: MAM_MC_Engage (AutonomousEngagement)\_CA12 | Begin when target within ROE AND supervisory constraint intact AND GCS override not issued AND weapon authorized in mode | Target ID · ROE · supervisory · GCS override · weapon auth | pos/unknown · within/outside · valid/violated · none/issued · authorized/prohibited |
| CA13: MAM_CSP_Engage (CommandSwarm)\_CA13 | Begin when swarm formation intact AND target coord valid AND swarm ROE satisfied AND GCS not overriding | Swarm state · target coord · ROE swarm · GCS | intact/degraded · valid/invalid · satisfied/violated · none/override |
| CA14: MC_EWPod_Engage (ActivateJamming)\_CA14 | Begin when EW target designated AND frequency deconflicted AND EW allowed in mode | EW target · freq · EW mode auth | designated/none · deconflicted/conflict · allowed/prohibited |
| CA15: PIC_MC_Engage (FireGun)\_CA15 | Begin ONLY when mode = Crewed AND gun-safe area confirmed AND ROE satisfied | Mode · gun-safe · ROE | Crewed/Non-crewed · confirmed/not · satisfied/violated |
| CA16: MAM_UAVs_Egress (RecoverySequence)\_CA16 | Begin when UAV type = recoverable AND recovery zone reachable AND fuel sufficient | UAV type · recovery zone · fuel | recoverable/expendable · reachable/not · sufficient/low |
| CA17: UAVs_Self_Egress (ZeroizeOnCompromise)\_CA17 | Begin when capture imminent (mesh lost + geofence violation + timeout) OR MAM zeroize cmd | Mesh · geofence · timeout · zeroize cmd | connected/lost · in/out · not-elapsed/elapsed · none/issued |
| CA18: Maint_SDLP_Debrief (ExtractData)\_CA18 | Begin when SML cert valid AND SDLP port authorized AND Sec GW sanitize pass | SML cert · SDLP state · Sec GW sanitize | authed/unauth · authorized/unauthorized · pass/fail |
| CA19: GCS_MAM_Any (IssueOverride)\_CA19 | Begin when GCS operator identifies out-of-envelope MAM behavior AND override credential valid | MAM behavior · GCS credential | in-envelope/out · valid/invalid |
| CA20: MC_HMS_Any (QueryHealth)\_CA20 | Continuous; fault triggers alert to PIC/GCS | HMS state · fault code · alert path | nominal/degraded · code/none · PIC/GCS/both |

## 4.8 Feedback

Based on the F/A-13 system architecture and control structure, feedback loops are broken out into those internal to the system boundary and those external. The two categories are treated separately because their security controls are different (internal loops rely on Security Gateway mediation and 1553/1760/AFDX integrity; external loops rely on Type-1 crypto, key management, and physical chain of custody).

### 4.8.1 Inside the System (Internal Feedback Loop)

Internal feedback flows upward from physical hardware components through the automated control layers to the human operator or the autonomy supervisor. Key internal loops include:

> **HMS → MC → PIC / GCS.** Health-monitoring telemetry from every LRU is aggregated at HMS, forwarded to MC over 1553, and surfaced to the PIC's glass cockpit displays and (in Autonomous mode) to the GCS console. Any fault code triggers an alert (CA20). Security measures: HMS integrity depends on 1553 bus determinism and PMA log-pull attestation; a false-normal report from a tampered HMS is an H5 driver.
>
> **SFE → MC → PIC display / MAM.** Sensor fusion combines radar, EO/IR, and EW into a unified track file, distributed to MC over AFDX and to MAM over 1553 + AFDX. Security measures: SFE input integrity depends on vendor sensor firmware (RMT / EST chain) and on MC bus arbitration; a poisoned SFE is an H3 driver via CA1 or CA2.
>
> **UAV mesh → MAM.** UAV sensor and status data returns via the encrypted RF mesh to the host aircraft; MC distributes over AFDX; MAM consumes for swarm-coordination logic. Security measures: mesh crypto keying and per-UAV Zeroize; the mesh itself is an H4 driver via CA13 if spoofed.
>
> **MAM behavior sampling → shadow-ROE comparator.** A shadow-ROE monitor (recommended mitigation, Section 5.4) samples MAM decisions in flight and compares them against a reference ROE library. Drift triggers a positive-confirm request to GCS.

### 4.8.2 Outside the System (External Feedback Loop)

External feedback loops sit outside the aircraft/GCS boundary and include:

> **Debrief data → DES → MPS.** Post-mission data flows from the onboard recorder through MC and the Security Gateway to DTC/SDLP, then into the DES in a secure facility, and ultimately back into the MPS enclave to inform the next mission's MDL. Security measures: DTC/SDLP Type-1 crypto; DES air-gap; MPS enclave access control; MACCE chain-of-custody verification at every transfer.
>
> **GCS telemetry → Combatant Commander.** Autonomous-mode telemetry and BDA are relayed from GCS onward to the higher command echelon (ACC A6/2/3KM and CCMD). Security measures: SIPR-equivalent secure network transport; multi-level release rules; GCS-side sanitization.
>
> **MACCE anomaly reports → 9350 ADW chain.** Any anomaly detected by the MACCE (integrity failure at Sec GW, DTC provenance failure, shadow-ROE drift, unauthorized vendor tool connection) is reported up the Wing chain to the Cdr (Brig Gen Kirby), with copy to ACC A6/2/3KM. Security measures: written report on classified system; incident-response playbook.
>
> **CROWS / PMO advisories → fleet.** CROWS and PMO issue advisories and forced updates to the fleet in response to vendor zero-days or discovered vulnerabilities. Security measures: PMO distribution channel; MACCE verification of receipt and application.

# 5. Critical Information Flow / Four Bins of Badness

## 5.1 Mission Relevant Terrain — Cyber (MRT-C)

The MRT-C scope covers all cyber systems and communications methods identified by 91 FS and its supporting organizations as required for one or more mission tasks during execution. Not all MRT-C is KT-C to the Wing mission and therefore does not appear on the final KT-C list. However, KT-C is a derivative of MRT-C, and the determination is fluid: MRT-C not previously identified as KT-C can become KT-C as the threat picture, mission tasking, or system baseline changes.

For the F/A-13 supporting the 91 FS mission, the MRT-C includes: (a) all onboard cyber processing nodes (MC, MAM, VMC, SFE, SMS, WIU, FCC, FADEC, HMS, Security Gateway); (b) all onboard buses (1553B, 1760, ARINC 664 / AFDX); (c) all external through-the-skin interfaces (Maint Ethernet, SDLP, Weapon Load Interface, Power/BIT, MAM Access Bay, DTU, and the three vendor direct-connect ports); (d) all seven maintenance tools (PMA, MSMT, WIT, RMT, EST, EFT, MSK) and their CROWS/PMO update chain; (e) the MPS classified enclave and the DTC/DTU/SML load chain; (f) the Ground Control Station (GMCC, ASM, Comms Segment); (g) external RF surfaces (Link-16, ATDL, SATCOM, LOS HF/VHF/UHF, and the encrypted UAV RF mesh); and (h) the CASU/CTK physical tool control infrastructure. The KT-C table in Section 5.3 is the filtered subset of this MRT-C whose compromise directly enables one or more commander hazards.

## 5.2 Hazardous Control Actions (Four Bins of Badness)

For each of the 20 CAs, four hazardous-behavior bins are examined: Applied when unsafe, Not Applied when needed, Applied Early(E) / Late(L), and Applied Short(S) / Long(A). Each cell lists which commander hazard(s) that behavior would enable.

| **CA** | **Applied when unsafe** | **Not Applied when needed** | **Early (E) / Late (L)** | **Short (S) / Long (A)** |
|----|----|----|----|----|
| CA1: Vendor_RMT_GroundOps (UpdateRadar)\_CA1 | H3, H5 (bad radar FW → false fusion picture) | H5 (stale / vuln radar) | E: H3; L: H5 | S: H5; A: H3 |
| CA2: Vendor_EST_GroundOps (UpdateEW)\_CA2 | H3, H4 (false ES data → wrong ROE picture) | H5 (degraded EW) | E: H3; L: H5 | S: H5; A: H3 |
| CA3: Vendor_EFT_GroundOps (UpdateFADEC)\_CA3 | H1, H5 (engine mis-response → envelope excursion) | H5 | E: H1; L: H5 | S: H5; A: H1 |
| CA4: Maint_PMA_GroundOps (UpdateFirmware)\_CA4 | H5, H3 (bad FW to MC/HMS/VMC) | H5 | E: H5; L: H5 | S: H5; A: H3 |
| CA5: Maint_MSK_GroundOps (UpdateMAM)\_CA5 | H4, H3 (bad AI model, altered ROE) | H4 (stale ROE library) | E: H4; L: H4 | S: H4; A: H4 |
| CA6: MPS_DTC_MissionPlan (BuildMDL)\_CA6 | H3 (bad MDL from compromised MPS) | H5 (no MDL = no mission) | E: H3; L: H5 | S: H3; A: H3 |
| CA7: Maint_DTU_MissionPlan (LoadMDL)\_CA7 | H3 (bad DTC → MC compromise) | H5 | E: H3; L: H5 | S: H5; A: H3 |
| CA8: MPS_GCS_MissionPlan (PushMDLAutonomous)\_CA8 | H3, H4 (compromised ground picture) | H4 (no MDL to GCS) | E: H3; L: H4 | S: H4; A: H3 |
| CA9: MC_MAM_Ingress (InitializeAutonomy)\_CA9 | H4 (autonomy init with wrong ROE / abort criteria) | H4 (MAM without ROE) | E: H4; L: H4 | S: H4; A: H4 |
| CA10: MC_CSPUAV_Ingress (LaunchProgram)\_CA10 | H4, H2 (wrong tasking = wrong target) | H5 (no swarm) | E: H4; L: H4 | S: H4; A: H4 |
| CA11: PIC_MC_Engage (AuthorizeWeaponRelease)\_CA11 | H2 (bad target = friendly/civilian hit) | H5 (weapon never released) | E: H2; L: H2 | S: H2; A: H2 |
| CA12: MAM_MC_Engage (AutonomousEngagement)\_CA12 | H4, H2 (engages outside ROE) | H4 (refuses valid engagement) | E: H4; L: H4 | S: H4; A: H4 |
| CA13: MAM_CSP_Engage (CommandSwarm)\_CA13 | H4, H2 (swarm strikes non-combatant infra) | H5 (no swarm effect) | E: H4; L: H4 | S: H4; A: H4 |
| CA14: MC_EWPod_Engage (ActivateJamming)\_CA14 | H2, H3 (jams friendly comms or wrong freq) | H5 (no EW = degraded mission) | E: H2; L: H2 | S: H2; A: H2 |
| CA15: PIC_MC_Engage (FireGun)\_CA15 | H2 (fired in Autonomous → H4 violation) | H5 (no close-range engage) | E: H2; L: H2 | S: H2; A: H2 |
| CA16: MAM_UAVs_Egress (RecoverySequence)\_CA16 | H1, H4 (recovery over friendly territory / bad timing) | H5 (loss of UAVs) | E: H1; L: H1 | S: H5; A: H1 |
| CA17: UAVs_Self_Egress (ZeroizeOnCompromise)\_CA17 | H4 (zeroize valid asset by mistake) | H3 (compromised UAV survives with keys) | E: H4; L: H3 | S: H3; A: H4 |
| CA18: Maint_SDLP_Debrief (ExtractData)\_CA18 | H3 (contaminated SML pulls data through Sec GW) | (n/a — post-mission) | (n/a) | (n/a) |
| CA19: GCS_MAM_Any (IssueOverride)\_CA19 | H4 (bad override = removes valid autonomy) | H4 (missed override = MAM out of envelope) | E: H4; L: H4 | S: H4; A: H4 |
| CA20: MC_HMS_Any (QueryHealth)\_CA20 | H5 (false-normal hides real fault) | H5 (fault missed) | E: H5; L: H5 | S: H5; A: H5 |

## 5.3 Key Terrain — Cyber (KT-C)

MRT-C is filtered to KT-C by testing whether compromise of a node directly enables one or more commander hazards. Fifteen KT-C are identified below. The five rows shaded green are elevated to critical for risk assessment (Section 5.4) and detailed causal-scenario development (Section 6.1).

| **\#** | **Node** | **Bus / Path** | **Hazards Enabled** | **Category** |
|----|----|----|----|----|
| 1 | Security Gateway (×2) | Mediates all external ports to 1553 / 1760 / AFDX | H3, H4, H5 | Mission System |
| 2 | Mission Autonomy Module (MAM) | 1553 + AFDX (all I/O via Sec GW); MSK for updates | H3, H4 | Mission System |
| 3 | Mission Computer (MC) | 1553 Bus Controller + AFDX | H2, H3, H5 | Mission System |
| 4 | DTC / DTU + Type-1 crypto chain | External media path to MC via Sec GW | H3, H4 | Mission Support |
| 5 | MPS (Mission Planning System) classified enclave | Produces MDL; source of pre-flight ingress | H3, H4 | Mission Support (2nd degree) |
| 6 | Vendor direct-connect ports (Radar / EW / FADEC) | Bypass Security Gateway; direct to LRU | H1, H3, H5 | Mission Support (1st degree — direct) |
| 7 | Ground Control Station (GCS) | ATDL / SATCOM; primary human authority in Autonomous | H4 | Mission System (Autonomous mode) |
| 8 | CROWS / PMO update-validation chain | Every tool and firmware update transits here | H3, H5 | Ancillary Support |
| 9 | MSMT | Maint Ethernet + can reach 1553 | H3, H5 | Mission Support |
| 10 | PMA | Maint Ethernet | H5 | Mission Support |
| 11 | Sensor Fusion Engine (SFE) | 1553 + AFDX | H3 | Mission System |
| 12 | Stores Management System (SMS) | 1553 + 1760 (via WIU) | H2 | Mission System |
| 13 | Weapon Interface Unit (WIU) | 1553 ↔ 1760 translator | H2 | Mission System |
| 14 | CSP + UAV RF Mesh | External RF; 1760 + AFDX aircraft-side | H2, H4, H5 | Mission System |
| 15 | CASU / CTK physical tool control | Physical access; Commander memo | H3, H5 | Ancillary Support |

## 5.4 Mitigation Phase / Risk Management

The five KT-C shaded in Section 5.3 receive full risk assessment and detailed mitigation. Scoring follows the AFPAM 63-128 semi-qualitative L × I model, with L (Likelihood) and I (Impact) each on a 1-5 scale and Score = L × I:

> **1-6 Low**
>
> **7-12 Medium**
>
> **13-19 High**
>
> **20-25 Critical**

| **ID** | **KT-C** | **Threat / Vulnerability Summary** | **Primary UL** | **L** | **I** | **Score** | **Band** |
|----|----|----|----|----|----|----|----|
| R-01 | KT-C 1 Security Gateway | Adversary supply-chain or firmware compromise reaches the Sec GW; an attested-but-malicious payload passes into 1553 / 1760 / AFDX and propagates to MC, MAM, SFE, SMS. | UL-2, UL-3, UL-4 | 3 | 5 | 15 | High |
| R-02 | KT-C 2 Mission Autonomy Module (MAM) | AI-model poisoning or ROE-library tampering via the MSK bench or the vendor supply chain; MAM authorizes engagements outside intended ROE or refuses valid engagements. | UL-1, UL-3, UL-5 | 3 | 5 | 15 | High |
| R-03 | KT-C 4 DTC / DTU + Type-1 Crypto Chain | MDL supply-chain compromise: adversary in the MPS enclave, at the Type-1 key management function, in the physical DTC custody chain, or on the SML alternate loader. | UL-1, UL-4, UL-5 | 4 | 5 | 20 | Critical |
| R-04 | KT-C 6 Vendor Direct-Connect Ports (Radar / EW / FADEC) | Vendor tool bypasses the Security Gateway. Compromised RMT / EST / EFT loads malicious firmware directly to the LRU (radar, EW suite, or FADEC). | UL-2, UL-4 | 4 | 5 | 20 | Critical |
| R-05 | KT-C 7 GCS in Autonomous mode | GCS override authority hijacked via SATCOM / ATDL exploit, or via credential theft on the secure-network path from MPS; adversary issues false overrides or blocks valid ones. | UL-1, UL-3, UL-5 | 3 | 5 | 15 | High |

### R-01 Mitigation — Security Gateway (KT-C 1)

Threat / vulnerability. The Security Gateway mediates every external ingress to the internal 1553 / 1760 / AFDX buses. It is the single choke point for trust boundary enforcement, and a NO-GO condition exists if both gateways fail. An adversary who succeeds in placing a signed/attested-but-malicious payload — whether via a compromised vendor firmware build (upstream of CROWS), a compromised PMO distribution, or a compromised on-aircraft attestation path — achieves compromise of MC, MAM, SFE, and SMS in a single stroke.

> **Hardware fix:** Deploy redundant, hardware-attested Security Gateway pairs sourced from independent vendor chains (dual-vendor supply). Add tamper-evident hardware seals on each gateway and require verification at each installation.
>
> **Software fix:** Require dual-vendor CROWS re-attestation for every accepted payload; log every accepted payload to write-once media; enable behavioral anomaly detection at each gateway with alerts to the MACCE console.
>
> **Policy / procedure fix:** MACCE monthly review of Security Gateway acceptance logs; enforce a NO-GO condition when either gateway reports any behavioral anomaly (do not wait for both to fail before grounding); rotate gateway attestation keys per COMSEC-defined cadence.

### R-02 Mitigation — Mission Autonomy Module (MAM) (KT-C 2)

Threat / vulnerability. The MAM houses the AI models, ROE library, and abort criteria that govern Autonomous-mode engagement. High-authority updates are intended to occur only on the MSK bench in an off-aircraft air-gapped environment, but the bench itself is a target; and even a validated model can carry planted biases or backdoors if the vendor's AI supply chain is compromised.

> **Hardware fix:** Site the MSK bench in a dedicated SCIF with continuous physical monitoring; require tamper-evident hardware for both the bench and the transported media used to move a new AI model onto the bench.
>
> **Software fix:** Multi-source AI-model validation — an ensemble check that requires two independent validators (with independent tooling) to accept a candidate model before MSK deployment; adversarial red-team of the model against the ROE test set prior to every deployment; shadow-ROE behavior monitoring in flight that samples MAM decisions against a reference ROE and alerts on drift.
>
> **Policy / procedure fix:** Two-person integrity for every MSK bench load and every MAM AI-model deployment; require GCS operator to positively confirm every autonomous engagement above a defined threat category; MACCE-witnessed load of every AI model into MSK.

### R-03 Mitigation — DTC / DTU + Type-1 Crypto Chain (KT-C 4)

Threat / vulnerability. Every MDL flows through this chain, and adversary opportunity exists at multiple points: inside the MPS classified enclave, at the Type-1 key management function, in the physical DTC custody chain during transport to the aircraft, and on the Secure Maintenance Laptop (SML) if the SDLP alternate path is used. This KT-C scores at the Critical threshold (20/25) because a compromised MDL corrupts every downstream consumer — SFE threat library, MAM ROE, SMS weapon profiles, and (in Autonomous mode) the GCS copy — and because adversary access opportunity is high across the chain.

> **Hardware fix:** Add a hardware token / smart-card authentication requirement to the DTC when inserted into the DTU (defense in depth beyond the Type-1 crypto alone). Add tamper-evident packaging for every DTC in physical transit.
>
> **Software fix:** Independent DTC hash verification path separate from the Type-1 crypto (the two must both pass for MC to accept the MDL); Security Gateway reconciles an out-of-band MDL manifest transmitted via a separate secure channel against the DTC-carried MDL manifest, failing closed on any mismatch.
>
> **Policy / procedure fix:** Two-person integrity for the MDL build at MPS; rotate Type-1 keys every mission cycle; MACCE provenance verification of every DTC prior to load; physical chain-of-custody log signed at each hand-off between MPS, courier, and aircraft; MACCE-witnessed load.

### R-04 Mitigation — Vendor Direct-Connect Ports (KT-C 6)

Threat / vulnerability. The Radar Service Port, EW Service Port, and FADEC direct interface bypass the Security Gateway by design. Vendor tools (RMT, EST, EFT) — while CROWS-validated in principle — become the sole trust gate at the aircraft. Adversary opportunity exists at the vendor tool build environment, on the vendor tech's laptop between CROWS validation and physical use, in a substituted or off-inventory tool, and via an insider vendor tech. This KT-C also scores at the Critical threshold (20/25); it is the single most cost-effective engineering change available to the fleet.

> **Hardware fix:** Submit a priority Engineering Change Request (ECR) to the F/A-13 Program Office to extend Security Gateway mediation to all three vendor direct-connect ports (Radar Service, EW Service, FADEC direct). Retrofit tamper-evident seals on all vendor tools with pre-connection and post-connection inspection.
>
> **Software fix:** CROWS re-attestation of the vendor tool at the aircraft (not just at build); dual-tool validation for high-consequence firmware (require two independent vendor tools to agree on the payload before FADEC or Radar update proceeds); log every vendor-tool connection to a write-once record.
>
> **Policy / procedure fix:** Mandatory MACCE-witnessed tool connection for every vendor direct-connect update on any aircraft; Commander-signed memorandum specifically lists authorized vendor technicians (already required for CASU); pre-connection inspection of the vendor tool for tamper indicators.

### R-05 Mitigation — GCS in Autonomous Mode (KT-C 7)

Threat / vulnerability. In Autonomous mode the GCS is the primary human authority in the loop. If any of the three consoles is hijacked, or if the MPS → GCS secure network is compromised, adversary can issue false overrides that remove valid MAM authority, or block valid overrides so that MAM proceeds on bad data. Either outcome is a direct H4 violation.

> **Hardware fix:** Hardware attestation of every GCS console at the start of each mission (TPM-anchored measurement of the console state; deploy only if attestation passes); physical presence detection at each console; enforce console-to-network binding so that a substituted console cannot join the GCS fabric.
>
> **Software fix:** Per-transaction credential re-authentication for any override action; MPS → GCS transport over two independent secure networks with cross-validation of the delivered MDL; independent MAM abort criteria (in the MDL) that trigger safe-mode RTB regardless of GCS state when specific thresholds are hit.
>
> **Policy / procedure fix:** Multi-console consensus required for override (Pilot/Operator AND Mission Commander must both concur); operator authentication tied to CAC + biometric + presence detection; run GCS console attestation as a formal step in the pre-mission checklist.

## 5.5 System-Wide Foundational Controls

The mitigations above are targeted at the five critical KT-C. The following cross-cutting controls apply system-wide and reduce residual risk against every KT-C on the list (including the ten not carried into the individual risk assessment). These controls should be adopted regardless of the specific mitigation status of any single KT-C.

> **Extend Security Gateway mediation to vendor direct-connect ports.** ECR to the F/A-13 Program Office. Closes the largest single as-designed bypass in the aircraft.
>
> **Two-person integrity across every load transaction.** Applies to MDL build at MPS, MSK bench loads for MAM, and any vendor-tool firmware push. Removes single-insider authorship of high-consequence changes.
>
> **CROWS re-attestation at the aircraft.** Not just at the tool-build environment. Prevents an adversary who successfully compromises a validated tool in transit from successfully connecting to the aircraft.
>
> **MACCE-witnessed vendor tool connections.** Every RMT / EST / EFT session, every session. Non-negotiable procedural control until the ECR closes the direct-connect bypass.
>
> **Rotate Type-1 keys per mission cycle.** COMSEC discipline. Compresses adversary window between key theft and detection.
>
> **Multi-console consensus for any autonomous-mode override.** Removes the single-console hijack path.
>
> **Write-once acceptance logging at the Security Gateway with MACCE monthly review.** Detection layer for attested-but-malicious payloads.
>
> **Multi-source AI model validation with adversarial red-team pre-deployment.** Ensemble check before every MAM AI model deployment.
>
> **Shadow-ROE behavior monitoring in flight with GCS positive-confirm threshold.** In-flight detection layer for autonomy drift.
>
> **Zero-day exception governance.** Zero-day updates from vendors (permitted by the documented governance model) must be reviewed by MACCE and the 91 FS Cdr before application, not just applied under CROWS advisory alone.

# 6. Scenario and Mission-Owner Action Plan

## 6.1 Representative Mission Scenarios

Five representative causal scenarios follow — one for each of the five critical KT-C. Each scenario is presented in narrative form covering the title, the HCAs involved, the commander hazards enabled, the ULs at stake, the IOTCT causal chain from initial adversary access through to loss of joint force freedom of maneuver, and the recommended countermeasures.

### Scenario 1 — Security Gateway Compromise

HCAs involved: CA4 Applied (bad PMA firmware accepted), CA7 Applied (bad DTC accepted at DTU), CA18 Applied (bad debrief sanitize). Hazards enabled: H3, H4, H5. Losses at stake: UL-1, UL-2, UL-3, UL-4, and UL-5.

Scenario. An adversary at a vendor build environment (or at a downstream supply-chain partner used by that vendor) implants malicious code into a firmware payload before the CROWS validation step. CROWS attestation either occurs on a compromised build artifact (and therefore attests the malicious payload as legitimate) or PMO distribution is separately compromised such that the payload arriving at the aircraft carries a valid signature envelope. When the maintenance crew loads that payload — via PMA on the Maintenance Ethernet Port, or via DTU insertion, or via SDLP — the Security Gateway performs its normal validation, sees a valid signature, and passes the payload through to MC, which propagates to MAM, SFE, SMS, and the datalink stack.

Consequences. The aircraft flies the mission on corrupted state. Depending on which payload was targeted, the outcome can be any combination of: MAM operates on altered ROE (H4 → UL-1, UL-3, UL-5), SFE reports false threats (H3 → mis-engagement of a friendly or a non-combatant → UL-1, UL-5), an FADEC responds unexpectedly to a throttle input (H1 → UL-2), or the fleet is grounded pending forensics (UL-4).

Recommendations. Deploy redundant hardware-attested Security Gateway pairs sourced from independent vendor chains; require dual-vendor CROWS re-attestation per update; log every accepted payload to write-once media at both gateways; MACCE monthly review of Security Gateway acceptance logs; enforce a NO-GO condition when either gateway reports any behavioral anomaly (do not wait for both to fail before grounding the aircraft). Cross-reference Section 5.4 R-01 for the detailed hardware, software, and policy fixes.

### Scenario 2 — MAM Autonomy Library Poisoning

HCAs involved: CA5 Applied (bad MSK-loaded AI model), CA9 Applied (autonomy initialized with altered ROE), CA12 Applied (autonomous engagement outside intended ROE). Hazards enabled: H3, H4. Losses at stake: UL-1, UL-3, UL-4, UL-5.

Scenario. The MSK bench, though intended to be air-gapped, is itself a target: an adversary compromises the bench environment through a supply-chain-planted utility, insider access, or an ill-controlled transport medium. Alternatively, the AI model vendor's own build environment is compromised such that a CROWS-attested model arrives with planted biases or a backdoor trigger. When the model is loaded onto MAM and the aircraft flies in Autonomous or Loyal Wingman mode, MAM authorizes engagements against a class of targets the ROE was supposed to prohibit, or (a subtler failure) refuses valid engagements at critical moments.

Consequences. Autonomy constraint violation is the direct effect (H4). The shape of the loss depends on the specific poisoning: an engage-when-should-not produces UL-1 and UL-5; a refuse-when-should produces UL-4 (mission failure) and cascading loss of joint force freedom of maneuver. Because MAM is a single LRU with authority across the whole Autonomous mode, a single poisoned model propagates across the entire mission set.

Recommendations. Multi-source AI-model validation via ensemble check pre-deployment; adversarial red-team of the model against the ROE test set before every deployment; MAM behavior sampling in flight against a shadow-ROE (any drift triggers a positive-confirm request to GCS); require GCS operator to positively confirm every autonomous engagement above a defined threat category; site the MSK bench in a dedicated SCIF with two-person integrity for every load. Cross-reference Section 5.4 R-02.

### Scenario 3 — MDL Supply-Chain Compromise via Encrypted DTC

HCAs involved: CA6 Applied (bad MDL from compromised MPS), CA7 Applied (bad DTC accepted at DTU), CA8 Applied (bad MDL pushed to GCS in Autonomous mode). Hazards enabled: H3, H4. Losses at stake: UL-1, UL-3, UL-4, UL-5.

Scenario. Adversary access at any of several points in the MDL chain permits a DTC to be produced that carries a valid Type-1 crypto envelope but a malicious MDL payload. Access points include: an insider or implant in the MPS classified enclave, a compromise of Type-1 key management, an intercept of the DTC in physical custody between MPS and the aircraft, or a compromise of the SML that is used as the alternate loading path via SDLP. Because the crypto envelope is valid, the DTU accepts the DTC, and MC distributes the payload to MAM (ROE, abort criteria, autonomy plan), SFE (threat library), SMS (weapon profiles), and the datalink stack (communications plan, crypto keys). In Autonomous mode, the same corrupted MDL is also pushed to GCS via the secure network.

Consequences. Engagement occurs on the adversary's chosen target picture. Specific outcomes range from fratricide (a friendly labeled as hostile in the threat library — UL-1), to civilian-infrastructure damage (an altered target coordinate — UL-5), to refused engagement (MAM refuses valid ROE — mission failure), to autonomy free-flight (altered abort criteria — UL-3). Because both aircraft and GCS operate on the same corrupted MDL, GCS is not a check on the aircraft in this scenario.

Recommendations. Two-person integrity for the MDL build at MPS; independent DTC hash verification path separate from the Type-1 crypto (defense in depth against key compromise); rotate Type-1 keys every mission cycle; MACCE verification of DTC provenance before load; out-of-band MDL manifest transmitted via a separate secure channel for cross-check, reconciled by the Security Gateway on load. Cross-reference Section 5.4 R-03.

### Scenario 4 — Vendor Direct-Connect Port Abuse (Radar / EW / FADEC Bypass)

HCAs involved: CA1 Applied (bad RMT firmware), CA2 Applied (bad EST firmware), CA3 Applied (bad EFT firmware). Hazards enabled: H1, H3, H5. Losses at stake: UL-1, UL-2, UL-4.

Scenario. Adversary compromises the vendor's tool-build environment for one of the three vendor-provided ruggedized laptops (RMT for AESA, EST for the EW Suite, or EFT for FADEC). Alternatively, the tech's laptop is compromised between CROWS validation and physical use at the aircraft (custody gap), or an insider tech uses a substituted off-inventory tool that carries a malicious payload. Because the vendor direct-connect ports bypass the Security Gateway by design, once the tool connects to the port there is no mediator between the malicious payload and the target LRU. Malicious firmware is loaded directly to the AESA, the EW Suite, or the FADEC.

Consequences. In flight, the radar reports false threats or fails to detect real ones (H3 → downstream H2 → UL-1); the EW Suite jams a friendly frequency or fails to jam the intended threat (H3 → mission failure); or the FADEC responds unexpectedly to a throttle input, producing an envelope excursion at combat airspeeds (H1 → UL-2 and possibly UL-1). Because these ports affect flight-critical hardware directly, this KT-C scores at the Critical threshold and is singled out as the top-priority engineering change in Section 6.2.

Recommendations. Submit a priority ECR to the F/A-13 Program Office to extend Security Gateway mediation to all three vendor direct-connect ports; mandatory MACCE-witnessed tool connection for every vendor direct-connect update; CROWS re-attestation of the vendor tool at the aircraft; dual-tool validation for high-consequence firmware; tamper-evident seals on vendor tools with pre-connection and post-connection inspection. Cross-reference Section 5.4 R-04.

### Scenario 5 — GCS Override Authority Hijacked in Autonomous Mode

HCAs involved: CA19 Applied (unauthorized GCS override), CA19 Not Applied (missed override when MAM went out of envelope), CA8 Applied (compromised MDL pushed to GCS). Hazards enabled: H4. Losses at stake: UL-1, UL-3, UL-4, UL-5.

Scenario. Adversary compromises the GCS via one of several paths: an exploit delivered over the MPS → GCS secure network transport, a SATCOM or ATDL exploit against the GCS Communications Segment, or credential theft targeting a GCS operator (Pilot/Operator, Mission Commander, or Swarm Control). Once the adversary controls a console — or, worse, controls the secure network path — they can issue false overrides that remove valid MAM authority at inopportune moments, or block valid overrides so that MAM proceeds on bad data. In Autonomous mode, either action is a direct H4 violation.

Consequences. Either MAM loses supervisory control (an override is issued that removes an in-progress engagement, converting a good outcome into an aborted one) or MAM gains unchecked authority (a needed override never arrives, and the airframe or the swarm proceeds outside envelope). Both directions of failure produce autonomy constraint violation and its downstream losses. The single-console attack path is the most cost-effective adversary approach and is specifically addressed in the recommendations.

Recommendations. Hardware attestation of GCS consoles at the start of each mission; per-transaction credential re-authentication for any override action; multi-console consensus required for override (Pilot/Operator AND Mission Commander must both concur); operator authentication tied to CAC + biometric + presence detection; MPS → GCS transport over two independent secure networks with cross-validation of the delivered MDL; independent MAM abort criteria (loaded in the MDL) that trigger safe-mode RTB regardless of GCS state when specific thresholds are reached. Cross-reference Section 5.4 R-05.

## 6.2 Final Mission-Owner Recommendations

Consolidated action plan for the 91 FS Commander (Lt Col Marcus "Specter" Vance) — copy to the 9350 ADW Commander (Brig Gen Kirby) and to ACC A6/2/3KM. Actions are grouped by feasibility horizon: Immediate (adoptable within 30 days by 91 FS + 9350 MSG action alone), Near-term (30-90 days with 9350 ADW coordination), and Program-level (\>90 days, requires PMO engineering change).

### Immediate (0 - 30 days)

> **Institute MACCE-witnessed vendor tool connections.** Every RMT / EST / EFT session on any aircraft. Applies unit-wide immediately; requires only a change to the 9350 MXG SOP and Commander memo. Addresses R-04 procedural coverage.
>
> **Enable write-once acceptance logging at both Security Gateways.** Configuration change requiring vendor advisory but no hardware. Combine with MACCE monthly review of the acceptance log. Addresses R-01 detection layer.
>
> **Establish Type-1 key rotation cadence per mission cycle.** COMSEC discipline adjustment. Coordinate with the wing COMSEC custodian. Addresses R-03 partial.
>
> **Publish updated CROWS zero-day exception procedure requiring MACCE + Cdr concurrence.** Removes the standing exception risk on any zero-day patch.

### Near-term (30 - 90 days)

> **Implement two-person integrity procedures at MPS and at the MSK bench.** Requires coordination with 9350 OSS (MPS) and 9350 MXG (MSK bench). Addresses R-02 and R-03 primary procedural controls.
>
> **Implement multi-console consensus requirement for any GCS override.** Requires GCS software configuration change from the GCS vendor; propagate through PMO. Addresses R-05 primary procedural control.
>
> **Deploy shadow-ROE behavior monitoring in flight with GCS positive-confirm threshold.** Requires MAM software update coordinated through CROWS/PMO. Addresses R-02 detection layer.
>
> **Independent DTC hash verification path (defense in depth beyond Type-1 crypto).** Software change in the DTU / Security Gateway acceptance logic. Addresses R-03 primary technical control.
>
> **MPS → GCS dual secure network transport with cross-validation.** Requires communications infrastructure coordination; ADW-level. Addresses R-05 network control.

### Program-level (\>90 days — Engineering Change Request)

> **Extend Security Gateway mediation to vendor direct-connect ports.** Priority ECR to the F/A-13 Program Office. Highest-value engineering change identified by this analysis. Addresses R-04 primary control and closes the largest single as-designed bypass.
>
> **Hardware attestation of GCS consoles per mission start.** TPM-anchored console measurement; requires GCS hardware baseline change. Addresses R-05 hardware control.
>
> **Redundant hardware-attested Security Gateway pairs from independent vendor supply chains.** Requires PMO vendor-management action to establish dual sourcing. Addresses R-01 hardware control.
>
> **Formalize AI-model multi-source validation as a PMO release-gate step.** Every MAM AI model deployed to the fleet must pass an independent-tooling ensemble validation and adversarial red-team gate prior to PMO distribution. Addresses R-02 primary control.

# 7. Operational Process Flows

## 7.1 Mission Planning Process

The F/A-13 mission-planning process produces a Mission Data Load (MDL) package at the MPS classified enclave, transports it via Type-1 encrypted DTC (or SML alternate) to the aircraft, and — in Autonomous mode — pushes a synchronized copy to the GCS via secure network. The end-to-end process is described below, with trust points and MACCE verification insertion clearly identified.

### Step 1 — MDL Build at MPS

The Mission Planning System is a workstation (or ruggedized laptop) in a classified enclave, operated by a mission planner and an intel officer. The MDL is built from the Air Tasking Order (ATO) plus weather, intel, ISR, and target-package inputs from other classified sources. The completed MDL package contains: (a) flight plan (waypoints, altitudes, routing); (b) threat library (SAMs, radars, EW profiles); (c) target packages (coordinates, aimpoints); (d) weapon profiles (fuzing, release envelopes); (e) communications plan (frequencies and crypto keys); (f) UAV / swarm tasking (if CSP used); and (g) autonomy constraints (ROE, MAM abort criteria).

*MACCE insertion: Two-person integrity for the MDL build. Every MDL is signed and countersigned within the enclave before Type-1 encryption. (Recommended mitigation.)*

### Step 2 — Type-1 Encryption and DTC Write

The completed MDL is written to a Data Transfer Cartridge — a removable solid-state module — protected with Type-1 encryption keyed by the wing COMSEC custodian on a per-mission-cycle rotation. The DTC is placed in tamper-evident packaging.

*MACCE insertion: DTC serial and hash logged; independent hash carried out-of-band. (Recommended mitigation.)*

### Step 3 — Physical Transport to the Aircraft

The DTC is physically transported from the MPS enclave to the aircraft by a cleared courier. Chain-of-custody is logged at each hand-off (MPS → courier → aircraft crew chief). Where MPS is co-located with the flight line, this may reduce to a single hand-off; where it is not, additional hand-offs are logged.

*MACCE insertion: MACCE verifies chain-of-custody log and tamper-evident seal at the aircraft prior to insertion. (Recommended mitigation.)*

### Step 4 — Alternate Load Path (SML → SDLP)

An alternate loading path uses the Secure Maintenance Laptop (SML) connected to the Secure Data Load Port (SDLP) on the external avionics access panel. This path is available when the DTC/DTU path is not, and carries the same MDL content. The SML itself is a maintenance-tool asset governed under the same CROWS/PMO chain as PMA and MSMT.

### Step 5 — On-Aircraft Ingest via DTU or SDLP

The DTC is inserted into the DTU; alternatively the SML connects to the SDLP. The Mission Computer (MC) reads the DTC or SDLP, performs Type-1 decryption, and forwards the decrypted MDL through the Security Gateway.

### Step 6 — Security Gateway Validation and Distribution

The Security Gateway validates the MDL signature, applies domain-partitioning rules, and distributes MDL components to the appropriate downstream systems: MAM (autonomy logic — AI model reference, ROE, abort criteria), SFE (threat library), SMS (weapon profiles), and Datalink stack (communications plan and crypto keys). A copy is committed to onboard mission-data storage.

*MACCE insertion: Out-of-band MDL manifest reconciled at Sec GW; failure to reconcile fails the load closed. (Recommended mitigation.)*

### Step 7 — Autonomous Mode Branch: MPS → GCS

In Fully Autonomous mode, MPS also pushes a synchronized copy of the MDL to the GCS via secure network transfer. The GCS holds the MDL to enable supervisory monitoring, override authority, and swarm coordination during the mission.

*MACCE insertion: In Autonomous mode, dual secure network transport with cross-validation prevents a single-path adversary from delivering different MDLs to aircraft and GCS. (Recommended mitigation.)*

### Step 8 — Aircrew / GCS Brief and MDL Acceptance

The PIC (Crewed or Loyal Wingman modes) or the GCS operator (Autonomous mode) conducts a mission brief that includes explicit review and acceptance of the loaded MDL — ROE, abort criteria, autonomy constraints, threat picture, and weapon profiles. Acceptance is signed on AFTO 781A (aircrew) or the equivalent GCS mission-log record.

# Appendix: Acronyms and References

## Acronyms

| **Acronym** | **Definition**                                                |
|-------------|---------------------------------------------------------------|
| ACC         | Air Combat Command                                            |
| ADW         | Air Dominance Wing                                            |
| AFDX        | Avionics Full-Duplex Switched Ethernet (also ARINC 664)       |
| AFTO        | Air Force Technical Order (AFTO 781A = aircraft acceptance)   |
| AI          | Artificial Intelligence                                       |
| A/A         | Air-to-Air                                                    |
| A/G         | Air-to-Ground                                                 |
| AMXS        | Aircraft Maintenance Squadron                                 |
| ARINC       | Aeronautical Radio, Incorporated (bus standard)               |
| ASM         | Autonomy Supervisory Module (GCS-side counterpart to MAM)     |
| AST         | As a System To (FMA-C mission-statement structure)            |
| ATDL        | Air Tasking Data Link (loyal-wingman datalink)                |
| ATO         | Air Tasking Order                                             |
| BDA         | Battle Damage Assessment                                      |
| BIT         | Built-In Test                                                 |
| BMO         | By Means Of (FMA-C mission-statement structure)               |
| BVR         | Beyond Visual Range                                           |
| C-1..C-5    | Commander-provided Constraints (this report)                  |
| CA          | Control Action                                                |
| CAC         | Common Access Card                                            |
| CASU        | Controlled Access Storage Unit                                |
| CCMD        | Combatant Command                                             |
| CES         | Civil Engineer Squadron                                       |
| CMBRE       | Common Munitions Built-in-test Reprogramming Equipment        |
| COMSEC      | Communications Security                                       |
| CROWS       | Cyber Resiliency Office for Weapon Systems                    |
| CS          | Communications Squadron                                       |
| CSP         | Collaborative Swarm Pod                                       |
| CTK         | Central Tool Kit                                              |
| DES         | Debrief Exploitation System                                   |
| DTC         | Data Transfer Cartridge                                       |
| DTU         | Data Transfer Unit                                            |
| ECR         | Engineering Change Request                                    |
| EFT         | Engine / FADEC Tool                                           |
| EO/IR       | Electro-Optical / Infrared                                    |
| EST         | EW Suite Tool                                                 |
| EW          | Electronic Warfare                                            |
| FADEC       | Full Authority Digital Engine Control                         |
| FCC         | Flight Control Computer                                       |
| FMA-C       | Functional Mission Analysis — Cyber                           |
| FSS         | Force Support Squadron                                        |
| GCS         | Ground Control Station                                        |
| GMCC        | Ground Mission Computer Cluster                               |
| GO / NO-GO  | MEL dispatch determination for combat mission                 |
| H1..H5      | Commander-provided Hazards (this report)                      |
| HCA         | Hazardous Control Action                                      |
| HMD         | Helmet-Mounted Display                                        |
| HMS         | Health Monitoring System                                      |
| HOTAS       | Hands-On Throttle and Stick                                   |
| HPM         | High-Power Microwave                                          |
| IOTCT       | In Order To Contribute To (FMA-C mission-statement structure) |
| ISR         | Intelligence, Surveillance, Reconnaissance                    |
| KT          | Key Task                                                      |
| KT-C        | Key Terrain — Cyber                                           |
| LRS         | Logistics Readiness Squadron                                  |
| LRU         | Line-Replaceable Unit                                         |
| LW          | Loyal Wingman (operating mode)                                |
| MAM         | Mission Autonomy Module                                       |
| MACCE       | Mission Assurance Cyber Coordinator Element                   |
| MC          | Mission Computer                                              |
| MDL         | Mission Data Load                                             |
| MEL         | Minimum Essential List                                        |
| MET         | Mission Essential Task                                        |
| MOS         | Maintenance Operations Squadron                               |
| MPS         | Mission Planning System (also Mission Processing System)      |
| MRT-C       | Mission-Relevant Terrain — Cyber                              |
| MSG         | Mission Support Group                                         |
| MSK         | MAM Support Kit                                               |
| MSMT        | Mission Systems Maintenance Terminal                          |
| MSS         | Mission Support Squadron                                      |
| MTOW        | Maximum Takeoff Weight                                        |
| MXG         | Maintenance Group                                             |
| MXS         | Maintenance Squadron                                          |
| NIPR        | Non-classified Internet Protocol Router network               |
| OG          | Operations Group                                              |
| OSS         | Operations Support Squadron                                   |
| PIC         | Pilot in Command                                              |
| PMA         | Portable Maintenance Aid                                      |
| PMD         | Process Model Description                                     |
| PMO         | Program Management Office                                     |
| PMV         | Process Model Variable                                        |
| PMVV        | Process Model Variable Value                                  |
| POA&M       | Plan of Action and Milestones                                 |
| RMT         | Radar Maintenance Tool                                        |
| ROE         | Rules of Engagement                                           |
| RRT         | Rapid Response Team                                           |
| SAR         | Synthetic Aperture Radar                                      |
| SATCOM      | Satellite Communications                                      |
| SCIF        | Sensitive Compartmented Information Facility                  |
| SDB         | Small-Diameter Bomb                                           |
| SDLP        | Secure Data Load Port                                         |
| SFE         | Sensor Fusion Engine                                          |
| SFS         | Security Forces Squadron                                      |
| SIPR        | SECRET Internet Protocol Router network                       |
| SML         | Secure Maintenance Laptop                                     |
| SMS         | Stores Management System                                      |
| SOP         | Standard Operating Procedure                                  |
| SOW         | Special Operations Wing                                       |
| TCA         | Time-Critical Action                                          |
| TPM         | Trusted Platform Module                                       |
| UAV         | Unmanned Aerial Vehicle                                       |
| UL          | Unacceptable Loss (UL-1..UL-5)                                |
| VMC         | Vehicle Management Computer                                   |
| WIT         | Weapons Integration Tool                                      |
| WIU         | Weapon Interface Unit                                         |
| WSO         | Weapon Systems Officer                                        |
| WVR         | Within Visual Range                                           |

## References

> F/A-13 "Peacemaker" Technical Data Sheet, Version 0.3 (CAO 4/2/2026, 22 pp) — UNCLASSIFIED, FOR TRAINING ONLY.
>
> 91st Fighter Squadron Commander's Mission Statement and Commander's Intent, briefed 21 July 2026.
>
> 9350th Air Dominance Wing organizational structure and personnel roster, as presented in the 21 July 2026 MACCE Capstone Exercise Brief.
>
> MACCE Capstone Exercise Evaluation (grading rubric), 21 July 2026.
>
> Mission Assurance Student Guide, MACCE 2026 (Course 6).
>
> Risk Assessment for Cyber Operations Student Guide, MACCE 2026 (Course 8).
>
> AFPAM 63-128, Integrated Life Cycle Management (Air Force guide to risk management principles applied to weapon-system risk register scoring).
>
> DoDI 3020.45, Mission Assurance Construct (Mission Assurance principles and terminology).
