---
doc_id: ALR-DDR-003
title: AltiRig requirement decisions (R6, R10)
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
  change: Amish's requirement decisions 41B and 42B carried out
---

# 0003: Requirement decisions on the chamber effect and cost

- **Date:** 2026-10-03
- **Status:** accepted
- **Decided by:** Amish Chadha, 2026-10-03, accepting every recommendation put to him in the second round of requirement decisions: "i agree with all the 46 recommendations you provided. please proceed." For AltiRig: 41B (R6) and 42B (R10).

> **Safety:** Neither decision changes the vessel's design or its safety case. The baffle is inside the vessel and carries no pressure. Surplus pipe and heads are accepted only after the roundness and thickness checks on which the shell's collapse factor of 6.7 depends, and the host lab's DC supply is always switched through the cabinet's interlocked contactor and emergency stop (R11). The host lab's pump must have a thermal overload and an oil-mist exhaust filter led outdoors.

## Context

At TRL 3 (ALR-CAL-001 v0.2) two requirements were at risk or not met on paper. R6 was at risk: with the 63 % open baffle the chamber was estimated to give 2.9 % (same power) to 5.3 % (same speed) more thrust than open air, against a 5 % target. R10 was not met: USD 4,920 against the USD 1,000 value-engineering target. Each was put to Amish as state, options and a recommendation in `docs/REVIEW.md`.

## Options considered

- **R6 (decision 41):** A: keep the 63 % baffle. B (chosen): an 80 % open baffle on the same tabs. C: a 1,016 mm (40 in) vessel with the 63 % baffle.
- **R10 (decision 42):** A: keep the parts as specified (USD 4,920). B (chosen): surplus pipe offcut and tank heads, the host lab's existing DC supply and a workshop vacuum pump with a thermal overload and exhaust filter (about USD 3,700 to 4,000). C: a 610 mm (24 in) vessel for propellers up to about 280 mm (R5 no longer met).

## Decision

1. **41B.** The baffle (BOM line 17) is 2 mm perforated steel with 22 mm square holes on a 24.5 mm square pitch: 80.6 % open, 2.5 mm bars, cut to the same 790 mm disc and bolted to the same four tabs. About 1.5 kg; USD 85 (USD 10 more). The 1,016 mm vessel is held in reserve if the TRL 4 comparison runs still show more than 5 %.
2. **42B.** The shell (line 1) is a surplus pipe offcut (USD 150, was USD 420) and the two heads (line 3) are second-hand or overstock (USD 130 each, was USD 260). The host lab provides its vacuum pump (line 29: only the hose, clamps and adapter are bought, USD 45, was USD 260) and its DC supply (line 32: USD 0, was USD 320). The surplus pipe and heads pass the checks in the register before purchase; the pump is rated no less than 140 L/min; the supply gives at least 1,500 W at 24 V and is switched by the cabinet's contactor.
3. **R10 restated** in `docs/03-requirements.md` v0.4: complete rig at or below USD 4,000, built with a surplus pipe offcut and tank heads that pass the roundness and thickness checks, and the host lab's existing DC supply and vacuum pump; the USD 1,000 value-engineering target is kept as a control figure (`budget_usd` unchanged).

## Results (ALR-CAL-001 v0.3)

| Requirement | Before | After | Status |
| --- | --- | --- | --- |
| R6, chamber effect | 2.9 % to 5.3 % (63 % baffle) | 1.8 % (same power) to 3.3 % (same speed), target 5 % | Met on paper; TRL 4 comparison runs decide |
| R10, cost | USD 4,920 against USD 1,000 | USD 3,865 against the restated USD 4,000 (USD 135 under) | Met as restated |
| R8, pump-down | 4.0 min with a new 170 L/min pump | Unchanged with a 170 L/min host lab pump; about 4.9 min at 140 L/min | Met if the pump is at least 140 L/min |

Value-engineering target: USD 1,000. Estimated cost of the constructable design: USD 3,865 (USD 2,865 over the target). Mass: about 585 kg with the pump and cabinet in the model; the 80 % baffle is 1.3 kg lighter than the 63 % sheet. (The model had counted the baffle as a solid 7.7 kg disc; it now counts the solid share of the sheet only.)

## Consequences

- Model: `BAF_OPEN` 0.80, `BAF_HOLE` 22, `BAF_PITCH` 24.5 in `cad/src/model.py`, with checks that the open area is at least 80 % and the bars are no thinner than the sheet. STEP and STL regenerated.
- Drawings: ALR-DWG-001 Rev P3 (baffle note); making sketches ALR-DWG-101 Rev P2 (surplus pipe checks), ALR-DWG-110 Rev P2 (surplus head checks), ALR-DWG-115 Rev P2 (80 % sheet).
- The cost now depends on the host lab: a project without a lab supply and pump would pay about USD 535 more (USD 4,400), over the restated R10.
