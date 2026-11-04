<img src="media/image1.jpg" style="width:6.5in;height:4.33333in" />

Technical Data Sheet

Version 0.3 – 4/2/2026

<table style="width:99%;">
<colgroup>
<col style="width: 99%" />
</colgroup>
<tbody>
<tr>
<td style="text-align: center;"><p>IMPORTANT NOTICE:</p>
<p>THIS IS NOT A REAL AIRCRAFT. THE SYSTEMS AND CONFIGURATION WERE GENERATED FROM PUBLICLY AVAILABLE INFORMATION AND REPRESENTS BOTH REAL AND IMAGINED CAPABILITIES. NO SENSITIVE INFORMATION ABOUT THOSE SYSTEMS THAT DO EXIST IS INCLUDED IN THIS DOCUMENT. WE MADE IT ALL UP.</p></td>
</tr>
</tbody>
</table>

**Table of Contents**

[***Executive Summary: 3***](#executive-summary)

[***Physical Characteristics 3***](#physical-characteristics)

[***Munitions Capabilities 4***](#munitions-capabilities)

> [**Collaborative Swarm Pod overview: 4**](#collaborative-swarm-pod-overview)
>
> [Control and Coordination of Swarm Drones 5](#control-and-coordination-of-swarm-drones)
>
> [UAV Recovery: 6](#uav-recovery)
>
> [**Restrictions to munitions options based on operating mode: 7**](#restrictions-to-munitions-options-based-on-operating-mode)

[***System Architecture 7***](#system-architecture)

> [**Key Processing Nodes: 7**](#key-processing-nodes)
>
> [**Devices on the 1553 Bus: 8**](#devices-on-the-1553-bus)
>
> [Devices on the 1760 bus: 9](#devices-on-the-1760-bus)
>
> [**Devices on ARINC 664 (AFDX): 10**](#devices-on-arinc-664-afdx)
>
> [**Mission Autonomy Module (MAM): 11**](#mission-autonomy-module-mam)
>
> [**Ground Control Station (GCS): 12**](#ground-control-station-gcs)

[***Mission Timeline 13***](#mission-timeline)

> [1. Mission Data Load (pre-flight) 13](#_heading=h.cepbhm573nrv)
>
> [2. Post-Mission Data Removal (Intel/Debrief) 14](#_heading=h.zez00oc8kqsc)
>
> [3. Log and Diagnostic Data Removal 15](#_heading=h.n4jm5lkwhg5c)

[***Maintenance tools for onboard systems: 16***](#maintenance-tools-for-onboard-systems)

> [**Maintenance Tools: 16**](#maintenance-tools)
>
> [**Maintenance Tool Security: 17**](#maintenance-tool-security)
>
> [**Maintenance Tool Updates: 17**](#maintenance-tool-updates)

[***Minimum Essential List: 18***](#minimum-essential-list)

# Executive Summary:

The **F/A-13 Peacemaker** is a next-generation, multi-role fighter/attack aircraft designed to bridge the gap between current fifth-generation air superiority platforms like the F-22 Raptor and multirole strike platforms like the F-35 Lightning II. With a combination of stealth-optimized airframe, internal weapons bays, and high-bandwidth sensor fusion, the F/A-13 provides both air dominance and precision strike capabilities. Its modular autonomy architecture allows it to operate in traditional crewed mode, as a loyal wingman under a lead aircraft, or fully autonomously under remote human supervision. This flexibility gives the U.S. Air Force the ability to project power in contested environments while maintaining operational redundancy, reducing risk to human pilots, and extending mission persistence through deployable UAV systems.

Positioned strategically between the F-22 and F-35 in capability and role, the F/A-13 combines high-speed supercruise, advanced sensor fusion, and multi-mission payload capacity with a significant operational endurance advantage enabled by distributed UAV operations. Through integration with collaborative swarm systems, the aircraft can project ISR, electronic warfare, and strike effects across a wider area and duration, mimicking key aspects of platforms such as the MQ-1 Predator and RQ-4 Global Hawk while retaining the survivability and responsiveness of a fighter. Its internal **Mission Autonomy Module (MAM)** allows seamless transitions between manned and unmanned operations, making it an ideal platform for future combat concepts including swarm integration, networked strike operations, persistent sensing, and AI-assisted targeting. The F/A-13 represents a synthesis of stealth, survivability, distributed autonomy, and mission persistence, providing the USAF with a highly flexible and adaptable tool for modern and near-future battlefields.

# Physical Characteristics

<table>
<colgroup>
<col style="width: 56%" />
<col style="width: 43%" />
</colgroup>
<tbody>
<tr>
<td style="text-align: left;"><p><strong>Dimensions</strong></p></td>
<td style="text-align: left;"><p><strong>Fuel, and Range</strong></p></td>
</tr>
<tr>
<td style="text-align: left;"><ul>
<li><p>Length: 64.5 ft (19.7 m)</p></li>
<li><p>Wingspan: 45.8 ft (14.0 m)</p></li>
<li><p>Height: 15.2 ft (4.6 m)</p></li>
<li><p>Wing Area: 565 sq ft (52.5 m²)</p></li>
<li><p>Empty Weight: ~41,000 lb (18,600 kg)</p></li>
<li><p>Internal Fuel Weight: ~22,000 lb (9,980 kg)</p></li>
<li><p>Max Takeoff Weight (MTOW): ~78,000 lb (35,380 kg)</p></li>
<li><p>Payload Capacity:</p>
<ul>
<li><p>Internal (Stealth): ~5,500 lb</p></li>
<li><p>External (Beast Mode): ~22,000 lb</p></li>
</ul></li>
</ul></td>
<td style="text-align: left;"><ul>
<li><p>Internal Fuel Capacity: ~3,300 gallons (12,500 L)</p></li>
<li><p>Combat Radius: ~750–900 nmi (internal weapons, high survivability profile)</p></li>
<li><p>Ferry Range: ~1,800+ nmi (with external tanks)</p></li>
<li><p>Aerial refueling: Boom receptacle (USAF standard)</p></li>
</ul></td>
</tr>
</tbody>
</table>

# Munitions Capabilities

- Weapons Bays: There are 2 Main bays and 2 Side bays.

  - The Main bays support 2x AMRAAM-class or 4x SDB-class or 1 Large Weapon (JASSM-class)

  - The Side bays support 1 AIM-9X each

- External Stations: There are 12-14 Hardpoints, 8-10 on the wings and 2-4 on the fuselage

- Supported Munitions:

  - Beyond Visual Range (BVR) Air-to-Air Munitions:

    - AIM-120 AMRAAM

    - AIM-260 JATM (next-gen BVR)

  - Within Visual Range (WVR) Air-to-Air Munitions:

    - AIM-9x Sidewinder

  - Air-to-Ground Precision Guided Munitions:

    - GBU-31/32 JDAM

    - GBU-53/B StormBreaker (in-flight retargeting via 664 datalink)

  - Air-to-Ground Stand-off Munitions:

    - AGM-158 JASSM/LRASM

  - Close Air Support/Tactical

    - AGM-65 Maverick

  - Loitering & Autonomous Munitions

    - Networked: Air-launched Loitering Munition (ALLM) (AI assisted target search)

    - Collaborative Swarm Pods: Swarm Drone Dispenser

  - Electronic & Non-Kinetic Payloads

    - Next-Gen Jammer Pod (EW Suite)

    - High-Power Microwave (HPM) pod (disables electronics)

  - Internal Gun System: 25mm internal cannon

## Collaborative Swarm Pod overview:

The **Collaborative Swarm Pod (CSP)** is an external smart dock and launch pod designed to host, initialize, and deploy multiple small UAVs in complex battlespace scenarios. It is fully integrated with the **Mission Computer (MC)** and **Mission Autonomy Module (MAM)**, which remain the authoritative controllers for swarm operations in both crewed and autonomous modes. The pod can be mounted on standard wing or fuselage hardpoints and interfaces with the aircraft via **MIL-STD-1760** for stores management and **ARINC 664** for pre-launch programming, status, and data exchange.

**Functions**:

- Deploys UAVs for ISR, electronic warfare (EW), decoy operations, and precision strike missions.

- Provides power, initialization, mission data loading, and health/status monitoring for UAVs while docked.

- Supports pre-launch configuration and optional pre-launch RF link establishment between UAVs and the aircraft mission system.

- Executes controlled UAV launch sequences under SMS/WIU authority via MIL-STD-1760.

- Does not perform mission-level swarm control after UAV deployment.

**UAV Physical Description**

- Length: 5.5 ft (1.68 m)

- Wingspan: 6.2 ft (1.9 m)

- Height: 1.2 ft (0.37 m)

- Weight: ~75 lb. (34 kg) fully fueled, with payload

- Propulsion: Electric ducted fan

- Launch Method: Canister ejection from CSP, small wings deploy mid-air

**Payload & Sensors**

- ISR: Mini EO/IR camera, synthetic aperture radar (SAR) sensor

- EW: Mini jammer for communications or radar deception

- Strike: Small precision micro-munitions (~10 lb. each)

- Communications: Encrypted RF mesh network linking UAVs with the host aircraft and other swarm assets

### Control and Coordination of Swarm Drones

**Swarm Control**: Hosted in the **MC/MAM**, with decentralized autonomy on each UAV.

- Each UAV maintains autonomous flight while receiving tasking and updates directly from the aircraft via RF communications.

- A lead UAV may provide local coordination and data aggregation within the swarm but is not the primary command authority.

**Host Integration**:

- UAVs communicate directly with the aircraft via RF links through the aircraft communications systems; data is processed by the MC and distributed over the ARINC 664 network.

- The pilot or MAM can task, retask, or override individual UAVs or the swarm in real-time.

**Autonomy Modes**:

- Pre-planned: UAVs execute assigned mission profiles after release.

- Semi-autonomous: UAVs respond to mission conditions with MC/MAM oversight.

- Fully autonomous: UAVs coordinate locally while remaining bounded by mission constraints and aircraft-provided tasking.

<img src="media/image7.png" style="width:5.08276in;height:3.38851in" />

### UAV Recovery:

The F/A-13 *Peacemaker* is designed to support multiple UAV end-of-mission pathways, not just one. The UAVs are primarily expendable, but the system supports recoverable behavior in specific cases depending on mission configuration.

|  |  |  |  |
|:---|:---|:---|:---|
| **UAV Type** | **Default Fate** | **Recovery Option** | **Notes** |
| **Strike** | Expendable | No | One-way mission |
| **EW / Decoy** | Expendable | Rare | Attritable |
| **ISR (low-cost)** | Expendable | Optional | Mission-dependent |
| **ISR (high-value)** | Recoverable | Yes | Ground/parachute |
| **Relay / Network** | Persistent | Possible | May remain in theater |

Regardless of recovery option, all UAVs are equipped with encrypted storage and a Zeroize/Self-wipe capability.

## Restrictions to munitions options based on operating mode:

Some munitions cannot be used or are strictly controlled while the aircraft is in autonomous mode. This is due to control, legal, and targeting requirements:

| Munition Type/MODE | Crewed | Loyal Wingman | Autonomous |
|:---|:--:|:--:|:--:|
| Air-to-Air Missiles | Allowed | Allowed | <span class="mark">Conditional</span> |
| Precision Bombs | Allowed | Allowed | <span class="mark">Controlled</span> |
| Air-to-Ground Missiles | Allowed | Allowed | <span class="mark">Limited</span> |
| Anti-Radiation | Allowed | Allowed | Allowed |
| Gun | Allowed | <span class="mark">Limited</span> | **<span class="mark">NOT ALLOWED</span>** |
| Swarm UAVs | Allowed | Allowed | Allowed |
| Electronic Attack | Allowed | Allowed | Allowed |

- ***Allowed** – The munition may be employed in this mode without restriction under normal operating procedures.*

- ***Controlled** – The munition may be used, but only with positive human authorization or supervisory control.*

- ***Conditional** – The munition may be used only when specific predefined conditions or criteria are met.*

- ***Limited** – The munition may be used in a restricted manner (e.g., reduced functionality, modes, or employment envelope).*

- ***Not Allowed** – The munition may not be employed in this mode under any circumstances.*

# System Architecture

The three core networks present onboard the F/A-13 are:

- MIL-STD-1553B (C2 Backbone)

- MIL-STD-1760 (Weapons Interface Bus)

- ARINC 664/AFDX (High-bandwidth data network)

## Key Processing Nodes:

- **Mission Computer (MC)**: The MC is the heart of the system. It communicates on both the 664 and 1553 buses and is the authority for tactical decision-making and sensor fusion coordination. Acts as the Bus Controller for all connected buses.

- **Vehicle Management Computer (VMC)**: The VMC is responsible for coordinating flight control laws, engine operations, and overall health monitoring.

- **Sensor Fusion Engine (SFE)**: The SFE combines radar, EO/IR, and EW data to generate unified track files.

- **Stores Management System (SMS)**: The SMS is responsible for weapons inventory and control.

- **Mission Autonomy Module (MAM)**: The *removable* MAM is responsible for autonomous mission execution.

How the key processing nodes are interconnected:

<img src="media/image4.png" style="width:6.5in;height:1.25in" />

## Devices on the 1553 Bus:

The 1553 bus is a deterministic, redundant bus used for critical control and status information.

|  |  |  |  |
|:---|:---|:---|:---|
| **Device** | **Role** | **Talks to (bus)** | **Outputs** |
| **Mission Computer (MC)** | Aircraft control | SFE (664), MAM (664 + 1553), HUD/HMD (664), SMS (1553) | Target Assignments, weapons release authorization |
| **Vehicle Management Computer (VMC)** | Flight control | Flight Control Computers (1553), Engine FADEC (1553), MC (1553) | Control surface commands, Engine thrust requests |
| **Stores Management System (SMS)** | Weapon inventory and control | MC (1553), WIU (1553) | Weapon readiness, Launch commands |
| **Flight Control Computers (FCC)** | Executes control laws | VMC (1553) | Actuator commands |
| **Engine FADEC** | Engine control | VMC (1553) | Fuel flow, thrust control |
| **Health Monitoring System (HMS)** | BIT, fault logging | All major LRU (1553), MX interface (664) | Fault reports |
| **Mission Autonomy Module (MAM)** | Autonomous mission execution | MC (1553 + 664), Datalink (664) | Command overrides, Engagement decisions (subject to ROE) |

How the devices are interconnected on the 1553 bus:

<img src="media/image8.png" style="width:6.5in;height:1.91667in" />

## Devices on the 1760 bus:

The 1760 bus provides a digital interface for smart weapons and provides power and data between the aircraft and the munition.

|  |  |  |  |
|:---|:---|:---|:---|
| **Device** | **Role** | **Talks to (bus)** | **Outputs** |
| **Weapon Interface Unit (WIU)** | Protocol translator between 1553 SMS and 1760 Stores | SMS (1553), Weapons (1760) | relays between the two busses |
| **Smart Munitions (e.g., JDAM, SDB, AIM-series)** | Execute strike | SMS(WIU) (1760) | Target coordinates, Terminal guidance updates (via 664 relay) |
| **Weapons Pylons/Stations** | Physical interface | SMS(WIU) (1760) | Weapon presence, status |
| **Collaborative Swarm Pod (CSP)** | Docking for UAVs | SMS(WIU)(1760), ARINC 664 | UAV presence, pre-launch status |

How the devices are interconnected on the 1760 bus:

<img src="media/image6.png" style="width:6.5in;height:2.26389in" />

## Devices on ARINC 664 (AFDX):

AFDX is a high-bandwidth, ethernet-based bus used for sensor data, video, and AI processing

|  |  |  |  |
|:---|:---|:---|:---|
| **Device** | **Function** | **Talks to (bus)** | **Outputs** |
| **Sensor Fusion Engine (SFE)** | Combines radar, EO/IR, and EW data | Radar (664), EO/IR (664), EW Suite (664), MC (664), MAM (664) | Unified Track Files |
| **AESA Radar** | Air/Ground targeting | SFE (664) | Track data, SAR maps |
| **EO/IR Targeting System** | Visual/IR targeting | SFE (664) | Imagery, laser designation |
| **EW Suite** | Threat detection and jamming | SFE (664), MAM (664) | Threat libraries, Countermeasure deployment cues |
| **Datalink Systems (Link-16/ATDL)** | External Comms | MC (664), MAM (664), Remote aircraft/ground station (Link-16), Loyal Wingman (ATDL) | Tasking updates, sensor sharing |
| **Glass Cockpit Displays** | Pilot interface | MC (664) | Pilot inputs (via HOTAS -\> MC) |
| **Helmet-mounted Display (HMD)** | Cueing and targeting | MC (664) | Line-of-sight targeting |
| **Ground Control Interface (Autonomous mode)** | Remote pilot oversight | Datalink (664), MAM (664) | Control channel for remote pilot in autonomous mode |
| **SATCOM** | High-bandwidth messaging | MC (664), External radio/antenna | Beyond LOS voice/data communications |
| **LOS(HF/VHF/UHF)** | Voice/Radio communications | MC (664), External radio/antenna | Voice communications |
| **Collaborative Swarm Pod (CSP)** | Docking for UAVs | SMS(WIU)(1760), ARINC 664 | UAV pre-launch status and programming |

How the devices are connected to the AFDX:

<img src="media/image2.png" style="width:6.5in;height:2.04167in" />

The following image is an overall bus diagram, showing the external interface access to MC/MAM/VMC:

<img src="media/image3.png" style="width:6.5in;height:3.38889in" />

The following image is a zoom in on the external, "through-the-skin" interfaces:

<img src="media/image5.png" style="width:6.5in;height:2.52778in" />

## Mission Autonomy Module (MAM):

The **Mission Autonomy Module (MAM)** on the F/A-13 *Peacemaker* is a rugged, line-replaceable computing module that provides onboard autonomous mission execution, sensor-driven decision-making, and swarm coordination capability. Physically, the MAM is installed in the forward avionics bay and measures approximately 54 × 30 × 24 inches, with a weight ranging from 650 to 900 pounds depending on configuration. It is mounted on a rail-based quick-install system with blind-mate electrical and data connectors, allowing rapid installation or removal in under 30 minutes. The unit is liquid-cooled via the aircraft’s environmental control system and includes EMI-shielded construction for survivability in high-threat environments.

Internally, the MAM contains a high-performance compute cluster (CPU and GPU/TPU accelerators), encrypted mission data storage, secure processing elements for authentication and key management, and multiple network interface modules. It connects primarily to the aircraft via dual-redundant ARINC 664 (AFDX) interfaces for high-bandwidth data exchange with sensors, datalinks, and the mission computer, and secondarily via MIL-STD-1553 for command, control, and health monitoring. All external data and command pathways to the MAM are mediated through the aircraft’s Security Gateway, ensuring strict enforcement of authentication, data validation, and domain separation.

Operationally, the MAM functions as the aircraft’s autonomy engine, enabling mission planning, target selection, engagement support, and collaborative swarm control while remaining subordinate to the Mission Computer and overarching system safety constraints. It can operate in active, standby, or removed configurations, allowing the aircraft to flex between fully autonomous and traditionally crewed roles. Designed for modularity, security, and scalability, the MAM provides a plug-in capability that can be upgraded independently of the airframe while maintaining strict integration with flight, mission, and weapons systems.

## Ground Control Station (GCS):

A **distributed mission control system** designed to supervise autonomous operations, manage collaborative assets (including swarm UAVs), and enforce human authority over lethal decisions when required. The GCS can be deployed at a fixed site, in a mobile shelter, or even as a set of distributed nodes.

The GCS has three working consoles:

1.  **The Pilot/Operator Console**: Basically, a cockpit on the ground, using similar control interfaces to allow the pilot to interact with the aircraft just as if they were in the air. From here the pilot or operator can monitor the state of the aircraft, override any autonomy decisions, approve or deny weapons release, and change mission objectives.

2.  **The Mission Commander Console**: Provides the tactical map and sensor fusion display, and is used to assign targets, define ROE boundaries, and coordinate with other assets.

3.  **The Swarm Control Console**: A dedicated interface for UAV swarm control. It allows the swarm behavior (ISR, EW, Strike) to be set or changed, it allows the pilot/operator to monitor the status of each UAV individually and adjust autonomy levels as needed.

The rest of the GCS is made up of components that interact with the aircraft:

1.  **The Ground Mission Computer Cluster (GMCC)**: High-performance compute nodes with AI-assisted decision support. These nodes mirror the operations of the onboard Mission Computer.

2.  **Autonomy Supervisory Module (ASM)**: The ground-side counterpart to the onboard MAM, this module validates autonomy decisions, enforces ROE constraints, and provides override authority.

3.  **Communications Segment**: Consists of ground terminals for multi-band SATCOM, LOS Datalink, and a tactical network gateway, allowing for bridging to other aircraft, command networks, and ISR platforms.

The GCS' role will vary based on how the aircraft is deployed. The GCS can monitor and be an advisory during crewed flight. While in Loyal Wingman mode, the GCS acts as the secondary control, ready to take over should the primary (manned) aircraft lose connectivity. In Autonomous mode, the GCS is the primary human authority in the loop.

# Mission Timeline

The next section details the mission execution workflow for the F/A-13 Peacemaker across crewed, loyal wingman, and autonomous operating modes.

## Mission Data Load (pre-flight)

A mission planner and intel officer using the Mission Planning System workstation or ruggedized laptop from a classified enclave develop the mission data from the ATO. Part of the process includes gathering data from sources other than the ATO, such as Weather and Intel.

The result of this step in the workflow is a Mission Data Load (MDL) package, which includes:

- Flight plan (waypoints, altitudes, routing)

- Threat library (SAMs, radars, EW profiles)

- Target packages (coordinates, aimpoints)

- Weapon profiles (fuzing, release envelopes)

- Communications plan (frequencies, crypto keys)

- Swarm/UAV tasking (if CSP used)

- Autonomy constraints (ROE, abort criteria for MAM)

In *crewed* and *loyal wingman* modes, the MDL is loaded onto the Data Transfer Cartridge (DTC) to transfer to the aircraft. The DTC is a removable solid-state module, encrypted with Type-1 encryption, and loaded into the Data Transfer Unit (DTU) on the aircraft.

In *autonomous* mode, the MDL is distributed to both the aircraft and the Ground Control Station (GCS). The aircraft receives the MDL via DTC or Secure Data Load Port, while the GCS receives the same mission baseline via secure network transfer from the Mission Planning System.

As an alternative loading method, a Secure Maintenance Laptop (SML) can connect via the Secure Data Load Port on the external avionics access panel to load the mission files.

Regardless of the loading method, all files are authenticated via the Security Gateway and loaded into the appropriate system/subcomponent.

The data flow for this step:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td style="text-align: center;"><p>Mission Planner (MPS)<br />
↓<br />
Encrypted MDL written to DTC (and network distribution to GCS in autonomous mode)<br />
↓<br />
DTC inserted into aircraft or SDLP connection established<br />
↓<br />
Mission Computer (MC)<br />
↓ (ARINC 664)<br />
Security Gateway (validation + partitioning)<br />
↓<br />
Distributed to</p>
<ul>
<li><p>MAM (autonomy logic)</p></li>
<li><p>SFE (threat library)</p></li>
<li><p>SMS (weapon profiles)</p></li>
<li><p>Datalink system (network plan)<br />
↓<br />
Stored in onboard mission data storage</p></li>
</ul></td>
</tr>
</tbody>
</table>

In *autonomous* mode, the GCS stores a synchronized copy of the MDL for supervisory control and mission monitoring.

## Post-Mission Data Removal (Intel/Debrief)

An intel analyst and debrief team uses the Debrief Exploitation System (DES) in a secure facility to examine and assess the post mission information.

In *crewed mode*, debrief data is collected entirely post-flight from onboard systems.

In *loyal wingman* mode, a portion of mission data (such as status, tracks, and limited BDA) may be transmitted in-flight to the lead aircraft, but full data extraction still occurs post-flight.

In *autonomous* mode, mission data is partially transmitted in real-time to the GCS during execution, providing a continuous operational picture; however, full-resolution data and complete system records are still retrieved post-flight from the aircraft.

In addition to pilot or operator inputs, the debrief team collects the following information:

- Sensor recordings (radar, EO/IR, EW)

- Track files (air & ground)

- Weapon employment data

- Battle Damage Assessment (BDA/BDM estimates)

- Datalink traffic (network picture)

- UAV swarm data (if used)

This data is extracted from the aircraft via the DTC, or the Secure Data Load Port in the avionics bay. The data is encrypted at rest and sanitized by the MC for classification domains. The security gateway contributes by ensuring that intel and system performance data are kept separate.

The data flow for this step:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td style="text-align: center;">Onboard Mission Data Recorder<br />
↓<br />
Mission Computer (MC)<br />
↓<br />
Security Gateway (sanitize/export rules)<br />
↓<br />
DTC or SDLP<br />
↓<br />
Debrief Exploitation System (DES)<br />
↓<br />
Intel analysis / BDM evaluation</td>
</tr>
</tbody>
</table>

In *autonomous* mode, GCS-collected data may supplement the debrief but does not replace aircraft-derived data.

## Log and Diagnostic Data Removal

The maintenance team or an avionics technician removes the log and diagnostic data using the PMA or vendor-specific diagnostic tools.

This process is consistent across crewed, loyal wingman, and autonomous modes, as maintenance data is always considered authoritative when retrieved directly from the aircraft.

The types of data removed include:

- Built-In Test (BIT) results

- Fault codes (LRU-level)

- Health Monitoring System (HMS) logs

- Engine performance (FADEC logs)

- Bus traffic/error logs (1553 / 664 / 1760)

- Thermal and power system logs

The data is extracted using the PMA via the connection to the Maintenance Ethernet Port in the avionics bay. Some sub-systems also have direct access connections, such as the FADEC direct interface, the Radar maintenance port, and the EW Suite vendor port.

The data flow for this step:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td style="text-align: center;">Technician (PMA)<br />
↓<br />
Maintenance Port (Ethernet)<br />
↓<br />
Security Gateway (sanitize/export rules)<br />
↓<br />
Mission Computer (MC)<br />
↓<br />
Vehicle Mgmt Computer (VMC)<br />
↓<br />
Health Monitoring System (HMS)<br />
↓<br />
Subsystem LRUs: (FCC, FADEC, Radar, EW)<br />
↓<br />
Logs returned to PMA</td>
</tr>
</tbody>
</table>

In *autonomous* mode, GCS monitoring data may assist in troubleshooting but is not used as a substitute for onboard maintenance logs.

# Maintenance tools for onboard systems:

Besides the normal engine and airframe maintenance tools (maintaining the physical aircraft), there are several tools used to maintain the electronic systems onboard the F/A-13.

The maintenance philosophy of the F/A-13 is to use a modular, condition-based approach built around Line Replaceable Units (LRUs), Built-In Tests (BITs) and the onboard Health Monitoring System (HMS). A key part of this philosophy is the "Pluck and Chuck" approach; in other words, replace LRUs versus repairing them on-aircraft. LRUs will be sent to higher-level maintenance for repair away from the flight-line. In addition, data and BIT will be absolutely verified before any action is taken.

There will always be a strict separation between maintenance and mission domains, and all maintenance tools will be strictly controlled.

## Maintenance Tools:

- The **Portable Maintenance Aid (PMA)** is a ruggedized government laptop that interfaces the aircraft via the Maintenance Ethernet Port and is used to access HMS logs, run BIT, query various subsystems (MC, VMC, FCC, FADEC, SMS), and upload/download maintenance data.

- The **Mission Systems Maintenance Terminal (MSMT)** is a ruggedized government laptop that hosts multiple approved mission-system applications as containers. The MSMT can access the aircraft through different interfaces: The Maintenance Ethernet Port is the primary interface, and it can access the 1553 bus for certain requirements. The loaded tools include:

  - Radar high-level diagnostics

  - EO/IR basic calibration tools

  - Sensor fusion verification tools

  - Datalink configuration tools

  - MAM operational-level interface

- The **Weapons Integration Tool (WIT)** is a ruggedized government laptop used to test and validate munitions (essentially, a modernized CMBRE device). It connects through the skin via the Weapon Load Interface in the avionics panel, or uses added 1760 adapters and *connects directly to smart munitions*. The WIT provides weapon presence and identification, BIT, and station/pylon diagnostics.

- The **Radar Maintenance Tool (RMT**) is a vendor-provided ruggedized laptop that connects via the *Radar Service Port (direct connect)* to perform calibration and tuning of the radar suite.

- The **EW Suite Tool (EST)** is a vendor-provided ruggedized laptop that connects via the *EW Service Port (direct connect)* to perform calibration and tuning of the EW suite.

- The **Engine/FADEC tool (EFT)** is a vendor-provided ruggedized laptop that connects via the *FADEC (direct connect)* to perform low-level diagnostics on the FADEC.

- The **MAM Support Kit (MSK)** is a multi-component, highly controlled maintenance and development toolkit consisting of a secure support terminal, interface hardware, and a bench test environment that allows full lifecycle management of the Mission Autonomy Module. While limited interaction is possible on-aircraft through the *Maintenance Ethernet Port* (and Security Gateway), all high-authority functions—such as software updates, AI model changes, and deep diagnostics—are performed off-aircraft in a controlled, air-gapped environment to ensure safety, security, and system integrity.

## Maintenance Tool Security:

Security for the maintenance tools is applied at several levels, intended to protect both the aircraft and the tool. From an electronic standpoint, it can be said that the system is like a zero-trust environment in that nothing is assumed about any component, and certificates and the like are validated for each transaction.

All the specialized tools are stored in Controlled Access Storage Units (CASU) managed by the Central Tool Kit (CTK). They are stored in locked racks that allow for easy visual inventory without unlocking the container. All the tools are serialized and tracked electronically for check-in and check-out, and there is a memorandum signed by the Commander indicating exactly who is allowed to sign out the equipment.

All of the laptops, government or vendor-provided, are protected at runtime through several mechanisms, including secure boot, encrypted onboard storage, anti-virus/malware and digital certificates.

## Maintenance Tool Updates:

To ensure security and survivability of the aircraft, no updates to maintenance tools is trusted outright. Everything must be validated. CROWS will validate all updates before distributing them through the PMO. There may be individual cases where a near-real-time update from a vendor is required to solve for an exploited zero day.

When the tool is connected to the aircraft, it again goes through validation (the aircraft does not trust it), using various certificates.

# Minimum Essential List:

Category defines the maximum allowable repair period:

- CAT A: Time-limited repair (hours/days specified)

- CAT B: ≤ 3 days

- CAT C: ≤ 10 days

- CAT D: ≤ 120 days

- “GO/NO-GO” reflects dispatch for combat mission, not ferry/training

Core Compute and Control:

| System | Qty Installed | Qty Required | MEL Dispatch | Category | Operational Restrictions |
|----|----|----|----|----|----|
| Mission Computer (MC) | 2 | 1 | GO | B | Reduced multi-targeting, limited swarm ops |
| Mission Autonomy Module (MAM) | 1 | 0–1 (mode dependent) | GO (Crewed only) | D | No autonomy or swarm control |
| Vehicle Mgmt Computer (VMC) | 2 | 1 | GO | A (24 hr) | Reduced automation |
| Flight Control Computers (FCC) | 3 | 2 | GO | A (12 hr) | Reduced maneuver envelope |

Sensor Systems (ARINC 664)

| System | Qty Installed | Qty Required | MEL Dispatch | Category | Operational Restrictions |
|----|----|----|----|----|----|
| AESA Radar | 1 | 0 | GO | C | No BVR targeting |
| EO/IR Targeting | 1 | 0 | GO | C | No visual ID / laser designation |
| Sensor Fusion Engine (SFE) | 2 | 1 | GO | B | Degraded track quality |
| Electronic Warfare Suite | 1 | 0 | GO | B | No jamming / threat geolocation |

Communications and Datalink

| System | Qty Installed | Qty Required | MEL Dispatch | Category | Operational Restrictions |
|----|----|----|----|----|----|
| Datalink (Link-16 / Tactical Net) | 2 | 0–1 (mode dependent) | GO (Crewed only) | C | No networked targeting / remote control |
| Secure Communications | 2 | 1 | GO | C | Reduced redundancy |

Weapons Systems (1553/1760)

| System | Qty Installed | Qty Required | MEL Dispatch | Category | Operational Restrictions |
|----|----|----|----|----|----|
| Stores Mgmt System (SMS) | 2 | 1 | GO | B | Limited simultaneous weapon control |
| Weapon Interface Unit (WIU) | 2 | 1 | GO | C | Reduced station availability |
| Internal Gun | 1 | 0 | GO | D | Gun unavailable |
| External Stations | 12–14 | Mission dependent | GO | — | Reduced payload capacity |

Autonomy and Swarm Systems

| System | Qty Installed | Qty Required | MEL Dispatch | Category | Operational Restrictions |
|----|----|----|----|----|----|
| Mission Autonomy Module (MAM) | 1 | Required for autonomy | NO-GO (if required) | — | No autonomous ops |
| Collaborative Swarm Pod (CSP) | Optional | 0 | GO | — | No swarm capability |
| Swarm Control Function | MAM-based | 1 (if CSP used) | NO-GO (if CSP used) | — | UAVs unusable |

Human Interface

| System | Qty Installed | Qty Required | MEL Dispatch | Category | Operational Restrictions |
|----|----|----|----|----|----|
| Glass Cockpit Displays | 2–3 | 1 | GO | A (24 hr) | Reduced situational awareness |
| Helmet Mounted Display (HMD) | 1 | 0 | GO | D | No off-boresight targeting |

Network & Security

| System | Qty Installed | Qty Required | MEL Dispatch | Category | Operational Restrictions |
|----|----|----|----|----|----|
| Security Gateway | 2 | 1 | GO | B | Reduced throughput |
| Security Gateway (both failed) | 2 | 1 | NO-GO | — | No safe cross-bus comms |

Propulsion & Flight Critical

| System | Qty Installed | Qty Required | MEL Dispatch | Category | Operational Restrictions |
|----|----|----|----|----|----|
| Engines | 2 | 2 (combat) | NO-GO (combat) | — | Single engine = ferry only |
| Engines (ferry) | 2 | 1 | GO | A | Ferry only |
| FADEC | 2 | 1 per engine | NO-GO | — | Engine unsafe |

Maintenance & Diagnostics

| System | Qty Installed | Qty Required | MEL Dispatch | Category | Operational Restrictions |
|----|----|----|----|----|----|
| Health Monitoring System (HMS) | 1 | 0 | GO | D | No automated fault reporting |
| Maintenance Interface Ports | Multiple | 0 | GO | — | Manual servicing required |

Mission Level Summary Table

| Capability         | Required Systems                | Dispatch Status       |
|--------------------|---------------------------------|-----------------------|
| Full Combat        | MC, FCC (≥2), VMC, SMS, Gateway | GO                    |
| Autonomous Mission | \+ MAM, Datalink                | GO only if present    |
| Loyal Wingman      | \+ Datalink, MAM                | GO only if present    |
| ISR Only           | Minimal sensors + MC            | GO (degraded allowed) |
| Ferry Flight       | 1 engine, minimal avionics      | GO                    |
