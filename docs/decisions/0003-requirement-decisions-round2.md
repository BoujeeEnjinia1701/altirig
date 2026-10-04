---
doc_id: ALR-DDR-003
title: AltiRig requirement decisions, round 2
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
  change: R6 (chamber effect) and R10 (cost) decided by Amish on 2026-10-03, both as recommended
---

# 0003: Requirement decisions, round 2

- **Date:** 2026-10-03
- **Status:** decided. Decided by Amish Chadha, 2026-10-03: "i approve all of the 47 recommendations provided by you. Execute them." Both decisions below were the recommended options in the TRL 3 review note (`docs/REVIEW.md`, Decisions for Amish) and are taken exactly as worded there.

## Context

At TRL 3 two requirements were not met or at risk on paper (ALR-CAL-001 v0.2). R6 (chamber effect) was at risk: the closed loop of air, crossing the 63 % open perforated baffle twice, was estimated to give 2.9 % (same power) to 5.3 % (same speed) more thrust than open air, against a 5 % target. R10 (cost) was not met: USD 4,920 against the USD 1,000 value-engineering target, driven by about 470 kg of vessel steel, USD 650 of welding and about USD 780 for the motor supply, speed controller and safety controls. Each was posed to Amish with three options and a recommendation.

> **Safety:** Neither decision relaxes a safety provision. Second-hand steel is accepted only after the roundness and thickness checks that the shell's collapse factor of 6.7 depends on; a borrowed pump is used only if it has a thermal overload and an exhaust filter; a borrowed supply stays behind the interlocked contactor and the emergency stop.

## Options considered

*Table 1. Options for each decision.*

| Requirement | A | B | C |
| --- | --- | --- | --- |
| R6, chamber effect | Keep the 63 % open baffle: 2.9 % to 5.3 % (at risk), no change to cost or mass | 80 % open perforated or expanded-metal baffle on the same tabs: 1.8 % to 3.3 %, about USD 10 more, about 3 kg less | 1,016 mm (40 in) vessel with the 63 % baffle: 1.1 % to 2.0 %, about USD 900 more, about 150 kg more |
| R10, cost | Keep the parts as specified: USD 4,920 | Surplus pipe offcut and tank heads, the host lab's DC supply and a suitable workshop vacuum pump: about USD 3,700 to 4,000, no mass change, provided the surplus pipe passes the roundness and thickness checks | 610 mm (24 in) vessel for propellers to about 280 mm: about USD 4,200, about 150 kg less, R5 not met and R6 worse |

## Decision

*Table 2. Decisions taken.*

| # | Requirement | Option chosen | Effect | Condition |
| --- | --- | --- | --- | --- |
| 1 | R6, chamber effect | B: an 80 % open perforated or expanded-metal baffle on the same four tabs | Estimated chamber thrust excess 1.8 % (same power) to 3.3 % (same speed), both under the 5 % target: R6 met on paper. Baffle line USD 75 to USD 85. Baffle metal about 1.5 kg against about 2.9 kg for the 63 % plate (1.3 kg less; the option's "about 3 kg" was rounded high). No change to the vessel, the tabs or the clearances | Option C, the 1,016 mm vessel, is held in reserve if the TRL 4 side-by-side comparison still shows more than 5 % |
| 2 | R10, cost | B: surplus pipe offcut and tank heads, the host lab's DC supply and a suitable workshop vacuum pump | Estimated cost USD 3,920 (was USD 4,920; includes the USD 10 baffle increase), still USD 2,920 over the target: R10 still not met. No mass change, no other requirement affected | The surplus pipe passes the roundness (no more than 8 mm between largest and smallest diameter) and thickness (no less than 5.9 mm anywhere) checks, and the heads match the pipe; otherwise new steel is bought (estimate USD 4,390). The supply must give 1,500 W at 20 to 28 V with a remote on/off input, and the pump at least 170 L/min with a thermal overload and an exhaust filter; otherwise they are bought (estimate USD 4,930 with new steel as well) |

## Consequences

- `cad/src/model.py`: `BAF_OPEN` 0.80 and the hole pattern recorded as 10 mm across-flats hexagonal holes on an 11.2 mm pitch. The disc is still drawn solid, so the outer geometry and every clearance are unchanged; its mass now counts only the metal left by the open area (model total 586 kg, was 593 kg because the old disc was counted solid).
- `docs/04-calcs/sizing.py` and `results.csv` (ALR-CAL-001 v0.3): R6 met on paper at 1.8 % to 3.3 %; the 63 % baffle and the reserve 1,016 mm vessel kept as comparison lines; R10 at USD 3,920, with the cost if the conditions fail.
- `bom/bom.csv`: lines 1 (shell, surplus, USD 210 estimate), 3 (heads, surplus, USD 130 each estimate), 17 (baffle, 80 % open, USD 85), 29 (workshop pump borrowed, hose and adapter USD 40 estimate) and 32 (host lab's supply, USD 0). The surplus prices are estimates at about half the new prices in the TRL 3 bill of materials.
- Build plan ALR-BLD-001 v0.2: acceptance checks for the surplus pipe and heads, the new baffle specification, and the specification the borrowed supply and pump must meet.
- Drawings: ALR-DWG-001 to Rev P3 (baffle note); ALR-DWG-115 and the concept blueprint ALR-DWG-010 regenerated with the new text.
- `docs/03-requirements.md` v0.4: R6 and R10 status updated; no target restated.
- This record supersedes the "63 % open" in ALR-DDR-001 D9 and ALR-DDR-002 C8; the rest of those decisions stands.
