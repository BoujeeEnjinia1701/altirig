---
doc_id: ALR-DDR-002
title: AltiRig design for construction
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
  change: Constructability review and changes C1 to C17, decided under Amish's 2026-10-03 pre-approvals
---

# 0002: Design for construction

- **Date:** 2026-10-03
- **Status:** decided. Amish, 2026-10-03: "start with the first 14 repos from the list of 29 projects. I pre-approve the batch runs along with any recommendations you come up with. I also accept any cost overruns or variations from the assumed scope cost." And, for this batch: "Proceed with the remaining 15 scaffolds". Standard section 18 (Amish, 2026-09-30): "fix the design assumptions to match and be physically feasible".

## Context

The TRL 2 concept named a vessel, a window, feed-throughs, a stand and baffles but not how any of them is made or held. The constructability review went through every component: how it is made, which faces touch its neighbours, what holds them, and in what order it goes together. The model (`cad/src/model.py`) was checked with build123d for overlaps between every pair of parts (none remain) and for clearances (`clearances()`); the masses come from the solids. Nothing below changes what AltiRig does, its pitch or its safety case; the safety-related changes (C3, C15, C16) are all in the conservative direction.

> **Safety:** The vessel is a vacuum vessel. Welding on it is done by a qualified welder, and no part of it is put under vacuum until the safety stops in ALR-BLD-001, section 6, are passed.

## Changes

*Table 1. Changes made for construction.*

| # | Component | The concept had | The constructable design has | Why |
| --- | --- | --- | --- | --- |
| C1 | Shell | "A steel drum or tank" | An 813 x 6.35 mm pipe offcut, 1,500 mm long, ends square, holes cut to the nozzle outside sizes | A stocked item; round within 1 % so the buckling calculation holds |
| C2 | Flange rings and door seal | A door with no detail | Two 20 mm plate rings, 960 OD, bored to fit over the pipe and over the door head's skirt; fillet welded both sides; a 6 mm closed-cell EPDM sponge gasket glued to the shell ring's face | Flat cut rings need no machining; the sponge takes up 1 to 2 mm of weld distortion; under vacuum the air closes the joint |
| C3 | Nozzles | A window and feed-throughs in the wall | Heavy-wall set-in stubs (10 in XS for the window, 6 in XS for the feed-through) with square-cut ends standing 16 to 40 mm into the vessel, welded inside and out; no reinforcing pads | No saddle-shaped contour cut on the stub; the heavy wall replaces the metal removed (1.7 and 2.3 times the area needed) |
| C4 | Window | "A polycarbonate or laminated window" | A 340 mm, 20 mm polycarbonate disc on a 6 mm EPDM ring gasket, held by a 10 mm clamp ring over a 25 mm spacer ring with 8 x M10 into the tapped flange | The spacer sets the gasket squeeze (6 to 5 mm) so the window is never over-clamped; no holes in the window |
| C5 | Feed-through | "Sealed feed-through connectors" | A 15 mm aluminium plate with five M20 IP68 glands, cables potted in epoxy for 50 mm, on a 2 mm gasket | Stock glands; potting stops air leaking along the strands |
| C6 | Saddles | Not shown | Two welded saddles: 10 mm web with a curved top, rolled wear plate over 120°, base plate with two anchor holes | Carries the 470 kg vessel at axis height 800 mm with the load spread along the wear plates |
| C7 | Deck | Not shown | Two 50 x 50 x 6 angles welded inside, hanging legs scribed to the wall; an 8 mm aluminium deck bolted to the top legs | The stand needs a flat, removable base; the deck slides in through the door |
| C8 | Baffle | "Flow straightener and baffles" | One 790 mm perforated steel disc, 63 % open, bolted to four welded tabs 590 mm downstream of the propeller | Removable, so the comparison runs can be made with and without it (R6) |
| C9 | Hinge | Not shown | Two 15 mm lugs on each flange ring and a 20 mm pin on the far side; the door lugs' holes slotted 3 mm | Carries the 72 kg door; the slot lets the door seat evenly on the gasket |
| C10 | Latches | Not shown | Three bolt-on latch clamps, at least 3 kN each, at the top, the window side and the bottom | Pull the door into the sponge for the first seal (6.3 kN in all); vacuum does the rest |
| C11 | Thrust stand | "Load cells measuring thrust" | 12 mm base plate; two 0.5 mm spring-steel leaves in slit aluminium clamps; anchor block and hanger holding an upright 10 kg bar cell; 10 mm carriage | A bending-beam cell must be loaded across its length: standing it upright lets the carriage push its top end along the axis |
| C12 | Torque head | "Reaction torque" | Housing bored for two 6202 bearings; 15 mm shaft with a hub and an 80 mm motor plate; a 60 mm arm clamped on the shaft resting on a 5 kg cell on a bracket, through a 3 mm ball | The motor's reaction torque is read without the thrust passing through the torque cell; bearing friction 0.001 N m |
| C13 | Speed sensor | "Optical or electrical RPM" | Optical sensor on an aluminium post on the base plate, 15 mm from the propeller plane, 140 mm below the axis | Fixed to the stand so it moves with nothing; clear of the blades |
| C14 | Valve manifold | "Bleed valve" | A 2 in stub with a tapped 150 mm flange on top; a bought manifold of fittings (relief valve, gauge, bleed and needle valve, vent valve, isolation valve, pump port) bolted on with a gasket | Every valve is a stock fitting; one flange to seal |
| C15 | Bleed valve | Any bleed valve | A normally-open solenoid bleed valve | The chamber vents if power is lost or the emergency stop is pressed (R11) |
| C16 | Feed-through position | Not placed | On the window side, 740 mm from the flange face, 20.9° clear of the propeller plane | Keeps the cable plate out of the fragment zone and close to the control cabinet |
| C17 | Pump and cabinet | Not placed | Pump on the floor on the far side with its exhaust led outdoors; cabinet in front of the door on the window side, so the operator sees the window and reaches the emergency stop | The door swings to the far side; the operator's side stays clear |

## Consequences

- The general arrangement is at Rev P2 (ALR-DWG-001); making sketches ALR-DWG-101 to 122 and the build plan ALR-BLD-001 describe this design.
- The calculations were re-run (ALR-CAL-001 v0.2). The set-in nozzles meet the opening area rule without pads; the stand error budgets are unchanged.
- The bill of materials gains the gaskets, latches, spacer and clamp rings, tabs, hinge and welding labour; the estimated cost is USD 4,920 against the USD 1,000 value-engineering target.
- `design_state: constructable` is set in `project.yaml`.
