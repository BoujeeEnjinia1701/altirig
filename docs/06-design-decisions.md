---
doc_id: ALR-DEC-001
title: AltiRig design decisions register
project: AltiRig
doc_type: Design decisions register
version: "0.1"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-03'
  author: Amish Chadha
  change: Register opened at TRL 3; design decisions made under Amish's 2026-10-03 pre-approvals; R6 and R10 posed to Amish
---

# AltiRig design decisions register

Every design decision still to be made, and every decision made, in one place. Each decision is argued in full in its decision record under `docs/decisions/`; this register is the index Amish works from. The build plan (`docs/05-build-plan.md`) describes the design as it stands.

> **Safety:** AltiRig is a vacuum vessel with a spinning propeller inside, run from mains power. Every decision that touches safety took the conservative option, and the evidence that would relax it is named in its record. Nothing here makes the chamber certified pressure or test equipment.

## Open decisions

Two requirements are not met or at risk on paper. They are not decided here; each is set out with its options and a recommendation in `docs/REVIEW.md` (TRL 3 section, Decisions for Amish).

| # | Decision needed | Options | Recommendation | Affects in the build | Source |
| --- | --- | --- | --- | --- | --- |
| O1 | R6, chamber effect: estimated 2.9 % to 5.3 % more thrust in the chamber than in open air with the 63 % open baffle | A: keep the 63 % baffle as designed. B: fit an 80 % open baffle instead (estimate 1.8 % to 3.3 %, about USD 10 more, 3 kg lighter). C: a 1,016 mm (40 in) vessel (estimate 1.1 % to 2.0 %, about USD 900 more, about 150 kg heavier) | B. Proposed, awaiting Amish | Baffle plate (3.15); vessel parts for C | ALR-CAL-001 F; REVIEW.md |
| O2 | R10, cost: estimated USD 4,920 against the USD 1,000 value-engineering target | A: keep the design and parts as specified. B: source the pipe and heads as surplus and use a lab's existing bench supply and pump (estimate USD 3,700 to 4,000). C: a 610 mm (24 in) vessel for propellers up to about 280 mm (estimate USD 4,200, about 150 kg lighter; R5 would then not be met) | B. Proposed, awaiting Amish | Shell, heads, motor supply, pump (sourcing only for B) | ALR-CAL-001 H; REVIEW.md |

## To confirm when parts are bought

| # | What to confirm | Why it matters | Source |
| --- | --- | --- | --- |
| 1 | The pipe offcut's out-of-roundness (no more than 8 mm between largest and smallest diameter) and wall thickness (6.35 mm, no less than 5.9 mm at any point) | The shell's collapse factor of 6.7 assumes both | ALR-CAL-001 B |
| 2 | The tank heads' skirt length (40 mm), thickness and outside diameter match the pipe | The door ring fits over the skirt; the rear head butts to the pipe | ALR-DDR-002, C2 |
| 3 | Flatness of both flange ring faces after welding (within 1 mm) | The 6 mm sponge must seal the door at the first pump-down | ALR-BLD-001, 3.2 |
| 4 | The relief valve's adjustable range covers 55 kPa below atmosphere and it is rated for vacuum service | R12 | ALR-DDR-001, D4 |
| 5 | The load cells' stiffness (deflection at full scale) and combined error class | Sets the share of thrust carried by the leaves (2.9 % assumed) and the error budgets | ALR-CAL-001 E |
| 6 | The pump's speed curve between 50 and 100 kPa inlet | Pump-down time (R8) assumes 85 % of the 170 L/min rating | ALR-CAL-001 C |
| 7 | The example propeller's static coefficients (0.10 and 0.042 assumed) | Speeds, power and torque at 50 N; the supply limit of about 44 N at 5,000 m density | ALR-CAL-001 E |
| 8 | Latch clamps hold at least 3 kN | The first seal needs about 2.1 kN each | ALR-CAL-001 B |

## Value engineering

Value-engineering target: USD 1,000 (a hypothetical control target, not a limit). Estimated cost of the constructable design: USD 4,920 (USD 3,920 over the target). Main cost drivers and savings worth trying:

- The vessel steel, heads and nozzles (about USD 1,630 with the saddles, rings and window rings) and the welding labour (USD 650). Surplus pipe offcuts and second-hand tank heads, or a used air receiver of the same size with its own heads, are the savings worth pricing first.
- The motor supply, speed controller and power sensor (USD 420) and the safety controls and cabinet (USD 360). A lab that already has a programmable DC supply can use it, keeping the interlocked contactor.
- The valve manifold and pump (USD 480). A refrigeration vacuum pump already in a workshop will do if it has a thermal overload and an exhaust filter.
- The thrust stand itself is cheap (about USD 300 including the load cells); it is not where the money goes.

## Decisions made

| Date | Decision | Decided by | Record |
| --- | --- | --- | --- |
| 2026-10-03 | TRL 2 review items D1 to D14: match density not pressure, pipe and tank-head vessel, design for full vacuum, R12 relief valve, R11 interlocks, polycarbonate window outside the fragment zone, flexure stand, room temperature only, removable baffle with comparison runs, no batteries inside, external motor supply, propeller kit left to Lift and Range, shared blocks, not-certified notice with engineer review and proof pump-down | Amish: "start with the first 14 repos from the list of 29 projects. I pre-approve the batch runs along with any recommendations you come up with. I also accept any cost overruns or variations from the assumed scope cost." and "Proceed with the remaining 15 scaffolds" | [ALR-DDR-001](decisions/0001-trl2-review-decisions.md) |
| 2026-10-03 | Co-design: the first candidate partner to approach is the Department of Aerospace Engineering, IIT Kanpur, then Kathmandu University; first candidate region the Nepal and Indian Himalaya; candidates, not agreed | Amish, same pre-approvals | [ALR-DDR-001](decisions/0001-trl2-review-decisions.md), D11 |
| 2026-10-03 | Design for construction C1 to C17: pipe shell, flat flange rings with a sponge gasket, set-in heavy-wall nozzles, window stack with a spacer ring, potted feed-through plate, saddles, rails and bolted deck, bolted baffle on tabs, hinge and latches, flexure stand with an upright cell, torque head on bearings, speed post, manifold on a stub flange, normally-open bleed valve, feed-through placement, pump and cabinet placement | Amish, same pre-approvals | [ALR-DDR-002](decisions/0002-design-for-construction.md) |
| 2026-10-03 | Cost overrun against the value-engineering target accepted; `budget_usd` left at USD 1,000 | Amish, same pre-approval ("I also accept any cost overruns") | This register, Value engineering |
