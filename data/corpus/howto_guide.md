**UNCLASSIFIED // FOR TRAINING ONLY**

**The MACCE's Guide to\
Functional Mission Analysis — Cyber (FMA-C)**

*A step-by-step methodology for any airframe,\
illustrated with the CF-189 exercise*

**Cameron Partlow**

Personal study guide written during the ACC MACCE course. All platforms notional.

14 July 2026

Version 2.0

*A general-purpose FMA-C methodology guide organized around the Concept → Recipe → Worked Example teaching pattern. Airframe-neutral in the body; CF-189 in the yellow callouts.*

**Table of Contents**

**Part 1 — Foundations: What to Understand Before You Touch the Workbook**

------------------------------------------------------------------------

This first part is background. It exists because MACCE students who dive straight into the Excel template tend to get overwhelmed - they end up filling cells by pattern-matching without knowing what the FMA-C is actually trying to prove. Read these five short sections once, then come back to them whenever a later step feels arbitrary.

**1.1 What is FMA-C, and why does it exist?**

Functional Mission Analysis - Cyber (FMA-C) is a structured analytical process that maps a warfighting mission down to the specific cyber terrain the mission depends on. Its job is to answer a simple but consequential question: if a cyber effect were to reach into this wing's aircraft, which nodes would we have to defend first to keep the mission flyable?

The reason the DoD requires this analysis is that cyber defenders cannot possibly defend everything, so they have to know what actually matters. The MACCE (Mission Assurance Cyber Coordination Element) is the wing-level analyst who produces that prioritized list. As the MACCE Fundamentals course states, the MACCE's core duties include "Conduct FMA-C on assigned Mission Defense System (MDS)" and "Identify cyber vulnerabilities, risk, and mission impact." FMA-C is the primary analytical product a MACCE delivers to a wing commander.

<img src="data\corpus\media/media/image1.png" style="width:5.3in;height:6.85826in" />

*Figure 1.1 - MACCE Core Duties, from MACCE Fundamentals (Course 1) page 10. Note that FMA-C on the assigned MDS is duty number 2.*

**1.2 The MACCE's role in FMA-C**

A MACCE is the wing-level bridge between the mission and the cyber picture. You sit in the Operations Support Squadron (OSS), you attend aircrew debriefs, and you speak both languages - mission and cyber. Everything else you do at the wing (MADSS entries, KT-C briefings, Wing Commander in-briefs, quarterly ACC reports) is downstream of the FMA-C you produce for your assigned MDS. If your FMA-C is wrong, every product built on top of it is wrong too.

Per MACCE Fundamentals Course 1: the Project Officer coordinates the FMA-C Wing Commander in-brief and supports FMA-C report coordination "for KT-C approval." That single phrase - "for KT-C approval" - is what your FMA-C is aiming at. Everything in this guide is in service of producing a defensible KT-C list that a Wing Commander can look at, understand, and sign.

<img src="data\corpus\media/media/image2.png" style="width:5.3in;height:6.85826in" />

*Figure 1.2 - PROJO role from MACCE Fundamentals page 9 (highlights include: coordinate FMA-C Wing Commander in-brief; support FMA-C report coordination for KT-C approval).*

**1.3 The universal 3-source rule (any airframe)**

This is the most important rule in FMA-C, and it is not stated as a rule in the student guide - you have to notice it yourself. Every single entry you make in an FMA-C workbook traces back to exactly one of three sources. If you cannot point to the source for a cell, the cell is wrong.

Stated generically, the three sources are:

- **The Commander / Exercise brief -** provides the Mission Statement, Commander's Intent, Mission Essential Function (MEF) / Mission Essential Tasks (METs), Time-Critical Actions (TCAs), Unacceptable Losses, and Mission Hazards. This is the "why" and the "what must not happen."

- **The aircraft / weapons-system Data Sheet -** provides the technical inventory of the airframe's mission systems: data buses, mission processors, controllers, update paths, and support equipment. This is the "how" of the aircraft.

- **The System Architecture Diagram -** provides the picture: components and their connections. It gives you a visual to point at when you tell the story, and it makes the Data Sheet's text much easier to reason about.

The doctrinal reference for the analytical process itself is the Mission Assurance Student Guide (Course 6 of the MACCE 2026 courseware). Think of the Mission Assurance guide as the instruction manual and the three source documents above as the raw material.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Worked Example - CF-189</strong></p>
<p><strong>For the CF-189 exercise, the three sources are:</strong></p>
<blockquote>
<p><strong>• Commander/Exercise brief:</strong> FMA-C Exercise (CF-189).docx</p>
<p><strong>• Aircraft Data Sheet:</strong> CF-189 Data Sheet.docx</p>
<p><strong>• System Architecture Diagram:</strong> CF-189 Diagram.pptx</p>
</blockquote>
<p><strong>Doctrinal reference: Mission Assurance Student Guide (Course 6).</strong></p>
<p>If you catch yourself writing something in the workbook that came from a memory of a previous CF-189 lecture rather than one of those three documents, stop and go look it up. Everything is in the documents.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

**1.4 The controller is where cyber threats live**

This subsection is doctrine - you can skip it once, but you will keep coming back to it every time Step 4 feels arbitrary. The reason the whole FMA-C process centers on the "controller" tier of the aircraft is that the controller tier is precisely where cyber effects reach into physical systems.

The Mission Systems Fundamentals course (Course 5) grounds this in the Purdue Model. In traditional IT, an attacker who compromises a server can steal data, deny service, or move laterally. In OT (Operational Technology) - the world of avionics, ICS, and embedded controllers - an attacker who compromises the controller can change what the physical world does. If you tell a Mission Computer that GPS says the target is over here when it is actually over there, an aircraft will drop a weapon in the wrong place. That is the OT-versus-IT distinction, and it is why FMA-C forces you to name every controller, every signal it accepts, and every state it can be in.

The FMA-C model has three tiers: Operator (human) at the top, Controller (computer/system) in the middle, and Function (mission effect) at the bottom. The operators are hard to attack over the network - they are humans. The functions are consequences, not attackable objects. The controllers are the middle layer, and they are the softest cyber targets on the aircraft. Everything in Step 4 (all seven sub-steps) is describing controllers in enough detail that Step 5 can ask "what if a bad guy lied to this controller?"

<img src="data\corpus\media/media/image3.png" style="width:5.3in;height:6.85826in" />

*Figure 1.3 - Mission Systems Fundamentals (Course 5) page 4 catalogs the on-aircraft controllers (Mission Computer, EWS, ADC, Display Systems, FADECs). These are the objects the FMA-C is trying to protect.*

<img src="data\corpus\media/media/image4.png" style="width:5.3in;height:6.85826in" />

*Figure 1.4 - OT cybersecurity agencies and the OT-vs-IT posture, from Course 5 page 11. The FMA-C is a CIP-flavored analysis applied to a weapons system.*

**1.5 Analytical constraints - what to do, what NOT to do**

Every FMA-C exercise you receive will come with constraints. Before you start filling any workbook, read the exercise document from top to bottom and note what is IN scope and what is OUT of scope. Skipping this step is how you end up doing three days of work you didn't need to do - or worse, delivering a product that doesn't answer the question the commander asked.

Typical constraints you may see in an FMA-C exercise:

- Whether specific-adversary threat analysis is in scope

- Whether vulnerability enumeration is in scope

- Whether risk scoring / prioritization is in scope

- Whether the analysis stops at KT-C identification or continues into Step 6 (MRT-C)

- Whether classification-restricted material may be referenced

- What briefing artifacts the deliverable includes (workbook only, workbook + slides, etc.)

In real-world FMA-C at a home station, all three legs of the KT-C Triad - Criticality, Vulnerability, and Threat - are on the table. Intel for Cyber (Course 7) is where you learn to reason about the Vulnerability and Threat legs. Risk Assessment (Course 8) is where you learn how the three legs combine into a risk score. In a training exercise, however, the instructor will often carve out just the Criticality leg to keep the workload manageable.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Worked Example - CF-189</strong></p>
<p><strong>The CF-189 exercise excludes:</strong></p>
<blockquote>
<p>• Threat / vulnerability / risk scoring (Course 7 and 8 content)</p>
<p>• Specific-adversary assumptions</p>
<p>• Network-security posture assessment</p>
<p>• Step 6 (MRT-C generation)</p>
</blockquote>
<p><strong>The CF-189 exercise INCLUDES:</strong></p>
<blockquote>
<p>• Steps 1 through 5</p>
<p>• KT-C identification (which is the OUTPUT of Step 5, not a separate step)</p>
<p>• A brief-to-Wing-CC deliverable (17 slides)</p>
</blockquote>
<p>The upshot: your CF-189 KT-C list is Criticality-only. You are not making judgments about how attackable each node is, only about how essential it is to the mission. That is a valid, self-contained subset of the full doctrine - and it happens to be the leg most students need to master first.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

**Part 2 - The FMA-C Process, Step by Step**

------------------------------------------------------------------------

This part walks all nine analytical steps in order: Step 1, Step 2, Step 3, Step 4.1, Step 4.2, Step 4.3, Steps 4.4 through 4.7 (treated together), Step 5, and finally the KT-C identification that falls out of Step 5. Every step follows the same seven-part template:

- The Concept - the doctrine, and why this step exists

- Sources - where the inputs come from (light-blue callout)

- The Recipe - a numbered airframe-agnostic procedure

- Worked Example - CF-189 - how the recipe played out for CF-189 (yellow callout)

- Mental Trick - a self-check question to unstick yourself (green callout)

- Common Mistakes - 3 to 4 typical student errors (red callout)

- A screenshot of the relevant Mission Assurance Student Guide page with a caption

The three subsections that most students find hardest - Step 4.1, Step 4.2, and Steps 4.4 through 4.7 - also embed a longer "In-Depth Explanation" block written in a plainer voice, based on the way the author has explained these steps to teammates who got stuck.

**Step 1 - Mission Purpose and Goal (AST / BMO / IOTCT)**

**The Concept**

Step 1 forces you to write down what the commander is actually trying to accomplish, in three specific parts: the Ability, System, or Task (AST) the wing performs; the {By Means Of} (BMO) - the concrete mission-generating actions the wing takes to deliver the AST; and the {In Order To} Comply/Task (IOTCT) - the outcome the higher command is trying to achieve. This is doctrine straight from the Mission Assurance Student Guide (pages 52-54).

You care so much about Step 1 because the BMO drives everything downstream. In Step 4.1, the verbs inside the BMO literally become the Functions row of the model. In Step 3 the crosswalk is checking whether each hazard would prevent one of those BMO actions. In Step 5 you are asking whether a control action failure would prevent the wing from executing the BMO. A weak or under-specified BMO makes every downstream step vague.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Sources</strong></p>
<p><strong>The Commander / Exercise brief provides all of Step 1.</strong></p>
<blockquote>
<p><strong>• AST -</strong> the Ability / System / Task the wing performs. Look for a sentence starting with the wing name and describing what it is fielded to do.</p>
<p><strong>• BMO ({By Means Of}) -</strong> the concrete verbs the wing uses to deliver the AST. Look for phrases like "by means of," "through," or "via."</p>
<p><strong>• IOTCT ({In Order To} Comply/Task) -</strong> the higher-command outcome. Look for phrases like "in order to," "to support," or a reference to a Combatant Command tasking.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>The Recipe</strong></p>
<blockquote>
<p><strong>1.</strong> Read the Commander / Exercise brief in full. Do not skip the Commander's Intent paragraph - that is where the AST usually lives.</p>
<p><strong>2.</strong> Pull the AST verbatim. Do not paraphrase. The AST should be a short, clean sentence naming the wing and what it does at the highest level.</p>
<p><strong>3.</strong> Pull the BMO verbatim. Preserve every verb - you will need each verb in Step 4.1. If the commander wrote "generating, providing airlift, providing precision strike," keep all three verbs; do not collapse them.</p>
<p><strong>4.</strong> Pull the IOTCT verbatim. This is what the wing exists to serve at the combatant-command level.</p>
<p><strong>5.</strong> Paste all three, exactly as worded, into the Step 1 sheet. Verbatim matters - a downstream reviewer will compare your Step 1 to the exercise brief and expect a match.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Worked Example - CF-189</strong></p>
<p><strong>AST:</strong></p>
<p>"189th Composite Wing conducts strategic airlift, aerial refueling, aeromedical evacuation, and precision strike."</p>
<p><strong>BMO ({By Means Of}):</strong></p>
<p>"generating aircraft, providing rapid, precision airlift support and precision strike capabilities."</p>
<p><strong>IOTCT ({In Order To} Comply/Task):</strong></p>
<p>"comply with the Wing Commander's tasking to project combat power in support of USCENTCOM operations."</p>
<p><strong>Why this BMO matters downstream:</strong></p>
<p>The three verbs - "generating," "providing airlift," "providing precision strike" - become the Functions row in Step 4.1 (labeled GEN, ALIFT, and STRIKE). Add PLAN as a fourth if you decide MET 2 deserves its own bucket. Everything else in Part 2 is built around these three or four verbs.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Mental Trick</strong></p>
<p>Ask yourself: "If I gave someone only my AST/BMO/IOTCT and asked them what the wing does, would they be able to draw the Functions row in Step 4.1 without any other information?" If the answer is no, your BMO is not concrete enough. Go back and find the verbs.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Common Mistakes</strong></p>
<blockquote>
<p><strong>• Paraphrasing the commander.</strong> The AST/BMO/IOTCT are a formal record. If you paraphrase, a reviewer cannot map your Step 1 back to the source.</p>
<p><strong>• Collapsing multi-verb BMOs into a single verb.</strong> "Generate, airlift, and strike" is three functions, not one - preserve all three.</p>
<p><strong>• Confusing the AST with the IOTCT.</strong> AST is what the wing does; IOTCT is what the higher command is trying to achieve by having the wing do it.</p>
<p><strong>• Leaving Step 1 for last.</strong> Because it feels like paperwork, students often skip Step 1 and start on Step 4. Do not. Step 1 anchors Step 4.1.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<img src="data\corpus\media/media/image5.png" style="width:5in;height:6.47059in" />

*Figure 2.1 - Mission Assurance Student Guide page 52: the tri-fold of Purpose (AST), Goal (BMO), and Task (IOTCT).*

<img src="data\corpus\media/media/image6.png" style="width:5in;height:6.47059in" />

*Figure 2.2 - Mission Assurance Student Guide page 54: the AST/BMO/IOTCT structure worked through in detail.*

**Step 2 - Unacceptable Losses (UL)**

**The Concept**

Unacceptable Losses are the outcomes the commander cannot accept - the specific consequences the wing must not produce. They are stated at the mission level ("loss of civilian life," "loss of aircraft," "failure to deliver time-critical cargo") rather than at the technical level ("corrupted GPS feed"). The Mission Assurance Student Guide (page 55) frames these as the north star of the analysis: everything downstream is asking whether some cyber effect could cause one of these Losses.

Losses are not risks and they are not causes. They are outcomes. In Step 3 you will identify the Hazards (causes) that could produce these Outcomes. In Step 5 you will connect specific control actions to specific Hazards to specific Losses. If your Losses are vague, your causal chain will be vague too.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Sources</strong></p>
<p><strong>The Commander / Exercise brief provides Unacceptable Losses verbatim.</strong></p>
<p>Look for a dedicated "Unacceptable Losses" or "Losses" section, usually numbered UL1, UL2, UL3. If the commander did not label them explicitly, look for phrases like "under no circumstances," "cannot accept," or "must not."</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>The Recipe</strong></p>
<blockquote>
<p><strong>1.</strong> Locate the Unacceptable Losses section of the Commander / Exercise brief.</p>
<p><strong>2.</strong> Paste each Loss verbatim into the Step 2 sheet, one per row, preserving the commander's numbering (UL1, UL2, UL3, ...).</p>
<p><strong>3.</strong> Do NOT invent new Losses. If you think the commander missed one, note it in a backbrief question - do not add it to Step 2 yourself. Losses are the commander's prerogative.</p>
<p><strong>4.</strong> For each Loss, confirm you can state it as an outcome (a bad thing that would have happened), not as a cause (a technical failure). If you cannot, you probably grabbed a Hazard by mistake.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Worked Example - CF-189</strong></p>
<p><strong>The CF-189 commander provides three Unacceptable Losses:</strong></p>
<blockquote>
<p><strong>• UL1:</strong> Loss of aircraft.</p>
<p><strong>• UL2:</strong> Loss of aircrew.</p>
<p><strong>• UL3:</strong> Failure to execute time-critical cargo or strike mission.</p>
</blockquote>
<p>Each is an outcome (a state of the world after the mission) rather than a cause. This is what makes the Step 3 crosswalk possible: for each Hazard in Step 3 you can now ask, cleanly, "does this Hazard produce UL1? UL2? UL3?" The answer is either Yes or No, not a fuzzy scale.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Mental Trick</strong></p>
<p>For each Loss, ask: "Is this something that has already happened, or something that would have to happen for the mission to fail?" A Loss is always something that WOULD have to happen - an outcome. If your entry sounds like a technical failure (something breaks), you have written a Hazard, not a Loss.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Common Mistakes</strong></p>
<blockquote>
<p><strong>• Mixing Losses and Hazards.</strong> "GPS is spoofed" is a Hazard; "aircraft is destroyed" is a Loss.</p>
<p><strong>• Editorializing.</strong> Do not soften or rewrite the commander's Losses. Paste them exactly.</p>
<p><strong>• Missing a Loss.</strong> If the commander wrote three Losses, you should have three rows. Not two, not four.</p>
<p><strong>• Treating Losses as ranked.</strong> The commander numbers them UL1-UL3 for reference, not priority. Do not treat UL1 as more important than UL3 unless the commander says so.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<img src="data\corpus\media/media/image7.png" style="width:5in;height:6.47059in" />

*Figure 2.3 - Mission Assurance Student Guide page 55: Unacceptable Losses as outcomes stated by the commander.*

**Step 3 - Mission Hazards, the H/L Crosswalk, and Constraints**

**The Concept**

Where Losses (Step 2) are outcomes, Hazards (Step 3) are CAUSES - the specific bad states of the world that could produce one of the Losses. The Mission Assurance Student Guide (pages 56-57) is explicit about this distinction. The Hazard/Loss (H/L) Crosswalk is a Y/N grid that connects each Hazard to the Loss(es) it would produce. That grid becomes the analytical backbone of Step 5, where you connect control actions to those same Hazards.

This step is also where Course 3 (Critical Reasoning and Structured Analysis) and Course 8 (Risk Assessment) become relevant. Course 3 teaches you to check assumptions and avoid "satisficing" - settling for a good-enough hazard when the real hazard is more precise. Course 8 teaches you to reason cleanly about hazard-to-consequence chains without collapsing them prematurely into a single "risk." You should think of the Hazard as the second half of a sentence whose first half is a technical event: "If \[technical event\], then \[Hazard\]; if \[Hazard\], then \[Loss\]."

Constraints are the flip side of Hazards. Every Hazard implies a Constraint - the thing you must prevent. If the Hazard is "aircraft cannot navigate to target," the Constraint is "navigation must be available and accurate." Inverting Hazards into Constraints gives you a clean statement of what the mission is protecting.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Sources</strong></p>
<p><strong>The Commander / Exercise brief provides the Hazards verbatim, plus the Loss list needed for the crosswalk.</strong></p>
<blockquote>
<p><strong>• Hazards -</strong> usually labeled H1, H2, H3 in a dedicated section. Copy them exactly.</p>
<p><strong>• H/L Crosswalk -</strong> you fill this yourself, using the commander's Hazards on one axis and the commander's Losses on the other.</p>
<p><strong>• Constraints -</strong> derived by inverting each Hazard into a positive requirement.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>The Recipe</strong></p>
<blockquote>
<p><strong>1.</strong> Paste each Hazard verbatim into the Step 3 sheet, one per row, preserving the commander's numbering (H1, H2, H3, ...).</p>
<p><strong>2.</strong> Build the H/L Crosswalk. Put the Hazards as row labels and the Losses as column labels. For each cell, ask: "If this Hazard occurred, would it produce this Loss?" Write Y or N. Do not write "maybe."</p>
<p><strong>3.</strong> For each Y in the crosswalk, verify you can state the causal chain out loud: "H1 (whatever it is) causes UL2 because ..." If you cannot state it, the Y is wrong.</p>
<p><strong>4.</strong> Invert each Hazard into a Constraint. If H1 = "aircraft cannot maintain navigation," then Constraint C1 = "aircraft must maintain accurate navigation." Write these into the Constraints portion of Step 3.</p>
<p><strong>5.</strong> Sanity check: at least one Y per Hazard column (otherwise the Hazard is not really a Hazard - it produces no Loss) and at least one Y per Loss row (otherwise the Loss has no identified Hazard driving it, which is a gap you should flag to the commander).</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Worked Example - CF-189</strong></p>
<p><strong>CF-189 Hazards (from the exercise doc):</strong></p>
<blockquote>
<p><strong>• H1:</strong> Aircraft cannot navigate to the tasked target/airfield.</p>
<p><strong>• H2:</strong> Aircraft delivers ordnance or cargo to the wrong location.</p>
<p><strong>• H3:</strong> Aircraft loses flight control or engine performance.</p>
<p><strong>• H4:</strong> Aircraft cannot communicate mission-critical data (targeting, coordination, medevac status).</p>
<p><strong>• H5:</strong> Aircraft cannot generate for tasking (mission systems fail before takeoff).</p>
</blockquote>
<p><strong>CF-189 H/L Crosswalk (Y = this Hazard could produce this Loss):</strong></p>
<p>H1 -&gt; UL1 Y, UL2 Y, UL3 Y - a nav failure endangers the aircraft, aircrew, and the mission.</p>
<p>H2 -&gt; UL1 N, UL2 N, UL3 Y - wrong-location delivery is a mission failure, not necessarily aircraft loss.</p>
<p>H3 -&gt; UL1 Y, UL2 Y, UL3 Y - a flight-control failure endangers all three.</p>
<p>H4 -&gt; UL1 N, UL2 N, UL3 Y - comms failure is a mission failure but not directly a physical loss.</p>
<p>H5 -&gt; UL1 N, UL2 N, UL3 Y - a pre-takeoff generation failure is a mission failure only.</p>
<p><strong>Constraints (inverted Hazards):</strong></p>
<blockquote>
<p><strong>• C1:</strong> Navigation must be available and accurate.</p>
<p><strong>• C2:</strong> Ordnance/cargo must be delivered to the tasked location.</p>
<p><strong>• C3:</strong> Flight controls and engines must operate within tolerance.</p>
<p><strong>• C4:</strong> Mission-critical communications must be reliable.</p>
<p><strong>• C5:</strong> Mission systems must be generatable before takeoff.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Mental Trick</strong></p>
<p>For every Y in the crosswalk, complete the sentence out loud: "If [Hazard] happened, then [Loss] would happen because ______." If you cannot fill in the blank confidently, the Y is either wrong or you are missing an intermediate step. This is the Critical Reasoning discipline from Course 3 - do not accept a "good enough" causal link.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Common Mistakes</strong></p>
<blockquote>
<p><strong>• Writing Hazards as Losses.</strong> "Loss of aircraft" is a Loss; "aircraft loses flight control" is a Hazard.</p>
<p><strong>• Writing "maybe" or "partial" in the crosswalk.</strong> Cells are Y or N. Force yourself to commit.</p>
<p><strong>• Marking every cell Y.</strong> If everything causes everything, the crosswalk carries no analytical information. Be honest.</p>
<p><strong>• Forgetting to invert into Constraints.</strong> The Constraints are what your Step 5 hazardous-control-action analysis is trying to prevent violating.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<img src="data\corpus\media/media/image8.png" style="width:5in;height:6.47059in" />

*Figure 2.4 - Mission Assurance Student Guide page 56: Mission Hazards as causes that would produce Losses.*

<img src="data\corpus\media/media/image9.png" style="width:5in;height:6.47059in" />

*Figure 2.5 - Mission Assurance Student Guide page 57: the H/L Crosswalk - Y/N grid connecting each Hazard to the Losses it could produce.*

<img src="data\corpus\media/media/image10.png" style="width:5in;height:6.47005in" />

*Figure 2.6 - Critical Reasoning & Structured Analysis (Course 3) page 55: the ACH matrix; the rigor of checking evidence against hypotheses maps directly to checking Hazards against Losses.*

<img src="data\corpus\media/media/image11.png" style="width:5in;height:7.06431in" />

*Figure 2.7 - Risk Assessment (Course 8) page 12: NIST RMF's seven steps; Step 3 of the FMA-C sits inside the Categorize / Prepare arc of the broader RMF.*

**Step 4.1 - The 3-Tier Model (Operator, Controller, Functions)**

**The Concept**

Step 4.1 is the first step where you stop copying from the commander and start doing analytical work of your own. It asks you to build a three-tier diagram of the mission: the Functions at the bottom (what the mission does), the Controllers in the middle (the systems/computers that execute those Functions), and the Operators at the top (the humans who command those Controllers). Mission Assurance Student Guide pages 60-61 lay out the structure with the A-10C example.

The reason Step 4.1 comes before Step 4.2 is that Step 4.2 needs a defined list of controllers to fill its rows. And the reason Step 4.1 puts Controllers in the middle is doctrinal: as Course 5 (Mission Systems Fundamentals) makes clear, the controller tier is the layer where OT cyber effects land. Operators are hard to attack; Functions are consequences; Controllers are attackable middle-layer computers. Step 4.1 is where you tell yourself, explicitly, what those middle-layer computers are for this airframe.

Cameron's teaching note: Step 4.1 is the only step in the whole FMA-C that is a DESIGN step. Every other step is a lookup step - go find the answer in a document. Step 4.1 is where you make scoping decisions. If two people fill Step 4.1 differently, that is normal; they are making different (equally defensible) scoping choices. This is why the in-depth explanation below is worth reading before you start filling boxes.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Sources</strong></p>
<blockquote>
<p><strong>• Functions row -</strong> from your Step 1 BMO verbs. Each verb becomes a Function.</p>
<p><strong>• Controllers row -</strong> from the Data Sheet's opening section describing the aircraft's data networks and controllers. Include only those that directly execute one of your Functions.</p>
<p><strong>• Operators row -</strong> from the METs in the Commander / Exercise brief. Each MET names a human role (Maintenance, Operations, Aircrew).</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>The Recipe</strong></p>
<blockquote>
<p><strong>1.</strong> Start at the BOTTOM (Functions). Copy your Step 1 BMO sentence out. Underline the verbs. Each verb becomes a Function box, with a short label suitable for a slide.</p>
<p><strong>2.</strong> Move to the MIDDLE (Controllers). Read the Data Sheet's opening section on primary data networks and controllers. For each candidate controller ask the yes/no question: "Does this component directly execute one of my Functions?" If yes, it belongs in Step 4.1. If no, it will still show up later in Step 4.2 as a supporting element.</p>
<p><strong>3.</strong> Move to the TOP (Operators). Read the METs. Each MET names a human role. Consolidate similar roles into a small number of Operator boxes - three is a good target (Operations, Aircrew, Maintenance), mirroring the A-10C example on Mission Assurance page 61.</p>
<p><strong>4.</strong> Sanity check tier-count: three tiers, three-to-four Functions, four-to-six Controllers, three Operators is a typical shape. If any tier has one box, you probably collapsed too aggressively; if any tier has ten boxes, you probably included support elements that belong in Step 4.2.</p>
<p><strong>5.</strong> This step lives on the briefing (slide 10) rather than on a dedicated Excel sheet. Draw it in the slide as a three-row box diagram.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Worked Example - CF-189</strong></p>
<p><strong>Step 4.1 for CF-189 uses these three tiers:</strong></p>
<p><strong>Functions (from BMO verbs):</strong></p>
<blockquote>
<p><strong>• GEN -</strong> generate aircraft (from BMO verb "generating aircraft")</p>
<p><strong>• PLAN -</strong> plan / brief / execute multi-role missions (from MET 2; a judgment call to break this out from GEN)</p>
<p><strong>• ALIFT -</strong> provide airlift (from BMO verb "providing rapid, precision airlift support")</p>
<p><strong>• STRIKE -</strong> provide precision strike (from BMO verb "providing precision strike capabilities")</p>
</blockquote>
<p><strong>Controllers (from Data Sheet's "three primary data networks" section):</strong></p>
<blockquote>
<p><strong>• MPN -</strong> Mission Planning Network</p>
<p><strong>• Mission Computer / BC -</strong> primary bus controller on MIL-STD-1553</p>
<p><strong>• DSMS -</strong> Digital Stores Management System on MIL-STD-1760</p>
<p><strong>• Display Controller -</strong> on AFDX</p>
<p><strong>• FMS -</strong> Flight Management System</p>
</blockquote>
<p><strong>Operators (from METs):</strong></p>
<blockquote>
<p><strong>• Operations -</strong> planners; drives PLAN</p>
<p><strong>• Aircrew (PIC) -</strong> executes ALIFT and STRIKE</p>
<p><strong>• Maintenance -</strong> drives GEN</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Mental Trick</strong></p>
<p>Do the rows in this order: Functions first (from BMO verbs), Controllers second (which components execute those Functions?), Operators third (which humans command those controllers?). If you try to do Operators first, you will end up with a wing organization chart, not an FMA-C model. Bottom-up is the only order that works.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Common Mistakes</strong></p>
<blockquote>
<p><strong>• Doing Operators first.</strong> You end up building an org chart instead of a mission-execution model.</p>
<p><strong>• Putting every Data-Sheet component in the Controllers row.</strong> The Controllers row is only for components that directly execute a Function. Support elements come later in Step 4.2.</p>
<p><strong>• Inventing Functions the BMO does not name.</strong> If your BMO said three verbs, you have three (or maybe four) Functions. Not seven.</p>
<p><strong>• Skipping the row-count sanity check.</strong> 3 Functions + 5 Controllers + 3 Operators is a healthy shape. Anything wildly outside that is worth a second look.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<img src="data\corpus\media/media/image12.png" style="width:5in;height:6.47059in" />

*Figure 2.8 - Mission Assurance Student Guide page 60: Step 4.1 introduces the three-tier model.*

<img src="data\corpus\media/media/image13.png" style="width:5in;height:6.47059in" />

*Figure 2.9 - Mission Assurance Student Guide page 61: the A-10C example uses three Operators (Operations, Pilot, MX). The "functions at the bottom of the model refer to the {By Means Of} in the mission purpose and goal" - page 61's most important sentence.*

**In-Depth Explanation - Functions-first recipe**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>In-Depth Explanation (from the author's cohort notes)</strong></p>
<p>Same pattern as 4.2 - the three rows in Step 4.1 each come from a different document, and once you know which document feeds which row, the whole thing gets easy. But there's one row (Functions) that's more important than the other two, so let me start there.</p>
<p><strong>Functions row - the bottom row is where you start, not where you finish</strong></p>
<p>The single most important sentence in the entire Mission Assurance Student Guide, for Step 4.1, is on page 61: "The functions at the bottom of the model refer to the {By Means Of} in the mission purpose and goal." Read that twice.</p>
<p>Your BMO from Step 1 was: "generating aircraft, providing rapid, precision airlift support and precision strike capabilities." Underline the verbs: generating, providing airlift, providing precision strike. Those verbs literally become the boxes in your Functions row. I called them GEN, ALIFT, STRIKE (short labels for briefing purposes). I added a fourth box, PLAN, because MET 2 ("Plan, Brief, and Execute Multi-Role Missions") is such a distinct phase that it deserves its own function - that's a judgment call on my part, and honestly you could argue it belongs under GEN. If your team decides three boxes fit better than four, you're not wrong.</p>
<p>So the rule for the Functions row is: go back to your Step 1 BMO sentence, pull the verbs out of it, and each verb becomes a Functions box. That's it. The bottom row is the mission's action verbs.</p>
<p>Why does this row matter so much? Because the Controller row (middle) is derived from it. You don't pick controllers first and then figure out what they do - you look at your functions and ask "which components are needed to execute this function?" That question is what fills the Controller row.</p>
<p><strong>Controller row - the computers/systems that actually do the functions</strong></p>
<p>The Controller row is the middle tier: MPN, Mission Computer/BC, DSMS, Display Controller, FMS. Every single one of those came from one section of the CF-189 Data Sheet: the very top of the doc, under "There are three primary data networks on the aircraft." That section walks through 1553, 1760, and AFDX and lists what's on each.</p>
<p>But that section lists WAY more components than what I put in Step 4.1. Why?</p>
<p>Because the Controller row is only for components that directly execute one of your Functions. Ask each candidate the question: "Does this component directly do GEN, PLAN, ALIFT, or STRIKE?" If yes, it's a controller in Step 4.1. If no - even if it's an important cyber node - it doesn't belong here (it'll still show up later in Step 4.2 as a supporting element).</p>
<p><strong>Operator row - the humans who tell the controllers what to do</strong></p>
<p>The top row is the humans. Three sources:</p>
<p>First, look at your METs. MET 1 says "Perform maintenance and inspections, Fuel and arm aircraft, Load cargo and personnel" - that's Maintenance. MET 2 says "Develop mission plans, Configure weapons and sensors, Conduct aircrew briefings" - that's Operations. MET 3 and MET 4 both say "Execute" - that's Aircrew.</p>
<p>Second, the A-10C example on page 61 sets the pattern. They used exactly three Operator boxes: Operations, Pilot, MX. I mirrored that structure because it's clean and covers every phase of a sortie.</p>
<p><strong>The mental trick for Step 4.1</strong></p>
<p>Do the rows in this order: Functions first, Controller second, Operator third.</p>
<p>Start at the bottom: pull the verbs out of your BMO. That's Functions.</p>
<p>Move to the middle: for each Function, ask "which components on the aircraft directly execute this?" Include only those. That's Controllers.</p>
<p>Move to the top: ask "who are the humans who directly command those controllers?" Look at your METs for the answer. That's Operators.</p>
<p>Step 4.1 is the only step that's a design step. Every other step is a lookup step (go find the answer in the docs). Step 4.1 is where you decide how you're going to organize the analysis. If two people on your team fill out Step 4.1 differently, that's normal - they're making different scoping decisions.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

**Step 4.2 - Responsibilities Matrix (Elements x Mission Modes)**

**The Concept**

Step 4.2 is a big responsibilities matrix. The rows are all the elements that touch the mission (a superset of the Step 4.1 Controllers - you add supporting equipment and human roles), and the columns are the mission modes (the phases of a typical sortie). Each cell answers one question: "What is this element doing at this moment?" Mission Assurance Student Guide page 62 defines Step 4.2 as the responsibilities view of the model.

The reason this step matters so much is that everything downstream is derived from it. The arrows you draw in Step 4.3 come from the responsibilities you list here. The control actions you name in Step 4.4-4.7 come from those arrows. The hazardous control actions you analyze in Step 5 come from those control actions. If Step 4.2 is thin or wrong, everything downstream is thin or wrong.

Tactical Planning (Course 10) is where the mission-modes concept comes from: a sortie has a natural timeline (ground, plan, ingress, on-target, egress, recovery) that maps to how the aircrew and support elements actually spend their time. You want your columns to read left-to-right in that time order, because that is how you (and the commander) will think about the mission when the briefing lands on their desk.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Sources</strong></p>
<blockquote>
<p><strong>• Rows come from three places:</strong> (a) every box in Step 4.1; plus (b) any element listed in the Data Sheet's "Management, Updates, and Ancillary Equipment" section that has an update or maintenance path; plus (c) any human or organizational role the Exercise / Commander brief names as having a mission role.</p>
<p><strong>• Columns come from the METs, collapsed into a sortie timeline.</strong> Do not just paste the MET names as columns - the METs overlap in time. Instead, translate them into ground -&gt; plan -&gt; ingress -&gt; on-target -&gt; egress phases so the table reads left-to-right chronologically.</p>
<p><strong>• Cells come from the Data Sheet.</strong> Every cell paraphrases a statement in the Data Sheet about what the element does during that phase. If you cannot cite the Data Sheet, the cell should say "Standby" or "(n/a)".</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>The Recipe</strong></p>
<blockquote>
<p><strong>1.</strong> Build the row list. Copy every Step 4.1 box (Operators AND Controllers) into the leftmost column. Then walk the Data Sheet's ancillary-equipment section and add any support element that has an update path or maintenance role. Finally, walk the Commander brief and add any human role it names.</p>
<p><strong>2.</strong> Build the column list. Take the METs and translate them into a sortie timeline: usually Ground Ops -&gt; Mission Planning -&gt; Ingress -&gt; On-Target -&gt; Egress/RTB. Adjust based on whether the aircraft's mission is cargo-heavy, strike-heavy, or dual-role.</p>
<p><strong>3.</strong> Fill each cell by asking "What is this element doing during this mode, and where is that documented?" Paraphrase the Data Sheet. If the element isn't doing anything in a mode, write "Standby" or "(n/a)" - do NOT leave blanks and do NOT invent activity.</p>
<p><strong>4.</strong> For controllers, be specific about what interfaces are open and what data flows are active. "Accepts firmware over USB" and "listens on 1553" belong in the cell if they are active in that mode.</p>
<p><strong>5.</strong> Do a two-column read-through: pick a row and read it left-to-right; the row should tell a coherent story of what that element does over a sortie. Pick a column and read it top-to-bottom; the column should list everything happening in that phase. Both readings should feel complete.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Worked Example - CF-189</strong></p>
<p><strong>Row list (elements) - 15 to 18 rows total:</strong></p>
<blockquote>
<p>• From Step 4.1: PIC, Aircrew, Maintenance, MPN, Mission Computer/BC, DSMS, Display Controller, FMS</p>
<p>• From Data Sheet ancillary section: FADEC, Secondary BC / Bus Monitor, CMBRE, EFB, Vendor Tech</p>
<p>• From Exercise / Commander brief: COMSEC Custodian, MACCE</p>
</blockquote>
<p><strong>Column list (modes) - five modes, mapped from the four METs:</strong></p>
<blockquote>
<p><strong>• Ground Ops -</strong> covers MET 1 (maintenance, fueling, loading, arming)</p>
<p><strong>• Mission Planning -</strong> covers MET 2 (OFP load, map load, brief)</p>
<p><strong>• Ingress -</strong> between takeoff and target area</p>
<p><strong>• Cargo Ops / Strike -</strong> the actual execution of MET 3 or MET 4</p>
<p><strong>• Egress / RTB -</strong> recovery: fly home, land, taxi, shutdown</p>
</blockquote>
<p><strong>Sample row - DSMS (Digital Stores Management System):</strong></p>
<blockquote>
<p><strong>• Ground Ops:</strong> Standby / self-test.</p>
<p><strong>• Mission Planning:</strong> Accept weapon/stores profile via SSD (vendor); Wi-Fi disabled.</p>
<p><strong>• Ingress:</strong> Standby.</p>
<p><strong>• Cargo Ops / Strike:</strong> Manage stores state, execute release, chaff/flare, UAV control via Link.</p>
<p><strong>• Egress / RTB:</strong> Standby (weapons expended or safed).</p>
</blockquote>
<p>Every one of those cells came from paraphrasing a specific line in the Data Sheet. If a cell is invented rather than cited, the Step 5 analysis built on top of it will be wrong.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Mental Trick</strong></p>
<p>When you're stuck, chant: "Rows come from Step 4.1 plus Data Sheet plus Exercise Doc. Columns come from the METs collapsed into a timeline. Cells come from paraphrasing the Data Sheet." If you cannot point to a document for a cell, either the element doesn't do anything in that mode (write Standby) or you are missing a document you should be reading.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Common Mistakes</strong></p>
<blockquote>
<p><strong>• Using MET names as column headers.</strong> METs overlap in time. Use a timeline (Ground -&gt; Plan -&gt; Ingress -&gt; Target -&gt; Egress) so cells describe what's happening moment-to-moment.</p>
<p><strong>• Inventing activity.</strong> If the Data Sheet doesn't say the element does something in this mode, do not put it in the cell. Write "Standby."</p>
<p><strong>• Forgetting support elements.</strong> The DSMS is a controller from Step 4.1. But the Vendor Tech who ships the DSMS Wi-Fi update laptop is a separate row in Step 4.2 - and that laptop is where the cyber exposure lives.</p>
<p><strong>• One-word cells.</strong> "Active" is not enough. Say what the element is DOING: which interfaces are open, what data flows, what state changes.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<img src="data\corpus\media/media/image14.png" style="width:5in;height:6.47059in" />

*Figure 2.10 - Mission Assurance Student Guide page 62: Step 4.2 responsibilities matrix.*

<img src="data\corpus\media/media/image15.png" style="width:5in;height:6.47005in" />

*Figure 2.11 - Tactical Planning (Course 10) page 30: the mission-mode/sortie-timeline concept is standard tactical-planning doctrine and is what your columns should reflect.*

**In-Depth Explanation - Where the rows and columns came from**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>In-Depth Explanation (from the author's cohort notes)</strong></p>
<p>Great question, and honestly Step 4.2 is the one that matters most - everything downstream (4.3 arrows, 4.4-4.7 control actions, Step 5 hazards) is literally derived from it. If 4.2 is wrong, everything else is wrong. So it's worth understanding exactly how I built it.</p>
<p>The Step 4.2 table has two things you have to figure out before you can fill a single cell: the rows (who are the elements?) and the columns (what mission phases are the modes?). Let me walk through where each came from.</p>
<p><strong>Where the rows came from</strong></p>
<p>Every element I put in that table came from one of three places, and each one is a document you already have.</p>
<p>First stop: your Step 4.1 boxes. Every blue box in slide 10 becomes a row in 4.2. So PIC, Aircrew, Maintenance (the Operator tier); MPN, Mission Computer, DSMS, Display Controller, FMS (the Controller tier). That gives me eight rows for free just from the diagram I already drew.</p>
<p>Second stop: the CF-189 Data Sheet under "Management, Updates, and Ancillary Equipment Details." That section is a goldmine - it lists every piece of ground support equipment that touches the aircraft and describes exactly what it does. From that section I picked up FADEC, Secondary BC/Bus Monitor, CMBRE, and EFB. I also picked up Vendor Tech (because the data sheet mentions vendors constantly - "vendor-supplied laptop," "shipped via USPS from the Vendor," "vendor maintenance shop"). If the data sheet says an element has an update path or a maintenance responsibility, it belongs in Step 4.2, even if it wasn't in your Step 4.1 boxes.</p>
<p>Third stop: the exercise document itself. The FMA-C Exercise doc mentioned COMSEC Custodian (loading keys to IFF, RWR, Missile Warning) and MACCE (that's you and your team). Anyone the commander or the exercise names as having a role - even a support role - gets a row.</p>
<p>So the rule is simple: any element that either (a) appears in your Step 4.1 diagram, (b) has a documented update or maintenance path in the CF-189 Data Sheet, or (c) is called out in the exercise document as having a role - that element belongs in Step 4.2. If it doesn't fit one of those three tests, it probably doesn't belong there.</p>
<p><strong>Where the columns came from</strong></p>
<p>The columns are the mission modes, and this is where a lot of people get stuck. The temptation is to invent modes, but they're actually sitting right there in the exercise document under the METs.</p>
<p>Your exercise doc lists four METs:</p>
<p>MET 1: Generate and Sustain C/F-189 Aircraft</p>
<p>MET 2: Plan, Brief, and Execute Multi-Role Missions</p>
<p>MET 3: Conduct Airlift Operations</p>
<p>MET 4: Conduct Combat Operations</p>
<p>I mapped those METs into the sequence of things that happen in time on any given sortie:</p>
<p>Ground Ops covers MET 1 (the pre-flight world - maintenance, fueling, loading cargo, arming stores)</p>
<p>Mission Planning covers MET 2 (loading the OFP, loading maps, briefing the crew)</p>
<p>Ingress is what happens between takeoff and the target area (flying to where you're going to do the job)</p>
<p>Cargo Ops / Strike covers the actual execution of MET 3 or MET 4</p>
<p>Egress / RTB is the reverse of Ingress (fly home, land, taxi)</p>
<p>Why not just use the four MET names as columns? Because the METs overlap in time - MET 1 keeps happening while MET 2 is happening. What you want for the columns is a timeline of the sortie, not a taxonomy of tasks. Ground Ops -&gt; Mission Planning -&gt; Ingress -&gt; [Cargo or Strike] -&gt; Egress reads left-to-right the way the day actually unfolds, which makes it much easier to think about "what is this element doing right now?" for every cell.</p>
<p><strong>How I filled each cell</strong></p>
<p>Once I had rows and columns, filling the cells is a lookup exercise. For every Element x Mode intersection, I asked one question: "What is this element doing at this moment, and where is that documented?" Then I went to the CF-189 Data Sheet to find the answer.</p>
<p>Let me walk you through one row - DSMS - so you can see the method.</p>
<p>DSMS x Ground Ops: Data sheet says the DSMS is a COTS Android tablet that sits on the 1760 bus and manages stores. Before flight, it's not doing anything active. So the cell reads: "Standby / self-test."</p>
<p>DSMS x Mission Planning: Data sheet: "Has an SSD slot which is used to load new weapon/stores profiles supplied by the stores vendors" and "Can only be updated by the manufacturer via the built-in Wi-Fi connection. Wi-Fi should always be disabled except when at a vendor maintenance shop." So the cell reads: "Accept weapon/stores profile via SSD (vendor); Wi-Fi disabled." I lifted that directly from the data sheet - I didn't invent it.</p>
<p>DSMS x Ingress: Between takeoff and target, the weapons aren't being managed yet. Cell: "Standby."</p>
<p>DSMS x Cargo Ops / Strike: Data sheet: "The DSMS can be connected to the Link 16/22 transceiver over a Link Adapter Module and Signal Processing Controller to control active stores such as UAVs, semi-autonomous missiles, and smart munitions." Plus the Stores Control Panels (TAP/OCP/ACP) route through DSMS. Cell: "Manage stores state, execute release, chaff/flare, UAV control via Link."</p>
<p>DSMS x Egress / RTB: Weapons are expended or safed. Cell: "Standby."</p>
<p>Every row was built the same way - pick an element, walk through the five modes, and for each mode ask "does the data sheet or the exercise doc say what this element does here?" If yes, paraphrase it into the cell. If no, write "Standby" or "(n/a)" or "Ground role only." You are not supposed to invent responsibilities. If you can't find a source for a cell's content, either the element doesn't do anything in that mode (and the cell should say so), or you're missing a document you should be looking at.</p>
<p><strong>The mental trick</strong></p>
<p>When you're stuck, remember the sequence: rows come from Step 4.1 + Data Sheet + Exercise Doc. Columns come from the METs collapsed into a timeline. Cells come from paraphrasing the Data Sheet's descriptions.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

**Step 4.3 - Control Relationships (Command Down, Feedback Up)**

**The Concept**

Step 4.3 is the arrow-drawing step. You take the three-tier diagram from Step 4.1 and, for every connection between two boxes, draw two arrows: a Command arrow going down (Operator -\> Controller, Controller -\> Function) and a Feedback arrow going up (Function -\> Controller, Controller -\> Operator). Mission Assurance Student Guide page 63 shows the pattern.

The reason this matters is that every arrow becomes a control action in Steps 4.4-4.7, and every control action becomes a candidate for hazardous-control-action analysis in Step 5. The arrows are how you enumerate the things that can go wrong. If you skip an arrow in 4.3, you skip a control action in 4.4, and you may miss a KT-C node in the final list.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Sources</strong></p>
<blockquote>
<p><strong>• The Step 4.1 diagram -</strong> gives you the boxes that arrows connect.</p>
<p><strong>• The Data Sheet -</strong> tells you which controllers accept commands from which operators and produce which feedback signals. Every arrow should be citable back to something the Data Sheet says.</p>
<p><strong>• The System Architecture Diagram -</strong> confirms the physical/logical paths (which bus, which port) - useful as a sanity check.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>The Recipe</strong></p>
<blockquote>
<p><strong>1.</strong> Redraw the Step 4.1 three-tier diagram (Operators top, Controllers middle, Functions bottom) on a new slide (typically slide 12 in the CF-189 briefing template).</p>
<p><strong>2.</strong> For each Operator -&gt; Controller pair the Data Sheet describes a command relationship for, draw a solid arrow going DOWN from the Operator to the Controller. Label the arrow with the command name.</p>
<p><strong>3.</strong> For each Controller -&gt; Function pair the Data Sheet describes an execution relationship for, draw a solid arrow going DOWN from the Controller to the Function.</p>
<p><strong>4.</strong> For each Controller -&gt; Operator or Function -&gt; Controller pair the Data Sheet describes a feedback path for (status displays, telemetry, sensor returns), draw a dashed arrow going UP.</p>
<p><strong>5.</strong> Count the arrows. Each solid Command arrow is a control action you will enumerate in Step 4.4. Each dashed Feedback arrow is a potential integrity target (a spoofed feedback signal is a common cyber effect).</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Worked Example - CF-189</strong></p>
<p><strong>Representative arrows in the CF-189 Step 4.3 diagram (slide 12):</strong></p>
<blockquote>
<p><strong>• MPN -&gt; Mission Computer (down, solid):</strong> LoadOFP - the mission planner pushes the Operational Flight Plan into the Mission Computer over the SIPR-connected Mission Load Laptop.</p>
<p><strong>• Aircrew -&gt; FMS (down, solid):</strong> SelectRoute - pilot selects a route on the FMS during flight.</p>
<p><strong>• Aircrew -&gt; DSMS (down, solid):</strong> ReleaseStores - pilot commands weapon release via TAP/OCP/ACP through the DSMS.</p>
<p><strong>• Vendor Tech -&gt; Display Controller (down, solid):</strong> LoadFirmware - vendor pushes firmware via Windows 10 laptop over USB-A/B.</p>
<p><strong>• Mission Computer -&gt; Aircrew (up, dashed):</strong> StatusDisplay - Mission Computer sends state to Display Controller which the aircrew reads.</p>
<p><strong>• FMS -&gt; Mission Computer (up, dashed):</strong> NavFeedback - FMS reports current position/heading back to Mission Computer.</p>
</blockquote>
<p>In the CF-189 briefing template, this diagram appears on slide 12. Every arrow you draw here becomes exactly one row in Step 4.4-4.7 downstream.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Mental Trick</strong></p>
<p>For every arrow, say out loud: "[SOURCE] tells [DESTINATION] to [do this thing]" for commands, or "[SOURCE] reports [this state] to [DESTINATION]" for feedback. If you can say it, the arrow is real. If you can't, the arrow is speculative and belongs off the diagram.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Common Mistakes</strong></p>
<blockquote>
<p><strong>• Drawing arrows the Data Sheet doesn't support.</strong> Every arrow should be citable - if you can't point to a Data Sheet sentence, don't draw it.</p>
<p><strong>• Forgetting the Feedback arrows.</strong> Feedback loops are cyber targets too. Spoofing a status feedback so the operator thinks all is well while the controller is doing something wrong is a classic OT attack.</p>
<p><strong>• Labeling arrows inconsistently.</strong> Adopt a naming convention (e.g., SOURCE_DEST_FUNCTION) and use it for every arrow. Step 4.4 will thank you.</p>
<p><strong>• Merging arrows.</strong> Each command is its own arrow. Do not draw one arrow labeled "multiple commands" - you will lose them in Step 4.4.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<img src="data\corpus\media/media/image16.png" style="width:5in;height:6.47059in" />

*Figure 2.12 - Mission Assurance Student Guide page 63: Step 4.3 control relationships diagram (Command arrows down, Feedback arrows up).*

**Steps 4.4-4.7 - Control Actions and Process Models (CA / PMD / PMV / PMVV)**

**The Concept**

This is the block where students get stuck for days. The Mission Assurance Student Guide (page 64) throws four sub-steps at you with dense acronyms (CA, PMD, PMV, PMVV) and does not make it obvious that they are describing the SAME control action from four different angles. Understand the connection and the four sub-steps collapse into a single, repeatable recipe.

A Control Action (CA) is one arrow from your Step 4.3 diagram, given a serial name. A Process Model Description (PMD) is an IF/THEN sentence describing when the CA should fire. The Process Model Variables (PMV) are the nouns inside that sentence - the things the controller has to check before acting. The Process Model Variable Values (PMVV) are the possible states each PMV can be in. In other words:

- 4.5 (PMD) is the sentence.

- 4.6 (PMV) is the nouns in that sentence.

- 4.7 (PMVV) is the possible values for each noun.

The reason the analysis forces you to do all four is that Step 5 (hazardous control actions) asks "what if this action fired at the WRONG time, or with the WRONG values?" That question only has meaning if you have already written down the conditions under which the action was supposed to fire (PMD), the things the controller was supposed to check (PMV), and the values those checks could return (PMVV). PMD/PMV/PMVV is the setup for the hazardous-control-action analysis.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Sources</strong></p>
<blockquote>
<p><strong>• The Step 4.3 diagram -</strong> each arrow becomes one CA row.</p>
<p><strong>• The Data Sheet -</strong> tells you the conditions under which each controller accepts a command (authentication, signatures, physical connections, etc.). The PMD is a paraphrase of what the Data Sheet says.</p>
<p><strong>• The System Architecture Diagram -</strong> confirms the physical inputs the controller checks.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>The Recipe</strong></p>
<blockquote>
<p><strong>1.</strong> Pick one arrow from your Step 4.3 diagram. Say it out loud in a full sentence: "[Operator] sends [command] to [controller] via [path]."</p>
<p><strong>2.</strong> Name it: use a serial convention like SOURCE_DEST_MODE_FUNCTION_CA# (e.g., MPN_MissionComputer_MissionPlan_LoadOFP_CA1). This is Step 4.4.</p>
<p><strong>3.</strong> Write the IF/THEN sentence: "Begin [command] when [condition A] AND [condition B] AND [condition C]." This is Step 4.5 (PMD).</p>
<p><strong>4.</strong> Underline the nouns in that sentence. Each noun is a PMV. Step 4.6 is just the list of nouns.</p>
<p><strong>5.</strong> For each noun, list the possible states. Usually two or three (authenticated / unauthenticated, connected / disconnected, valid / invalid). This is Step 4.7 (PMVV).</p>
<p><strong>6.</strong> Repeat for every arrow in Step 4.3. Most rows should take under two minutes once you have the pattern.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Worked Example - CF-189</strong></p>
<p><strong>CA1 - Loading the Operational Flight Plan (OFP) from the MPN into the Mission Computer:</strong></p>
<blockquote>
<p><strong>• Step 4.4 name:</strong> MPN_MissionComputer_MissionPlan_LoadOFP_CA1</p>
<p><strong>• Step 4.5 PMD sentence:</strong> Begin loading the OFP when the SIPR link is authenticated AND the OFP has a valid digital signature AND the Mission Load Laptop's wire is connected to the Mission Computer.</p>
<p><strong>• Step 4.6 PMVs (nouns):</strong> SIPR authentication, OFP digital signature, Wire connection</p>
<p><strong>• Step 4.7 PMVVs (values):</strong> SIPR = authenticated / unauthenticated; OFP sig = valid / invalid; Wire = connected / disconnected</p>
</blockquote>
<p><strong>Why this works:</strong></p>
<p>In Step 5 you will ask: "What if the Mission Computer accepted the OFP even though the SIPR link was unauthenticated?" That question is meaningful only because you named SIPR authentication as a PMV in Step 4.6 and gave it possible values in Step 4.7. Without 4.4-4.7, Step 5 has nothing to attack.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Mental Trick</strong></p>
<p>Sentence -&gt; nouns -&gt; values -&gt; name. Do them in that order. Pick an arrow, write the conditions-of-firing as a sentence (PMD), underline the nouns (PMVs), list the possible values for each noun (PMVVs), and give the whole thing a serial name (CA). If you follow that recipe you can fill a row in about ninety seconds.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Common Mistakes</strong></p>
<blockquote>
<p><strong>• Trying to fill CA, PMD, PMV, PMVV in column order.</strong> That is how the workbook is laid out, but not how a human thinks. Write the sentence (PMD) first, then extract nouns (PMVs), then list values (PMVVs), then name it (CA).</p>
<p><strong>• Under-specifying the PMD.</strong> "Begin loading when authenticated" is too vague. Enumerate every condition the controller actually checks.</p>
<p><strong>• Listing only one PMV per CA.</strong> Most controllers check multiple conditions. If your PMD had one AND, you probably missed conditions.</p>
<p><strong>• Skipping arrows.</strong> Every Step 4.3 arrow must appear as a CA row. If you have 12 arrows in slide 12 but only 6 CAs, you missed six.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<img src="data\corpus\media/media/image17.png" style="width:5in;height:6.47059in" />

*Figure 2.13 - Mission Assurance Student Guide page 64: Steps 4.4-4.7 build the process model around each control action.*

<img src="data\corpus\media/media/image18.png" style="width:5in;height:6.47059in" />

*Figure 2.14 - Mission Assurance Student Guide page 59: three degrees of controllability - useful mental scaffolding for the PMD.*

**In-Depth Explanation - The toaster analogy (child-friendly walkthrough)**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>In-Depth Explanation (from the author's cohort notes)</strong></p>
<p>Yeah - Steps 4.2 through 4.7 is where everyone hits the wall. The reason isn't that you're missing something. It's that the FMA-C guide throws six sub-steps at you with fancy names (PMD, PMV, PMVV) that all sound similar and never explains what problem those steps are actually solving. Once you see the problem, the steps become obvious.</p>
<p>So let me start with a toaster.</p>
<p><strong>The toaster you learned to use when you were five</strong></p>
<p>You have a toaster. You want toast. To get toast, three things exist:</p>
<p>You (the person who wants toast) -&gt; The toaster (the thing that decides when to turn heat on and when to pop up) -&gt; The bread (the thing that actually gets cooked).</p>
<p>That's it. That's the FMA-C model. In the student guide they call these three things Operator, Controller, and Functions. But it's just you, the toaster, and the bread.</p>
<p>Now here's the thing that makes it FMA-C instead of just "make toast": the toaster is where things can go wrong. If YOU forget to plug it in, no toast. If the BREAD is frozen, weird toast. But if the toaster's brain gets confused - if it thinks the bread is already toasted when it isn't, or thinks you didn't push the lever when you did - that's when your kitchen catches fire. The controller in the middle is where cyber threats live. So the whole point of Step 4 is to describe, in painful detail, exactly what the toaster is thinking so that later you can ask "what if a bad guy lied to the toaster?"</p>
<p><strong>Now let's do the six sub-steps on the toaster</strong></p>
<p>Step 4.2 - Responsibilities. Just a list of who does what. You: put bread in, push lever, wait, get toast out. Toaster: notice lever went down, turn on heat, run timer, pop up. Bread: absorb heat and turn brown. That's it. On your CF-189 sheet, this is the giant table with elements down the left side (PIC, Mission Computer, DSMS, etc.) and mission modes across the top (Ground Ops, Mission Planning, Ingress, etc.). You're just listing what each element's job is in each phase. Boring but easy.</p>
<p>Step 4.3 - Control Relationships. Draw arrows. Commands go DOWN (you push the lever = command down to the toaster; the toaster turns on the heating coils = command down to the bread). Feedback goes UP (the bread smells done = feedback up to the toaster's timer; the toaster pops up = feedback up to you). That's the diagram you already have on slide 12. Every arrow going down is a command. Every arrow going up is a feedback. Done.</p>
<p>Step 4.4 - Name every command. Now you give each arrow a serial number. The naming rule in the guide is SOURCE_DESTINATION_FUNCTION_CA#. So the arrow where YOU tell the TOASTER to start cooking becomes: You_Toaster_MakeToast_CA1. The arrow where the toaster tells the bread to cook becomes Toaster_Bread_MakeToast_CA1. You just give each thing a name so you can talk about it. That's it.</p>
<p>Step 4.5 - PMD (Process Model Description). For each named command, write an IF/THEN sentence describing when it should happen. For our toaster: "You_Toaster_MakeToast_CA1 begins when: bread is in the slot AND lever is pushed down AND toaster is plugged in." That IF/THEN is the PMD. It's the rules for when the command fires.</p>
<p>Step 4.6 - PMV (Process Model Variables). List the things the toaster has to check to decide. From the IF/THEN above, the toaster checks: bread in slot, lever position, power state. Those three checkable things are the PMVs. You're just naming what the toaster is looking at.</p>
<p>Step 4.7 - PMVV (Process Model Variable Values). For each PMV, list what values it can take. Bread in slot: yes / no. Lever position: up / down. Power state: on / off. That's the PMVVs. All the possible answers to each PMV question.</p>
<p>So 4.5 is the sentence, 4.6 is the nouns in that sentence, 4.7 is the possible answers for each noun. That's the whole trick. Once you see it that way, you stop thinking of them as three separate steps and start thinking of them as one control action described three different ways.</p>
<p><strong>Now the same thing on the CF-189</strong></p>
<p>Let's do CA1 - loading the Operational Flight Plan from the Mission Planning Network into the Mission Computer.</p>
<p>Who's involved? Operator = MPN Operator/Maintainer. Controller = Mission Computer (via the Mission Load Laptop). Function = "generate aircraft" - specifically loading the OFP so the plane knows where it's going.</p>
<p>Step 4.4 - name it: MPN_MissionComputer_MissionPlan_LoadOFP_CA1. The source is MPN, the destination is Mission Computer, the mission mode is Mission Planning, the function is LoadOFP, and it's control action number 1.</p>
<p>Step 4.5 - the IF/THEN sentence: Begin loading the OFP when the SIPR link is authenticated AND the OFP has a valid digital signature AND the Mission Load Laptop's wire is connected to the Mission Computer. That's the PMD.</p>
<p>Step 4.6 - pull the nouns out of that sentence: SIPR authentication, OFP digital signature, Wire connection. Those three are the PMVs. They are the things the Mission Computer is checking before it agrees to accept the OFP.</p>
<p>Step 4.7 - for each PMV, list its possible values: SIPR: authenticated / unauthenticated. OFP sig: valid / invalid. Wire: connected / disconnected. Those are the PMVVs.</p>
<p>That's a complete Step 4.4-4.7 entry. One row. Every other control action follows exactly this pattern - pick a command from your Step 4.3 diagram, name it, write the "when" sentence, pull the nouns, list the values.</p>
<p><strong>Why the guide made you do it this way</strong></p>
<p>Here's the payoff that makes all this suffering worth it. In Step 5 you're going to ask, for each control action, "what happens if this action fires when it shouldn't?" That question only has meaning if you've already written down the conditions under which it should fire. So Step 4.5 (the IF/THEN) isn't paperwork - it's the setup for the "hazardous control action" analysis in Step 5. When you say "the Mission Computer accepted the OFP even though the SIPR link wasn't authenticated," that's a hazard, and it's a hazard you can only describe because you took the time in 4.6 to say "SIPR authentication is one of the variables the controller checks."</p>
<p><strong>The mental trick that unsticks you</strong></p>
<p>When you're staring at a blank Step 4.4-4.7 row and don't know what to write, do these in this order:</p>
<p>Pick one arrow from your Step 4.3 control-relationships diagram. Say it out loud: "Vendor sends a Display Controller firmware update over the Windows 10 laptop." Now write the sentence: "Begin loading firmware when the vendor laptop is authenticated AND the USB-A/B cable is plugged in AND the firmware hash matches the vendor's published hash." Now underline the nouns in your sentence: laptop authentication, USB cable, firmware hash. Those are your PMVs. Now for each noun, write down the two or three possible states: authed/unauthed, connected/disconnected, match/mismatch. Those are your PMVVs. Then name it: Vendor_DisplayController_Maint_LoadFirmware_CA6.</p>
<p>That's the whole thing. Pick an arrow, write a sentence, underline the nouns, list the values, name it. If you follow that recipe you can fill a row in about ninety seconds.</p>
<p>The reason your team got stuck isn't that it's hard - it's that the guide describes the outputs (PMD, PMV, PMVV) without telling you the recipe. The recipe is: sentence -&gt; nouns -&gt; values -&gt; name.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

**Step 5 - Hazardous Control Actions (Four-Bin Analysis)**

**The Concept**

Step 5 is where the payoff of Step 4 arrives. For each control action you named in Step 4.4, you now ask four systematic bin questions - the "four bins" of hazardous control-action analysis. Mission Assurance Student Guide page 65 defines the bins. Each bin describes a way the control action could fail: not providing when required, providing when not required, providing at the wrong time, or stopping too soon / continuing too long.

Course 8 (Risk Assessment) provides the analytical mechanics behind this - you are essentially running a lightweight FMEA (Failure Mode and Effects Analysis) on each control action. Course 7 (Intel for Cyber) provides the KT-C Triad frame (Criticality + Vulnerability + Threat). In a training exercise you may be asked to reason only about the Criticality leg (this control action matters); in a real FMA-C at your home station, you would combine all three legs of the Triad to produce a full risk picture.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Sources</strong></p>
<blockquote>
<p><strong>• Every Control Action from Step 4.4 -</strong> each CA gets one Step 5 row.</p>
<p><strong>• The Hazards list from Step 3 -</strong> each bin failure maps to one or more commander-defined Hazards.</p>
<p><strong>• Mission Assurance Student Guide page 65 -</strong> defines the four bin categories.</p>
<p><strong>• The Data Sheet -</strong> tells you the physical/logical paths so you can identify which nodes are involved.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>The Recipe</strong></p>
<blockquote>
<p><strong>1.</strong> For each Step 4.4 CA, add a Step 5 row (or a set of four cells) for that CA.</p>
<p><strong>2. Ask Bin 1 - "Not Provided When Required":</strong> if this control action failed to happen when it should have, which of the commander's Hazards (H1-H5) would that produce? Write the Hazard numbers in the cell.</p>
<p><strong>3. Ask Bin 2 - "Provided When Not Required":</strong> if this control action fired when it shouldn't have, which Hazards would that produce?</p>
<p><strong>4. Ask Bin 3 - "Provided at the Wrong Time or in Wrong Order":</strong> if this control action fired too early, too late, or out of sequence, which Hazards would that produce?</p>
<p><strong>5. Ask Bin 4 - "Applied Too Long or Stopped Too Soon":</strong> if this control action ran for the wrong duration, which Hazards would that produce?</p>
<p><strong>6.</strong> For each bin that maps to any Hazard, identify the specific NODES involved (the controller, the operator, the physical path). Those nodes are your KT-C candidates.</p>
<p><strong>7.</strong> Sanity check: a healthy Step 5 row has at least one bin with a real hazard mapping. A CA where all four bins are "no impact" is either mis-scoped or truly irrelevant to the mission - flag it for review.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Worked Example - CF-189</strong></p>
<p><strong>CA1 - MPN_MissionComputer_MissionPlan_LoadOFP_CA1 - Step 5 four-bin analysis:</strong></p>
<blockquote>
<p><strong>• Bin 1 (Not Provided):</strong> If the OFP never loads, the aircraft has no route. Produces H1 (cannot navigate), H5 (cannot generate for tasking).</p>
<p><strong>• Bin 2 (Provided When Not Required):</strong> If an OFP loads without authorization (e.g., replayed from an old sortie), the aircraft flies the wrong route. Produces H1 and H2 (wrong-location delivery).</p>
<p><strong>• Bin 3 (Wrong Time / Wrong Order):</strong> If the OFP loads AFTER weapons are configured against the old route, coordinates and weapon assignments are misaligned. Produces H2.</p>
<p><strong>• Bin 4 (Wrong Duration):</strong> Load timing is transactional; N/A.</p>
</blockquote>
<p><strong>Nodes touched by this CA (KT-C candidates):</strong></p>
<blockquote>
<p>• MPN (source)</p>
<p>• Mission Load Laptop (transport)</p>
<p>• SIPR authentication service (validator)</p>
<p>• Mission Computer (destination)</p>
</blockquote>
<p>Every one of those nodes is a candidate for the KT-C list, because a cyber effect at any of them can produce H1, H2, or H5.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Mental Trick</strong></p>
<p>For each of the four bins, ask the question with your finger on the Step 3 Hazards list: "Would this failure mode cause H1? H2? H3? H4? H5?" If the answer is yes for any Hazard, the bin has a hazard mapping. If the answer is no for all Hazards, that bin is empty for this CA - write "N/A" and move on. Don't stare at the ceiling; look at the Hazards list.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Common Mistakes</strong></p>
<blockquote>
<p><strong>• Reasoning about attacks instead of failures.</strong> Bin analysis is about failure modes (what if the CA behaves wrong), not about attacker techniques. In this exercise threat is excluded - stay on failure modes.</p>
<p><strong>• Skipping Bin 4.</strong> Duration failures matter for streaming CAs (bus traffic, sensor updates). Even if most CAs are transactional, some are not.</p>
<p><strong>• Forgetting to name nodes.</strong> Bins without nodes don't produce KT-C entries. Always list the specific components involved.</p>
<p><strong>• Marking bins with Hazards they don't actually produce.</strong> Force yourself to state the causal chain for every hazard you cite. If you can't, the mapping is wrong.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<img src="data\corpus\media/media/image19.png" style="width:5in;height:6.47059in" />

*Figure 2.15 - Mission Assurance Student Guide page 65: the four bins of hazardous control-action analysis.*

<img src="data\corpus\media/media/image20.png" style="width:5in;height:7.06431in" />

*Figure 2.16 - Risk Assessment (Course 8) page 13: mission-focused prepare tasks - the mission-impact reasoning behind Step 5 lives here.*

**KT-C - Key Terrain Cyber Identification**

**The Concept**

Key Terrain Cyber (KT-C) is the OUTPUT of the FMA-C process, not an input. Mission Assurance Student Guide pages 22-26 define KT-C as those cyber nodes whose compromise or loss would prevent execution of a mission essential function. Course 7 (Intel for Cyber) frames KT-C identification through the KT-C Triad: Criticality (does the mission depend on this?), Vulnerability (can it be attacked?), and Threat (is there an adversary who would attack it?).

In this exercise you are computing only the Criticality leg - a node is KT-C if the mission depends on it. In a full-doctrine FMA-C at your home station, a node is KT-C only if all three legs of the Triad concur. Do not delete the Vulnerability and Threat legs from your mental model just because they are out of scope for this exercise - every real KT-C list is eventually pressure-tested against all three legs.

Cyber Incident Response (Course 9) explains what happens to the KT-C list downstream. When an incident occurs on the wing, incident responders "focus recovery efforts on the most critical assets and systems identified as key terrain-cyber (KT-C)." Your KT-C list is what tells them what to save first. That is why the list must be defensible, granular, and traceable back to Step 5 - a hand-wavy KT-C list means a hand-wavy incident response.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Sources</strong></p>
<blockquote>
<p><strong>• Every Step 5 bin analysis -</strong> any node touched by a CA whose bin produces a commander Hazard is a KT-C candidate.</p>
<p><strong>• Mission Assurance Student Guide pages 22-26 -</strong> the doctrinal definition of MRT-C vs KT-C and the KT-C Triad.</p>
<p><strong>• Course 7 pages 21-22, 28 -</strong> additional Triad context (Threat and Vulnerability legs).</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>The Recipe</strong></p>
<blockquote>
<p><strong>1.</strong> Walk every Step 5 row. For each bin that produces a Hazard, collect all nodes involved (from the CA definition in Step 4.4 and the Data Sheet path).</p>
<p><strong>2.</strong> Deduplicate - the same node will appear in multiple CAs. That is a signal it is highly critical.</p>
<p><strong>3.</strong> For each unique node, write a one-line justification: which Hazards are enabled if this node is compromised, and via which CAs.</p>
<p><strong>4.</strong> Rank the list by number of Hazards enabled (nodes enabling more Hazards are higher priority). This is a Criticality-only ranking - do not attempt to fold Threat/Vulnerability into it in this exercise.</p>
<p><strong>5.</strong> Format the final list as a table: Node | Bus/Path | Hazards enabled | Justification. This becomes slide 16 of the briefing.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Worked Example - CF-189</strong></p>
<p><strong>Representative CF-189 KT-C entries (subset - the full list has ~10-14 nodes):</strong></p>
<blockquote>
<p><strong>• Mission Computer / Bus Controller:</strong> enables H1, H2, H5 (nav, wrong-location, cannot generate). Central bus controller on 1553; compromise cascades through most CAs.</p>
<p><strong>• MPN + Mission Load Laptop:</strong> enables H1, H2 (loads OFP; corrupted OFP = wrong route or wrong target).</p>
<p><strong>• DSMS:</strong> enables H2 (manages stores; corrupted stores profile = wrong ordnance to wrong location).</p>
<p><strong>• FMS:</strong> enables H1 (navigation source of truth).</p>
<p><strong>• Display Controller + Vendor Windows 10 Laptop:</strong> enables H1 (displays wrong nav data to pilot); firmware update path is a supply-chain surface.</p>
<p><strong>• FADEC:</strong> enables H3 (engine control; compromise = loss of flight).</p>
<p><strong>• COMSEC Custodian workflow (IFF/RWR/MW keys):</strong> enables H4 (mis-loaded keys = comms and IFF failure).</p>
</blockquote>
<p>Note how each entry cites specific Hazards. That traceability - Node -&gt; Hazard -&gt; Loss - is what makes the list defensible when the Wing Commander asks "why this one?"</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Mental Trick</strong></p>
<p>KT-C is not a step you do - it is a list you HARVEST from Step 5. If a node appears in any Step 5 bin that produces any Hazard, that node is on the list. Your only work is deduplication, justification, and ranking.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Common Mistakes</strong></p>
<blockquote>
<p><strong>• Trying to identify KT-C before finishing Step 5.</strong> KT-C is derivative. Skipping Step 5 and jumping straight to KT-C is guessing.</p>
<p><strong>• Listing controllers only, not paths.</strong> The Mission Load Laptop is on the list too, not just the Mission Computer. Attack paths are terrain.</p>
<p><strong>• Confusing MRT-C and KT-C.</strong> MRT-C (Mission-Relevant Terrain Cyber) is the broader set; KT-C is the essential subset. See MA guide page 22.</p>
<p><strong>• Forgetting the ranking.</strong> The Wing Commander wants to know which two or three matter most. Rank by Hazard count and add a brief justification for the top items.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<img src="data\corpus\media/media/image21.png" style="width:5in;height:6.47059in" />

*Figure 2.17 - Mission Assurance Student Guide page 22: MRT-C and the broader terrain concept.*

<img src="data\corpus\media/media/image22.png" style="width:5in;height:6.47059in" />

*Figure 2.18 - Mission Assurance Student Guide page 23: KT-C as the essential subset.*

<img src="data\corpus\media/media/image23.png" style="width:5in;height:6.47059in" />

*Figure 2.19 - Mission Assurance Student Guide page 24: the KT-C Triad - Criticality + Vulnerability + Threat.*

<img src="data\corpus\media/media/image24.png" style="width:5in;height:6.47059in" />

*Figure 2.20 - Mission Assurance Student Guide page 26: KT-C flow chart tying the analysis back into the operational picture.*

<img src="data\corpus\media/media/image25.png" style="width:5in;height:6.47005in" />

*Figure 2.21 - Intel for Cyber (Course 7) page 28: KT-C Triad detail from the Intel course.*

<img src="data\corpus\media/media/image26.png" style="width:5in;height:6.47005in" />

*Figure 2.22 - Cyber Incident Response (Course 9) page 14: the downstream use of the KT-C list - incident responders prioritize recovery of KT-C nodes.*

**Part 3 - Building the Briefing (From Workbook to Slides)**

------------------------------------------------------------------------

**3.1 Why brief the results?**

Communications and Briefings (Course 4) starts from a simple observation: a wing commander does not read Excel workbooks. The FMA-C work is only useful to the wing when it is compressed into a defensible briefing that a commander can absorb in ten to twenty minutes and sign. Everything you did in Part 2 exists to feed this briefing.

A good FMA-C briefing does three things: (1) it shows the commander what you were told and asked to protect (Steps 1-3, and the METs/TCAs from the exercise brief); (2) it shows how you decomposed the mission into elements, responsibilities, control actions, and hazards (Step 4 and Step 5); and (3) it hands the commander a short, defensible KT-C list to sign. If any of those three arcs is missing from your slides, the commander cannot approve the analysis.

**3.2 Universal briefing structure**

Every FMA-C briefing - for any airframe - should include, in this order:

- Cover / title slide (wing, MDS, brief title, date, briefer name)

- Mission / Commander's Intent / CI (from the Commander brief)

- MEF / METs (from the Commander brief)

- TCAs (from the Commander brief)

- Step 1 - AST / BMO / IOTCT

- Step 2 - Unacceptable Losses

- Step 3 - Mission Hazards

- Step 3 - H/L Crosswalk (grid)

- IPR 1 - Interim Progress Review checkpoint

- Step 4.1 - 3-tier model diagram (Operators / Controllers / Functions)

- Step 4.2 - Responsibilities matrix (elements x modes)

- Step 4.3 - Control relationships diagram (arrows)

- Step 4.4-4.7 - Control actions and process model (subset table)

- IPR 2 - Interim Progress Review checkpoint

- Step 5 - Four-bin analysis (subset table)

- KT-C - Identified terrain (final table, ranked)

- Questions / contact

**3.3 Slide-by-slide mapping (generic + CF-189 example)**

The table below lists a canonical 17-slide FMA-C briefing. The "What Feeds It" column is airframe-agnostic - you would use the same sources for any MDS. The "CF-189 Presentation Note" column is specific to the CF-189 exercise.

| **\#** | **Slide** | **What Feeds It** | **CF-189 Presentation Note** |
|----|----|----|----|
| 1 | Title | Static - wing name, MDS, brief title, date, briefer | "189th Composite Wing - CF-189 FMA-C - 14 Jul 2026" |
| 2 | Mission / CI | Commander brief | Copy verbatim from exercise doc |
| 3 | MEF / METs | Commander brief | List MEF and four METs verbatim |
| 4 | TCAs | Commander brief | Time-critical actions (medevac, strike windows) |
| 5 | Step 1 - AST/BMO/IOTCT | Step 1 workbook / Part 2 Step 1 | Paste verbatim from the Excel Step 1 sheet |
| 6 | Step 2 - Unacceptable Losses | Step 2 workbook | Three ULs verbatim |
| 7 | Step 3 - Hazards | Step 3 workbook | Five Hazards verbatim |
| 8 | Step 3 - H/L Crosswalk | Step 3 crosswalk cells | Paste as 5x3 grid with Y/N |
| 9 | IPR 1 | Post-backbrief | Name/date/time of reviewer |
| 10 | Step 4.1 - Model | Derived (BMO + Data Sheet + METs) | 3-tier box diagram - Ops/Aircrew/MX top; MPN/MC/DSMS/DC/FMS middle; GEN/PLAN/ALIFT/STRIKE bottom |
| 11 | Step 4.2 - Responsibilities | Step 4.2 workbook | Paste as table with 8pt font |
| 12 | Step 4.3 - Control Relationships | Derived (4.1 diagram + Data Sheet paths) | Same 3-tier diagram, plus solid Command arrows down and dashed Feedback arrows up |
| 13 | Step 4.4-4.7 - CA/PMD/PMV/PMVV | Step 4.4-4.7 workbook | Paste a subset (5-6 CAs fit); reference full list in workbook |
| 14 | IPR 2 | Post-SME backbrief | Name/date/time |
| 15 | Step 5 - Four Bins | Step 5 workbook | Paste subset (top CAs) |
| 16 | KT-C Identified | Step 5 -\> KT-C harvest | Ranked table: Node \| Bus/Path \| Hazards \| Justification |
| 17 | Questions | Static | Contact info; back-brief POC |

Do not add slides. If your instinct is to add a "conclusions" or "recommendations" slide, resist - the KT-C table on slide 16 IS the recommendation. Adding editorial slides softens the commander's decision.

**3.4 Presenting to the Commander**

Course 4 (Communications & Briefings) offers a few guardrails specific to briefing a wing commander:

- Frame each slide with one sentence of context BEFORE clicking to the next slide. "This is Step 3 - the five Hazards the commander has already told us they cannot accept." Commanders track state through your framing sentences.

- Speak Hazards and Losses in the commander's language, not the analyst's. "Loss of aircraft" not "Availability compromise."

- For the KT-C slide, name the top two or three nodes out loud and explain what happens if they are lost. Do not read the whole table - the table is the record; you are the interpreter.

- Anticipate three questions: (a) "Are we exposed?" (b) "What are you doing about it?" (c) "What do you need from me?" Course 4 recommends holding one-line answers to these ready.

- Close by naming what you need the commander to do next: sign the KT-C list, approve the follow-on assessment, or task additional data collection.

The briefing is the moment the analysis meets the mission owner. Everything in Parts 1 and 2 was preparation for the ten minutes on slide 16.

**Part 4 - Common Pitfalls and FAQ**

------------------------------------------------------------------------

Questions students have actually asked while working through an FMA-C for the first time. Answers assume a training-exercise context but note where a home-station FMA-C would differ.

**1. Do we do threat or vulnerability analysis?**

Not in this exercise - the CF-189 exercise explicitly excludes threat, vulnerability, and risk scoring. Your KT-C list is Criticality-only. In a real home-station FMA-C the full KT-C Triad from Course 7 applies (Criticality + Vulnerability + Threat), and Course 8's risk mechanics combine the three into a scored risk register.

**2. Which document wins when two of my sources conflict?**

The Commander / Exercise brief wins for anything about the mission (MEF, METs, TCAs, Losses, Hazards). The Aircraft Data Sheet wins for anything about the airframe (buses, controllers, update paths). If they conflict on a topic they both address, note it in an IPR question - do not silently resolve.

**3. How much detail per Step 4.2 cell?**

Enough that a reviewer who doesn't know the aircraft can tell what interfaces are open and what data is flowing. A one-liner is fine; a complete sentence is better. "Active" is not enough; "Manages stores state, executes release, chaff/flare, UAV control via Link" is right-sized.

**4. What if the Data Sheet doesn't mention something my team thinks is important?**

Two options. Either (a) it's out of scope for this analysis and you drop it, or (b) it's a gap in your source material and you flag it as an IPR question for the SME. Do not invent content to fill the gap. Invented content propagates into Step 5 and pollutes the KT-C list.

**5. Do I need a row in Step 4.2 for every human on the base?**

No. Only humans who directly execute a mission function or command a controller. The COMSEC Custodian is in because they load keys into IFF/RWR/MW; the base commander is out because they do not touch a controller. If in doubt, ask: "Does this person's action change what a controller does?"

**6. Step 4.1 lives on a slide, not on an Excel sheet. Is that right?**

Yes. The BLANK Excel template does not have a dedicated Step 4.1 sheet. Step 4.1 is drawn on slide 10 of the briefing. This is a common source of confusion for students expecting a 1:1 mapping between workbook sheets and briefing slides.

**7. How many Control Actions should Step 4.4-4.7 have?**

Exactly as many as there are Command arrows in your Step 4.3 diagram. If you drew 12 arrows, you should have 12 CA rows. Fewer = you missed some. More = you doubled up.

**8. My PMD sentence has ten AND conditions. Is that OK?**

It's fine, but try to group them. If the controller checks five things about the incoming OFP (signature, source, timestamp, sequence, hash), you can write "OFP validation passes" as a single PMV with a compound PMVV. Just be explicit in a sub-note about what the compound check covers.

**9. How do I decide which nodes make the KT-C list?**

Every node that appears in any Step 5 bin that produces any Hazard is a KT-C candidate. Deduplicate, then rank by how many distinct Hazards each node enables. The top 5-10 nodes are your KT-C. This is a Criticality-only ranking - see Q1.

**10. How does the KT-C list get used after I deliver it?**

Course 9 (Cyber Incident Response) explains this: when an incident hits the wing, incident responders prioritize recovery based on the KT-C list. That is why the list must be defensible and specific. "The Mission Computer" is a KT-C entry; "cyber stuff on the plane" is not.

**11. My teammate and I filled Step 4.1 differently. Which of us is right?**

Probably both. Step 4.1 is the only step in the FMA-C that is a DESIGN step - you make scoping choices. Two competent MACCEs will make slightly different choices (three Functions vs four; PLAN as a separate box or folded into GEN). What matters is that your choice is defensible and consistent through the rest of your analysis. Pick one, commit, and carry it through.

**Part 5 - Appendices**

------------------------------------------------------------------------

**Appendix A - MACCE 2026 Course Cross-Reference**

The FMA-C process draws on multiple MACCE 2026 courses. Use this table to find which course you should reread when you're stuck at a specific step. Course numbers correspond to the MACCE 2026 courseware sequence.

| **MACCE 2026 Course** | **FMA-C Steps Supported** | **How It Helps** |
|----|----|----|
| Course 1 - MACCE Fundamentals | Part 1 sections 1.1-1.2 | Grounds the MACCE role and situates FMA-C as the primary analytical product. |
| Course 3 - Critical Reasoning & Structured Analysis | Step 3 (H/L Crosswalk), Step 5 | Provides the analytic-rigor techniques (ACH, Key Assumptions Check) for causal reasoning. |
| Course 4 - Communications & Briefings | Part 3 (all sections) | Framework for structuring the FMA-C briefing and communicating with commanders. |
| Course 5 - Mission Systems Fundamentals | Part 1 section 1.4; Step 4.1; Step 4.2 | Purdue Model, OT/ICS context, the on-aircraft controller inventory (MC, EWS, ADC, FADEC, etc.). |
| Course 6 - Mission Assurance | All of Part 2 (main reference) | The FMA-C process itself - every step in Part 2 references a page in this student guide. |
| Course 7 - Intel for Cyber | Step 5, KT-C | The KT-C Triad (Criticality + Vulnerability + Threat); threat vectors relevant to embedded/OT systems. |
| Course 8 - Risk Assessment | Step 3, Step 5 | NIST RMF context; the hazard/likelihood/impact reasoning behind Step 5. |
| Course 9 - Cyber Incident Response | KT-C (downstream use) | Explains how KT-C is used by incident responders to prioritize recovery. |
| Course 10 - Tactical Planning | Step 4.2 (mode selection) | The sortie-timeline concept that becomes the columns of the Step 4.2 responsibilities matrix. |

**Appendix B - CF-189 Source Documents**

This appendix embeds the primary source materials referenced throughout the guide, in the same order a student would encounter them. Use it as a quick reference when working through the exercise.

**B.1 CF-189 Data Sheet (6 pages)**

<img src="data\corpus\media/media/image27.png" style="width:5.3in;height:6.85882in" />

*Figure B.1.1 - CF-189 Data Sheet page 1.*

<img src="data\corpus\media/media/image28.png" style="width:5.3in;height:6.85882in" />

*Figure B.1.2 - CF-189 Data Sheet page 2.*

<img src="data\corpus\media/media/image29.png" style="width:5.3in;height:6.85882in" />

*Figure B.1.3 - CF-189 Data Sheet page 3.*

<img src="data\corpus\media/media/image30.png" style="width:5.3in;height:6.85882in" />

*Figure B.1.4 - CF-189 Data Sheet page 4.*

<img src="data\corpus\media/media/image31.png" style="width:5.3in;height:6.85882in" />

*Figure B.1.5 - CF-189 Data Sheet page 5.*

<img src="data\corpus\media/media/image32.png" style="width:5.3in;height:6.85882in" />

*Figure B.1.6 - CF-189 Data Sheet page 6.*

**B.2 CF-189 Diagram (7 slides)**

<img src="data\corpus\media/media/image33.png" style="width:5.8in;height:3.2625in" />

*Figure B.2.1 - CF-189 Diagram slide 1.*

<img src="data\corpus\media/media/image34.png" style="width:5.8in;height:3.2625in" />

*Figure B.2.2 - CF-189 Diagram slide 2.*

<img src="data\corpus\media/media/image35.png" style="width:5.8in;height:3.2625in" />

*Figure B.2.3 - CF-189 Diagram slide 3.*

<img src="data\corpus\media/media/image36.png" style="width:5.8in;height:3.2625in" />

*Figure B.2.4 - CF-189 Diagram slide 4.*

<img src="data\corpus\media/media/image37.png" style="width:5.8in;height:3.2625in" />

*Figure B.2.5 - CF-189 Diagram slide 5.*

<img src="data\corpus\media/media/image38.png" style="width:5.8in;height:3.2625in" />

*Figure B.2.6 - CF-189 Diagram slide 6.*

<img src="data\corpus\media/media/image39.png" style="width:5.8in;height:3.2625in" />

*Figure B.2.7 - CF-189 Diagram slide 7.*

**B.3 FMA-C Exercise (CF-189) (3 pages)**

<img src="data\corpus\media/media/image40.png" style="width:5.3in;height:6.85882in" />

*Figure B.3.1 - FMA-C Exercise (CF-189) page 1.*

<img src="data\corpus\media/media/image41.png" style="width:5.3in;height:6.85882in" />

*Figure B.3.2 - FMA-C Exercise (CF-189) page 2.*

<img src="data\corpus\media/media/image42.png" style="width:5.3in;height:6.85882in" />

*Figure B.3.3 - FMA-C Exercise (CF-189) page 3.*

**B.4 Mission Assurance Student Guide - Key Pages**

<img src="data\corpus\media/media/image21.png" style="width:5in;height:6.47059in" />

*Figure B.4 - Mission Assurance Student Guide: MRT-C (page 22) - the broader mission-relevant terrain concept.*

<img src="data\corpus\media/media/image22.png" style="width:5in;height:6.47059in" />

*Figure B.4 - Mission Assurance Student Guide: KT-C (page 23) - the essential subset.*

<img src="data\corpus\media/media/image23.png" style="width:5in;height:6.47059in" />

*Figure B.4 - Mission Assurance Student Guide: KT-C Triad (page 24) - Criticality + Vulnerability + Threat.*

<img src="data\corpus\media/media/image24.png" style="width:5in;height:6.47059in" />

*Figure B.4 - Mission Assurance Student Guide: KT-C Flow Chart (page 26) - how KT-C feeds operational cyber decisions.*

<img src="data\corpus\media/media/image5.png" style="width:5in;height:6.47059in" />

*Figure B.4 - Mission Assurance Student Guide: Step 1 tri-fold (page 52) - Purpose / Goal / Task.*

<img src="data\corpus\media/media/image6.png" style="width:5in;height:6.47059in" />

*Figure B.4 - Mission Assurance Student Guide: Step 1 (page 54) - AST/BMO/IOTCT structure.*

<img src="data\corpus\media/media/image7.png" style="width:5in;height:6.47059in" />

*Figure B.4 - Mission Assurance Student Guide: Step 2 (page 55) - Unacceptable Losses.*

<img src="data\corpus\media/media/image8.png" style="width:5in;height:6.47059in" />

*Figure B.4 - Mission Assurance Student Guide: Step 3 (page 56) - Mission Hazards.*

<img src="data\corpus\media/media/image9.png" style="width:5in;height:6.47059in" />

*Figure B.4 - Mission Assurance Student Guide: Step 3 (page 57) - H/L Crosswalk.*

<img src="data\corpus\media/media/image18.png" style="width:5in;height:6.47059in" />

*Figure B.4 - Mission Assurance Student Guide: Three Degrees of Controllability (page 59).*

<img src="data\corpus\media/media/image12.png" style="width:5in;height:6.47059in" />

*Figure B.4 - Mission Assurance Student Guide: Step 4.1 (page 60) - 3-tier model.*

<img src="data\corpus\media/media/image13.png" style="width:5in;height:6.47059in" />

*Figure B.4 - Mission Assurance Student Guide: Step 4.1 continued (page 61) - A-10C example.*

<img src="data\corpus\media/media/image14.png" style="width:5in;height:6.47059in" />

*Figure B.4 - Mission Assurance Student Guide: Step 4.2 (page 62) - Responsibilities matrix.*

<img src="data\corpus\media/media/image16.png" style="width:5in;height:6.47059in" />

*Figure B.4 - Mission Assurance Student Guide: Step 4.3 (page 63) - Control Relationships.*

<img src="data\corpus\media/media/image17.png" style="width:5in;height:6.47059in" />

*Figure B.4 - Mission Assurance Student Guide: Steps 4.4-4.7 (page 64) - CA / PMD / PMV / PMVV.*

<img src="data\corpus\media/media/image19.png" style="width:5in;height:6.47059in" />

*Figure B.4 - Mission Assurance Student Guide: Step 5 (page 65) - Four bins of hazardous control-action analysis.*

<img src="data\corpus\media/media/image43.png" style="width:5in;height:6.47059in" />

*Figure B.4 - Mission Assurance Student Guide: Step 6 (page 66) - beyond the exercise scope; shown for context.*

**Appendix C - CF-189 Full Answers (Cheat Sheet)**

Concise reference of the actual filled cells and briefing slide contents for the CF-189 exercise. This is the "cheat sheet" collapsed into a single appendix so the body of the guide can stay generic. Use it to cross-check your own workbook, not as a copy-paste source.

**C.1 Step 1 - AST / BMO / IOTCT**

- **AST:** 189th Composite Wing conducts strategic airlift, aerial refueling, aeromedical evacuation, and precision strike.

- **BMO:** generating aircraft, providing rapid, precision airlift support and precision strike capabilities.

- **IOTCT:** comply with the Wing Commander's tasking to project combat power in support of USCENTCOM operations.

**C.2 Step 2 - Unacceptable Losses**

- **UL1:** Loss of aircraft.

- **UL2:** Loss of aircrew.

- **UL3:** Failure to execute time-critical cargo or strike mission.

**C.3 Step 3 - Mission Hazards and Crosswalk**

- **H1:** Aircraft cannot navigate to the tasked target/airfield.

- **H2:** Aircraft delivers ordnance or cargo to the wrong location.

- **H3:** Aircraft loses flight control or engine performance.

- **H4:** Aircraft cannot communicate mission-critical data.

- **H5:** Aircraft cannot generate for tasking.

H/L Crosswalk (Y/N):

| **Hazard** | **UL1 (Aircraft)** | **UL2 (Aircrew)** | **UL3 (Mission)** |
|----|----|----|----|
| H1 Cannot navigate | Y | Y | Y |
| H2 Wrong-location delivery | N | N | Y |
| H3 Flight/engine loss | Y | Y | Y |
| H4 Comms failure | N | N | Y |
| H5 Cannot generate | N | N | Y |

**C.4 Step 4.1 - Three-Tier Model**

- **Operators (top):** Operations, Aircrew (PIC), Maintenance

- **Controllers (middle):** MPN, Mission Computer/BC, DSMS, Display Controller, FMS

- **Functions (bottom):** GEN, PLAN, ALIFT, STRIKE

**C.5 Step 4.2 - Responsibilities (illustrative rows)**

| **Element** | **Ground Ops** | **Mission Planning** | **Ingress** | **Cargo/Strike** | **Egress/RTB** |
|----|----|----|----|----|----|
| PIC | Preflight, walk-around | Attend brief | Fly to target | Execute delivery/release | Fly home, land |
| Mission Computer | Self-test | Accept OFP | Nav + comms mgmt | Coordinate stores/nav | Log + shutdown |
| DSMS | Standby | Accept stores profile (SSD) | Standby | Manage stores; execute release | Standby |
| FMS | Init | Load route | Nav to route | Nav to target | Nav to base |
| MPN | n/a | Generate/sign OFP | n/a | n/a | Receive post-flight data |
| Vendor Tech | Firmware push if scheduled | n/a | n/a | n/a | n/a |
| COMSEC Custodian | Load IFF/RWR/MW keys | n/a | n/a | n/a | Recover keys |

**C.6 Step 4.3 - Representative Arrows**

- MPN -\> Mission Computer: LoadOFP (down, solid)

- Aircrew -\> FMS: SelectRoute (down, solid)

- Aircrew -\> DSMS: ReleaseStores (down, solid)

- Vendor Tech -\> Display Controller: LoadFirmware (down, solid)

- COMSEC Custodian -\> IFF/RWR/MW: LoadKeys (down, solid)

- Mission Computer -\> Aircrew (via Display Controller): StatusDisplay (up, dashed)

- FMS -\> Mission Computer: NavFeedback (up, dashed)

**C.7 Step 4.4-4.7 - CA1 (LoadOFP)**

- **CA name:** MPN_MissionComputer_MissionPlan_LoadOFP_CA1

- **PMD:** Begin loading the OFP when the SIPR link is authenticated AND the OFP has a valid digital signature AND the Mission Load Laptop's wire is connected to the Mission Computer.

- **PMVs:** SIPR authentication; OFP digital signature; Wire connection

- **PMVVs:** SIPR: authenticated / unauthenticated; OFP sig: valid / invalid; Wire: connected / disconnected

**C.8 Step 5 - Four-Bin Analysis for CA1**

- **Bin 1 (Not Provided):** H1 (nav), H5 (generate)

- **Bin 2 (Provided When Not Required):** H1, H2 (wrong-location)

- **Bin 3 (Wrong Time):** H2

- **Bin 4 (Wrong Duration):** N/A

**C.9 KT-C List (Ranked)**

| **Rank** | **Node** | **Bus / Path** | **Hazards Enabled** | **Justification** |
|----|----|----|----|----|
| 1 | Mission Computer / BC | 1553 | H1, H2, H5 | Central bus controller; compromise cascades. |
| 2 | MPN + Mission Load Laptop | SIPR -\> wired | H1, H2 | OFP source; corruption = wrong route/target. |
| 3 | DSMS | 1760 | H2 | Stores mgmt; corrupt profile = wrong ordnance. |
| 4 | FMS | AFDX | H1 | Nav source of truth. |
| 5 | Display Controller + Vendor W10 Laptop | AFDX + USB | H1 | Displays nav; firmware supply chain. |
| 6 | FADEC | Engine control bus | H3 | Engine control; compromise = loss of flight. |
| 7 | COMSEC Custodian workflow | Key-load path | H4 | Bad keys = IFF/RWR/MW failure. |

**Appendix D - BLANK Template Map**

The FMAC Tables for CF189 (BLANK) workbook contains one sheet per FMA-C step. Use this map as a checklist so you know which sheet holds which analysis.

| **Sheet** | **Contents** | **Row Labels** | **Column Labels** | **Notes** |
|----|----|----|----|----|
| Step 1 | AST / BMO / IOTCT | AST; BMO; IOTCT | Value column | Paste verbatim from Commander brief. |
| Step 2 | Unacceptable Losses | UL1; UL2; UL3 | Description | Paste verbatim; one per row. |
| Step 3 | Hazards + H/L Crosswalk + Constraints | H1-H5 | UL columns Y/N + Constraint text | Fill Y/N grid; invert each Hazard into a Constraint. |
| Step 4.1 | (not in workbook) | \- | \- | Lives on briefing slide 10, not on a sheet. |
| Step 4.2 | Responsibilities matrix | Elements (15-18 rows) | Mission modes (5 columns) | Rows = 4.1 boxes + Data Sheet ancillary + Exercise doc roles. |
| Step 4.3 | (not in workbook) | \- | \- | Lives on briefing slide 12 as an arrow diagram. |
| Step 4.4-4.7 | Control Actions + PMD/PMV/PMVV | CA rows (one per Step 4.3 arrow) | CA name; PMD; PMV; PMVV | Fill sentence -\> nouns -\> values -\> name. |
| Step 5 | Four-bin hazardous control action | CA rows | Bin 1; Bin 2; Bin 3; Bin 4 (each cell lists Hazards) | Harvest KT-C candidates from non-empty bins. |
| KT-C | Final ranked list | Nodes | Bus/Path; Hazards enabled; Justification | Deduplicated from Step 5; ranked by Hazard count. |

The two "(not in workbook)" rows are worth internalizing: Step 4.1 and Step 4.3 both live on briefing slides rather than Excel sheets. Students who expect a 1:1 mapping between workbook sheets and briefing slides get confused when the workbook "is missing" Steps 4.1 and 4.3. It is not missing them - they are drawn artifacts, not tabular ones.
