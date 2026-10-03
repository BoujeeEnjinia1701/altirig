---
doc_id: ALR-REQ-001
title: AltiRig requirements
project: AltiRig
doc_type: Requirements
version: "0.3"
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
---

# AltiRig requirements

Ten of the twelve requirements are met on paper by the constructable design; R6 (chamber effect) is at risk and R10 (cost) is not met. Targets are unchanged from the scaffold except for the two safety requirements added at the TRL 2 review (R11 and R12). Status is on paper only: every requirement is verified by test at TRL 4.

*Table 1. Requirements and their status at TRL 3.*

| ID | Requirement | Target | Verification (TRL 4 or later) | Status at TRL 3 |
| --- | --- | --- | --- | --- |
| R1 | Density range | Hold any air density from ambient down to 0.74 kg/m3 (5,000 m equivalent) at room temperature | Pressure and temperature log over a 10 min hold at several set points | Met on paper: 0.736 kg/m3 needs 61.9 kPa at 20 °C; the pump reaches far lower and the relief valve stops at 46.3 kPa (ALR-CAL-001, A) |
| R2 | Density control | Density held within plus or minus 1% of set point during a run | Logged density during motor runs | Met on paper: error budget 0.6 % (ALR-CAL-001, D) |
| R3 | Thrust range and accuracy | 0 to 50 N thrust with error no more than 1% of full scale | Calibration with certified masses before and after a test series | Met on paper: flexure stand with a 10 kg cell, error budget 0.13 N, 0.27 % (ALR-CAL-001, E) |
| R4 | Torque and speed | Torque 0 to 2 N m within 2%; speed within 0.5% | Calibration arm with masses; optical tachometer cross-check | Met on paper: torque error 0.3 %, speed 0.02 % (ALR-CAL-001, E) |
| R5 | Propeller size | Propellers up to 380 mm (15 in) diameter | Fit check and clearance measurement | Met on paper: 210 mm from tip to wall, 80 mm to the deck (ALR-CAL-001, E) |
| R6 | Chamber effect | At ambient pressure, chamber thrust within 5% of an open-air stand for the same propeller and speed | Side-by-side comparison tests | At risk: estimated 2.9 % to 5.3 % high with the 63 % open baffle (ALR-CAL-001, F); see the review note |
| R7 | Vessel safety factor | Collapse pressure at least 4 times the maximum working pressure difference (target) | Calculation reviewed by a qualified engineer, then proof test behind a guard | Met on paper, at full vacuum: shell 6.7, heads 40, window 7.1 on yield (ALR-CAL-001, B) |
| R8 | Pump-down time | Ambient to 54 kPa in no more than 5 min | Timed pump-down with pressure log | Met on paper: 4.0 min with a 170 L/min pump (ALR-CAL-001, C) |
| R9 | Data output | Results saved as CSV with density, thrust, torque, speed, voltage and current at 10 Hz or more | Inspection of logged files | Met on paper: 20 Hz logging, amplifiers at 80 Hz (ALR-CAL-001, G) |
| R10 | Cost | Complete rig at or below USD 1,000 | Costed bill of materials | Not met: estimated USD 4,920, over the value-engineering target by USD 3,920 (ALR-CAL-001, H) |
| R11 | Interlocks | The motor can be powered only with the door latched and the arming key turned; the emergency stop removes motor and pump power; the bleed valve opens and vents the chamber on loss of power | Function check of each interlock before first power | Met on paper by design (ALR-BLD-001, sections 4 and 6); the door is also held shut by 24 kN of air load at the 5,000 m point |
| R12 | Over-vacuum protection | A relief valve stops the chamber going below 46.3 kPa absolute (55 kPa below atmosphere); the vessel is still designed for full vacuum | Relief valve set and checked against the gauge before first pump-down | Met on paper (ALR-CAL-001, A and B) |

## Requirements not met or at risk

- **R6, at risk.** The closed loop of air inside the vessel adds a little resistance to the propeller's own flow, so the propeller is expected to give slightly more thrust in the chamber than in open air. Two simple models give 2.9 % and 5.3 % with the 63 % open baffle. Options and a recommendation are in `docs/REVIEW.md` for Amish to decide.
- **R10, not met.** The vessel parts, the welding, the motor supply and the safety controls take the estimate to USD 4,920. The budget is a value-engineering target, not a limit; options to bring the cost down are in `docs/REVIEW.md` and in the design decisions register.

## Assumptions

- Matching air density is the main effect; the small differences in viscosity and speed of sound between a room-temperature chamber and real air at 5,000 m and -17.5 °C are second order for small propellers (to be checked). Blade Reynolds number falls by about 39 % at 5,000 m density (ALR-CAL-001, E), which the chamber reproduces because density, not pressure, is matched.
- A surplus or new-cut 813 mm steel pipe offcut and two tank heads can be bought; the out-of-roundness of the pipe is no more than 1 % of its diameter (to confirm when bought).
- The chamber effect is measured by side-by-side runs at ambient pressure and recorded with every published data set.
- Earlier physics estimate: hover time at 5,000 m and -20 °C is about 47 % of sea level; AltiRig will test the aerodynamic share of that estimate.

> **Safety:** R7, R11 and R12 are safety requirements. They are met on paper only; no pump-down or motor run is made until the safety stops in the build plan (ALR-BLD-001, section 6) are passed and a qualified engineer has reviewed the vessel calculation.
