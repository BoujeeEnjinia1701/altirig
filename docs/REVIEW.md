# Review note: AltiRig

## Session 2026-09-30: scaffolded

### What was done

- Repository created from kit 1.6.0 at TRL 1, target TRL 2.
- `docs/01-problem.md` (ALR-PRB-001 v0.1): problem with cited evidence, users, environment, constraints, prior work, open questions.
- `docs/02-concept.md` (ALR-PRC-001 v0.1): how it works, components, patent design-arounds, shared blocks, safety.
- `docs/03-requirements.md` (ALR-REQ-001 v0.1): 10 proposed requirements.
- `README.md` with concept rationale, burning platform, where it could be used, and what sparked the idea.

### Next

- Run `/populate` to bring the repo to a strong TRL 2 with concept media (done 2026-10-03, below).

## Session 2026-10-03: TRL 2 (populate)

Run under Amish's 2026-10-03 instructions: "start with the first 14 repos from the list of 29 projects. I pre-approve the batch runs along with any recommendations you come up with. I also accept any cost overruns or variations from the assumed scope cost." and "Proceed with the remaining 15 scaffolds". Kit updated to 1.7.0.

### What was done

- `docs/01-problem.md` (ALR-PRB-001 v0.2): open questions settled, density target at room temperature explained, co-design candidates and checklist, safety section.
- `docs/03-requirements.md` (ALR-REQ-001 v0.2): concept status for every requirement; R11 (interlocks) and R12 (over-vacuum protection) added.
- `docs/02-concept.md` (ALR-PRC-001 v0.2): how it works, components, key design choices, safety.
- `docs/decisions/0001-trl2-review-decisions.md` (ALR-DDR-001): TRL 2 review decisions D1 to D14.
- Concept media from `cad/src/concept_media.py`: `media/hero.png`, `cutaway.png`, `exploded.png`, `flow.png`, `concept-blueprint.png` and `.pdf` (ALR-DWG-010), `model.glb` (1.3 MB) and `viewer.html`. The media were regenerated from the constructable model at TRL 3.

### Results

- Vessel type chosen: an 813 mm pipe with two 2:1 ellipsoidal tank heads, one as the door; density matched (61.9 kPa at 20 °C for 5,000 m), not pressure.

### Requirements not met

- None decided at TRL 2; R6 and R10 are reported in the TRL 3 section.

### Decisions made under the pre-approval

- D1 to D14 in ALR-DDR-001, including the co-design candidates (IIT Kanpur first, Kathmandu University second; candidates, not agreed) and the conservative safety choices: vessel designed for full vacuum (relax only with a code calculation and a strain-gauged proof test), polycarbonate window outside the fragment zone (relax only with impact tests), no batteries inside (relax only with a vent and fire plan and abuse tests).

### Safety concerns

- Vacuum vessel (implosion, window failure), door held by tonnes of force, spinning propeller, mains power. Safety sections are in every document.

## Session 2026-10-03: TRL 3 (advance and build plan)

### What was done

- `docs/04-calcs/01-sizing.md`, `sizing.py`, `results.csv` (ALR-CAL-001 v0.2): density, vessel strength, pump-down, heating and density control, stand, chamber effect, data, cost; results against every requirement.
- `cad/src/model.py`: parametric build123d model of 48 components with an overlap check (none) and clearances; `cad/step/altirig-assembly.step`, `altirig-vessel.step`, `altirig-stand.step`; `cad/stl/altirig-stand.stl`, `altirig-assembly.stl`.
- `cad/src/sheets.py`: general arrangement ALR-DWG-001 Rev P2.
- `bom/bom.csv`: 38 lines, every line priced with a supplier type.
- `docs/decisions/0002-design-for-construction.md` (ALR-DDR-002): changes C1 to C17.
- `cad/src/build_plan_media.py`: overview, 22 making sketches (ALR-DWG-101 to 122), 10 joint close-ups, 20 step pictures.
- `docs/05-build-plan.md` (ALR-BLD-001) and `docs/06-design-decisions.md` (ALR-DEC-001).
- `cad/src/product_model.py` (hero, exploded, detail) and scenes exported to `/home/claude/renders/altirig` for the photoreal renders on Amish's Mac.
- `docs/02-concept.md` v0.3, `docs/03-requirements.md` v0.3, README, `project.yaml` (trl 3, design_state constructable).

### Results

- Density of 5,000 m: 0.736 kg/m3 at 61.9 kPa (20 °C); relief at 46.3 kPa absolute.
- Vessel at full vacuum: shell collapse factor 6.7, heads 40, window 7.1 on yield; openings 1.7 and 2.3 times the area needed; door held by 24 kN at the 5,000 m point.
- Pump-down to 54 kPa: 4.0 min with a 170 L/min pump; 0.93 m3 free volume.
- Stand: thrust error 0.13 N (0.27 % of 50 N); torque 0.28 % of 2 N m; speed 0.02 %; density error 0.6 %.
- Example 15 x 5 in propeller at 50 N and 5,000 m density: 10,830 rpm, about 1,800 W electrical, so the 1,500 W supply limits it to about 44 N.
- Mass: about 470 kg vessel, about 590 kg with pump and cabinet.
- Value-engineering target: USD 1,000. Estimated cost of the constructable design: USD 4,920 (USD 3,920 over the target).

### Requirements not met

- **R6 (chamber effect): at risk.** Estimated 2.9 % (same power) to 5.3 % (same speed) more thrust in the chamber than in open air with the 63 % open baffle.
- **R10 (cost): not met.** USD 4,920.

### Decisions for Amish

**R6, chamber effect.**

- **State:** the estimate is 2.9 % to 5.3 % above open air at the same speed, against the R6 target. Cause: the perforated baffle, crossed twice by the loop of air inside the closed vessel, adds resistance that slows the propeller's own flow, so it makes more thrust at the same speed.
- **Option A:** keep the 63 % open baffle as designed. Effect on R6: 2.9 % to 5.3 % (at risk). Cost and mass: no change.
- **Option B:** use an 80 % open perforated or expanded-metal baffle, still bolted to the same tabs. Effect on R6: 1.8 % to 3.3 %. Cost: about USD 10 more. Mass: about 3 kg less. It still breaks up the jet and the swirl; the comparison runs at TRL 4 are made with and without it.
- **Option C:** a 1,016 mm (40 in) vessel with the 63 % baffle. Effect on R6: 1.1 % to 2.0 %. Cost: about USD 900 more (pipe, heads, rings, welding). Mass: about 150 kg more.
- **Recommendation: B.** It brings both estimates under the target at almost no cost and keeps the vessel; C is held in reserve if the TRL 4 comparison still shows more than 5 %.

**R10, cost.**

- **State:** USD 4,920 against the USD 1,000 value-engineering target. Cause: a vessel safe at full vacuum needs about 470 kg of pipe, heads and plate and about USD 650 of welding; the 1,500 W motor supply, speed controller and safety controls add about USD 780.
- **Option A:** keep the parts as specified. Cost: USD 4,920. No effect on any other requirement.
- **Option B:** source the pipe offcut and tank heads as surplus, and use the host lab's existing DC supply and a workshop vacuum pump that has a thermal overload and exhaust filter. Cost: about USD 3,700 to 4,000 (saving about USD 900 to 1,200). Mass: no change. Requirements: none affected, provided the surplus pipe meets the roundness and thickness checks in the register.
- **Option C:** a 610 mm (24 in) vessel for propellers up to about 280 mm. Cost: about USD 4,200. Mass: about 150 kg less. R5 would then not be met (380 mm propellers no longer fit), and R6 would worsen with the same propellers.
- **Recommendation: B.** It saves the most without touching what the rig does; the safety checks on second-hand steel are already in the plan.

### Decisions made under the pre-approval

- ALR-DDR-002, design for construction C1 to C17 (listed below and in the register).
- Cost overrun against the value-engineering target accepted; `budget_usd` left at USD 1,000.

### Design changes made for construction (2026-10-03)

- C1 shell from an 813 x 6.35 mm pipe offcut; C2 flat flange rings with a sponge gasket, door held shut by air; C3 heavy-wall set-in nozzles with square-cut ends, no pads; C4 window stack with a spacer ring that sets the gasket squeeze; C5 potted IP68 feed-through plate; C6 welded saddles; C7 deck rails and bolted deck; C8 bolted 63 % baffle on four tabs; C9 hinge with slotted door lugs; C10 three latch clamps; C11 flexure stand with an upright bar cell between anchor and hanger; C12 torque head on two bearings with an arm on a second cell; C13 speed sensor post; C14 manifold on a stub flange; C15 normally-open bleed valve; C16 feed-through on the window side outside the fragment zone; C17 pump and cabinet placement.

### Build plan findings

- Twenty-two made components, ten joints and twenty steps. Every part was checked for overlap with every other (none) in the model.
- The shell's strength depends on the rear head and the flange ring being welded continuously all round (with no end support the factor falls to about 1); the plan makes this a hold point.
- The 80 mm propeller-to-deck clearance and the 15 mm sensor-to-propeller gap are the tightest clearances.
- The door weighs about 72 kg and the shell about 185 kg: the welding steps need a hoist.

### Appearance model deviations (product_model.py)

- The baffle is drawn as a plain disc; its holes are not modelled.
- The control cabinet is left out of the hero render; a 1.75 m mannequin stands beside the door end, not between the camera and the vessel.
- In the exploded render the stand, the deck and the test article are lifted out above the vessel.
- These are appearance choices only and are decided under the pre-approval; no dimension differs from `model.py`.

### Safety concerns

- Implosion or window failure under vacuum: vessel designed for full vacuum, relief valve, polycarbonate only, proof pump-down behind a guard after a qualified engineer's review.
- The door under vacuum carries up to 62 kN at full vacuum: vent before unlatching.
- Propeller failure: window and feed-through outside the 15° fragment zone; steel shell contains fragments; interlocked arming.
- Mains: RCD, earthed vessel, emergency stop, normally-open bleed valve.
- Batteries are excluded from the chamber in this version.

### Recommended next step

- Amish decides R6 and R10 above. Then, for TRL 4 (when the phase cap allows): have the vessel calculation reviewed by a qualified engineer, build the vessel with the co-design partner, proof-test it, and run the R6 comparison with and without the baffle.

## 2026-10-03: photoreal renders

Rendered with Blender Cycles on Amish's Mac from `cad/src/product_model.py`; captioned with `.kit/photo_caption.py`; `media/card.png` and `media/social-preview.png` made with `.kit/cards.py`. Views: hero, exploded, detail. image_qc passes and `render.py --check` has no FAIL.

## 2026-10-03: Amish's requirement decisions carried out

Amish, 2026-10-03: "i agree with all the 46 recommendations you provided. please proceed." For AltiRig these are decisions 41B (R6) and 42B (R10), each as recommended in the TRL 3 section above. Recorded in `docs/decisions/0003-requirement-decisions.md` (ALR-DDR-003) and the register `docs/06-design-decisions.md` v0.2. Not committed or pushed (batch run).

### Changes

- **41B, R6.** The baffle (BOM line 17) is now 2 mm perforated steel with 22 mm square holes on a 24.5 mm square pitch: 80.6 % open, 2.5 mm bars, the same 790 mm disc on the same four tabs. About 1.5 kg; USD 85 (USD 10 more; price basis: the 63 % sheet's USD 75 plus a less common square-hole pattern). The 1,016 mm vessel is held in reserve if the TRL 4 comparison runs show more than 5 %.
- **42B, R10.** Shell (line 1) a surplus offcut, USD 150 (was 420; about 185 kg at about USD 0.80 a kg). Heads (line 3) second-hand or overstock, USD 130 each (was 260; about half the new price). Vacuum pump (line 29) from the host lab: only the hose, clamps and adapter are bought, USD 45 (was 260). Motor DC supply (line 32) from the host lab, USD 0 (was 320), still switched through the cabinet's interlocked contactor and emergency stop. R10 restated in `docs/03-requirements.md` v0.4 as "complete rig at or below USD 4,000, built with a surplus pipe offcut and tank heads that pass the roundness and thickness checks, and the host lab's existing DC supply and vacuum pump; the USD 1,000 value-engineering target is kept as a control figure".
- **Model.** `cad/src/model.py`: `BAF_OPEN` 0.80, `BAF_HOLE` 22, `BAF_PITCH` 24.5, new `baffle_open()`; new checks that the open area is at least 80 % and the bars are no thinner than the sheet; the baffle's mass now counts only the solid share of the sheet (it had been counted as a solid 7.7 kg disc). Checks: no overlaps, both new checks pass. STEP and STL regenerated.
- **Calculations.** `docs/04-calcs/sizing.py` and `01-sizing.md` v0.3: section F with the 80 % baffle as designed (superseded 63 % case and the 1,016 mm reserve kept for comparison), section H with the restated R10 and a cost-change table with a price basis per line; `results.csv` re-run.
- **Pictures.** General arrangement ALR-DWG-001 Rev P3 (baffle note 80 % open). Making sketches ALR-DWG-101 Rev P2 (surplus pipe checks before buying), ALR-DWG-110 Rev P2 (surplus head checks), ALR-DWG-115 Rev P2 (80 % square-hole sheet). Concept blueprint key figures (chamber effect and cost) and the concept media regenerated (`model.glb` is now 3.9 MB, was 1.3 MB, at the required glTF deflections). The overview, joint 7 and Step 12 are unchanged: the model draws the baffle as a plain disc, so they look the same.
- **Text.** `docs/05-build-plan.md` v0.2 (summary, 3.1 shell, 3.15 baffle, 3.23 bought components with the host lab's pump and supply, Step 20), `docs/02-concept.md` v0.4, `README.md`, `project.yaml` (budget comment, trl_evidence).
- **Appearance model.** `cad/src/product_model.py` now cuts the baffle's square holes (inside an 8 mm rim, clear of the bolt holes) so the exploded render shows the open sheet; scenes re-exported to `/home/claude/renders/altirig`. This replaces the earlier plain-disc deviation.

### New results (ALR-CAL-001 v0.3)

- R6: met on paper. 1.8 % (same power) to 3.3 % (same speed) more thrust than open air, against 5 % (was 2.9 % to 5.3 %). Baffle removed: 1.4 % to 2.5 %. The TRL 4 comparison runs with and without the baffle decide it.
- R10: met as restated. USD 3,865 against USD 4,000 (USD 135 under). Value-engineering target: USD 1,000. Estimated cost of the constructable design: USD 3,865 (USD 2,865 over the target). `budget_usd` unchanged.
- R8: unchanged at 4.0 min with a 170 L/min host lab pump; a pump rated 140 L/min gives about 4.9 min, so the host lab's pump must be at least 140 L/min.
- Mass: about 585 kg with the pump and cabinet (model); the 80 % baffle is 1.3 kg lighter than the 63 % sheet.
- All twelve requirements are now met on paper.

### For Amish

- No new decision. The cost now depends on the host lab: without its pump and supply the rig costs about USD 4,400, over the restated R10. What the lab's pump and supply must meet is in the register's To confirm list (rows 6 and 9).
- The photoreal renders (`media/render-*.png`), card and social preview still show the plain baffle disc; re-render on the Mac from the re-exported scenes.

### Cross-repo actions

- None. Neither decision touches another repo.

### Safety

- No change to the vessel or its safety case. Surplus pipe and heads are accepted only after the roundness and thickness checks that the shell's collapse factor of 6.7 assumes; the build plan and making sketches now put these checks before purchase.
- The host lab's DC supply is never wired straight to the speed controller: it is switched by the cabinet's interlocked contactor and emergency stop (R11). The host lab's pump must have a thermal overload and an oil-mist filter, exhausting outdoors.
- The 80 % baffle carries no pressure; its rim is filed smooth to remove sharp part-holes.

## 2026-10-04: photoreal renders redone after the round-2 and round-3 decisions

Views: hero, exploded, detail; cards regenerated; image_qc passes and `render.py --check` has no FAIL.
