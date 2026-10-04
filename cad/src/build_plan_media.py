"""AltiRig prototype build plan pictures (ALR-BLD-001, STANDARDS section 18).

Run from the repo root (one group per process keeps memory low):
    python cad/src/build_plan_media.py overview
    python cad/src/build_plan_media.py sheets [101 102 ...]
    python cad/src/build_plan_media.py joints [1 2 ...]
    python cad/src/build_plan_media.py steps [1 2 ...]
Every picture is drawn from cad/src/model.py (components()), so the pictures and the model agree:
    docs/05-build-plan/overview.png        every component pulled apart, numbered in build order
    cad/drawings/ALR-DWG-101 to 122        making sketches for the made components
    docs/05-build-plan/joint-NN.png        close-ups of the joints that need explaining
    docs/05-build-plan/step-NN.png         one picture per assembly step
Uses .kit/build_views.py. BUILD PLAN ILLUSTRATION, PLAN NOT YET BUILT.
"""
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / ".kit"), str(ROOT / "cad" / "src")]
import build_views as bv  # noqa: E402
from build_views import Part  # noqa: E402
from build123d import Compound, Pos, Rot  # noqa: E402
import model as m  # noqa: E402
from model import PARAMS as P, box, levels  # noqa: E402

OUT = ROOT / "docs" / "05-build-plan"
DATE = "2026-10-03"
L = levels(P)
Z = P["Z_AX"]
_C = None

COL = {"shell": "#4B6584", "shell_ring": "#3B4F6B", "rear_head": "#5B7594", "win_nozzle": "#334155",
       "ft_nozzle": "#334155", "man_stub": "#334155", "saddle1": "#374151", "saddle2": "#374151",
       "rail_p": "#6B7280", "rail_n": "#6B7280", "tabs": "#B45309", "hinge_fixed": "#1F2937",
       "door_ring": "#3B4F6B", "door_head": "#5B7594", "door_lugs": "#1F2937", "pin": "#DC2626",
       "gasket": "#111827", "latches": "#B45309", "win_gasket": "#111827", "window": "#60A5FA",
       "win_spacer": "#475569", "win_clamp": "#0F766E", "ft_gasket": "#111827", "ft_plate": "#94A3B8",
       "deck": "#CBD5E1", "baffle": "#94A3B8", "stand_base": "#0F766E", "leaves": "#D4A017",
       "clamps": "#115E59", "carriage": "#14B8A6", "anchor": "#115E59", "thrust_cell": "#2563EB",
       "hanger": "#7C3AED", "housing": "#0D9488", "bearings": "#6B7280", "shaft": "#9CA3AF", "mplate": "#64748B",
       "arm": "#EA580C", "torque_cell": "#2563EB", "tc_bracket": "#115E59", "speed_post": "#7C3AED",
       "motor": "#111827", "prop": "#1F2937", "sensors": "#F59E0B", "manifold": "#B91C1C", "pump": "#DC2626",
       "hose": "#111827", "cabinet": "#E5E7EB"}


def comps():
    global _C
    if _C is None:
        _C = m.by_key()
    return _C


def K(key, name=None, color=None, explode=None, shape=None):
    c = comps()[key]
    return Part(name or c.name, shape if shape is not None else c.shape, color or COL[key], c.bom,
                tuple(explode) if explode is not None else c.explode)


def W(key, bx, name=None, color=None):
    """The part of a component inside a box (close-ups and cut-open views)."""
    s = comps()[key].shape & box(*bx)
    return K(key, name, color, (0, 0, 0), s)


def fuse(*keys):
    return Compound([comps()[k].shape for k in keys])


def at_origin(shape):
    bb = shape.bounding_box()
    return Pos(-bb.center().X, -bb.center().Y, -bb.min.Z) * shape


# ------------------------------------------------------------------ overview
BUILD_ORDER = ["shell", "shell_ring", "rear_head", "win_nozzle", "ft_nozzle", "man_stub", "saddle1", "saddle2",
               "rail_p", "rail_n", "tabs", "hinge_fixed", "door_ring", "door_head", "door_lugs", "pin", "gasket",
               "latches", "win_gasket", "window", "win_spacer", "win_clamp", "ft_gasket", "ft_plate", "manifold",
               "baffle", "deck", "stand_base", "clamps", "leaves", "anchor", "thrust_cell", "hanger", "carriage",
               "housing", "bearings", "shaft", "mplate", "arm", "tc_bracket", "torque_cell", "speed_post", "sensors",
               "motor", "prop", "pump", "hose", "cabinet"]

OV_EXPLODE = {  # pulled-apart positions for the overview, mm
    "shell": (0, 0, 0), "shell_ring": (-600, 0, 0), "rear_head": (700, 0, 0), "win_nozzle": (0, -700, 0),
    "ft_nozzle": (0, -700, 0), "man_stub": (0, 0, 500), "saddle1": (0, 0, -500), "saddle2": (0, 0, -500),
    "rail_p": (0, 1300, -250), "rail_n": (0, 1000, -250), "tabs": (600, 1300, 0), "hinge_fixed": (-600, 500, 0),
    "door_ring": (-1250, 0, 0), "door_head": (-1500, 0, 0), "door_lugs": (-1250, 500, 0), "pin": (-900, 800, -350),
    "gasket": (-900, 0, 0), "latches": (-950, -200, 0), "win_gasket": (0, -900, 0), "window": (0, -1150, 0),
    "win_spacer": (0, -1400, 0), "win_clamp": (0, -1650, 0), "ft_gasket": (0, -900, 0), "ft_plate": (0, -1050, 0),
    "manifold": (0, 0, 800), "baffle": (1200, 1300, 0), "deck": (0, 1300, 50),
    "stand_base": (0, 1300, 250), "clamps": (0, 1300, 380), "leaves": (0, 1300, 480), "anchor": (0, 1300, 330),
    "thrust_cell": (0, 1300, 600), "hanger": (0, 1300, 700), "carriage": (0, 1300, 800), "housing": (0, 1300, 900),
    "bearings": (-150, 1300, 1000), "shaft": (-150, 1300, 1080), "mplate": (150, 1300, 1080), "arm": (-300, 1300, 1150),
    "tc_bracket": (0, 1450, 1000), "torque_cell": (-300, 1450, 1150), "speed_post": (150, 1300, 900),
    "sensors": (0, 1300, 300), "motor": (400, 1300, 1080), "prop": (650, 1300, 1080), "pump": (500, 600, 0),
    "hose": (500, 600, 0), "cabinet": (-500, -300, 0)}


ROW1 = ["stand_base", "clamps", "leaves", "anchor", "thrust_cell", "hanger", "carriage", "housing", "bearings"]
ROW2 = ["shaft", "mplate", "arm", "tc_bracket", "torque_cell", "speed_post", "sensors", "motor", "prop"]


def overview():
    ex = dict(OV_EXPLODE)
    ex["deck"] = (-150, -200, 1250)
    for row, zt in ((ROW1, 2050.0), (ROW2, 2550.0)):
        for i, k in enumerate(row):
            c = comps()[k].shape.bounding_box().center()
            ex[k] = (-300 + 280 * i - c.X, -200 - c.Y, zt - c.Z)
    parts = [K(k, explode=ex[k]) for k in BUILD_ORDER]
    return bv.overview(parts, OUT / "overview.png", "AltiRig prototype: every component, pulled apart",
                       subtitle="Numbered in build order: vessel 1 to 18, window and feed-through 19 to 24, fittings and "
                                "inside 25 to 27, stand 28 to 43, test article 44 and 45, pump and cabinet 46 to 48",
                       size=(12, 8), key=True, elev=22, azim=-55)


# ------------------------------------------------------------------ making sketches
def sheet(n, key, title, material, notes, neighbours=(), view_shape=None, inset=(24, -58), name=None, shape=None,
          rev="P1", revisions=None):
    c = comps()[key]
    part = Part(name or c.name, shape if shape is not None else c.shape, COL[key], c.bom)
    nb = [comps()[k] if isinstance(k, str) else k for k in neighbours]
    nbp = [Part(x.name, x.shape, "#D1D5DB") if hasattr(x, "key") else x for x in nb]
    return bv.component_sheet(part, nbp, project="AltiRig", dwg_no=f"ALR-DWG-{n}", title=title, material=material,
                              notes=notes, date=DATE, view_shape=view_shape, inset_view=inset, rev=rev,
                              revisions=revisions)


def sheets(which=None):
    ro = L["ro"]
    S = {}
    S[101] = lambda: sheet(101, "shell", "AltiRig shell: pipe offcut with nozzle holes",
                           "Steel pipe 813 OD x 6.35 wall (32 in x 1/4 in), 1,500 long", [
        "Surplus offcut: before buying, check it is round within 8 mm (largest",
        "  less smallest diameter) and the wall is 5.9 or more at 8 points",
        "  round each end; reject a dented or pitted pipe",
        "Cut the pipe 1,500 long, ends square within 1 mm",
        f"Mark a line along the top; hole centres measured from the door end:",
        f"  window hole 273.1 dia at {P['WIN_X']:.0f}, on the side 90 deg from the top",
        f"  feed-through hole 168.3 dia at {P['FT_X']:.0f}, same side as the window",
        f"  manifold hole 60.3 dia at {P['MN_X']:.0f}, on the top line",
        "Cut each hole to the nozzle's outside size plus 1 to 2 mm, square to",
        "  the axis; grind smooth; bevel the outside edge for the fillet weld",
        "Saddles, rails, tabs, ring and head are welded on (assembly steps 1 to 5)",
        "Check: holes on the right side and line; nozzle stubs slide in",
    ], ["shell_ring", "rear_head", "saddle1", "saddle2"], rev="P2",
        revisions=[("P1", "Making sketch", DATE, "AC"),
                   ("P2", "Surplus pipe checks before buying (decision 42B)", DATE, "AC")])
    S[102] = lambda: sheet(102, "shell_ring", "AltiRig flange rings: shell end and door (make 2)",
                           "Steel plate 20 thick (S275 or A36)", [
        "Cut two rings 960 OD x 813 ID from 20 mm plate (plasma or waterjet)",
        "The ring is a close fit over the pipe and the door head's skirt",
        "Mark the face that will touch the gasket on each ring and keep it",
        "  clean of spatter; weld only on the back face and in the bore",
        "Shell ring: slide on until its gasket face is flush with the pipe end;",
        "  fillet weld all round on both sides of the ring (6 mm leg)",
        "Door ring: fits over the door head's 40 mm skirt, face flush with",
        "  the skirt's end; fillet weld all round on both sides",
        "Weld in short runs at opposite points to keep the faces flat",
        "Check: each gasket face flat within 1 mm on a straight edge",
    ], ["shell"], inset=(20, -40))
    S[103] = lambda: sheet(103, "win_nozzle", "AltiRig window nozzle and flange",
                           "Pipe 273.1 x 12.7 (10 in XS) and 20 mm steel plate", [
        "Stub: cut 160 long from 10 in XS pipe, both ends square",
        "Ring: 400 OD x 255 ID from 20 mm plate; drill and tap 8 x M10",
        "  on a 373 circle, 25 deep, first hole 22.5 deg off the top",
        "Weld the ring on one stub end, face square to the stub",
        "Set the stub into the shell's window hole so the ring face is 520",
        "  from the vessel axis and the stub ends 360 from the axis inside",
        "  (it stands 16 to 40 mm proud of the inner wall)",
        "Fillet weld the stub to the shell outside and inside, 8 mm leg",
        "Check: ring face flat within 0.5 mm and square to the stub",
    ], ["shell"], inset=(20, -70))
    S[104] = lambda: sheet(104, "ft_nozzle", "AltiRig feed-through nozzle and flange",
                           "Pipe 168.3 x 10.97 (6 in XS) and 20 mm steel plate", [
        "Stub: cut 140 long from 6 in XS pipe, both ends square",
        "Ring: 260 OD x 154 ID from 20 mm plate; drill and tap 8 x M10",
        "  on a 225 circle, 25 deep",
        "Weld the ring on one stub end, face square to the stub",
        f"Set the stub into the shell's feed-through hole ({P['FT_X']:.0f} from the",
        "  door end) so the ring face is 500 from the axis; inner end 360",
        "Fillet weld the stub to the shell outside and inside, 8 mm leg",
        "Check: ring face flat and square; the plate's holes line up",
    ], ["shell"], inset=(20, -70))
    S[105] = lambda: sheet(105, "man_stub", "AltiRig manifold stub and flange",
                           "Pipe 60.3 x 3.91 (2 in sch 40) and 12 mm steel plate", [
        "Stub: cut 105 long from 2 in pipe, ends square",
        "Plate: 150 dia from 12 mm plate, bore 52.5 through the centre;",
        "  drill and tap 4 x M8 on a 110 circle",
        "Weld the plate on one end of the stub, flush with the bore",
        f"Set the stub into the top hole ({P['MN_X']:.0f} from the door end);",
        f"  plate top face {P['MN_TOP'] + P['MF_T']:.0f} above the floor, level",
        "Fillet weld to the shell all round outside, 5 mm leg",
        "Check: plate level within 1 deg; stub clear inside",
    ], ["shell"])
    S[106] = lambda: sheet(106, "saddle1", "AltiRig saddle (make 2)", "Steel plate 10 thick", [
        "Base: 200 x 900 plate, two 18 dia holes 40 from each end",
        "Web: 840 wide x 597 high with a 833 dia curved cut in the top,",
        "  centred, its centre 800 above the floor",
        "Wear plate: 160 wide strip rolled to 813 inside dia over 120 deg",
        "Weld web to base on its centre line, square, both sides",
        "Weld the wear plate onto the web's curved top, centred",
        "Set both saddles on a level floor 950 apart and lower the shell",
        "  in; the wear plates take the shell along their full arc",
        "Fillet weld each wear plate to the shell along both edges",
        "Check: shell axis level and 800 above the floor at both ends",
    ], ["shell"], view_shape=at_origin(comps()["saddle1"].shape))
    S[107] = lambda: sheet(107, "rail_p", "AltiRig deck rail (make 2)", "Steel angle 50 x 50 x 6, 900 long", [
        "Cut two angles 900 long",
        "Drill three 9 dia holes in one leg, 19 from the outer edge:",
        "  50 and 450 and 850 from the door end",
        "Inside the shell: the drilled leg is the top, flat, pointing out",
        "  to the wall; the other leg hangs down and is cut to the curve",
        "Top of the angle 522 above the floor, 150 out from the centre line",
        "  (300 apart, faces inside), starting 80 from the shell ring face",
        "Scribe the hanging leg to the shell and grind to a close fit",
        "Fillet weld the hanging leg to the shell, 4 mm leg, both sides",
        "Check: both top legs level with each other within 1 mm",
    ], ["shell"], view_shape=at_origin(comps()["rail_p"].shape))
    S[108] = lambda: sheet(108, "tabs", "AltiRig baffle tabs (make 4)", "Steel flat 40 x 10", [
        "Cut four tabs 40 wide, 10 thick, 45 long",
        "Drill one 9 dia hole in each, 18 from the inner end",
        f"Inside the shell, {P['BAF_X']:.0f} from the shell ring face (the",
        "  face the baffle bolts to), at 45, 135, 225 and 315 deg",
        "Each tab stands radially; its outer end scribed to the wall",
        "Fillet weld to the shell on both sides, 5 mm leg",
        "Check: the four bolt faces in one plane within 2 mm",
    ], ["shell"], view_shape=at_origin(comps()["tabs"].shape), inset=(20, -30))
    S[109] = lambda: sheet(109, "hinge_fixed", "AltiRig hinge lugs and pin", "Steel plate 15 thick; 20 mm bar", [
        "Cut four lugs from 15 mm plate; drill each 21 dia for the pin",
        "Two lugs on the shell ring at its far edge (+Y), 395 apart",
        "  vertically, the upper one 190 above the axis",
        "Two lugs on the door ring, each 2 mm above a shell-ring lug",
        "Pin hole centres 16 in front of the shell ring face and 515",
        "  out from the axis; set them on one vertical line with a rod",
        "Pin: 20 dia bar 450 long, head on top, collar under the lowest lug",
        "Slot the door lugs' holes 3 mm toward the axis so the door",
        "  can settle evenly on the gasket",
        "Check: the door swings freely and closes square on the gasket",
    ], ["shell_ring", "door_ring"], view_shape=at_origin(comps()["hinge_fixed"].shape), inset=(20, -20))
    S[110] = lambda: sheet(110, "door_head", "AltiRig door: head welded into a flange ring",
                           "Bought 813 OD 2:1 head, 6.35; door flange ring (sheet 102)", [
        "The door is the second tank head with the second flange ring",
        "Surplus heads: 813 OD, wall 5.9 or more, 40 mm skirt; check",
        "  before buying that the skirt fits the ring and the pipe",
        "Set the ring over the head's 40 mm skirt, face flush with the",
        "  skirt's open end; check the face is flat within 1 mm",
        "Fillet weld ring to skirt both sides in short balanced runs",
        "Weld the two door lugs to the ring's edge (sheet 109)",
        "Grind the gasket face smooth where the welds meet it",
        "The door weighs about 72 kg: lift it with a hoist or two people",
        "Check: door face flat; no weld proud of the face",
    ], ["door_ring", "door_lugs"], name="Door (head, flange ring and lugs)",
        shape=fuse("door_head", "door_ring", "door_lugs"), inset=(20, -130), rev="P2",
        revisions=[("P1", "Making sketch", DATE, "AC"),
                   ("P2", "Surplus head checks before buying (decision 42B)", DATE, "AC")])
    S[111] = lambda: sheet(111, "window", "AltiRig window", "Clear polycarbonate sheet 20 thick (never acrylic)", [
        f"Cut a {P['WIN_D']:.0f} dia disc from 20 mm polycarbonate",
        "Sand the edge smooth and break it with a 1 mm chamfer",
        "No holes in the window; it is held by the clamp ring only",
        "Leave the protective film on until it is fitted",
        "Clean with water and mild soap only; solvents craze it",
        "Check: no scratches deeper than a fingernail catches",
    ], ["win_nozzle", "win_spacer", "win_clamp"], inset=(15, -100))
    S[112] = lambda: sheet(112, "win_spacer", "AltiRig window spacer and clamp rings", "Steel plate 25 and 10 thick", [
        "Spacer: 400 OD x 346 ID from 25 mm plate",
        "Clamp: 400 OD x 290 ID from 10 mm plate",
        "Drill both together: 8 x 11 dia on a 373 circle, 22.5 deg start,",
        "  matching the tapped holes in the window flange",
        "The spacer sets the gap: gasket 6 mm squeezed to 5 plus window 20",
        "The clamp ring overlaps the window rim by 25 all round",
        "Deburr; paint all faces except the face that touches the window",
        "Check: rings sit flat together; holes line up with the flange",
    ], ["win_nozzle", "window"], inset=(15, -100))
    S[113] = lambda: sheet(113, "ft_plate", "AltiRig feed-through plate", "Aluminium 6082 plate 15 thick", [
        "Cut a 260 dia disc; drill 8 x 11 dia on a 225 circle",
        "Drill five 20 dia holes: one at the centre, four on a 70 x 60",
        "  rectangle around it",
        "Fit M20 IP68 cable glands, O-ring on the inside face",
        "Motor phases: three 6 mm2 cores through one gland; signals and",
        "  sensors through the others; blank any spare gland",
        "Pot each cable in epoxy for 50 mm inside the gland so air",
        "  cannot leak along the strands",
        "Check: glands tight; plate flat; potting fully cured",
    ], ["ft_nozzle"], inset=(15, -100))
    S[114] = lambda: sheet(114, "deck", "AltiRig deck plate", "Aluminium 6082 or 5083 plate 8 thick, 900 x 400", [
        "Cut 900 x 400; drill six 9 dia holes 169 each side of the centre",
        "  line, at 50, 450 and 850 from the door end, to the rails",
        "Drill and tap four M8 holes for the stand base: 140 and 400",
        "  from the deck's door-end edge, 80 each side of the centre line",
        "The deck bolts onto the rails' top legs with M8 bolts and nuts",
        "Check: deck slides in through the door opening and sits flat",
    ], ["rail_p", "rail_n"], view_shape=at_origin(comps()["deck"].shape))
    S[115] = lambda: sheet(115, "baffle", "AltiRig baffle plate", "Perforated steel 2 thick, 80 % open", [
        f"Cut a {P['BAF_D']:.0f} dia disc from perforated sheet ({P['BAF_HOLE']:.0f} mm square",
        f"  holes on a {P['BAF_PITCH']} mm square pitch, 80 % open); file the rim smooth",
        "Drill four 9 dia holes at 45, 135, 225 and 315 deg on a 764 circle",
        "  to match the tabs; fit them where the solid edge allows",
        "Bolt to the tabs with M8 bolts, nuts and washers",
        "The baffle comes out for the comparison runs without it",
        "Check: 5 mm gap to the wall all round",
    ], ["tabs"], inset=(15, -100), rev="P2",
        revisions=[("P1", "Making sketch, 63 % open sheet", DATE, "AC"),
                   ("P2", "80 % open sheet (decision 41B)", DATE, "AC")])
    S[116] = lambda: sheet(116, "stand_base", "AltiRig stand base plate", "Aluminium 6082 plate 12 thick, 300 x 200", [
        "Cut 300 x 200; four 9 dia holes 20 in from each corner to the deck",
        "Tap M5 holes for the two lower flexure clamps (centres 50 and 250",
        "  from the door-end edge), the anchor block and the speed post",
        "Face the top flat; the clamps and anchor sit on it",
        "Check: flat within 0.1 mm across the clamp positions",
    ], ["deck", "clamps", "anchor"], view_shape=at_origin(comps()["stand_base"].shape))
    S[117] = lambda: sheet(117, "clamps", "AltiRig flexure leaves and clamps", "Spring steel shim 0.5; aluminium bar", [
        "Leaves: two 120 x 110 cut from 0.5 hardened spring steel shim;",
        "  cut with snips or a guillotine, no bends or kinks",
        "Clamps: four blocks 30 x 140 x 20; slit each along its middle",
        "  so the leaf is gripped between two halves; two M5 screws each",
        "Lower clamps screw to the base plate, upper to the carriage,",
        "  200 apart, so the leaves stand parallel and 80 free between",
        "Assemble with a 80 spacer block between the clamps to set height",
        "Check: carriage moves freely fore and aft, springs back to zero",
    ], ["stand_base", "carriage", "leaves"], view_shape=at_origin(fuse("clamps", "leaves")),
        name="Flexure leaves and clamps", shape=fuse("clamps", "leaves"))
    S[118] = lambda: sheet(118, "anchor", "AltiRig thrust cell anchor block and hanger", "Aluminium 6082 bar", [
        "Anchor: 30 x 40 x 58 block; two M5 tapped holes up into the base",
        "  plate side, two M5 through on its back face for the cell",
        "Hanger: 27 x 40 x 62 block; two M5 tapped holes in its top to the",
        "  carriage, two M5 through its front face for the cell",
        "The load cell stands upright between them: its lower end bolts",
        "  to the anchor, its upper end to the hanger",
        "Check: the cell hangs plumb and touches nothing between its ends",
    ], ["thrust_cell", "stand_base"], name="Anchor block and hanger", shape=fuse("anchor", "hanger"),
        view_shape=at_origin(fuse("anchor", "hanger")))
    S[119] = lambda: sheet(119, "carriage", "AltiRig carriage plate", "Aluminium 6082 plate 10 thick, 240 x 160", [
        "Cut 240 x 160; drill for the two upper clamps (M5 clearance),",
        "  the hanger (two M5) and the torque head housing (four M6)",
        "The carriage hangs on the two leaves and carries the torque head",
        "Check: flat; no screw head proud on the underside near the cell",
    ], ["clamps", "housing", "hanger"], view_shape=at_origin(comps()["carriage"].shape))
    S[120] = lambda: sheet(120, "housing", "AltiRig torque head: housing, shaft and motor plate",
                           "Aluminium 6082 block; 15 mm stainless bar; 6 mm aluminium", [
        "Housing: 50 x 90 x 178 block; bore 35 H7 through, centre 128",
        "  up from its base; four M6 tapped holes in the base",
        "Press in two 6202 bearings, one at each end of the bore",
        "Shaft: 15 dia, 115 long with a 40 dia hub 13 long at the motor end",
        "Motor plate: 80 dia disc 6 thick, bolted to the hub; drill it for",
        "  the motor's own pattern (16, 19, 25 or 30 mm circles)",
        "Shaft axis 800 above the floor, on the vessel axis",
        "Check: shaft turns freely by hand with no end play",
    ], ["carriage", "arm", "motor"], name="Torque head (housing, bearings, shaft, motor plate)",
        shape=fuse("housing", "bearings", "shaft", "mplate"), view_shape=at_origin(fuse("housing", "bearings", "shaft", "mplate")))
    S[121] = lambda: sheet(121, "arm", "AltiRig torque arm and cell bracket", "Aluminium 6082, 10 thick", [
        "Arm: 10 thick; 30 dia hub bored 15 and slit, clamped with one M4",
        "  screw; the bar reaches 60 from the axis to the cell",
        "Bracket: 40 x 21 x 33 block, two M5 to the housing side",
        "Torque cell lies along the axis on the bracket, fixed end down",
        "  on the bracket, free end under the arm's tip",
        "A 3 mm steel ball in a dimple carries the arm onto the cell",
        "Check: arm rests on the cell with the shaft free to turn",
    ], ["housing", "torque_cell"], name="Torque arm and cell bracket", shape=fuse("arm", "tc_bracket"),
        view_shape=at_origin(fuse("arm", "tc_bracket")))
    S[122] = lambda: sheet(122, "speed_post", "AltiRig speed sensor post", "Aluminium bar 16 x 20", [
        "Post: 16 x 20 bar 128 long; two M5 tapped holes in its foot",
        "Sensor block on top faces the propeller, 15 from its plane",
        "Sensor 140 below the axis, so the blades pass across it",
        "Stick a 10 mm square of reflective tape on one blade",
        "Check: sensor reads one pulse per turn when the blade is turned",
    ], ["stand_base", "prop"], view_shape=at_origin(comps()["speed_post"].shape))
    for n in (which or sorted(S)):
        print("sheet", n, S[int(n)]())


# ------------------------------------------------------------------ joints
def joints(which=None):
    ro = L["ro"]
    J = {}
    J[1] = lambda: bv.joint([W("shell", (-60, 120, -100, 100, Z + 330, Z + 500)),
                             W("shell_ring", (-60, 120, -100, 100, Z + 330, Z + 500)),
                             W("gasket", (-60, 120, -100, 100, Z + 330, Z + 500)),
                             W("door_ring", (-60, 120, -100, 100, Z + 330, Z + 500)),
                             W("door_head", (-60, 120, -100, 100, Z + 330, Z + 500)),
                             W("latches", (-60, 120, -100, 100, Z + 330, Z + 530))],
                            OUT / "joint-01.png", "Joint 1: door closed on the shell ring, latch on",
                            "Cut open at the top: gasket glued to the shell ring; air presses the door ring onto it",
                            cut="+Y", elev=10, azim=-80)
    J[2] = lambda: bv.joint([W("shell", (1400, 1650, -150, 150, Z + 300, Z + 420)),
                             W("rear_head", (1400, 1650, -150, 150, Z + 300, Z + 420)),
                             W("man_stub", (1220, 1380, -60, 80, Z + 360, Z + 520)),
                             W("manifold", (1220, 1420, -100, 80, Z + 360, Z + 640))],
                            OUT / "joint-02.png", "Joint 2: rear head butt weld and manifold stub",
                            "Head skirt butt welded to the pipe end; 2 in stub fillet welded into the top",
                            cut="+Y", elev=12, azim=-75)
    bxw = (P["WIN_X"] - 230, P["WIN_X"] + 230, -600, -330, Z - 10, Z + 230)
    J[3] = lambda: bv.joint([W("shell", bxw), W("win_nozzle", bxw), W("win_gasket", bxw), W("window", bxw),
                             W("win_spacer", bxw), W("win_clamp", bxw)],
                            OUT / "joint-03.png", "Joint 3: window stack on the window nozzle",
                            "Cut through the centre: gasket, window, 25 mm spacer, clamp ring, 8 x M10 into the flange",
                            cut="+X", elev=20, azim=-30)
    bxf = (P["FT_X"] - 150, P["FT_X"] + 150, -600, -330, Z - 10, Z + 150)
    J[4] = lambda: bv.joint([W("shell", bxf), W("ft_nozzle", bxf), W("ft_gasket", bxf), W("ft_plate", bxf)],
                            OUT / "joint-04.png", "Joint 4: feed-through plate on its nozzle",
                            "Cut through the centre: 2 mm gasket, 15 mm plate with glands, 8 x M10",
                            cut="+X", elev=20, azim=-30)
    bxh = (-60, 40, 380, 560, Z - 230, Z + 260)
    J[5] = lambda: bv.joint([W("shell_ring", bxh), W("door_ring", bxh), W("hinge_fixed", bxh), W("door_lugs", bxh),
                             W("pin", bxh)],
                            OUT / "joint-05.png", "Joint 5: door hinge",
                            "Two lugs on each ring, one 20 mm pin; door lug holes slotted 3 mm",
                            elev=18, azim=-35)
    bxr = (400, 560, -260, 260, L["shell_bottom_in"] - 10, L["deck_top"] + 15)
    J[6] = lambda: bv.joint([W("shell", bxr), W("rail_p", bxr), W("rail_n", bxr), W("deck", bxr)],
                            OUT / "joint-06.png", "Joint 6: deck on its rails",
                            "Cut across: hanging legs scribed and welded to the wall; deck bolted to the top legs",
                            elev=12, azim=-90)
    bxb = (P["BAF_X"] - 60, P["BAF_X"] + 60, -330, 330, Z + 200, Z + 420)
    J[7] = lambda: bv.joint([W("shell", bxb), W("tabs", bxb), W("baffle", bxb)],
                            OUT / "joint-07.png", "Joint 7: baffle plate on the tabs",
                            "Four tabs welded inside; the baffle bolts to them and can be taken out", elev=20, azim=-30)
    bxs = (200, 500, -100, 100, L["deck_top"] - 8, L["car_z"][1] + 2)
    J[8] = lambda: bv.joint([W("deck", bxs), W("stand_base", bxs), W("clamps", bxs), W("leaves", bxs),
                             W("anchor", bxs), W("thrust_cell", bxs), W("hanger", bxs), W("carriage", bxs)],
                            OUT / "joint-08.png", "Joint 8: flexure stand and thrust cell",
                            "Cut along the axis: leaves in slit clamps carry the carriage; cell between anchor and hanger",
                            cut="+Y", elev=12, azim=-80)
    bxt = (320, 460, -50, 80, Z - 60, Z + 55)
    J[9] = lambda: bv.joint([W("housing", bxt), W("bearings", bxt), W("shaft", bxt), W("mplate", bxt), W("arm", bxt),
                             W("torque_cell", bxt), W("tc_bracket", bxt)],
                            OUT / "joint-09.png", "Joint 9: torque head",
                            "Shaft on two bearings; arm on the shaft rests on the torque cell and its bracket", elev=25, azim=-130)
    bxsd = (P["SAD_X"][0] - 120, P["SAD_X"][0] + 120, -470, -150, 0, Z - 150)
    J[10] = lambda: bv.joint([W("shell", bxsd), W("saddle1", bxsd)],
                             OUT / "joint-10.png", "Joint 10: saddle under the shell",
                             "Wear plate on the web's curved top, welded to the shell along both edges", elev=15, azim=-60)
    for n in (which or sorted(J)):
        print("joint", n, J[int(n)]())


# ------------------------------------------------------------------ steps
def steps(which=None):
    ro = L["ro"]
    cutY = box(-400, 1900, -10, 700, -10, 1400)          # keeps the far half of the vessel parts
    half = lambda k: K(k, shape=comps()[k].shape & cutY)  # noqa: E731
    T = {}

    def st(n, done, new, title, sub, **kw):
        return bv.step(done, new, OUT / f"step-{n:02d}.png", f"Step {n}: {title}", subtitle=sub, **kw)

    T[1] = lambda: st(1, [K("shell")], [K("shell_ring", explode=(-350, 0, 0))], "flange ring onto the shell end",
                      "Slide the ring over the pipe until its gasket face is flush with the pipe end; weld both sides")
    T[2] = lambda: st(2, [K("shell"), K("shell_ring")], [K("rear_head", explode=(450, 0, 0))], "rear head",
                      "Butt the head's skirt to the pipe's far end, root gap 2 to 3 mm; full-penetration weld all round")
    T[3] = lambda: st(3, [K("shell"), K("shell_ring"), K("rear_head")],
                      [K("win_nozzle", explode=(0, -350, 0)), K("ft_nozzle", explode=(0, -350, 0)),
                       K("man_stub", explode=(0, 0, 300))], "nozzles into the shell",
                      "Window and feed-through nozzles on the window side, manifold stub on top; set in and welded")
    T[4] = lambda: st(4, [K(k) for k in ("shell", "shell_ring", "rear_head", "win_nozzle", "ft_nozzle", "man_stub")],
                      [K("saddle1", explode=(0, 0, -350)), K("saddle2", explode=(0, 0, -350))], "saddles",
                      "Saddles 950 apart on a level floor; lower the shell onto the wear plates and weld along their edges",
                      label_done=False)
    T[5] = lambda: st(5, [half(k) for k in ("shell", "rear_head", "saddle1", "saddle2")] + [half("shell_ring")],
                      [K("rail_p", explode=(0, 0, 250)), K("rail_n", explode=(0, 0, 250)), half("tabs")],
                      "deck rails and baffle tabs inside",
                      "Shown with the window half of the vessel cut away. Rails 522 up, 300 apart; tabs 1,100 from the ring",
                      elev=20, azim=-75, label_done=False)
    T[6] = lambda: st(6, [K("door_head")], [K("door_ring", explode=(250, 0, 0)), K("door_lugs", explode=(250, 250, 0))],
                      "door: ring and lugs onto the second head",
                      "Ring over the skirt, face flush with the skirt end; lugs welded to its far edge", elev=20, azim=-130)
    T[7] = lambda: st(7, [K(k) for k in ("shell", "shell_ring", "rear_head", "saddle1", "saddle2", "hinge_fixed")],
                      [K("door_ring", explode=(-400, 0, 0)), K("door_head", explode=(-400, 0, 0)),
                       K("door_lugs", explode=(-400, 0, 0)), K("pin", explode=(0, 0, 450))],
                      "hang the door", "Lift the 72 kg door with a hoist, line up the lugs and drop the pin in from above",
                      label_done=False)
    T[8] = lambda: st(8, [K(k) for k in ("shell", "shell_ring", "rear_head", "saddle1", "saddle2", "hinge_fixed")],
                      [K("gasket", explode=(-250, 0, 0)), K("latches", explode=(-250, 0, 0))],
                      "door gasket and latches",
                      "Door swung open (not shown). Glue the sponge strip to the shell ring face; bolt on three latches",
                      label_done=False, elev=18, azim=-120)
    T[9] = lambda: st(9, [K(k) for k in ("shell", "win_nozzle")],
                      [K("win_gasket", explode=(0, -120, 0)), K("window", explode=(0, -220, 0)),
                       K("win_spacer", explode=(0, -320, 0)), K("win_clamp", explode=(0, -420, 0))], "window",
                      "Gasket, polycarbonate window, spacer ring, clamp ring; tighten 8 x M10 evenly in a star, hand tight "
                      "plus a quarter turn", elev=15, azim=-40, label_done=False)
    T[10] = lambda: st(10, [K(k) for k in ("shell", "ft_nozzle")],
                       [K("ft_gasket", explode=(0, -150, 0)), K("ft_plate", explode=(0, -300, 0))], "feed-through plate",
                       "Cables already potted in the glands; gasket, plate, 8 x M10 in a star", elev=15, azim=-40,
                       label_done=False)
    T[11] = lambda: st(11, [K(k) for k in ("shell", "rear_head", "man_stub")], [K("manifold", explode=(0, 0, 300))],
                       "valve manifold on the stub",
                       "Relief valve, gauge, bleed valve and pump port on one block; 4 x M8 with a 2 mm gasket",
                       elev=20, azim=-50, label_done=False)
    T[12] = lambda: st(12, [half(k) for k in ("shell", "rear_head", "tabs", "rail_p")],
                       [K("baffle", explode=(-500, 0, 0))], "baffle plate",
                       "Carried in through the door and bolted to the four tabs with M8 bolts",
                       elev=20, azim=-75, label_done=False)
    T[13] = lambda: st(13, [half(k) for k in ("shell", "rear_head", "tabs", "rail_p", "baffle")],
                       [K("deck", explode=(-700, 0, 0))], "deck plate",
                       "Slid in through the door onto the rails' top legs; six M8 bolts and nuts",
                       elev=20, azim=-75, label_done=False)
    ctx = [K("deck"), K("rail_p"), K("rail_n")]
    T[14] = lambda: st(14, ctx, [K("stand_base", explode=(0, 0, 120)), K("clamps", explode=(0, 0, 200)),
                                 K("leaves", explode=(0, 0, 280))], "stand base and flexures",
                       "Vessel not shown. Base plate onto the deck (4 x M8); lower clamps and leaves; upper clamps loose",
                       elev=22, azim=-50, label_done=False)
    T[15] = lambda: st(15, [K(k) for k in ("stand_base", "clamps", "leaves")],
                       [K("anchor", explode=(0, -150, 0)), K("thrust_cell", explode=(0, -250, 0)),
                        K("hanger", explode=(0, -350, 0)), K("carriage", explode=(0, 0, 200))],
                       "thrust cell and carriage",
                       "Anchor on the base, cell upright on it, hanger on the cell's top; carriage onto the upper clamps "
                       "and the hanger", elev=22, azim=-50, label_done=False)
    T[16] = lambda: st(16, [K(k) for k in ("stand_base", "clamps", "leaves", "anchor", "thrust_cell", "hanger",
                                                 "carriage")],
                       [K("housing", explode=(0, 0, 200)), K("bearings", explode=(0, 0, 200)),
                        K("shaft", explode=(200, 0, 200)), K("mplate", explode=(300, 0, 200))], "torque head",
                       "Housing with its bearings onto the carriage (4 x M6); shaft in from the motor side; motor plate on "
                       "the hub", elev=22, azim=-50, label_done=False)
    done16 = ("stand_base", "clamps", "leaves", "anchor", "thrust_cell", "hanger", "carriage", "housing", "bearings",
              "shaft", "mplate")
    T[17] = lambda: st(17, [K(k) for k in done16],
                       [K("tc_bracket", explode=(0, 150, 0)), K("torque_cell", explode=(0, 150, 100)),
                        K("arm", explode=(-150, 0, 0))], "torque cell and arm",
                       "Bracket on the housing side, torque cell on the bracket, arm clamped on the shaft resting on the cell",
                       elev=25, azim=-130, label_done=False)
    done17 = done16 + ("tc_bracket", "torque_cell", "arm")
    T[18] = lambda: st(18, [K(k) for k in done17],
                       [K("speed_post", explode=(0, -150, 0)), K("sensors", explode=(0, 0, 150))],
                       "speed sensor and air sensors", "Speed post on the base plate; air sensor box on the deck",
                       elev=22, azim=-50, label_done=False)
    done18 = done17 + ("speed_post", "sensors")
    T[19] = lambda: st(19, [K(k) for k in done18],
                       [K("motor", explode=(150, 0, 0)), K("prop", explode=(300, 0, 0))], "motor and propeller under test",
                       "Motor onto the motor plate with its own screws; propeller with the reflective tape on one blade",
                       elev=22, azim=-50, label_done=False)
    T[20] = lambda: st(20, [K(k) for k in ("shell", "shell_ring", "rear_head", "saddle1", "saddle2", "door_ring",
                                           "door_head", "manifold", "win_clamp", "ft_plate")],
                       [K("pump", explode=(0, 400, 0)), K("hose", explode=(0, 400, 0)), K("cabinet", explode=(-300, -300, 0))],
                       "pump, hose and control cabinet",
                       "Pump on the floor on the far side, exhaust led outdoors; cabinet in front of the door, on the "
                       "window side", label_done=False)
    for n in (which or sorted(T)):
        print("step", n, T[int(n)]())


if __name__ == "__main__":
    what = sys.argv[1] if len(sys.argv) > 1 else "all"
    args = [int(a) for a in sys.argv[2:]] or None
    if what in ("overview", "all"):
        print("overview", overview())
    if what in ("sheets", "all"):
        sheets(args)
    if what in ("joints", "all"):
        joints(args)
    if what in ("steps", "all"):
        steps(args)
