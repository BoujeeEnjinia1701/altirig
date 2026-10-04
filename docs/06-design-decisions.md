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
  change: O1 (R6) and O2 (R10) decided by Amish on 2026-10-03 as recommended (ALR-DDR-003) and moved to decisions made; value engineering updated
---

# AltiRig design decisions register

Every design decision still to be made, and every decision made, in one place. Each decision is argued in full in its decision record under `docs/decisions/`; this register is the index Amish works from. The build plan (`docs/05-build-plan.md`) describes the design as it stands.

> **Safety:** AltiRig is a vacuum vessel with a spinning propeller inside, run from mains power. Every decision that touches safety took the conservative option, and the evidence that would relax it is named in its record. Nothing here makes the chamber certified pressure or test equipment.

## Open decisions

O1 (R6, chamber effect) and O2 (R10, cost) were decided by Amish on 2026-10-03 and are listed under decisions made (ALR-DDR-003). Applying them raised one new question, set out in `docs/REVIEW.md` (round 2 session).

| # | Decision needed | Options | Recommendation | Affects in the build | Source |
| --- | --- | --- | --- | --- | --- |
| O3 | Baffle stiffness: the 80 % open disc, held at four tabs, is much less stiff than the 63 % plate and may deflect or flutter under the jet (about 30 N estimated at 50 N) | A: fit as specified and check its deflection in the TRL 4 runs. B: add a 20 x 3 mm rim ring (about USD 15 and 1.2 kg, estimates; open area about 72 %, R6 estimate 2.2 % to 4.0 %). C: expanded mesh with heavy strands only | A. Proposed, awaiting Amish | Baffle plate (3.15) | ALR-DDR-003; REVIEW.md |

## To confirm when parts are bought

| # | What to confirm | Why it matters | Source |
| --- | --- | --- | --- |
| 1 | The surplus pipe offcut's out-of-roundness (no more than 8 mm between largest and smallest diameter) and wall thickness (6.35 mm, no less than 5.9 mm at any point); if it fails, a new-cut length is bought (estimate USD 4,390 in all) | The shell's collapse factor of 6.7 assumes both; it is the condition on the R10 decision | ALR-CAL-001 B; ALR-DDR-003 |
| 2 | The surplus tank heads' skirt length (40 mm), thickness (no less than 5.9 mm) and outside diameter match the pipe, with no dents or pitting | The door ring fits over the skirt; the rear head butts to the pipe | ALR-DDR-002, C2; ALR-DDR-003 |
| 9 | The host lab's DC supply gives 1,500 W at 20 to 28 V with a remote on/off input the contactor can switch, and the workshop pump gives at least 170 L/min with a thermal overload and an exhaust filter; otherwise they are bought (estimate USD 540 more) | R10 decision condition; R8 pump-down and R11 interlocks | ALR-DDR-003 |
| 10 | The baffle's open area on the supplier's data sheet is 78 % to 82 % | R6 estimate of 1.8 % to 3.3 % assumes 80 % | ALR-DDR-003; ALR-CAL-001 F |
| 3 | Flatness of both flange ring faces after welding (within 1 mm) | The 6 mm sponge must seal the door at the first pump-down | ALR-BLD-001, 3.2 |
| 4 | The relief valve's adjustable range covers 55 kPa below atmosphere and it is rated for vacuum service | R12 | ALR-DDR-001, D4 |
| 5 | The load cells' stiffness (deflection at full scale) and combined error class | Sets the share of thrust carried by the leaves (2.9 % assumed) and the error budgets | ALR-CAL-001 E |
| 6 | The pump's speed curve between 50 and 100 kPa inlet | Pump-down time (R8) assumes 85 % of the 170 L/min rating | ALR-CAL-001 C |
| 7 | The example propeller's static coefficients (0.10 and 0.042 assumed) | Speeds, power and torque at 50 N; the supply limit of about 44 N at 5,000 m density | ALR-CAL-001 E |
| 8 | Latch clamps hold at least 3 kN | The first seal needs about 2.1 kN each | ALR-CAL-001 B |

## Value engineering

Value-engineering target: USD 1,000 (a hypothetical control target, not a limit). Estimated cost of the constructable design: USD 3,920 (USD 2,920 over the target), after the R10 decision (ALR-DDR-003); it was USD 4,920. Main cost drivers and savings still worth trying:

- The vessel steel, heads and nozzles (about USD 1,160 with the saddles, rings and window rings, with surplus pipe and heads) and the welding labour (USD 650). A used air receiver of the same size with its own heads is the next saving worth pricing.
- The speed controller and power sensor (USD 100) and the safety controls and cabinet (USD 360). The motor supply is now the host lab's own.
- The valve manifold (USD 220) and the pump hose (USD 40). The pump is now the host workshop's own.
- The thrust stand itself is cheap (about USD 300 including the load cells); it is not where the money goes.

## Decisions made

| Date | Decision | Decided by | Record |
| --- | --- | --- | --- |
| 2026-10-03 | TRL 2 review items D1 to D14: match density not pressure, pipe and tank-head vessel, design for full vacuum, R12 relief valve, R11 interlocks, polycarbonate window outside the fragment zone, flexure stand, room temperature only, removable baffle with comparison runs, no batteries inside, external motor supply, propeller kit left to Lift and Range, shared blocks, not-certified notice with engineer review and proof pump-down | Amish: "start with the first 14 repos from the list of 29 projects. I pre-approve the batch runs along with any recommendations you come up with. I also accept any cost overruns or variations from the assumed scope cost." and "Proceed with the remaining 15 scaffolds" | [ALR-DDR-001](decisions/0001-trl2-review-decisions.md) |
| 2026-10-03 | Co-design: the first candidate partner to approach is the Department of Aerospace Engineering, IIT Kanpur, then Kathmandu University; first candidate region the Nepal and Indian Himalaya; candidates, not agreed | Amish, same pre-approvals | [ALR-DDR-001](decisions/0001-trl2-review-decisions.md), D11 |
| 2026-10-03 | Design for construction C1 to C17: pipe shell, flat flange rings with a sponge gasket, set-in heavy-wall nozzles, window stack with a spacer ring, potted feed-through plate, saddles, rails and bolted deck, bolted baffle on tabs, hinge and latches, flexure stand with an upright cell, torque head on bearings, speed post, manifold on a stub flange, normally-open bleed valve, feed-through placement, pump and cabinet placement | Amish, same pre-approvals | [ALR-DDR-002](decisions/0002-design-for-construction.md) |
| 2026-10-03 | Cost overrun against the value-engineering target accepted; `budget_usd` left at USD 1,000 | Amish, same pre-approval ("I also accept any cost overruns") | This register, Value engineering |
| 2026-10-03 | R6, chamber effect: option B, an 80 % open perforated or expanded-metal baffle on the same tabs (estimate 1.8 % to 3.3 %, R6 met on paper), with the 1,016 mm vessel (option C) held in reserve if the TRL 4 comparison still shows more than 5 % | Amish: "i approve all of the 47 recommendations provided by you. Execute them." | [ALR-DDR-003](decisions/0003-requirement-decisions-round2.md) |
| 2026-10-03 | R10, cost: option B, surplus pipe offcut and tank heads, the host lab's DC supply and a suitable workshop vacuum pump (estimate USD 3,920, R10 still not met), provided the surplus pipe passes the roundness and thickness checks | Amish, same instruction | [ALR-DDR-003](decisions/0003-requirement-decisions-round2.md) |

## Change log

| Date | Change |
| --- | --- |
| 2026-10-03 | v0.1: register opened at TRL 3 with O1 (R6) and O2 (R10) open |
| 2026-10-03 | v0.2: O1 and O2 decided by Amish as recommended (ALR-DDR-003) and moved to decisions made; items 9 and 10 added to confirm when parts are bought; value engineering updated to USD 3,920; O3 (baffle stiffness) opened |
