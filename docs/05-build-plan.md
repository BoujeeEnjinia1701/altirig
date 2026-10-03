---
doc_id: ALR-BLD-001
title: AltiRig prototype build plan
project: AltiRig
doc_type: Build plan
version: "0.1"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-03'
  author: Amish Chadha
  change: First build plan; design made constructable (ALR-DDR-002)
---

# AltiRig prototype build plan

**Plan, not yet built.** How to build the first proof-of-concept AltiRig, component by component. Building and testing to it is TRL 4 work. Decisions still to be made are kept in the design decisions register (`docs/06-design-decisions.md`), not here.

> **Safety:** AltiRig is a vacuum vessel with a spinning propeller inside, run from mains power. At the 5,000 m point the air presses on the vessel with 39 kPa and holds the door shut with about 24 kN (2.5 t). A collapsed vessel or a failed window can throw fragments, and a propeller can break at speed. Welding on the vessel is done by a qualified welder. Nothing is pumped down until a qualified engineer has reviewed the vessel calculation (ALR-CAL-001, section B), and the first pump-down is a proof test behind a guard (section 6). No battery goes inside the chamber. This is a prototype for testing, not certified pressure or test equipment.

## 1. What you are building

![Figure 1. Every component, pulled apart and numbered in build order](05-build-plan/overview.png)

*Figure 1. Every component pulled apart and numbered in build order: the vessel 1 to 18, window and feed-through 19 to 24, valve manifold, baffle and deck 25 to 27, the thrust stand 28 to 43, the motor and propeller under test 44 and 45, and the pump, hose and control cabinet 46 to 48.*

The prototype is a horizontal steel vacuum vessel about 2 m long and 813 mm in diameter, standing on two saddles with its axis 800 mm above the floor, with a flexure thrust stand inside. The vessel is a length of steel pipe with a bought dished head welded on the rear end; the door is a second head welded into a flange ring, hung on a hinge and pulled onto a sponge gasket by three latches. A polycarbonate window and a cable feed-through plate sit on short pipe nozzles on the near side, and a valve manifold sits on top. Inside, a deck carries the stand: a base plate, two spring-steel leaves holding a carriage, a load cell for thrust, a torque head on bearings with a second load cell, and a speed sensor. Twenty-two kinds of part are made, in a welding shop and a small machine shop: cutting pipe and plate, drilling and tapping, rolling one strip, welding, boring and turning. The pump, valves, gaskets, load cells, electronics and test article are bought. The parts cost about USD 4,920 from the bill of materials.

## 2. What changed to make it buildable

The TRL 2 concept named the parts but not how they are made or held. Each change keeps what the chamber does; all are recorded in decision record ALR-DDR-002.

*Table 1. Changes from the concept.*

| Component | The concept had | The buildable design has | Why |
| --- | --- | --- | --- |
| Shell | "A steel drum or tank" | An 813 x 6.35 mm pipe offcut with holes cut to the nozzle sizes | Stocked, round enough for the buckling calculation |
| Door seal | A door with no detail | Two flat 20 mm rings, one on the shell and one on the door head, with a sponge gasket between (Figure 26) | No machining; the sponge takes up weld distortion; vacuum closes the joint |
| Nozzles | A window and feed-throughs in the wall | Heavy-wall stubs set in through the wall and cut square, welded inside and out (Figures 28 and 29) | No contour cutting; the heavy wall replaces the steel removed, so no pads |
| Window | "A polycarbonate or laminated window" | 20 mm polycarbonate clamped over a spacer ring that sets the gasket squeeze (Figure 28) | Never over-clamped; no holes in the window |
| Feed-through | "Sealed connectors" | An aluminium plate with five potted IP68 cable glands (Figure 29) | Stock parts; potting stops leaks along the strands |
| Saddles, deck, baffle | Not shown | Welded saddles; two angles inside with a bolted deck; a bolted perforated baffle on four tabs (Figures 31, 32 and 35) | Something to stand on, build on and take out |
| Hinge and latches | Not shown | Lugs and a pin on the far side; three bolt-on latches (Figure 30) | Carry the 72 kg door and pull it on for the first seal |
| Thrust stand | "Load cells" | Two spring-steel leaves carrying a carriage; an upright bar cell between an anchor and a hanger (Figure 33) | No friction; a bending-beam cell is loaded across its length |
| Torque | "Reaction torque" | A torque head on two bearings, with an arm resting on a second cell (Figure 34) | Reads torque without thrust passing through it |
| Bleed valve | Any bleed valve | A normally-open valve | The chamber vents when power is lost |

## 3. Making the components

Sizes are in millimetres. "Door end" is the end with the door; distances along the vessel are measured from the face of the shell's flange ring. The window side is the near side in the pictures.

### 3.1 Shell

![Figure 2. Making sketch, shell](../cad/drawings/ALR-DWG-101.png)

*Figure 2. Shell (ALR-DWG-101).*

**What it is and what it is made from.** The body of the vessel: steel pipe 813 mm outside diameter with a 6.35 mm wall (32 in x 1/4 in), welded line pipe or water pipe, 1,500 mm long. About 185 kg.

**How to make it.**

1. Cut the pipe 1,500 mm long with both ends square to within 1 mm.
2. Measure the diameter at three places around each end and in the middle. The largest less the smallest must be no more than 8 mm. Reject a dented pipe.
3. Mark a straight line along the top. Mark the window hole centre 250 mm from the door end and the feed-through hole centre 740 mm from the door end, both on the side, a quarter turn from the top line. Mark the manifold hole 1,300 mm from the door end on the top line.
4. Cut the holes to the nozzle outside sizes plus 1 to 2 mm: 275 mm for the window, 170 mm for the feed-through, 62 mm for the manifold. Cut square to the pipe's axis. Grind smooth and bevel the outside edge.

**How it fits the parts next to it.** The flange ring slides over the door end, the rear head butts against the far end, the nozzles pass through the holes, and the saddles' wear plates take it from below. All are welded (steps 1 to 5).

**Check before moving on.** Holes on the right side and the right line; each nozzle stub slides in.

### 3.2 Flange rings (make 2)

![Figure 3. Making sketch, flange rings](../cad/drawings/ALR-DWG-102.png)

*Figure 3. Flange rings (ALR-DWG-102).*

**What it is and what it is made from.** Two identical rings of 20 mm steel plate (S275 or A36), 960 mm outside, 813 mm inside. One goes on the shell's door end, one on the door head. The door seals between their faces.

**How to make it.**

1. Cut both rings by plasma or waterjet.
2. Mark the gasket face on each ring and keep it clean of spatter.
3. Check that each ring slides over the pipe end and over the door head's skirt with a close fit.

**How it fits the parts next to it.** The shell ring slides over the pipe until its gasket face is flush with the pipe end and is fillet welded on both sides (6 mm leg). The door ring goes over the door head's 40 mm skirt the same way. Weld in short runs at opposite points to keep the faces flat.

![Figure 26. Joint 1, door closed on the shell ring](05-build-plan/joint-01.png)

*Figure 26. Joint 1: the door ring against the gasket on the shell ring, with a latch over both rings.*

**Check before moving on.** After welding, each gasket face is flat to within 1 mm under a straight edge.

### 3.3 Window nozzle and flange

![Figure 4. Making sketch, window nozzle](../cad/drawings/ALR-DWG-103.png)

*Figure 4. Window nozzle and flange (ALR-DWG-103).*

**What it is and what it is made from.** A 160 mm stub of 273.1 mm pipe with a 12.7 mm wall (10 in XS) and a 20 mm steel ring, 400 mm outside and 255 mm inside.

**How to make it.**

1. Cut the stub 160 mm long, both ends square.
2. Cut the ring. Drill and tap eight M10 holes 25 mm deep on a 373 mm circle, the first 22.5° off the top.
3. Weld the ring onto one end of the stub, face square to the stub.

**How it fits the parts next to it.** The stub goes through the shell's window hole until the ring face is 520 mm from the vessel's axis; its inner end is then 360 mm from the axis and stands 16 to 40 mm proud of the inner wall. It is fillet welded to the shell outside and inside (8 mm leg). The window stack bolts to the ring (Figure 28).

**Check before moving on.** Ring face flat to 0.5 mm and square to the stub.

### 3.4 Feed-through nozzle and flange

![Figure 5. Making sketch, feed-through nozzle](../cad/drawings/ALR-DWG-104.png)

*Figure 5. Feed-through nozzle and flange (ALR-DWG-104).*

**What it is and what it is made from.** A 140 mm stub of 168.3 mm pipe with a 10.97 mm wall (6 in XS) and a 20 mm ring, 260 mm outside and 154 mm inside, with eight M10 tapped holes on a 225 mm circle.

**How to make it.** As the window nozzle: cut the stub square, cut and tap the ring, weld the ring on square.

**How it fits the parts next to it.** Set into the feed-through hole until the ring face is 500 mm from the axis; inner end 360 mm from the axis. Welded inside and out. The feed-through plate bolts to the ring (Figure 29).

**Check before moving on.** Ring face flat and square; the plate's holes line up with the tapped holes.

### 3.5 Manifold stub and flange

![Figure 6. Making sketch, manifold stub](../cad/drawings/ALR-DWG-105.png)

*Figure 6. Manifold stub and flange (ALR-DWG-105).*

**What it is and what it is made from.** A 105 mm stub of 60.3 mm pipe (2 in schedule 40) with a 150 mm disc of 12 mm plate on top, bored 52.5 mm and tapped for four M8 screws on a 110 mm circle.

**How to make it.** Cut the stub, cut and bore the disc, tap it, weld it to the stub flush with the bore.

**How it fits the parts next to it.** The stub goes into the top hole with the disc level, its top face 1,302 mm above the floor, and is fillet welded all round (5 mm leg). The valve manifold bolts on top (Figure 27).

**Check before moving on.** Disc level to within 1°.

### 3.6 Saddles (make 2)

![Figure 7. Making sketch, saddle](../cad/drawings/ALR-DWG-106.png)

*Figure 7. Saddle (ALR-DWG-106).*

**What it is and what it is made from.** A welded support of 10 mm plate: a 200 x 900 mm base plate, an 840 mm wide web 597 mm high with a curved top, and a 160 mm wear plate rolled to the shell's outside diameter over 120°. About 55 kg each.

**How to make it.**

1. Cut the base plate and drill two 18 mm holes 40 mm from each end.
2. Cut the web with an 833 mm curve in its top, the curve's centre 800 mm above the bottom of the base plate.
3. Roll the wear plate to 813 mm inside diameter.
4. Weld the web upright on the base's centre line, then the wear plate onto the web's curved top.

**How it fits the parts next to it.** The shell rests in the wear plates, which are welded to it along both edges (Figure 36). The base plates are bolted to the floor.

![Figure 36. Joint 10, saddle under the shell](05-build-plan/joint-10.png)

*Figure 36. Joint 10: the wear plate on the web's curved top, welded to the shell.*

**Check before moving on.** With both saddles on a level floor 950 mm apart, the shell's axis is level and 800 mm above the floor.

### 3.7 Deck rails (make 2)

![Figure 8. Making sketch, deck rail](../cad/drawings/ALR-DWG-107.png)

*Figure 8. Deck rail (ALR-DWG-107).*

**What it is and what it is made from.** Steel angle 50 x 50 x 6 mm, 900 mm long.

**How to make it.** Cut to length. Drill three 9 mm holes in one leg, 19 mm from its outer edge, at 50, 450 and 850 mm from the door end. Scribe the other leg to the inside of the shell and grind to a close fit.

**How it fits the parts next to it.** Inside the shell, the drilled leg is the top, flat and pointing out toward the wall, 522 mm above the floor; the hanging leg sits on the wall, 150 mm out from the centre line, so the rails are 300 mm apart. They start 80 mm from the shell ring face and are fillet welded along the hanging leg (Figure 32). The deck bolts on top.

![Figure 32. Joint 6, deck on its rails](05-build-plan/joint-06.png)

*Figure 32. Joint 6: the rails welded inside the shell and the deck bolted to their top legs.*

**Check before moving on.** Both top legs level with each other to within 1 mm.

### 3.8 Baffle tabs (make 4)

![Figure 9. Making sketch, baffle tabs](../cad/drawings/ALR-DWG-108.png)

*Figure 9. Baffle tabs (ALR-DWG-108).*

**What it is and what it is made from.** Four pieces of 40 x 10 mm steel flat, 45 mm long, each with one 9 mm hole 18 mm from its inner end.

**How to make it.** Cut, drill and scribe the outer end of each to the shell's curve.

**How it fits the parts next to it.** Welded inside the shell 1,100 mm from the shell ring face, standing toward the axis, at 45°, 135°, 225° and 315° from the top. The baffle bolts to their door-side faces (Figure 35).

**Check before moving on.** The four bolt faces lie in one plane to within 2 mm.

### 3.9 Hinge lugs and pin

![Figure 10. Making sketch, hinge](../cad/drawings/ALR-DWG-109.png)

*Figure 10. Hinge lugs and pin (ALR-DWG-109).*

**What it is and what it is made from.** Four lugs of 15 mm steel plate, each with a 21 mm hole, and a 20 mm steel pin 450 mm long with a head and a collar.

**How to make it.**

1. Cut the four lugs and drill the holes. Slot the two door lugs' holes 3 mm toward the vessel's axis.
2. Weld two lugs to the shell ring's far edge, 395 mm apart vertically, the upper one 190 mm above the axis.
3. Weld two lugs to the door ring's far edge, each 2 mm above a shell-ring lug.
4. Set all four holes on one vertical line with a rod before the welds cool.

**How it fits the parts next to it.** The pin drops through all four lugs from above; the hole centres are 16 mm in front of the shell ring face and 515 mm out from the axis (Figure 30).

![Figure 30. Joint 5, door hinge](05-build-plan/joint-05.png)

*Figure 30. Joint 5: the lugs on both rings and the pin.*

**Check before moving on.** The door swings freely and closes square on the gasket.

### 3.10 Door

![Figure 11. Making sketch, door](../cad/drawings/ALR-DWG-110.png)

*Figure 11. Door: the second head welded into the second flange ring (ALR-DWG-110).*

**What it is and what it is made from.** A bought 2:1 ellipsoidal tank head, 813 mm outside diameter, 6.35 mm, with a 40 mm straight skirt, welded into the second flange ring, with the two door lugs. About 72 kg.

**How to make it.**

1. Set the ring over the head's skirt with its gasket face flush with the skirt's open end.
2. Fillet weld both sides in short balanced runs.
3. Grind the gasket face smooth where the welds meet it.

**How it fits the parts next to it.** The door hangs on the hinge and closes onto the gasket on the shell ring; three latches hold it for the first seal (Figure 26).

**Check before moving on.** Gasket face flat; no weld proud of it. Lift the door only with a hoist or two people.

### 3.11 Window

![Figure 12. Making sketch, window](../cad/drawings/ALR-DWG-111.png)

*Figure 12. Window (ALR-DWG-111).*

**What it is and what it is made from.** A 340 mm disc of clear polycarbonate sheet, 20 mm thick. Never acrylic or glass: they shatter.

**How to make it.** Cut the disc, sand the edge smooth and break it with a 1 mm chamfer. No holes. Leave the protective film on until fitted. Clean only with water and mild soap; solvents craze polycarbonate.

**How it fits the parts next to it.** It sits on a 6 mm EPDM ring gasket on the window flange and is held at its rim by the clamp ring (Figure 28). Under vacuum the air presses it onto the gasket.

![Figure 28. Joint 3, window stack](05-build-plan/joint-03.png)

*Figure 28. Joint 3: flange, gasket, window, spacer ring and clamp ring, cut through the window's centre.*

**Check before moving on.** No scratch deep enough to catch a fingernail.

### 3.12 Window spacer and clamp rings

![Figure 13. Making sketch, window rings](../cad/drawings/ALR-DWG-112.png)

*Figure 13. Window spacer and clamp rings (ALR-DWG-112).*

**What it is and what it is made from.** A spacer ring of 25 mm plate, 400 mm outside and 346 mm inside, and a clamp ring of 10 mm plate, 400 mm outside and 290 mm inside.

**How to make it.** Cut both rings. Clamp them together and drill eight 11 mm holes on a 373 mm circle, the first 22.5° off the top, to match the flange. Deburr and paint, except the clamp ring's face that touches the window.

**How it fits the parts next to it.** The spacer sits on the flange outside the gasket and the window. It is as thick as the gasket squeezed to 5 mm plus the window, so tightening the clamp ring squeezes the gasket by 1 mm and no more. The clamp ring overlaps the window's rim by 25 mm.

**Check before moving on.** The rings sit flat together and the holes line up with the flange.

### 3.13 Feed-through plate

![Figure 14. Making sketch, feed-through plate](../cad/drawings/ALR-DWG-113.png)

*Figure 14. Feed-through plate (ALR-DWG-113).*

**What it is and what it is made from.** A 260 mm disc of 15 mm aluminium plate with five M20 IP68 cable glands.

**How to make it.**

1. Cut the disc and drill eight 11 mm holes on a 225 mm circle.
2. Drill five 20 mm holes: one at the centre and four on a 70 x 60 mm rectangle around it.
3. Fit the glands with their O-rings on the inside face. Run the three motor phase wires (6 mm2) through one gland and the signal and sensor cables through the others; blank any spare gland.
4. Pot each cable in epoxy for 50 mm inside its gland so air cannot leak along the strands.

**How it fits the parts next to it.** It bolts to the feed-through flange with eight M10 bolts on a 2 mm EPDM gasket (Figure 29).

![Figure 29. Joint 4, feed-through](05-build-plan/joint-04.png)

*Figure 29. Joint 4: the plate on its gasket and flange, cut through the centre.*

**Check before moving on.** Glands tight; potting fully cured.

### 3.14 Deck plate

![Figure 15. Making sketch, deck](../cad/drawings/ALR-DWG-114.png)

*Figure 15. Deck plate (ALR-DWG-114).*

**What it is and what it is made from.** Aluminium plate 8 mm thick, 900 x 400 mm.

**How to make it.** Drill six 9 mm holes 169 mm each side of the centre line at 50, 450 and 850 mm from the door-end edge, to match the rails. Drill and tap four M8 holes for the stand base at 140 and 400 mm from the door-end edge, 80 mm each side of the centre line.

**How it fits the parts next to it.** It slides in through the door onto the rails' top legs and is bolted down with six M8 bolts and nuts (Figure 32).

**Check before moving on.** The deck sits flat on both rails.

### 3.15 Baffle plate

![Figure 16. Making sketch, baffle](../cad/drawings/ALR-DWG-115.png)

*Figure 16. Baffle plate (ALR-DWG-115).*

**What it is and what it is made from.** A 790 mm disc of 2 mm perforated steel with 10 mm round holes on a 12 mm staggered pitch (63 % open).

**How to make it.** Cut the disc and file any half holes at the rim smooth. Drill four 9 mm holes at 45°, 135°, 225° and 315° on a 764 mm circle to match the tabs.

**How it fits the parts next to it.** It bolts to the four tabs with M8 bolts, 590 mm downstream of the propeller, with a 5 mm gap to the wall (Figure 35). It is taken out for the comparison runs without it.

![Figure 35. Joint 7, baffle on its tabs](05-build-plan/joint-07.png)

*Figure 35. Joint 7: the baffle bolted to a tab welded inside the shell.*

**Check before moving on.** The gap to the wall is even all round.

### 3.16 Stand base plate

![Figure 17. Making sketch, stand base](../cad/drawings/ALR-DWG-116.png)

*Figure 17. Stand base plate (ALR-DWG-116).*

**What it is and what it is made from.** Aluminium plate 12 mm thick, 300 x 200 mm.

**How to make it.** Drill four 9 mm holes 20 mm in from each corner, counterbored for the M8 screws into the deck. Tap M5 holes for the two lower flexure clamps (centres 50 mm and 250 mm from the door-end edge), the anchor block and the speed sensor post. Face the top flat.

**How it fits the parts next to it.** It is screwed to the deck; the lower clamps, the anchor block and the speed post screw onto it (Figure 33).

**Check before moving on.** Flat to 0.1 mm across the clamp positions.

### 3.17 Flexure leaves and clamps

![Figure 18. Making sketch, flexures](../cad/drawings/ALR-DWG-117.png)

*Figure 18. Flexure leaves and clamps (ALR-DWG-117).*

**What it is and what it is made from.** Two leaves 120 x 110 mm cut from 0.5 mm hardened spring steel shim, and four aluminium clamp blocks 30 x 140 x 20 mm.

**How to make it.**

1. Cut the leaves with snips or a guillotine. Do not bend or kink them.
2. Slit each clamp block along its middle so a leaf is gripped between the two halves; drill for two M5 screws.

**How it fits the parts next to it.** The two lower clamps screw to the base plate 200 mm apart; the two upper clamps screw to the underside of the carriage. Each leaf is gripped 15 mm deep at top and bottom, with 80 mm free between the clamps, so the leaves stand parallel and the carriage can move a fraction of a millimetre along the axis (Figure 33). Set the height with an 80 mm spacer block between the clamps while tightening.

![Figure 33. Joint 8, flexure stand and thrust cell](05-build-plan/joint-08.png)

*Figure 33. Joint 8: the leaves in their clamps between the base plate and the carriage, and the thrust cell between the anchor and the hanger, cut along the axis.*

**Check before moving on.** The carriage moves freely along the axis and springs back to the same place.

### 3.18 Thrust cell anchor block and hanger

![Figure 19. Making sketch, anchor and hanger](../cad/drawings/ALR-DWG-118.png)

*Figure 19. Anchor block and hanger (ALR-DWG-118).*

**What it is and what it is made from.** Two blocks of aluminium bar: the anchor 30 x 40 x 58 mm and the hanger 27 x 40 x 62 mm.

**How to make it.** Drill and tap each for two M5 screws to its plate (the anchor down into the base plate, the hanger up into the carriage) and two M5 screws to the load cell.

**How it fits the parts next to it.** The 10 kg bar load cell stands upright between them: its lower end is screwed to the anchor's face and its upper end to the hanger's face. The propeller's thrust pushes the carriage, which pushes the top of the cell (Figure 33).

**Check before moving on.** The cell hangs plumb and touches nothing between its two ends.

### 3.19 Carriage plate

![Figure 20. Making sketch, carriage](../cad/drawings/ALR-DWG-119.png)

*Figure 20. Carriage plate (ALR-DWG-119).*

**What it is and what it is made from.** Aluminium plate 10 mm thick, 240 x 160 mm.

**How to make it.** Drill for the two upper clamps (M5 clearance), the hanger (two M5) and the torque head housing (four M6).

**How it fits the parts next to it.** It hangs on the two leaves through the upper clamps and carries the torque head.

**Check before moving on.** Flat; no screw head proud on its underside near the cell.

### 3.20 Torque head

![Figure 21. Making sketch, torque head](../cad/drawings/ALR-DWG-120.png)

*Figure 21. Torque head: housing, bearings, shaft and motor plate (ALR-DWG-120).*

**What it is and what it is made from.** An aluminium housing 50 x 90 x 178 mm, two 6202 sealed bearings, a 15 mm stainless steel shaft 115 mm long with a 40 mm hub, and an 80 mm aluminium motor plate 6 mm thick.

**How to make it.**

1. Bore the housing 35 mm (a light press fit for the bearings) right through, the bore's centre 128 mm above its base. Tap four M6 holes in its base.
2. Press a bearing into each end of the bore.
3. Turn the shaft with its hub at the motor end; tap the hub for the motor plate.
4. Drill the motor plate for the motor's own pattern (16, 19, 25 or 30 mm circles) and screw it to the hub.

**How it fits the parts next to it.** The housing screws to the carriage with the shaft on the vessel's axis, 800 mm above the floor. The motor screws to the motor plate. The torque arm clamps to the shaft's other end (Figure 34).

**Check before moving on.** The shaft turns freely by hand with no end play.

### 3.21 Torque arm and cell bracket

![Figure 22. Making sketch, torque arm](../cad/drawings/ALR-DWG-121.png)

*Figure 22. Torque arm and cell bracket (ALR-DWG-121).*

**What it is and what it is made from.** An aluminium arm 10 mm thick with a 30 mm hub bored 15 mm and slit, reaching 60 mm from the axis; and an aluminium bracket 40 x 21 x 33 mm.

**How to make it.** Bore and slit the arm's hub and drill it for one M4 clamp screw. Drill the bracket for two M5 screws into the housing's side and two M5 screws for the cell. Press a 3 mm steel ball into a dimple under the arm's tip.

**How it fits the parts next to it.** The bracket screws to the housing's side. The 5 kg bar load cell lies along the axis with its fixed end screwed down on the bracket and its free end under the arm's tip. The arm, clamped to the shaft, rests on the cell through the ball, so the motor's reaction torque presses on the cell (Figure 34).

![Figure 34. Joint 9, torque head](05-build-plan/joint-09.png)

*Figure 34. Joint 9: shaft on two bearings in the housing, the arm on the shaft resting on the torque cell, the cell on its bracket.*

**Check before moving on.** The arm rests on the cell with the shaft still free to turn.

### 3.22 Speed sensor post

![Figure 23. Making sketch, speed sensor post](../cad/drawings/ALR-DWG-122.png)

*Figure 23. Speed sensor post (ALR-DWG-122).*

**What it is and what it is made from.** A 16 x 20 mm aluminium bar 128 mm long with a block on top for the optical sensor.

**How to make it.** Cut, drill and tap two M5 holes in the foot; screw the sensor to the top block.

**How it fits the parts next to it.** It screws to the base plate so the sensor faces the propeller, 15 mm from its plane and 140 mm below the axis. A 10 mm square of reflective tape on one blade gives one pulse a turn.

**Check before moving on.** Turning the propeller by hand gives one pulse a turn.

### 3.23 Bought components

- **Dished heads (2):** 2:1 semi-ellipsoidal carbon steel tank heads, 813 mm outside diameter, 6.35 mm, 40 mm straight skirt. One is welded to the rear of the shell; one becomes the door.
- **Gaskets:** closed-cell EPDM sponge strip 6 x 45 mm, about 2.8 m, glued to the shell ring's face with contact adhesive, joined with a scarf cut at the bottom; solid EPDM sheet 6 mm and 2 mm cut to rings for the window and the feed-through.
- **Latch clamps (3):** adjustable latch clamps holding at least 3 kN, bolted to the back of the shell ring at the top, the window side and the bottom.
- **Valve manifold:** an adjustable vacuum relief valve set to open at 55 kPa below atmosphere; a 63 mm vacuum gauge; a normally-open solenoid bleed valve with a needle valve; a 1/2 in manual vent valve; a 1 in isolation ball valve and pump port. Assembled on one block with thread sealant and bolted to the stub flange with four M8 screws and a 2 mm gasket (Figure 27).
- **Load cells:** bending-beam bar cells 12.7 x 12.7 x 80 mm, C3 class or better: 10 kg for thrust, 5 kg for torque, with two 24-bit amplifiers.
- **Air sensors:** two barometric sensors accurate to 50 Pa absolute, one humidity sensor and two class A platinum probes, in a vented printed box on the deck.
- **Vacuum pump and hose:** single-stage rotary vane pump, 170 L/min, with an oil-mist filter; 25 mm bore wire-reinforced hose.
- **Control cabinet:** floor-standing steel enclosure with a 30 mA residual current device on the mains inlet, the 1,500 W motor supply, the speed controller and power sensor, the controller and logger, the emergency stop and contactors, the door interlock switch (on the top latch) and the arming key switch.
- **Motor and propeller under test:** an example 6S motor for 15 in propellers and a 15 x 5 in carbon propeller; users bring their own.

![Figure 27. Joint 2, rear head and manifold stub](05-build-plan/joint-02.png)

*Figure 27. Joint 2: the rear head's skirt butt welded to the pipe end, and the manifold stub with the manifold on top.*

## 4. Putting it together

Steps 1 to 6 are welding shop work; steps 7 to 20 are done in the lab. Fitted parts are grey; the part being fitted is in colour with an arrow showing the way it goes in.

### Step 1: flange ring onto the shell end

![Step 1](05-build-plan/step-01.png)

Slide the shell ring over the door end until its gasket face is flush with the pipe end. Fillet weld both sides, 6 mm leg, in short balanced runs. **Hold point:** check the face is flat to 1 mm before going on.

### Step 2: rear head

![Step 2](05-build-plan/step-02.png)

Butt the rear head's skirt against the far end of the pipe with a 2 to 3 mm root gap, tack at four points, then weld all round with full penetration. Grind the inside flush. **Hold point:** the weld is continuous all round; a broken weld here halves the shell's strength (ALR-CAL-001, section B).

### Step 3: nozzles into the shell

![Step 3](05-build-plan/step-03.png)

Set the window and feed-through nozzles into their holes on the window side with their flanges 520 mm and 500 mm from the axis, and the manifold stub on the top line. Weld each stub outside and inside.

### Step 4: saddles

![Step 4](05-build-plan/step-04.png)

Stand the saddles on a level floor 950 mm apart (centres 300 mm and 1,250 mm from the shell ring face). Lower the shell onto the wear plates with the window side toward the operator's side of the room, and weld the wear plates to the shell along both edges.

### Step 5: deck rails and baffle tabs inside

![Step 5](05-build-plan/step-05.png)

Shown with the window half of the vessel cut away. Weld the two rails inside, top legs 522 mm above the floor and 300 mm apart, and the four tabs 1,100 mm from the shell ring face. Grind away spatter inside.

### Step 6: door, ring and lugs onto the second head

![Step 6](05-build-plan/step-06.png)

Weld the door ring onto the second head's skirt, face flush with the skirt end, and the two door lugs to its far edge.

### Step 7: hang the door

![Step 7](05-build-plan/step-07.png)

With the shell ring's lugs already welded, lift the 72 kg door with a hoist, line up its lugs just above the fixed lugs and drop the pin in from above. Fit the collar.

### Step 8: door gasket and latches

![Step 8](05-build-plan/step-08.png)

With the door swung open, glue the sponge strip to the shell ring's face with contact adhesive, joint at the bottom. Bolt the three latch clamps to the back of the shell ring. Fit the door interlock switch to the top latch.

### Step 9: window

![Step 9](05-build-plan/step-09.png)

Lay the window gasket on the flange, then the window (film removed), the spacer ring and the clamp ring. Tighten the eight M10 bolts evenly in a star pattern, hand tight plus a quarter turn. Do not over-tighten: the spacer sets the squeeze.

### Step 10: feed-through plate

![Step 10](05-build-plan/step-10.png)

With the cables already potted in the glands, fit the gasket and the plate with eight M10 bolts in a star pattern.

### Step 11: valve manifold on the stub

![Step 11](05-build-plan/step-11.png)

Bolt the assembled manifold to the stub flange with its gasket and four M8 screws, the gauge facing the window side.

### Step 12: baffle plate

![Step 12](05-build-plan/step-12.png)

Carry the baffle in through the door, tilted, and bolt it to the four tabs.

### Step 13: deck plate

![Step 13](05-build-plan/step-13.png)

Slide the deck in through the door onto the rails and bolt it down with six M8 bolts and nuts.

### Step 14: stand base and flexures

![Step 14](05-build-plan/step-14.png)

The vessel is not shown from here on. Screw the base plate to the deck. Screw the two lower clamps to it with the leaves gripped in them; fit the upper clamps on the leaves loosely.

### Step 15: thrust cell and carriage

![Step 15](05-build-plan/step-15.png)

Screw the anchor block to the base, the thrust cell upright onto the anchor, and the hanger onto the top of the cell. Lower the carriage onto the upper clamps and the hanger and screw it down, with the 80 mm spacer between the clamps; then tighten all clamps and remove the spacer.

### Step 16: torque head

![Step 16](05-build-plan/step-16.png)

Screw the housing, with its bearings in, to the carriage with four M6 screws. Slide the shaft in from the motor side and screw the motor plate to its hub.

### Step 17: torque cell and arm

![Step 17](05-build-plan/step-17.png)

Screw the bracket to the housing's side and the torque cell onto the bracket. Clamp the arm on the shaft so its ball rests on the cell's free end.

### Step 18: speed sensor and air sensors

![Step 18](05-build-plan/step-18.png)

Screw the speed post to the base plate. Place the air sensor box on the deck and run all cables along the deck to the feed-through, tied down so they cannot reach the propeller. Leave a loose loop in the motor and cell cables where they cross from the deck to the carriage.

### Step 19: motor and propeller under test

![Step 19](05-build-plan/step-19.png)

Screw the motor to the motor plate with its own screws and thread-locker. Fit the propeller with the reflective tape on one blade. Connect the three motor phases at the feed-through.

### Step 20: pump, hose and control cabinet

![Step 20](05-build-plan/step-20.png)

Stand the pump on the floor on the far side and lead its exhaust outdoors or to an extract. Connect the hose from the manifold to the pump. Stand the control cabinet in front of the door end on the window side, earth the vessel to the cabinet's earth bar, and wire the pump, bleed valve, motor supply, sensors and interlocks.

## 5. First checks

These are listed here and recorded in a TRL 4 test report; none has been done.

*Table 2. First checks.*

| Check | Requirement | How | Pass when |
| --- | --- | --- | --- |
| Door seats and latches | R11 | Close and latch; look for even gasket squeeze | Gasket squeezed evenly all round; interlock switch reads closed only when latched |
| Interlocks | R11 | Try to arm the motor with the door unlatched, without the key, and with the emergency stop pressed | The motor supply stays off in every case; the emergency stop also stops the pump and opens the bleed valve |
| Relief valve | R12 | Pump down with the motor off, watching the gauge | Relief valve opens at 55 kPa below atmosphere (46.3 kPa absolute), within 2 kPa |
| Proof pump-down | R7 | Behind the guard, pump to the relief setting and hold 10 min; inspect welds, window and door | No movement, cracking, crazing or noise; pressure rise under 0.3 kPa/min with the pump isolated |
| Pump-down time | R8 | Time from ambient to 54 kPa | 5 min or less |
| Density hold | R1, R2 | Hold 0.736 kg/m3 for 10 min with the motor off, then with it running | Within 1 % of set point |
| Thrust and torque calibration | R3, R4 | Masses over the pulley along the axis; masses on the calibration arm | Errors within 1 % of 50 N and 2 % of 2 N m, before and after a test series |
| Speed | R4 | Optical sensor against a handheld tachometer | Within 0.5 % |
| Fit of the largest propeller | R5 | Turn a 380 mm propeller by hand | Clears the wall, the deck and the speed sensor |
| Chamber effect | R6 | Same propeller at the same speeds at ambient pressure in the chamber and on an open-air stand, with and without the baffle | Within 5 % (see the design decisions register) |
| Data | R9 | Inspect a logged file | CSV with density, thrust, torque, speed, voltage and current at 10 Hz or more |

## 6. Safety stops

Work stops at each point below until everything listed is true.

1. **Before the first pump-down.** A qualified engineer has reviewed the vessel calculation (ALR-CAL-001, section B) and the welds; the rear head and both flange rings are welded continuously all round; the window is polycarbonate; the relief valve has been set on a separate test and is fitted.
2. **Before every pump-down.** The guard is in place in front of the window; nobody stands in line with the window or the door; the door is latched and the gasket is clean; the gauge reads zero; the pump exhaust is led away.
3. **Before arming the motor.** The propeller is tight and undamaged; no tools, cables or loose parts are inside; the door is latched and the interlock reads closed; the arming key is turned by the operator, who keeps it; everyone is outside the line of the propeller plane. The motor is only run with the chamber closed.
4. **Before opening the door.** The motor is disarmed and stopped; the chamber is vented through the bleed or vent valve until the gauge reads zero. Never force the door: under vacuum it is held by tonnes of force.
5. **Batteries.** No battery pack goes inside the chamber.
6. **After any overpressure, crack, crazing or impact.** Stop, vent, and do not pump down again until the part is inspected and replaced if needed.

## 7. Tools, skills and workspace

- **Welding shop:** a qualified welder for the vessel welds (full-penetration butt weld of the rear head, fillet welds on rings, nozzles, saddles, rails, tabs and lugs); plasma or waterjet cutting of plate; a plate roll for the wear plates; a hoist for the shell and the door.
- **Machine shop:** a lathe for the shaft and a mill or boring head for the housing bore; drilling and tapping to M10.
- **Lab:** a level floor with room for the 2 m vessel and the door to swing open, a mains supply with an RCD, an extract or outdoor vent for the pump exhaust, hearing protection and safety glasses, a guard (for example a 6 mm polycarbonate sheet on a frame) for proof tests.
- **Skills:** basic electrical wiring of a control cabinet by a competent person; load cell wiring and calibration.

## 8. Where the numbers come from

- `cad/src/model.py`: the parametric model and every dimension (STEP in `cad/step/`).
- `cad/drawings/ALR-DWG-001`: general arrangement; `cad/drawings/ALR-DWG-101` to `ALR-DWG-122`: making sketches.
- `cad/src/build_plan_media.py`: the pictures in this plan.
- `docs/04-calcs/01-sizing.md` and `docs/04-calcs/sizing.py` (ALR-CAL-001): strength, pump-down, density, stand and chamber effect.
- `bom/bom.csv`: parts, specifications and prices.
- `docs/decisions/0002-design-for-construction.md` (ALR-DDR-002): the changes made for construction.
