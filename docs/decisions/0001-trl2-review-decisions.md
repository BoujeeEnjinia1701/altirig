---
doc_id: ALR-DDR-001
title: AltiRig TRL 2 review decisions
project: AltiRig
doc_type: Design decision record
version: "0.1"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-03'
  author: Amish Chadha
  change: TRL 2 review decisions D1 to D14, decided under Amish's 2026-10-03 pre-approvals
---

# 0001: TRL 2 review decisions

- **Date:** 2026-10-03
- **Status:** decided. Amish, 2026-10-03: "start with the first 14 repos from the list of 29 projects. I pre-approve the batch runs along with any recommendations you come up with. I also accept any cost overruns or variations from the assumed scope cost." And for this second batch, Amish, 2026-10-03: "Proceed with the remaining 15 scaffolds". Each decision below is the recommendation made at the TRL 2 review and is decided as recommended. Requirements that are not met or at risk are not decided here; they are posed to Amish in `docs/REVIEW.md` and the design decisions register.

## Context

The scaffold (ALR-PRC-001 v0.1) described a sealed vessel with a thrust stand inside and left open the vessel type, whether to chill the air, how to deal with the propeller's recirculating wake, and whether a propeller and motor kit belongs in this repo. The TRL 2 review settled these so the TRL 3 calculations (ALR-CAL-001), the model and the build plan could proceed. Choices that touch safety take the conservative option, and each says what evidence would relax it.

> **Safety:** AltiRig is a vacuum vessel with a spinning propeller inside, run from mains power. These decisions set the design basis on paper only. Nothing here makes the chamber safe to use; it is not certified pressure equipment or test equipment.

## Decisions

*Table 1. TRL 2 review decisions.*

| # | Decision | Reason | Affects |
| --- | --- | --- | --- |
| D1 | Match air density, not pressure: R1's 0.74 kg/m3 is reached at about 61.9 kPa at 20 °C; pressure and temperature are logged with every point | Thrust and power scale with density; at room temperature, 54 kPa would give the density of about 6,100 m | R1; controller; ALR-CAL-001 A |
| D2 | Vessel: a horizontal 813 mm (32 in) x 6.35 mm steel pipe offcut, 1,500 mm long, with two bought 2:1 ellipsoidal tank heads; one head welded on the rear, one on a flange ring as the door | A thin steel drum collapses at a few kPa of vacuum; a flat-panelled box needs heavy ribs; pipe and tank heads are stocked items a welding shop can join | Vessel parts; R5, R7; cost |
| D3 | Design the vessel for full vacuum (101.3 kPa difference) and apply R7's factor of 4 at full vacuum, not only at the working point | Conservative: the pump can reach near full vacuum if the relief valve sticks. Relax only with a code calculation by a qualified engineer and a strain-gauged proof test | R7; ALR-CAL-001 B |
| D4 | Add R12: an adjustable vacuum relief valve opens at 55 kPa below atmosphere, so the chamber cannot go below 46.3 kPa absolute in normal use | Covers every working point (lowest 57.4 kPa) with margin and limits the load on the window and the door | R12; valve manifold |
| D5 | Add R11: the motor can be armed only with the door latched (interlock switch) and the key turned; the emergency stop removes motor and pump power; the bleed valve is normally open, so the chamber vents on loss of power | The door is held shut by air under vacuum, so the hazard is a running propeller when the door is open or a run that cannot be stopped | R11; cabinet; build plan safety stops |
| D6 | Window: clear polycarbonate 20 mm, never acrylic or glass, placed with its nearest edge more than 15° from the propeller plane | Polycarbonate yields rather than shatters; keeping it out of the fragment zone protects the one non-steel wall. Relax only with impact tests of the window at TRL 4 | Window; R7, R11 |
| D7 | Thrust stand: two spring-steel flexure leaves (no rails), a 10 kg bending-beam cell for thrust, a torque head on two bearings with an arm on a 5 kg cell, an optical speed sensor | No sliding friction; bought C3 cells; the share carried by the leaves is fixed and calibrated out | R3, R4; stand parts |
| D8 | Room temperature only in the first version; chilling towards -20 °C is a later variant | Density, not temperature, sets thrust; chilling a 0.9 m3 vessel adds a refrigeration plant and condensation | Scope; R1 |
| D9 | Closed chamber with a removable 63 % open perforated baffle, and side-by-side comparison runs at ambient pressure published with every data set | The scaffold's open question on recirculation; the baffle breaks up the jet and swirl, and the comparison runs measure what the loop does. Whether R6 is met is posed to Amish separately | R6; baffle; ALR-CAL-001 F |
| D10 | No lithium or sodium-ion battery inside the chamber in the first version; the motor is powered from a 1,500 W supply outside through the feed-through | Conservative: a battery fire in a closed vessel raises the pressure and fills it with toxic fumes. Relax only with a vent, a fire-containment plan and abuse tests of the pack type | Scope; ColdCell; feed-through |
| D11 | Co-design: the first candidate partner to approach is the Department of Aerospace Engineering, IIT Kanpur; the second is the Department of Mechanical Engineering, Kathmandu University. First candidate region: the Nepal and Indian Himalaya. Recorded as candidates, not agreed | Propeller facilities and Himalayan users; a partner reviews the vessel calculation and runs the open-air comparison | ALR-PRB-001 co-design |
| D12 | The high-altitude propeller, motor and tuning kit is not part of this repo; AltiRig publishes measured data and the Kitewright Lift and Range frames publish their kits from it | Keeps AltiRig a test rig and the kits with the aircraft they serve | Scope; shared blocks |
| D13 | Shared blocks: CalRig's proof-load method calibrates the load cells; ColdCell packs are not tested inside the chamber in this version (D10) | Re-use across the portfolio without adding a battery hazard | ALR-PRC-001 shared blocks |
| D14 | Publish as an open engineering reference with a notice that it is not certified pressure or test equipment; before any use a qualified engineer reviews the vessel calculation and the first pump-down is a proof test behind a guard | Conservative; follows the safety notes in the scaffold | README and every document; build plan safety stops |

## Consequences

- R11 and R12 are added to ALR-REQ-001.
- The vessel, welding, motor supply and safety controls take the estimated cost well above the USD 1,000 value-engineering target (ALR-DEC-001, Value engineering). Amish accepted cost overruns in the same instruction; R10 is posed to Amish with options in `docs/REVIEW.md`.
