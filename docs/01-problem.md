---
doc_id: ALR-PRB-001
title: AltiRig problem statement
project: AltiRig
doc_type: Problem statement
version: "0.2"
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
  change: TRL 2 review; open questions settled under Amish's 2026-10-03 pre-approval (ALR-DDR-001); co-design candidate named; density target at room temperature clarified
---

# AltiRig problem statement

Thrust and power depend on air density. Most drone makers test propellers and motors in their own workshop air, then learn how they behave at altitude only when they fly there.

## The problem

The thrust and power coefficients that describe a propeller both include air density ([Tyto Robotics](https://www.tytorobotics.com/blogs/articles/how-to-measure-propeller-performance-coefficients)). At the same speed, a propeller at 5,000 m, where density is about 60% of sea level ([Engineering ToolBox](https://www.engineeringtoolbox.com/standard-atmosphere-d_604.html)), makes much less thrust, so the motor must spin faster, draw more current and run hotter to hold a hover. Small propellers also run at low Reynolds numbers, where published performance data show strong effects of size and speed ([Brandt and Selig, UIUC, 2011](https://m-selig.ae.illinois.edu/pubs/BrandtSelig-2011-AIAA-2011-1255-LRN-Propellers.pdf)); thinner air pushes them further into that range, so sea-level data cannot simply be scaled.

Tools exist but not in the right form. Thrust stands such as the Tyto Robotics Flight Stand 50 measure up to 50 kgf of thrust, torque and power, but at room conditions ([Tyto Robotics](https://www.tytorobotics.com/pages/flight-stand-50)). Research groups have tested small unmanned aircraft in low-pressure, low-temperature facilities ([Politecnico di Torino, UAS testing in low pressure and temperature conditions](https://www.researchgate.net/publication/347154436_UAS_testing_in_low_pressure_and_temperature_conditions)), and industrial altitude chambers are sold for equipment testing ([Sanatron](https://www.sanatron.com/articles/altitude-test-chamber-how-vacuum-chambers-simulate-high-altitudes.php)). What is missing is an open, low-cost chamber with a built-in thrust stand that a small team can build and use to choose propellers for a specific altitude.

## Users and context

| User | Need | Context |
| --- | --- | --- |
| Kitewright frame and payload builders | Measured thrust and power at 5,000 m density for Lift and Range propulsion | Design and verification before high-altitude flights |
| University aerospace and mechanical labs | An affordable way to study propellers in thin air | Teaching and research labs near sea level |
| Mountain rescue and survey drone operators | Confidence that a drone has hover margin at the altitude of a job | Pre-season checks of aircraft and spare propellers |
| Independent drone makers | Published, comparable altitude data for common propellers and motors | Choosing parts for high-altitude builds |

## Operating environment

- Indoor workshop or lab at or near sea level, on a solid bench or floor.
- Chamber interior from ambient pressure down to about 54 kPa (7.8 psi), the pressure at 5,000 m ([Engineering ToolBox](https://www.engineeringtoolbox.com/standard-atmosphere-d_604.html)); extension to 47 kPa (6,000 m) as a stretch target. Because the chamber air is at room temperature, not at the -17.5 °C of 5,000 m, the density of 5,000 m is reached at a higher pressure: about 61.9 kPa at 20 °C (ALR-CAL-001, section A). AltiRig matches density, which sets thrust and power, and records pressure and temperature with every run.
- Room temperature in the base version; optional chilling towards -20 C is a later variant.
- Mains power for the vacuum pump and a bench power supply or battery for the motor under test.

## Constraints

- Prototype budget ceiling USD 1,000 for chamber, pump, stand and instruments.
- Propellers up to about 380 mm (15 in) diameter in the first version (target).
- Pressure vessel designed with a clear safety factor against collapse; the pressure difference at 5,000 m equivalent is about 47 kPa (6.8 psi), which loads a large flat panel heavily.
- Built from bought parts and simple fabrication; no machining beyond a maker-space level.
- Open design: hardware under CERN-OHL-S-2.0, logging software under an open software licence.

## Out of scope

- Forward-flight (wind tunnel) testing; AltiRig covers static and hover thrust only.
- Full environmental certification testing to aerospace standards.
- Testing of combustion engines or fuel systems.
- Rating any propeller or motor as certified for flight; results are engineering data only.

## Prior work

| Prior work | What it does | Gap for these users | Source |
| --- | --- | --- | --- |
| Tyto Robotics Flight Stand 50 | Commercial thrust stand measuring up to 50 kgf thrust, 30 Nm torque, speed and electrical and mechanical power | Measures at room conditions only; no altitude simulation | [link](https://www.tytorobotics.com/pages/flight-stand-50) |
| UAS testing in low pressure and temperature conditions (Politecnico di Torino) | Research on testing small unmanned aircraft in a low-pressure, low-temperature facility | Institutional facility; not an open, buildable design | [link](https://www.researchgate.net/publication/347154436_UAS_testing_in_low_pressure_and_temperature_conditions) |
| Industrial altitude test chambers | Vacuum chambers that simulate high altitude for equipment testing | Built for general equipment; no integrated propeller thrust stand; industrial cost | [link](https://www.sanatron.com/articles/altitude-test-chamber-how-vacuum-chambers-simulate-high-altitudes.php) |
| UIUC propeller performance data (Brandt and Selig, 2011) | Measured performance of small propellers at low Reynolds numbers | Measured at test-section density; does not show performance at 5,000 m directly | [link](https://m-selig.ae.illinois.edu/pubs/BrandtSelig-2011-AIAA-2011-1255-LRN-Propellers.pdf) |

## Co-design

A university aerospace or mechanical engineering lab with a thrust stand or vacuum equipment, because they can check chamber safety, calibrate the stand and compare results with their own data. The first candidate to approach is the Department of Aerospace Engineering at IIT Kanpur, which has propeller and wind tunnel facilities and works with Himalayan users; the second is the Department of Mechanical Engineering at Kathmandu University, close to the Nepal users. Both are candidates, not agreed partners (ALR-DDR-001, D11).

Co-design checklist:

- [ ] Partner reviews the vessel calculation (ALR-CAL-001, section B) before any pump-down.
- [ ] Partner witnesses the first proof pump-down behind the guard.
- [ ] Side-by-side runs of the same propeller on the partner's open-air stand and in AltiRig at ambient pressure (R6).
- [ ] Partner agrees which propellers are tested first and how data are published.

## Open questions settled at the TRL 2 review

These were settled on 2026-10-03 under Amish's pre-approval; each is argued in ALR-DDR-001.

- **Closed-chamber accuracy.** A closed chamber is used, with a vessel 2.1 times the largest propeller diameter, a removable perforated baffle and side-by-side comparison runs at ambient pressure (R6). Whether R6 is met is still to be shown; the estimate and the options are in ALR-CAL-001, section F, and in the review note.
- **Cold air.** The first version runs at room temperature and matches density, not temperature. Chilling towards -20 °C is a later variant.
- **Vessel type.** A horizontal steel vessel made from an 813 mm (32 in) pipe offcut with two bought 2:1 ellipsoidal tank heads, one as the door. A thin steel drum would collapse under vacuum and a flat-panelled box needs heavy ribs, so both were rejected.
- **Propeller, motor and tuning kit.** It is not part of this repo. AltiRig publishes measured data; the Kitewright Lift and Range frames publish their propulsion kits using that data.

## Safety

> **Safety:** AltiRig is a vacuum vessel with a spinning propeller inside. At the 5,000 m density point the air outside pushes on the vessel with about 39 kPa, and the door alone carries about 24 kN (2.5 t). A collapsed vessel or a failed window can throw fragments; a propeller that breaks at speed releases fragments in its own plane. The motor supply and the vacuum pump run from mains power. AltiRig is an open engineering reference, not certified pressure or test equipment.
