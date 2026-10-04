"""AltiRig product appearance model (build123d), TRL 3, constructable design (ALR-DDR-002).

For photoreal renders only (.kit/export_views.py, then .kit/photoreal.py on Amish's Mac). Every
part is the model.py solid itself, in the same place, so every main dimension comes from
cad/src/model.py; colours and material classes are added for the look. Appearance choices not in
model.py, recorded in docs/REVIEW.md: the baffle's 22 mm square holes on a 24.5 mm pitch (80 % open,
decision 41B) are cut here for the look, inside a plain rim and clear of the four bolt holes (model.py keeps
it as a plain disc so the checks stay fast), the control cabinet left out of the hero (it stands apart, in front of the door), and a
1.75 m mannequin standing beside the door end, never between the camera and the vessel. In the
exploded view the stand, the deck and the test article are lifted out above the vessel.
CONCEPT, NOT FOR FABRICATION.

    from product_model import product_parts
    for p in product_parts(): print(p["name"], p["group"], p["material"])
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / ".kit"), str(ROOT / "cad" / "src")]
import math  # noqa: E402

from build123d import Box, Compound, Pos, Rot  # noqa: E402
from model import PARAMS as P, components  # noqa: E402

TITLE = "AltiRig: altitude test chamber with a thrust stand for propellers and motors"

RENDER_VIEWS = [
    {"name": "hero", "groups": ["shell", "context"], "explode": False, "el": 20, "az": -40,
     "note": "Product render from the front right and above (about 20 deg elevation): steel vacuum vessel on two "
             "saddles, door with three latches at the left end, polycarbonate window and cable feed-through on the "
             "near side, valve manifold on top, vacuum pump behind, and a 1.75 m person standing beside the door end"},
    {"name": "exploded", "groups": ["shell", "internal"], "explode": True, "el": 24, "az": -45,
     "note": "Exploded view from the front right and above (about 24 deg elevation): shell, flange rings, heads, door "
             "and hinge, window stack, feed-through plate, manifold and pump pulled apart; the flexure thrust stand, "
             "deck, motor and propeller lifted out above the vessel"},
    {"name": "detail", "groups": ["internal"], "explode": False, "el": 18, "az": -35,
     "note": "Detail of the thrust stand from the front right and above (about 18 deg elevation): deck plate, base, "
             "two spring-steel flexure leaves, thrust load cell, carriage, torque head on bearings with its arm and "
             "cell, speed sensor, motor and a 380 mm propeller; the vessel is not shown"},
]

LOOK = {  # key: (colour, material class)
    "shell": ("#3E5C7A", "painted"), "shell_ring": ("#3E5C7A", "painted"), "rear_head": ("#3E5C7A", "painted"),
    "win_nozzle": ("#3E5C7A", "painted"), "ft_nozzle": ("#3E5C7A", "painted"), "man_stub": ("#3E5C7A", "painted"),
    "saddle1": ("#2B2F36", "painted"), "saddle2": ("#2B2F36", "painted"), "rail_p": ("#6B7280", "metal"),
    "rail_n": ("#6B7280", "metal"), "tabs": ("#6B7280", "metal"), "hinge_fixed": ("#2B2F36", "painted"),
    "door_ring": ("#3E5C7A", "painted"), "door_head": ("#3E5C7A", "painted"), "door_lugs": ("#2B2F36", "painted"),
    "pin": ("#B8BDC4", "metal"), "gasket": ("#111111", "rubber"), "latches": ("#E0A100", "painted"),
    "win_gasket": ("#111111", "rubber"), "window": ("#DCEBFA", "clear"), "win_spacer": ("#2B2F36", "painted"),
    "win_clamp": ("#2B2F36", "painted"), "ft_gasket": ("#111111", "rubber"), "ft_plate": ("#C8CDD3", "metal"),
    "deck": ("#C8CDD3", "metal"), "baffle": ("#9AA1A9", "metal"), "stand_base": ("#0F766E", "painted"),
    "leaves": ("#8A8F96", "metal"), "clamps": ("#C8CDD3", "metal"), "carriage": ("#0F766E", "painted"),
    "anchor": ("#C8CDD3", "metal"), "thrust_cell": ("#C8CDD3", "metal"), "hanger": ("#C8CDD3", "metal"),
    "housing": ("#0F766E", "painted"), "bearings": ("#B8BDC4", "metal"), "shaft": ("#B8BDC4", "metal"),
    "mplate": ("#C8CDD3", "metal"), "arm": ("#C8CDD3", "metal"), "torque_cell": ("#C8CDD3", "metal"),
    "tc_bracket": ("#C8CDD3", "metal"), "speed_post": ("#C8CDD3", "metal"), "motor": ("#1F2937", "metal"),
    "prop": ("#151515", "plastic"), "sensors": ("#E5E7EB", "plastic"), "manifold": ("#B91C1C", "painted"),
    "pump": ("#C62828", "painted"), "hose": ("#111111", "rubber"), "cabinet": ("#D9DCE0", "painted"),
}
INTERNAL_KEYS = ("deck", "sensors")
LIFT = (-250.0, 0.0, 750.0)


def perforated_baffle(shape, P=P):
    """Cut the baffle's square holes (BAF_HOLE on BAF_PITCH) inside an 8 mm rim, clear of the bolt holes."""
    x0, z, h, p = P["BAF_X"], P["Z_AX"], P["BAF_HOLE"], P["BAF_PITCH"]
    r_rim = P["BAF_D"] / 2 - 8.0
    r_bolt = P["SH_OD"] / 2 - P["SH_T"] - 18.0
    bolts = [(r_bolt * math.cos(math.radians(a)), r_bolt * math.sin(math.radians(a))) for a in P["TAB_ANG"]]
    n = int(r_rim // p) + 1
    holes = []
    for i in range(-n, n + 1):
        for j in range(-n, n + 1):
            y, w = i * p, j * p
            if math.hypot(abs(y) + h / 2, abs(w) + h / 2) > r_rim:
                continue
            if any(math.hypot(y - by, w - bz) < h / 2 + 12.0 for by, bz in bolts):
                continue
            holes.append(Pos(x0 + P["BAF_T"] / 2, y, z + w) * Box(P["BAF_T"] + 2, h, h))
    return shape - Compound(holes)


def product_parts(P=P):
    out = []
    for c in components(P):
        color, mat = LOOK[c.key]
        if c.key == "baffle":
            c.shape = perforated_baffle(c.shape, P)
        if c.key == "cabinet":
            group = "cabinet"
        elif c.group in ("stand", "test") or c.key in INTERNAL_KEYS:
            group = "internal"
        else:
            group = "shell"
        ex = c.explode
        if group == "internal":
            ex = tuple(a + b for a, b in zip(ex, LIFT))
        out.append({"name": c.name, "shape": c.shape, "color": color, "material": mat, "bom": c.bom,
                    "group": group, "explode": tuple(float(v) for v in ex)})
    from context_parts import mannequin
    person = Pos(-1000.0, -300.0, 0) * Rot(0, 0, 40) * mannequin(1750, "stand")
    out.append({"name": "Person, 1.75 m (scale)", "shape": person, "color": "#D1D5DB", "material": "clay", "bom": None,
                "group": "context", "explode": (0.0, 0.0, 0.0)})
    return out


if __name__ == "__main__":
    for p in product_parts():
        s = p["shape"]
        print(f"{p['name']:44s} {p['group']:9s} {p['material']:9s} vol={s.volume / 1000:9.1f} cm3")
