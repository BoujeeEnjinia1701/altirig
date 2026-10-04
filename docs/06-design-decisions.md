---
doc_id: ALR-DEC-001
title: AltiRig design decisions register
project: AltiRig
doc_type: Design decisions register
version: "0.2"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-03'
  author: Amish Chadha
  change: Register opened at TRL 3; design decisions made under Amish's 2026-10-03 pre-approvals; R6 and R10 posed to Amish
- version: "0.2"
  date: '2026-10-03'
  author: Amish Chadha
  change: "Amish's decisions 41B (80 % open baffle) and 42B (surplus pipe and heads, host lab's DC supply and pump; R10 restated) moved to Decisions made (ALR-DDR-003)"
---

# AltiRig design decisions register

Every design decision still to be made, and every decision made, in one place. Each decision is argued in full in its decision record under `docs/decisions/`; this register is the index Amish works from. The build plan (`docs/05-build-plan.md`) describes the design as it stands.

> **Safety:** AltiRig is a vacuum vessel with a spinning propeller inside, run from mains power. Every decision that touches safety took the conservative option, and the evidence that would relax it is named in its record. Nothing here makes the chamber certified pressure or test equipment.

## Open decisions

None. The two requirement decisions put to Amish at TRL 3 (R6 and R10) were decided on 2026-10-03 as recommended (41B and 42B, below and in [ALR-DDR-003](decisions/0003-requirement-decisions.md)); carrying them out raised no new question for Amish. What the host lab's pump and supply must meet is listed under To confirm.

## To confirm when parts are bought

| # | What to confirm | Why it matters | Source |
| --- | --- | --- | --- |
| 1 | The surplus pipe offcut's out-of-roundness (no more than 8 mm between largest and smallest diameter) and wall thickness (6.35 mm, no less than 5.9 mm at any point), checked before buying | The shell's collapse factor of 6.7 assumes both; decision 42B makes the pipe surplus | ALR-CAL-001 B; ALR-DDR-003 |
| 2 | The surplus or overstock tank heads' skirt length (40 mm), thickness (no less than 5.9 mm) and outside diameter match the pipe, checked before buying | The door ring fits over the skirt; the rear head butts to the pipe | ALR-DDR-002, C2; ALR-DDR-003 |
| 3 | Flatness of both flange ring faces after welding (within 1 mm) | The 6 mm sponge must seal the door at the first pump-down | ALR-BLD-001, 3.2 |
| 4 | The relief valve's adjustable range covers 55 kPa below atmosphere and it is rated for vacuum service | R12 | ALR-DDR-001, D4 |
| 5 | The load cells' stiffness (deflection at full scale) and combined error class | Sets the share of thrust carried by the leaves (2.9 % assumed) and the error budgets | ALR-CAL-001 E |
| 6 | The host lab's pump: rated at least 140 L/min (170 L/min as calculated), with a thermal overload and an oil-mist exhaust filter; its speed curve between 50 and 100 kPa inlet | Pump-down time (R8) assumes 85 % of the rating; 140 L/min gives about 4.9 min against 5 min | ALR-CAL-001 C and H; ALR-DDR-003 |
| 7 | The example propeller's static coefficients (0.10 and 0.042 assumed) | Speeds, power and torque at 50 N; the supply limit of about 44 N at 5,000 m density | ALR-CAL-001 E |
| 8 | Latch clamps hold at least 3 kN | The first seal needs about 2.1 kN each | ALR-CAL-001 B |
| 9 | The host lab's DC supply gives at least 1,500 W at 24 V (adjustable 20 to 28 V), has overcurrent protection, and can be switched by the cabinet's motor contactor | A smaller supply lowers the thrust reached at 5,000 m density below about 44 N; R11 needs the contactor to cut it | ALR-CAL-001 E and H; ALR-DDR-003 |

## Value engineering

Value-engineering target: USD 1,000 (a hypothetical control target, not a limit). Estimated cost of the constructable design: USD 3,865 (USD 2,865 over the target). R10 is restated to USD 4,000 by Amish's decision 42B, and USD 3,865 is USD 135 under it. Main cost drivers and savings still worth trying:

- The vessel steel, heads and nozzles (about USD 1,270 with the surplus pipe and heads, saddles, rings, rails, tabs and window rings) and the welding labour (USD 650). A used air receiver of the same size with its own heads is the next saving worth pricing.
- The speed controller and power sensor (USD 100) and the safety controls and cabinet (USD 360). The host lab's DC supply is used (decision 42B), keeping the interlocked contactor.
- The valve manifold (USD 220) and hose (USD 45). The host lab's pump is used (decision 42B).
- The thrust stand itself is cheap (about USD 300 including the load cells); it is not where the money goes.

## Decisions made

| Date | Decision | Decided by | Record |
| --- | --- | --- | --- |
| 2026-10-03 | TRL 2 review items D1 to D14: match density not pressure, pipe and tank-head vessel, design for full vacuum, R12 relief valve, R11 interlocks, polycarbonate window outside the fragment zone, flexure stand, room temperature only, removable baffle with comparison runs, no batteries inside, external motor supply, propeller kit left to Lift and Range, shared blocks, not-certified notice with engineer review and proof pump-down | Amish: "start with the first 14 repos from the list of 29 projects. I pre-approve the batch runs along with any recommendations you come up with. I also accept any cost overruns or variations from the assumed scope cost." and "Proceed with the remaining 15 scaffolds" | [ALR-DDR-001](decisions/0001-trl2-review-decisions.md) |
| 2026-10-03 | Co-design: the first candidate partner to approach is the Department of Aerospace Engineering, IIT Kanpur, then Kathmandu University; first candidate region the Nepal and Indian Himalaya; candidates, not agreed | Amish, same pre-approvals | [ALR-DDR-001](decisions/0001-trl2-review-decisions.md), D11 |
| 2026-10-03 | Design for construction C1 to C17: pipe shell, flat flange rings with a sponge gasket, set-in heavy-wall nozzles, window stack with a spacer ring, potted feed-through plate, saddles, rails and bolted deck, bolted baffle on tabs, hinge and latches, flexure stand with an upright cell, torque head on bearings, speed post, manifold on a stub flange, normally-open bleed valve, feed-through placement, pump and cabinet placement | Amish, same pre-approvals | [ALR-DDR-002](decisions/0002-design-for-construction.md) |
| 2026-10-03 | Cost overrun against the value-engineering target accepted; `budget_usd` left at USD 1,000 | Amish, same pre-approval ("I also accept any cost overruns") | This register, Value engineering |
| 2026-10-03 | 41B, R6: an 80 % open baffle (2 mm sheet, 22 mm square holes on a 24.5 mm pitch) on the same tabs; chamber effect now 1.8 % to 3.3 % against 5 %; the 1,016 mm vessel held in reserve if the TRL 4 comparison shows more than 5 % | Amish, 2026-10-03: "i agree with all the 46 recommendations you provided. please proceed." | [ALR-DDR-003](decisions/0003-requirement-decisions.md) |
| 2026-10-03 | 42B, R10: surplus pipe offcut and tank heads (after the roundness and thickness checks) and the host lab's DC supply and vacuum pump; cost USD 3,865; R10 restated to "complete rig at or below USD 4,000 with surplus pipe and heads and the host lab's DC supply and pump" | Amish, 2026-10-03: "i agree with all the 46 recommendations you provided. please proceed." | [ALR-DDR-003](decisions/0003-requirement-decisions.md) |
