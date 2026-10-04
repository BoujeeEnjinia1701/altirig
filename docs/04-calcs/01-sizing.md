---
doc_id: ALR-CAL-001
title: AltiRig sizing calculations
project: AltiRig
doc_type: Calculation
version: "0.3"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-03'
  author: Amish Chadha
  change: First sizing of the TRL 3 concept against every requirement
- version: "0.2"
  date: '2026-10-03'
  author: Amish Chadha
  change: Re-run for the constructable design (ALR-DDR-002), with heavy-wall set-in nozzles, flexure stand, 63 % open baffle and bill of materials cost
- version: "0.3"
  date: '2026-10-03'
  author: Amish Chadha
  change: "Amish's decisions 41B and 42B (ALR-DDR-003): 80 % open baffle (R6 now 1.8 % to 3.3 %, met on paper); surplus pipe and heads with the host lab's DC supply and pump (USD 3,865); R10 restated"
---

# AltiRig sizing calculations

On paper the constructable design meets all twelve requirements, R10 as restated by Amish on 2026-10-03. The vessel is designed for full vacuum with a collapse factor of 6.7 on the shell, the stand measures 0 to 50 N within 0.27 % of full scale, and a 170 L/min pump reaches 54 kPa in about 4 minutes. With the 80 % open baffle (decision 41B) the closed loop of air is estimated to raise thrust by 1.8 % to 3.3 %, inside the 5 % of R6. With a surplus pipe and heads and the host lab's DC supply and vacuum pump (decision 42B) the estimated cost is USD 3,865, under the restated R10 limit of USD 4,000. Amish, 2026-10-03: "i agree with all the 46 recommendations you provided. please proceed."

> **Safety:** These are hand calculations for a concept on paper, made to choose sizes. They are not a pressure vessel design to any code and do not make the vessel safe to use. A qualified engineer reviews section B before any pump-down, and the first pump-down is a proof test behind a guard (ALR-BLD-001, section 6).

## Scope and method

`docs/04-calcs/sizing.py` makes every calculation and writes `docs/04-calcs/results.csv`. Dimensions come from the model (`cad/src/model.py`) and prices from `bom/bom.csv`, so a change to either is carried through by running the script again. Sections A to H follow the requirements; section I lists every result against every requirement.

## Assumptions

1. International Standard Atmosphere for altitude conditions; dry air, R = 287.05 J/(kg K).
2. Steel to S235 or A36 class: modulus 200 GPa, minimum yield 235 MPa. Polycarbonate: modulus 2.3 GPa, yield 62 MPa.
3. The vessel is designed for full vacuum (101.3 kPa difference), not only for the working point, because the pump can pull close to full vacuum if the relief valve sticks.
4. Shell buckling by the Windenburg and Trilling formula with a knock-down of 0.5 for out-of-roundness up to 1 % of the diameter and weld distortion. Heads treated as spheres of radius 0.9 D with a knock-down of 0.25 on the classical value.
5. Plastic windows: at least 6 on yield at full vacuum, simply supported at the gasket's outer edge.
6. Pump speed 85 % of the 170 L/min rating between 50 and 100 kPa, after the hose and the filter.
7. Example propeller 15 x 5 in, static thrust coefficient 0.10 and power coefficient 0.042 (typical of the UIUC static data for two-blade propellers of this pitch ratio); measured values replace them at TRL 4.
8. Heat transfer from the moving air to the steel wall 30 W/(m2 K); air temperature spread in the chamber plus or minus 1.5 K.
9. Chamber effect: actuator-disc momentum balance with the loop losses added (section F). Two blade models bracket the answer: the same shaft power, and the same speed with thrust falling linearly to zero at the pitch speed.

## A. Density targets (R1, R12)

The chamber matches density, not pressure. Room-temperature air reaches the density of 5,000 m at a higher pressure than the 54.0 kPa of 5,000 m, because the real air there is at -17.5 °C.

*Table 1. Density targets.*

| Quantity | Value |
| --- | --- |
| Standard atmosphere at 5,000 m | 54.0 kPa, -17.5 °C, 0.736 kg/m3 (60 % of sea level) |
| Standard atmosphere at 6,000 m | 0.660 kg/m3 |
| Chamber pressure for 0.736 kg/m3 at 15, 20, 25 and 30 °C | 60.9, 61.9, 63.0 and 64.1 kPa |
| Density at 54.0 kPa and 20 °C | 0.642 kg/m3, about the density of 6,100 m |
| Lowest working pressure needed (6,000 m density at 30 °C) | 57.4 kPa |
| Pressure difference at the R1 point (0.736 kg/m3, 20 °C) | 39.4 kPa |
| Relief valve: lowest chamber pressure | 46.3 kPa (55.0 kPa below atmosphere) |
| Design pressure difference for the vessel | 101.3 kPa (full vacuum) |

R1 is met: the pump reaches far below 61.9 kPa. R12 sets the relief valve below every working point, with a margin of 11 kPa under the lowest one.

## B. Vessel strength (R7, R11)

*Table 2. Vessel strength at full vacuum.*

| Part | Result | Factor |
| --- | --- | --- |
| Shell, 813 x 6.35 mm, unsupported length 1,718 mm | Elastic buckling 1,351 kPa; with the 0.5 knock-down 676 kPa; plastic limit 3,671 kPa | 6.7 on collapse (R7 target at least 4) |
| Shell, if the ends gave no support at all | Long-cylinder bound 209 kPa, halved | 1.0, so the flange ring and the head must stay welded all round |
| Heads, 2:1 ellipsoidal, 6.35 mm | Equivalent sphere 732 mm radius | 40 on collapse |
| Window opening (10 in XS set-in nozzle, 12.7 mm wall) | Area to replace 641 mm2 | 1.7 times the area needed, no pad |
| Feed-through opening (6 in XS set-in nozzle, 10.97 mm wall) | Area to replace 379 mm2 | 2.3 times the area needed, no pad |
| Window, polycarbonate 20 mm, span 165 mm radius | Bending stress 8.7 MPa; centre deflection 2.6 mm | 7.1 on yield (rule at least 6) |
| Feed-through plate, aluminium 15 mm | Bending stress 3.9 MPa | over 60 on yield |

The door is held shut by the air. Inside the gasket line the door area is 0.615 m2, so at the R1 point the door carries 24.2 kN (about 2.5 t) and at full vacuum 62.3 kN. Even 2 kPa of vacuum holds it with 1.2 kN, so nobody can open it until the chamber has been vented (R11). At full vacuum the sponge gasket carries 0.5 MPa and closes fully; the flange rings then bear on it. For the first seal the three latches pull the door 25 % into the sponge with about 6.3 kN, 2.1 kN each, against a rating of at least 3 kN. The 72 kg door hangs on the hinge with a horizontal force of 0.92 kN at each lug pair; stresses in the 20 mm pin and 15 mm lugs stay under 10 MPa.

## C. Volume and pump-down (R8, R11)

The free volume inside the vessel is 0.928 m3. With 144.5 L/min of effective pump speed, an isothermal pump-down takes 4.0 minutes to 54.0 kPa (R8, target 5 minutes) and 3.2 minutes to the R1 point. A leak of 0.2 L/min of free air is allowed for; at 54 kPa it raises the pressure by about 0.3 kPa a minute, which the controller makes up. Venting through the 6 mm bleed orifice from 54 kPa to ambient takes about 130 s, so the door cannot be opened in a rush after a run.

## D. Air heating and density control (R2)

All the electrical power put into the motor ends as heat inside the vessel. At 1,500 W the air settles about 9.5 K above the wall within a few seconds (time constant 4.4 s) and the 470 kg of steel warms by only 0.4 K a minute. To hold density, the controller raises the pressure by up to 3.2 % as the air warms, by opening the bleed valve.

*Table 3. Density error budget.*

| Source | Error |
| --- | --- |
| Pressure sensor, 50 Pa absolute | 0.08 % |
| Temperature probe, class A, 0.15 K | 0.05 % |
| Spread of air temperature in the chamber, 1.5 K | 0.51 % |
| Humidity correction | 0.07 % |
| Control band of the bleed loop | 0.30 % |
| Root sum square | 0.60 % (R2 target 1 %) |

## E. Propeller loads and the thrust stand (R3, R4, R5, R11)

*Table 4. Example propeller at 50 N (15 x 5 in, assumed coefficients).*

| Condition | Speed | Shaft power | Torque | Tip speed |
| --- | --- | --- | --- | --- |
| Sea level, 20 °C | 8,470 rpm | 1,126 W | 1.27 N m | 169 m/s |
| 5,000 m density | 10,830 rpm | 1,440 W | 1.27 N m | 216 m/s |

At 5,000 m density 50 N takes about 1,800 W of electrical power, more than the 1,500 W supply; with this propeller the supply allows about 44 N. The stand itself reads to 50 N; a larger supply is only needed for the heaviest propellers. The blade Reynolds number at three quarters of the radius falls from about 179,000 to 109,000 at 6,000 rpm, which is why sea-level data cannot simply be scaled.

The thrust stand is a parallelogram of two 0.5 mm spring-steel leaves, so it has no sliding friction. The leaves together are 11.7 N/mm stiff, carry 2.9 % of the thrust in parallel with the load cell (a fixed share, removed by calibration through the same path), move 0.12 mm at 50 N and are stressed to 5.8 MPa. Their buckling load is 17 times the 4.7 kg they carry. The 9.3 N m pitching moment from thrust acting above the cell is taken as tension and compression in the leaves.

*Table 5. Measurement error budgets.*

| Quantity | Budget | Result |
| --- | --- | --- |
| Thrust (R3) | Cell 0.05 % of 98 N, cable drag 0.1 N, zero drift, masses, flexure 0.1 % | 0.13 N, 0.27 % of 50 N (target 1 %) |
| Torque (R4) | Cell on a 60 mm arm (33 N at 2 N m on a 49 N cell), bearing friction 0.001 N m, cable drag 0.005 N m | 0.006 N m, 0.28 % of 2 N m (target 2 %) |
| Speed (R4) | Optical sensor, blade pass at up to 367 Hz, 1 microsecond timer | 0.02 % per revolution (target 0.5 %) |

Clearances (R5): the tip of a 380 mm propeller is 210 mm from the shell and 80 mm above the deck. The window's nearest edge is 18.3° from the propeller plane and the feed-through's 20.9°, both outside the 15° zone in which a broken blade's fragments travel (R11). A half blade of 25 g released at 50 N and 5,000 m density carries about 210 J, which the 6.35 mm steel shell contains.

## F. Chamber effect (R6)

The propeller drives a loop of air inside the vessel: down the middle, through the baffle, round the rear head and back along the wall. In open air the jet's kinetic energy is lost far downstream; in the chamber the same energy is lost where the jet mixes at the baffle, so to first order the propeller sees the same flow. What is added are the loop's own losses: the baffle, crossed twice, and the two 180° turns.

*Table 6. Chamber effect estimates at 50 N, ambient pressure.*

| Case | Extra loop loss (dynamic heads at the disc) | Thrust excess, same power | Thrust excess, same speed |
| --- | --- | --- | --- |
| As designed: 813 mm vessel, 80 % open baffle (decision 41B) | 0.22 | 1.8 % | 3.3 % |
| Baffle removed | 0.17 | 1.4 % | 2.5 % |
| Superseded: 63 % open baffle (TRL 3 design before decision 41B) | 0.36 | 2.9 % | 5.3 % |
| Reserve: 1,016 mm vessel with the 80 % baffle | about 0.08 | 0.7 % | 1.2 % |

The baffle is 2 mm steel sheet with 22 mm square holes on a 24.5 mm square pitch, so (22/24.5) squared gives 80.6 % open; its loss coefficient falls from 1.85 to 0.54 dynamic heads at the section velocity. The disc covers 23 % of the chamber section (inside diameter 2.1 times the propeller), and the return flow runs along the wall at about 3.9 m/s at 50 N. The same-speed model is the one that matters for R6, which compares thrust at the same speed. R6 is met on paper: 3.3 % against the 5 % target, a margin of 1.7 points. The inflow is less even than in open air, which these models do not capture, so the side-by-side runs at TRL 4, with and without the baffle, decide it. If they show more than 5 %, the 1,016 mm vessel is the reserve option (Amish's decision 41B keeps it in reserve).

## G. Data (R9)

The controller logs density, thrust, torque, speed, voltage and current to CSV at 20 Hz; the load-cell amplifiers sample at 80 Hz. R9 is met by design.

## H. Mass and cost (R10)

The vessel with its door, saddles and fittings is about 470 kg of steel; the whole rig with the pump and the control cabinet is about 585 kg (model masses). The 80 % baffle weighs about 1.5 kg, 1.3 kg less than the 63 % sheet (the model now counts only the solid share of the perforated sheet; before, it counted the baffle as a solid 7.7 kg disc). Decision 42B changes where parts come from, not what they are, so no other mass changes.

Value-engineering target: USD 1,000. Estimated cost of the constructable design: USD 3,865 (USD 2,865 over the target). R10, restated by Amish on 2026-10-03 (decision 42B), limits the rig to USD 4,000 built with a surplus pipe offcut and tank heads and the host lab's DC supply and vacuum pump: USD 3,865 is USD 135 under it.

*Table 6a. Cost changes from decisions 41B and 42B.*

| BOM line | Before | After | Price basis |
| --- | --- | --- | --- |
| 1 Shell | USD 420 (new-cut) | USD 150 (surplus offcut) | About 185 kg at about USD 0.80 a kg, surplus line-pipe remnant |
| 3 Dished heads (2) | USD 520 | USD 260 | About half the new price, second-hand or overstock heads |
| 17 Baffle plate | USD 75 (63 % open) | USD 85 (80 % open) | Less common square-hole pattern, about USD 10 more |
| 29 Vacuum pump and hose | USD 260 | USD 45 (hose, clamps, adapter) | Host lab's pump; hose about USD 12 a metre |
| 32 Motor power supply | USD 320 | USD 0 | Host lab's DC supply |
| Total | USD 4,920 | USD 3,865 | |

The largest items are now the welding labour (USD 650), the flange rings, saddles, nozzles and window rings (about USD 820), the valve manifold (USD 220), and the speed controller and safety controls (USD 280). The surplus pipe and heads are accepted only after the checks in the design decisions register: out-of-roundness no more than 8 mm, wall no less than 5.9 mm anywhere, head diameter, thickness and skirt matched to the pipe. The host lab's pump needs a rating of at least about 140 L/min (5 CFM) of free air to keep the pump-down within R8's 5 minutes (pump-down time scales inversely with pump speed: 4.0 min x 170 / 140 is about 4.9 min; section C), and its DC supply needs at least 1,500 W at 24 V, or the thrust reached at 5,000 m density falls below about 44 N (section E). Both are checked before the host lab's equipment is accepted.

## I. Results against every requirement

*Table 7. Results against every requirement.*

| ID | Result | Status |
| --- | --- | --- |
| R1 | 0.736 kg/m3 at 61.9 kPa and 20 °C; pump reaches far lower | Met |
| R2 | Density error 0.60 % | Met |
| R3 | 0 to 50 N, error 0.27 % of full scale | Met |
| R4 | Torque error 0.28 % of 2 N m; speed 0.02 % | Met |
| R5 | 380 mm propeller with 210 mm to the wall, 80 mm to the deck | Met |
| R6 | Thrust 1.8 % to 3.3 % high with the 80 % open baffle | Met (decision 41B) |
| R7 | Collapse factor 6.7 at full vacuum (shell); heads 40; window 7.1 on yield | Met |
| R8 | 4.0 min to 54 kPa | Met |
| R9 | 20 Hz CSV | Met |
| R10 | USD 3,865 against the restated USD 4,000 (value-engineering target USD 1,000, USD 2,865 over) | Met as restated (decision 42B) |
| R11 | Door held by 24 kN under vacuum; key, latch interlock and emergency stop; vent in about 130 s; window and feed-through outside the fragment zone | Met by design |
| R12 | Relief at 46.3 kPa; vessel designed for full vacuum | Met |
