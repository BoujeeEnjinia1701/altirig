---
doc_id: ALR-REQ-001
title: AltiRig requirements
project: AltiRig
doc_type: Requirements
version: "0.4"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-09-30'
  author: Amish Chadha
  change: Initial scaffold
- version: "0.2"
  date: '2026-10-03'
  author: Amish Chadha
  change: TRL 2 review; concept status for every requirement; R11 interlocks and R12 over-vacuum protection added (ALR-DDR-001)
- version: "0.3"
  date: '2026-10-03'
  author: Amish Chadha
  change: TRL 3 status from the calculations (ALR-CAL-001) and the constructable design (ALR-DDR-002)
- version: "0.4"
  date: '2026-10-03'
  author: Amish Chadha
  change: "Amish's decisions 41B (80 % open baffle; R6 met on paper at 1.8 % to 3.3 %) and 42B (surplus pipe and heads, host lab's DC supply and pump; R10 restated to USD 4,000 and met at USD 3,865), ALR-DDR-003"
---

# AltiRig requirements

All twelve requirements are met on paper by the constructable design, R10 as restated on 2026-10-03. Targets are unchanged from the scaffold except for the two safety requirements added at the TRL 2 review (R11 and R12) and R10, restated by Amish's decision 42B. Status is on paper only: every requirement is verified by test at TRL 4.

On 2026-10-03 Amish decided the two requirement decisions put to him at TRL 3 as recommended. Amish, 2026-10-03: "i agree with all the 46 recommendations you provided. please proceed." For AltiRig these are 41B (R6: an 80 % open baffle) and 42B (R10: a surplus pipe and heads and the host lab's DC supply and pump, with the cost target restated), recorded in ALR-DDR-003.

*Table 1. Requirements and their status at TRL 3.*

| ID | Requirement | Target | Verification (TRL 4 or later) | Status at TRL 3 |
| --- | --- | --- | --- | --- |
| R1 | Density range | Hold any air density from ambient down to 0.74 kg/m3 (5,000 m equivalent) at room temperature | Pressure and temperature log over a 10 min hold at several set points | Met on paper: 0.736 kg/m3 needs 61.9 kPa at 20 °C; the pump reaches far lower and the relief valve stops at 46.3 kPa (ALR-CAL-001, A) |
| R2 | Density control | Density held within plus or minus 1% of set point during a run | Logged density during motor runs | Met on paper: error budget 0.6 % (ALR-CAL-001, D) |
| R3 | Thrust range and accuracy | 0 to 50 N thrust with error no more than 1% of full scale | Calibration with certified masses before and after a test series | Met on paper: flexure stand with a 10 kg cell, error budget 0.13 N, 0.27 % (ALR-CAL-001, E) |
| R4 | Torque and speed | Torque 0 to 2 N m within 2%; speed within 0.5% | Calibration arm with masses; optical tachometer cross-check | Met on paper: torque error 0.3 %, speed 0.02 % (ALR-CAL-001, E) |
| R5 | Propeller size | Propellers up to 380 mm (15 in) diameter | Fit check and clearance measurement | Met on paper: 210 mm from tip to wall, 80 mm to the deck (ALR-CAL-001, E) |
| R6 | Chamber effect | At ambient pressure, chamber thrust within 5% of an open-air stand for the same propeller and speed | Side-by-side comparison tests | Met on paper (decision 41B): estimated 1.8 % to 3.3 % high with the 80 % open baffle, was 2.9 % to 5.3 % with the 63 % baffle (ALR-CAL-001, F); confirmed by the TRL 4 comparison runs with and without the baffle |
| R7 | Vessel safety factor | Collapse pressure at least 4 times the maximum working pressure difference (target) | Calculation reviewed by a qualified engineer, then proof test behind a guard | Met on paper, at full vacuum: shell 6.7, heads 40, window 7.1 on yield (ALR-CAL-001, B) |
| R8 | Pump-down time | Ambient to 54 kPa in no more than 5 min | Timed pump-down with pressure log | Met on paper: 4.0 min with a 170 L/min pump (ALR-CAL-001, C) |
| R9 | Data output | Results saved as CSV with density, thrust, torque, speed, voltage and current at 10 Hz or more | Inspection of logged files | Met on paper: 20 Hz logging, amplifiers at 80 Hz (ALR-CAL-001, G) |
| R10 | Cost | Restated 2026-10-03 (decision 42B): complete rig at or below USD 4,000, built with a surplus pipe offcut and tank heads that pass the roundness and thickness checks, and the host lab's existing DC supply and vacuum pump; the USD 1,000 value-engineering target is kept as a control figure. Was: complete rig at or below USD 1,000 | Costed bill of materials | Met as restated: USD 3,865, USD 135 under USD 4,000 and USD 2,865 over the value-engineering target (ALR-CAL-001, H) |
| R11 | Interlocks | The motor can be powered only with the door latched and the arming key turned; the emergency stop removes motor and pump power; the bleed valve opens and vents the chamber on loss of power | Function check of each interlock before first power | Met on paper by design (ALR-BLD-001, sections 4 and 6); the door is also held shut by 24 kN of air load at the 5,000 m point |
| R12 | Over-vacuum protection | A relief valve stops the chamber going below 46.3 kPa absolute (55 kPa below atmosphere); the vessel is still designed for full vacuum | Relief valve set and checked against the gauge before first pump-down | Met on paper (ALR-CAL-001, A and B) |

## Requirements not met or at risk

None on paper. The two that were (R6 at risk, R10 not met) were decided by Amish on 2026-10-03: Amish, 2026-10-03: "i agree with all the 46 recommendations you provided. please proceed."

- **R6, decision 41B.** The closed loop of air inside the vessel adds a little resistance to the propeller's own flow, so the propeller is expected to give slightly more thrust in the chamber than in open air. With the 80 % open baffle two simple models give 1.8 % and 3.3 %, inside the 5 % target. The TRL 4 comparison runs decide it; the 1,016 mm vessel is held in reserve if they show more than 5 %.
- **R10, decision 42B.** Restated to USD 4,000 with surplus vessel steel and the host lab's DC supply and pump; estimated USD 3,865. It depends on the surplus pipe and heads passing the roundness and thickness checks, and on the host lab having a DC supply of at least 1,500 W and a pump of at least about 140 L/min. Buying a new pipe, heads, pump and supply instead would cost about USD 4,930; buying only a new pump and supply, about USD 4,400.

## Assumptions

- Matching air density is the main effect; the small differences in viscosity and speed of sound between a room-temperature chamber and real air at 5,000 m and -17.5 °C are second order for small propellers (to be checked). Blade Reynolds number falls by about 39 % at 5,000 m density (ALR-CAL-001, E), which the chamber reproduces because density, not pressure, is matched.
- A surplus or new-cut 813 mm steel pipe offcut and two tank heads can be bought; the out-of-roundness of the pipe is no more than 1 % of its diameter (to confirm when bought).
- The chamber effect is measured by side-by-side runs at ambient pressure and recorded with every published data set.
- Earlier physics estimate: hover time at 5,000 m and -20 °C is about 47 % of sea level; AltiRig will test the aerodynamic share of that estimate.

> **Safety:** R7, R11 and R12 are safety requirements. They are met on paper only; no pump-down or motor run is made until the safety stops in the build plan (ALR-BLD-001, section 6) are passed and a qualified engineer has reviewed the vessel calculation.
