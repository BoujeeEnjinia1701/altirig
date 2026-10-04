"""AltiRig parametric model (build123d), TRL 3, constructable design (ALR-DDR-002).

Run from the repo root:
    python cad/src/model.py            build, check for overlaps, print masses, export STEP and STL
    python cad/src/model.py --check    build and check only

Every dimension lives in PARAMS. Coordinates in mm: X along the vessel axis (0 at the face of the
shell flange ring, the door at -X, the rear head at +X), Y across (window side at -Y), Z up from the
floor. The vessel axis is at Z = PARAMS["Z_AX"].

The chamber is a horizontal steel vessel made from an 813 mm (32 in) pipe offcut with a bought
2:1 ellipsoidal head welded on the rear end and a second head on a flange ring as the door. Air
pressure holds the door shut under vacuum. Inside, a flexure thrust stand on a deck carries the
motor and propeller on the axis, and a perforated baffle plate breaks up the wake. Outside: window,
cable feed-through plate, valve manifold, vacuum pump and control cabinet.
CONCEPT, NOT FOR FABRICATION.
"""
from __future__ import annotations

import math
import sys
from dataclasses import dataclass, field
from pathlib import Path

from build123d import (Axis, Box, Compound, Cylinder, Edge, Face, Plane, Pos, Rot, Wire, export_step, export_stl,
                       revolve)

ROOT = Path(__file__).resolve().parents[2]

PARAMS = {
    # vessel
    "SH_OD": 813.0, "SH_T": 6.35, "SH_L": 1500.0,          # shell: 32 in pipe, 1/4 in wall, length
    "Z_AX": 800.0,                                         # axis height above the floor
    "HEAD_SKIRT": 40.0, "HEAD_DEPTH": 200.0,               # 2:1 ellipsoidal head: straight skirt, inside depth
    "RING_T": 20.0, "RING_OD": 960.0,                      # flange rings (shell and door), ID = shell OD
    "GASKET_T": 6.0, "GASKET_ID": 840.0, "GASKET_OD": 930.0,
    # window nozzle (-Y side)
    "WIN_X": 250.0, "WN_OD": 273.1, "WN_T": 12.7, "WN_OUT": 520.0,      # nozzle end at y = -WN_OUT
    "SET_IN": 360.0,                                                   # set-in nozzles end square at |y| = SET_IN
    "WF_OD": 400.0, "WF_ID": 255.0, "WF_T": 20.0,                      # window flange ring
    "WG_T": 5.0, "WG_ID": 270.0, "WG_OD": 330.0,                       # window gasket, 6 mm EPDM compressed to 5
    "WIN_D": 340.0, "WIN_T": 20.0,                                     # polycarbonate window
    "WCL_ID": 290.0, "WCL_T": 10.0, "WSP_ID": 346.0,                   # clamp ring and spacer ring
    "WB_PCD": 373.0, "WB_N": 8, "WB_D": 11.0,                          # window bolts M10
    # feed-through nozzle (-Y side, downstream of the burst zone)
    "FT_X": 740.0, "FN_OD": 168.3, "FN_T": 10.97, "FN_OUT": 500.0,
    "FF_OD": 260.0, "FF_ID": 154.0, "FF_T": 20.0, "FP_T": 15.0, "FG_T": 2.0,
    # manifold stub (top)
    "MN_X": 1300.0, "MN_OD": 60.3, "MN_T": 3.91, "MN_TOP": 1290.0, "MF_D": 150.0, "MF_T": 12.0,
    # saddles
    "SAD_X": (300.0, 1250.0), "SAD_T": 10.0, "SAD_W": 840.0, "SAD_ZTOP": 597.0,
    "SAD_WEAR_W": 160.0, "SAD_BASE": (200.0, 900.0),
    # inside: deck rails, deck, baffle
    "RAIL_Y": 150.0, "RAIL_T": 6.0, "RAIL_LEG": 50.0, "RAIL_X": (80.0, 980.0), "DECK_Z": 522.0,
    "DECK_T": 8.0, "DECK_W": 400.0,
    "BAF_X": 1100.0, "BAF_D": 790.0, "BAF_T": 2.0, "BAF_OPEN": 0.80,   # 80 % open baffle (decision 41B, 2026-10-03)
    "BAF_HOLE": 22.0, "BAF_PITCH": 24.5,                   # square holes 22 mm on a 24.5 mm square pitch
    "TAB_ANG": (45.0, 135.0, 225.0, 315.0), "TAB_W": 40.0, "TAB_H": 40.0, "TAB_T": 10.0,
    # thrust stand (on the deck)
    "SB": (200.0, 500.0, 100.0, 12.0),                    # base plate x0, x1, half width, thickness
    "LEAF_X": (250.0, 450.0), "LEAF_T": 0.5, "LEAF_W": 120.0, "LEAF_FREE": 80.0,
    "CLAMP": (30.0, 140.0, 20.0),                          # clamp block x, y, z
    "CAR": (220.0, 460.0, 80.0, 10.0),                     # carriage plate x0, x1, half width, thickness
    "CELL_T": (12.7, 80.0),                                # bar load cell section and length
    "HOUS": (380.0, 430.0, 45.0, 850.0), "BRG_OD": 35.0, "BRG_W": 11.0, "SHAFT_D": 15.0,
    "SHAFT_X": (330.0, 432.0), "HUB": (432.0, 445.0, 40.0),
    "MPLATE": (445.0, 451.0, 80.0), "MOTOR": (451.0, 491.0, 58.0),
    "PROP_D": 380.0, "PROP_X": 510.0, "PROP_PITCH_IN": 5.0,
    "ARM_X": (335.0, 345.0), "ARM_REACH": 60.0, "ARM_HUB": 30.0,
    # hinge and latches
    "PIN_X": -16.0, "PIN_Y": 515.0, "PIN_D": 20.0, "LUG_T": 15.0,
    "LATCH_ANG": (90.0, 180.0, 270.0),                     # degrees in the Y-Z plane from +Y (top, -Y, bottom)
    # outside equipment
    "PUMP": (1150.0, 1480.0, 520.0, 650.0, 230.0), "HOSE_D": 25.0,
    "CAB": (-760.0, -300.0, -950.0, -650.0, 1100.0),
    # materials, kg/m3
    "RHO": {"steel": 7850.0, "al": 2700.0, "pc": 1200.0, "epdm": 500.0, "spring": 7850.0},
}


@dataclass
class Comp:
    key: str
    name: str
    shape: object
    bom: int
    material: str
    process: str
    explode: tuple = (0.0, 0.0, 0.0)
    group: str = "vessel"
    bought_mass: float | None = None     # kg, for bought parts whose model is a massing shape
    extra: dict = field(default_factory=dict)


# ---------------------------------------------------------------- helpers
def box(x0, x1, y0, y1, z0, z1):
    return Pos((x0 + x1) / 2, (y0 + y1) / 2, (z0 + z1) / 2) * Box(x1 - x0, y1 - y0, z1 - z0)


def cyl_x(r, x0, x1, y=0.0, z=0.0):
    return Pos((x0 + x1) / 2, y, z) * Rot(0, 90, 0) * Cylinder(r, x1 - x0)


def cyl_y(r, y0, y1, x=0.0, z=0.0):
    return Pos(x, (y0 + y1) / 2, z) * Rot(90, 0, 0) * Cylinder(r, y1 - y0)


def cyl_z(r, z0, z1, x=0.0, y=0.0):
    return Pos(x, y, (z0 + z1) / 2) * Cylinder(r, z1 - z0)


def ring_x(ro, ri, x0, x1, z):
    return cyl_x(ro, x0, x1, 0, z) - cyl_x(ri, x0 - 1, x1 + 1, 0, z)


def ring_y(ro, ri, y0, y1, x, z):
    return cyl_y(ro, y0, y1, x, z) - cyl_y(ri, y0 - 1, y1 + 1, x, z)


def bore(P, x0=-400.0, x1=2000.0):
    """Solid of the vessel's inside (shell inside radius), used to trim parts to the inner wall."""
    return cyl_x(P["SH_OD"] / 2 - P["SH_T"], x0, x1, 0, P["Z_AX"])


def head(P, x_skirt_end, direction):
    """2:1 ellipsoidal head: skirt from x_skirt_end toward the shell, dish bulging away (direction -1 or +1)."""
    ro = P["SH_OD"] / 2
    ri = ro - P["SH_T"]
    z = P["Z_AX"]
    sk = P["HEAD_SKIRT"]
    x_tan = x_skirt_end + direction * sk                     # tangent line between skirt and dish
    skirt = ring_x(ro, ri, min(x_skirt_end, x_tan), max(x_skirt_end, x_tan), z)
    a_o, a_i = P["HEAD_DEPTH"] + P["SH_T"], P["HEAD_DEPTH"]
    # quarter-ellipse profile between the outer and inner surfaces, revolved about the axis
    eo = Edge.make_ellipse(a_o, ro, Plane.XY, 0, 90)
    ei = Edge.make_ellipse(a_i, ri, Plane.XY, 0, 90)
    prof = Face(Wire([eo, Edge.make_line(eo.position_at(1), ei.position_at(1)), ei.reversed(),
                      Edge.make_line(ei.position_at(0), eo.position_at(0))]))
    dish = revolve(prof, Axis.X, 360)
    if direction < 0:
        dish = Rot(0, 0, 180) * dish
    dish = Pos(x_tan, 0, z) * dish
    return skirt + dish


def bolt_holes_y(P, pcd, n, d, y0, y1, x, z, start=22.5):
    out = None
    for k in range(n):
        a = math.radians(start + k * 360.0 / n)
        c = cyl_y(d / 2, y0 - 1, y1 + 1, x + pcd / 2 * math.cos(a), z + pcd / 2 * math.sin(a))
        out = c if out is None else out + c
    return out


def rot_about_axis(shape, ang_deg, P):
    """Rotate a shape about the vessel axis (an X-parallel line at y = 0, z = Z_AX)."""
    z = P["Z_AX"]
    return Pos(0, 0, z) * Rot(ang_deg, 0, 0) * Pos(0, 0, -z) * shape


# ---------------------------------------------------------------- derived levels
def levels(P=PARAMS):
    ro = P["SH_OD"] / 2
    ri = ro - P["SH_T"]
    L = dict(ro=ro, ri=ri, z=P["Z_AX"])
    L["door_ring"] = (-P["GASKET_T"] - P["RING_T"], -P["GASKET_T"])
    L["door_skirt_end"] = -P["GASKET_T"]
    L["door_tan"] = -P["GASKET_T"] - P["HEAD_SKIRT"]
    L["door_tip"] = L["door_tan"] - P["HEAD_DEPTH"] - P["SH_T"]
    L["rear_tan"] = P["SH_L"] + P["HEAD_SKIRT"]
    L["rear_tip"] = L["rear_tan"] + P["HEAD_DEPTH"] + P["SH_T"]
    L["deck_top"] = P["DECK_Z"] + P["DECK_T"]
    L["shell_bottom_in"] = P["Z_AX"] - ri
    x0, x1, hw, t = P["SB"]
    L["sb_top"] = L["deck_top"] + t
    L["leaf_z"] = (L["sb_top"] + 5.0, L["sb_top"] + 5.0 + P["LEAF_FREE"] + 30.0)
    L["clamp_bot"] = (L["sb_top"], L["sb_top"] + P["CLAMP"][2])
    L["car_z"] = (L["sb_top"] + 2 * P["CLAMP"][2] + P["LEAF_FREE"], L["sb_top"] + 2 * P["CLAMP"][2] + P["LEAF_FREE"] + P["CAR"][3])
    L["clamp_top"] = (L["car_z"][0] - P["CLAMP"][2], L["car_z"][0])
    # window stack along -Y
    y = -P["WN_OUT"]
    L["wf"] = (y - P["WF_T"], y)
    L["wg"] = (L["wf"][0] - P["WG_T"], L["wf"][0])
    L["win"] = (L["wg"][0] - P["WIN_T"], L["wg"][0])
    L["wsp"] = (L["win"][0], L["wf"][0])
    L["wcl"] = (L["win"][0] - P["WCL_T"], L["win"][0])
    # feed-through stack along -Y
    y = -P["FN_OUT"]
    L["ff"] = (y - P["FF_T"], y)
    L["fg"] = (L["ff"][0] - P["FG_T"], L["ff"][0])
    L["fp"] = (L["fg"][0] - P["FP_T"], L["fg"][0])
    L["burst_half_angle"] = math.degrees(math.atan2(P["PROP_X"] - (P["WIN_X"] + P["WF_ID"] / 2), ri))
    L["burst_half_angle_ft"] = math.degrees(math.atan2(P["FT_X"] - P["FF_ID"] / 2 - P["PROP_X"], ri))
    return L


def baffle_open(P=PARAMS):
    """Open area of the square-hole perforated baffle: (hole / pitch) squared."""
    return (P["BAF_HOLE"] / P["BAF_PITCH"]) ** 2


# ---------------------------------------------------------------- components
def components(P=PARAMS, door_open=False):
    L = levels(P)
    ro, ri, z = L["ro"], L["ri"], L["z"]
    C = []

    def add(key, name, shape, bom, material, process, explode=(0, 0, 0), group="vessel", bought_mass=None):
        C.append(Comp(key, name, shape, bom, material, process, tuple(float(v) for v in explode), group, bought_mass))

    inside = bore(P)

    # 1 shell with holes for the nozzles
    shell = ring_x(ro, ri, 0, P["SH_L"], z)
    shell = shell - cyl_y(P["WN_OD"] / 2, -ro - 20, -ri + 40, P["WIN_X"], z)
    shell = shell - cyl_y(P["FN_OD"] / 2, -ro - 20, -ri + 40, P["FT_X"], z)
    shell = shell - cyl_z(P["MN_OD"] / 2, z + ri - 40, z + ro + 20, P["MN_X"], 0)
    add("shell", "Shell", shell, 1, "steel", "cut, drill, weld", (0, 0, 0))

    # 2 flange rings
    shell_ring = ring_x(P["RING_OD"] / 2, ro, 0, P["RING_T"], z)
    add("shell_ring", "Shell flange ring", shell_ring, 2, "steel", "plasma cut, weld", (-250, 0, 0))
    dr0, dr1 = L["door_ring"]
    door_ring = ring_x(P["RING_OD"] / 2, ro, dr0, dr1, z)

    # 3 heads
    rear = head(P, P["SH_L"], +1)
    add("rear_head", "Rear head", rear, 3, "steel", "buy, weld", (400, 0, 0))
    door_head = head(P, L["door_skirt_end"], -1)

    # 4 window nozzle and flange
    wn = ring_y(P["WN_OD"] / 2, P["WN_OD"] / 2 - P["WN_T"], -P["WN_OUT"], -P["SET_IN"], P["WIN_X"], z)
    wf0, wf1 = L["wf"]
    wf = ring_y(P["WF_OD"] / 2, P["WF_ID"] / 2, wf0, wf1, P["WIN_X"], z) - \
        bolt_holes_y(P, P["WB_PCD"], P["WB_N"], 8.5, wf0, wf1, P["WIN_X"], z)
    add("win_nozzle", "Window nozzle and flange", wn + wf, 4, "steel", "cut, weld, drill, tap", (0, -350, 0))

    # 5 feed-through nozzle and flange
    fn = ring_y(P["FN_OD"] / 2, P["FN_OD"] / 2 - P["FN_T"], -P["FN_OUT"], -P["SET_IN"], P["FT_X"], z)
    ff0, ff1 = L["ff"]
    ff = ring_y(P["FF_OD"] / 2, P["FF_ID"] / 2, ff0, ff1, P["FT_X"], z) - \
        bolt_holes_y(P, 225.0, 8, 8.5, ff0, ff1, P["FT_X"], z)
    add("ft_nozzle", "Feed-through nozzle and flange", fn + ff, 5, "steel", "cut, weld, drill, tap", (0, -350, 0))

    # 6 manifold stub and flange plate
    ms = cyl_z(P["MN_OD"] / 2, z + ri - 15, P["MN_TOP"], P["MN_X"], 0) - \
        cyl_z(P["MN_OD"] / 2 - P["MN_T"], z + ri - 16, P["MN_TOP"] + 1, P["MN_X"], 0)
    mf = cyl_z(P["MF_D"] / 2, P["MN_TOP"], P["MN_TOP"] + P["MF_T"], P["MN_X"], 0) - \
        cyl_z(P["MN_OD"] / 2 - P["MN_T"], P["MN_TOP"] - 1, P["MN_TOP"] + P["MF_T"] + 1, P["MN_X"], 0)
    for k in range(4):
        a = math.radians(45 + 90 * k)
        mf = mf - cyl_z(4.25, P["MN_TOP"] - 1, P["MN_TOP"] + P["MF_T"] + 1, P["MN_X"] + 55 * math.cos(a), 55 * math.sin(a))
    add("man_stub", "Manifold stub and flange", ms + mf, 6, "steel", "cut, weld, drill, tap", (0, 0, 250))

    # 7 saddles (wear plate, web, base plate), welded to the shell
    t = P["SAD_T"]
    bx_, by_ = P["SAD_BASE"]
    for i, xs in enumerate(P["SAD_X"]):
        wear = (ring_x(ro + t, ro, xs - P["SAD_WEAR_W"] / 2, xs + P["SAD_WEAR_W"] / 2, z)
                & box(xs - 100, xs + 100, -500, 500, 0, P["SAD_ZTOP"]))
        web = box(xs - t / 2, xs + t / 2, -P["SAD_W"] / 2, P["SAD_W"] / 2, t, P["SAD_ZTOP"]) - \
            cyl_x(ro + t, xs - 20, xs + 20, 0, z)
        base = box(xs - bx_ / 2, xs + bx_ / 2, -by_ / 2, by_ / 2, 0, t)
        for yy in (-by_ / 2 + 40, by_ / 2 - 40):
            base = base - cyl_z(9, -1, t + 1, xs, yy)
        add(f"saddle{i + 1}", "Saddle" + (" (door end)" if i == 0 else " (rear end)"), wear + web + base, 7,
            "steel", "plasma cut, roll, weld", (0, 0, -300))

    # 8 deck rails (angles welded inside)
    x0, x1 = P["RAIL_X"]
    for sgn, nm in ((1, "Deck rail (far side)"), (-1, "Deck rail (window side)")):
        yv0, yv1 = sorted((sgn * (P["RAIL_Y"] - P["RAIL_T"]), sgn * P["RAIL_Y"]))
        leg_v = box(x0, x1, yv0, yv1, L["shell_bottom_in"] - 5, P["DECK_Z"]) & inside
        yh0, yh1 = sorted((sgn * (P["RAIL_Y"] - P["RAIL_T"]), sgn * (P["RAIL_Y"] - P["RAIL_T"] + P["RAIL_LEG"])))
        leg_h = box(x0, x1, yh0, yh1, P["DECK_Z"] - P["RAIL_T"], P["DECK_Z"])
        r = leg_v + leg_h
        for xx in (x0 + 50, (x0 + x1) / 2, x1 - 50):
            r = r - cyl_z(4.5, P["DECK_Z"] - 10, P["DECK_Z"] + 1, xx, sgn * (P["RAIL_Y"] + 19))
        add("rail_p" if sgn > 0 else "rail_n", nm, r, 8, "steel", "cut, drill, weld inside", (0, 0, -150), "inside")

    # 9 baffle tabs
    tabs = None
    for a in P["TAB_ANG"]:
        tb = box(P["BAF_X"] - P["TAB_T"], P["BAF_X"], -P["TAB_W"] / 2, P["TAB_W"] / 2,
                 z + ri - P["TAB_H"], z + ri + 5)
        tb = rot_about_axis(tb, a, P) & inside
        tb = tb - rot_about_axis(cyl_x(4.5, P["BAF_X"] - P["TAB_T"] - 1, P["BAF_X"] + 1, 0, z + ri - 18), a, P)
        tabs = tb if tabs is None else tabs + tb
    add("tabs", "Baffle tabs (4)", tabs, 9, "steel", "cut, drill, weld inside", (0, 0, 0), "inside")

    # 10 hinge: fixed lugs on the shell ring, door lugs on the door ring, pin
    pin_c = lambda zz0, zz1, r: cyl_z(r, zz0, zz1, P["PIN_X"], P["PIN_Y"])  # noqa: E731
    lt = P["LUG_T"]
    fixed = None
    for zc in (z + 190.0, z - 205.0):
        lug = box(0, P["RING_T"], 420, 540, zc, zc + lt) + box(-36, 0, 452, 540, zc, zc + lt)
        lug = lug - cyl_x(P["RING_OD"] / 2, -1, P["RING_T"] + 1, 0, z) - pin_c(zc - 1, zc + lt + 1, P["PIN_D"] / 2 + 0.5)
        fixed = lug if fixed is None else fixed + lug
    door_lugs = None
    for zc in (z + 190.0 + lt + 2, z - 205.0 + lt + 2):
        lug = box(-36, dr1, 420, 540, zc, zc + lt) - cyl_x(P["RING_OD"] / 2, dr0 - 1, dr1 + 1, 0, z)
        lug = lug - pin_c(zc - 1, zc + lt + 1, P["PIN_D"] / 2 + 0.5)
        door_lugs = lug if door_lugs is None else door_lugs + lug
    pin = pin_c(z - 215, z + 235, P["PIN_D"] / 2) + pin_c(z + 235, z + 245, 16) + pin_c(z - 225, z - 215, 16)
    add("hinge_fixed", "Hinge lugs on the shell ring", fixed, 10, "steel", "plasma cut, drill, weld", (0, 200, 0))

    # door assembly (moves together)
    door_parts = [("door_ring", "Door flange ring", door_ring, 2, "steel", "plasma cut, weld"),
                  ("door_head", "Door head", door_head, 3, "steel", "buy, weld"),
                  ("door_lugs", "Hinge lugs on the door ring", door_lugs, 10, "steel", "plasma cut, drill, weld"),
                  ("pin", "Hinge pin", pin, 10, "steel", "cut, turn")]
    for key, nm, sh, bom, mat, proc in door_parts:
        if door_open and key != "pin":
            sh = Pos(P["PIN_X"], P["PIN_Y"], 0) * Rot(0, 0, 100) * Pos(-P["PIN_X"], -P["PIN_Y"], 0) * sh
        ex = (-450, 0, 0) if key != "pin" else (-450, 0, 300)
        add(key, nm, sh, bom, mat, proc, ex, "door")

    # 11 door gasket (glued to the shell ring face)
    gk = ring_x(P["GASKET_OD"] / 2, P["GASKET_ID"] / 2, -P["GASKET_T"], 0, z)
    add("gasket", "Door gasket", gk, 11, "epdm", "buy, cut, glue", (-180, 0, 0))

    # 12 latch clamps (bought) at top, window side and bottom
    latches = None
    for a in P["LATCH_ANG"]:
        body = box(-40, 36, -20, 20, z + 490, z + 520)
        hook = box(-40, dr0, -15, 15, z + 455, z + 490)
        foot = box(P["RING_T"], 36, -15, 15, z + 440, z + 490)
        lt_ = body + hook + foot
        latches = rot_about_axis(lt_, a - 90.0, P) if latches is None else latches + rot_about_axis(lt_, a - 90.0, P)
    add("latches", "Latch clamps (3)", latches, 12, "steel", "buy, bolt on", (-200, 0, 0), bought_mass=3 * 0.8)

    # 13 window, 14 spacer and clamp rings, window gasket
    wg0, wg1 = L["wg"]
    wgk = ring_y(P["WG_OD"] / 2, P["WG_ID"] / 2, wg0, wg1, P["WIN_X"], z)
    add("win_gasket", "Window gasket", wgk, 11, "epdm", "buy, cut", (0, -480, 0), "window")
    w0, w1 = L["win"]
    win = cyl_y(P["WIN_D"] / 2, w0, w1, P["WIN_X"], z)
    add("window", "Polycarbonate window", win, 13, "pc", "cut, edge finish", (0, -560, 0), "window")
    s0, s1 = L["wsp"]
    sp = ring_y(P["WF_OD"] / 2, P["WSP_ID"] / 2, s0, s1, P["WIN_X"], z) - \
        bolt_holes_y(P, P["WB_PCD"], P["WB_N"], P["WB_D"], s0, s1, P["WIN_X"], z)
    add("win_spacer", "Window spacer ring", sp, 14, "steel", "plasma cut, drill", (0, -640, 0), "window")
    c0, c1 = L["wcl"]
    cl = ring_y(P["WF_OD"] / 2, P["WCL_ID"] / 2, c0, c1, P["WIN_X"], z) - \
        bolt_holes_y(P, P["WB_PCD"], P["WB_N"], P["WB_D"], c0, c1, P["WIN_X"], z)
    add("win_clamp", "Window clamp ring", cl, 14, "steel", "plasma cut, drill", (0, -720, 0), "window")

    # 15 feed-through plate with cable glands
    g0, g1 = L["fg"]
    fgk = ring_y(P["FF_OD"] / 2 - 10, P["FF_ID"] / 2 + 6, g0, g1, P["FT_X"], z)
    add("ft_gasket", "Feed-through gasket", fgk, 11, "epdm", "buy, cut", (0, -420, 0), "window")
    p0, p1 = L["fp"]
    fp = cyl_y(P["FF_OD"] / 2, p0, p1, P["FT_X"], z) - bolt_holes_y(P, 225.0, 8, P["WB_D"], p0, p1, P["FT_X"], z)
    glands = None
    for dx, dz in ((-35, 30), (35, 30), (-35, -30), (35, -30), (0, 0)):
        gl = cyl_y(12, p0 - 28, p0, P["FT_X"] + dx, z + dz) + cyl_y(10, p1, p1 + 12, P["FT_X"] + dx, z + dz)
        fp = fp - cyl_y(10, p0 - 1, p1 + 1, P["FT_X"] + dx, z + dz)
        glands = gl if glands is None else glands + gl
    add("ft_plate", "Feed-through plate with glands", fp + glands, 15, "al", "cut, drill, fit glands", (0, -520, 0), "window")

    # 16 deck plate
    dk = box(x0, x1, -P["DECK_W"] / 2, P["DECK_W"] / 2, P["DECK_Z"], L["deck_top"])
    for xx in (x0 + 50, (x0 + x1) / 2, x1 - 50):
        for sgn in (1, -1):
            dk = dk - cyl_z(4.5, P["DECK_Z"] - 1, L["deck_top"] + 1, xx, sgn * (P["RAIL_Y"] + 19))
    sx0, sx1, shw, st = P["SB"]
    for xx in (sx0 + 20, sx1 - 20):
        for yy in (-shw + 20, shw - 20):
            dk = dk - cyl_z(3.4, P["DECK_Z"] - 1, L["deck_top"] + 1, xx, yy)
    add("deck", "Deck plate", dk, 16, "al", "cut, drill, tap", (0, 0, 300), "inside")

    # 17 baffle plate
    baf = cyl_x(P["BAF_D"] / 2, P["BAF_X"], P["BAF_X"] + P["BAF_T"], 0, z)
    for a in P["TAB_ANG"]:
        baf = baf - rot_about_axis(cyl_x(4.5, P["BAF_X"] - 1, P["BAF_X"] + P["BAF_T"] + 1, 0, z + ri - 18), a, P)
    # the model is a plain disc; its mass counts only the solid share of the perforated sheet
    baf_mass = baf.volume * 1e-9 * P["RHO"]["steel"] * (1 - baffle_open(P))
    add("baffle", "Baffle plate (perforated)", baf, 17, "steel", "buy perforated sheet, cut, drill", (350, 0, 0), "inside",
        bought_mass=baf_mass)

    # 18 to 25 thrust stand
    dt = L["deck_top"]
    sb = box(sx0, sx1, -shw, shw, dt, L["sb_top"])
    for xx in (sx0 + 20, sx1 - 20):
        for yy in (-shw + 20, shw - 20):
            sb = sb - cyl_z(4.5, dt - 1, L["sb_top"] + 1, xx, yy)
    add("stand_base", "Stand base plate", sb, 18, "al", "cut, drill, tap", (0, 0, 120), "stand")

    cx, cy, cz = P["CLAMP"]
    lz0, lz1 = L["leaf_z"]
    leaves, clamps = None, None
    for lx in P["LEAF_X"]:
        lf = box(lx - P["LEAF_T"] / 2, lx + P["LEAF_T"] / 2, -P["LEAF_W"] / 2, P["LEAF_W"] / 2, lz0, lz1)
        leaves = lf if leaves is None else leaves + lf
        for zz0, zz1 in (L["clamp_bot"], L["clamp_top"]):
            cb = box(lx - cx / 2, lx + cx / 2, -cy / 2, cy / 2, zz0, zz1) - lf
            for yy in (-55, 55):
                cb = cb - cyl_x(2.75, lx - cx / 2 - 1, lx + cx / 2 + 1, yy, (zz0 + zz1) / 2)
            clamps = cb if clamps is None else clamps + cb
    add("leaves", "Flexure leaves (2)", leaves, 19, "spring", "cut from shim, drill", (0, 0, 220), "stand")
    add("clamps", "Flexure clamps (4)", clamps, 19, "al", "cut, slit, drill", (0, 0, 220), "stand")

    cx0, cx1, chw, ct = P["CAR"]
    car = box(cx0, cx1, -chw, chw, L["car_z"][0], L["car_z"][1])
    add("carriage", "Carriage plate", car, 21, "al", "cut, drill, tap", (0, 0, 360), "stand")

    ct_, cl_ = P["CELL_T"]
    anchor = box(270, 300, -20, 20, L["sb_top"], L["sb_top"] + 58)
    cell_z0 = L["sb_top"] + 3
    cell = box(300, 300 + ct_, -ct_ / 2, ct_ / 2, cell_z0, cell_z0 + cl_)
    hanger = box(300 + ct_, 340, -20, 20, L["sb_top"] + 58, L["car_z"][0])
    add("anchor", "Thrust cell anchor block", anchor, 20, "al", "cut, drill, tap", (0, 0, 120), "stand")
    add("thrust_cell", "Thrust load cell", cell, 24, "al", "buy", (-120, 0, 180), "stand", bought_mass=0.06)
    add("hanger", "Thrust cell hanger", hanger, 20, "al", "cut, drill, tap", (0, 0, 420), "stand")

    hx0, hx1, hhw, hz1 = P["HOUS"]
    hous = box(hx0, hx1, -hhw, hhw, L["car_z"][1], hz1) - cyl_x(P["BRG_OD"] / 2, hx0 - 1, hx1 + 1, 0, z)
    brgs = (ring_x(P["BRG_OD"] / 2, P["SHAFT_D"] / 2, hx0, hx0 + P["BRG_W"], z) +
            ring_x(P["BRG_OD"] / 2, P["SHAFT_D"] / 2, hx1 - P["BRG_W"], hx1, z))
    add("housing", "Torque head housing", hous, 22, "al", "cut, bore, drill, tap", (0, 0, 480), "stand")
    add("bearings", "Bearings (2)", brgs, 22, "steel", "buy, press in", (0, 0, 480), "stand", bought_mass=0.09)
    shaft = cyl_x(P["SHAFT_D"] / 2, P["SHAFT_X"][0], P["SHAFT_X"][1], 0, z) + \
        cyl_x(P["HUB"][2] / 2, P["HUB"][0], P["HUB"][1], 0, z)
    add("shaft", "Torque shaft and hub", shaft, 22, "steel", "turn, drill, tap", (250, 0, 480), "stand")
    mp = cyl_x(P["MPLATE"][2] / 2, P["MPLATE"][0], P["MPLATE"][1], 0, z)
    add("mplate", "Motor plate", mp, 22, "al", "cut, drill", (330, 0, 480), "stand")

    ax0, ax1 = P["ARM_X"]
    arm = (cyl_x(P["ARM_HUB"] / 2, ax0, ax1, 0, z) + box(ax0, ax1, 8, P["ARM_REACH"] + 6, z - 10, z + 6)) - \
        cyl_x(P["SHAFT_D"] / 2, ax0 - 1, ax1 + 1, 0, z)
    tc = box(330, 330 + cl_, P["ARM_REACH"] - ct_ / 2, P["ARM_REACH"] + ct_ / 2, z - 10 - ct_, z - 10)
    tcb = box(385, 425, hhw, P["ARM_REACH"] + ct_ / 2, z - 55, z - 10 - ct_)
    add("arm", "Torque arm", arm - cyl_x(P["SHAFT_D"] / 2, ax0 - 1, ax1 + 1, 0, z), 23, "al", "cut, bore, slit", (-150, 0, 480), "stand")
    add("torque_cell", "Torque load cell", tc, 24, "al", "buy", (-150, 150, 480), "stand", bought_mass=0.05)
    add("tc_bracket", "Torque cell bracket", tcb, 23, "al", "cut, drill, tap", (0, 150, 480), "stand")

    post = box(466, 482, -10, 10, L["sb_top"], 670) + box(482, 490, -10, 10, 650, 670)
    add("speed_post", "Speed sensor post and sensor", post, 25, "al", "cut, drill; buy sensor", (0, -150, 120), "stand")

    m0, m1, md = P["MOTOR"]
    motor = cyl_x(md / 2, m0, m1, 0, z) + cyl_x(6, m1, P["PROP_X"] - 10, 0, z)
    add("motor", "Motor under test (example)", motor, 26, "steel", "buy", (420, 0, 480), "test", bought_mass=0.33)
    hub = cyl_x(15, P["PROP_X"] - 10, P["PROP_X"] + 10, 0, z)
    blades = None
    R = P["PROP_D"] / 2
    for sgn in (1, -1):
        bl = box(-2.5, 2.5, -16, 16, 14, R)                     # blade along +Z, pitched 18 deg about Z
        bl = Pos(P["PROP_X"], 0, z) * Rot(20 if sgn > 0 else 200, 0, 0) * (Rot(0, 0, 18) * bl)
        blades = bl if blades is None else blades + bl
    add("prop", "Propeller under test (example, 380 mm)", hub + blades, 27, "pc", "buy", (520, 0, 480), "test",
        bought_mass=0.05)

    # 31 sensor box on the deck (pressure, temperature, humidity)
    sens = box(700, 760, 100, 160, dt, dt + 25)
    add("sensors", "Air sensor box", sens, 31, "pc", "buy, print housing", (0, 0, 200), "inside", bought_mass=0.1)

    # 28 valve manifold on the stub flange
    mz = P["MN_TOP"] + P["MF_T"]
    mx = P["MN_X"]
    vm = box(mx - 40, mx + 40, -40, 40, mz, mz + 50)
    vm = vm + cyl_z(20, mz + 50, mz + 120, mx, 0)                                   # vacuum relief valve
    vm = vm + cyl_y(6, -60, -40, mx, mz + 40) + cyl_y(32, -90, -60, mx, mz + 40)     # gauge on the window side
    vm = vm + cyl_x(10, mx + 40, mx + 80, 0, mz + 25) + box(mx + 80, mx + 110, -15, 15, mz + 10, mz + 40)  # bleed valve
    vm = vm + cyl_y(10, 40, 70, mx, mz + 25)                                        # pump port
    add("manifold", "Valve manifold", vm, 28, "steel", "buy fittings, assemble", (0, 0, 450), "outside", bought_mass=3.5)

    # 29 vacuum pump and hose
    px0, px1, py0, py1, ph = P["PUMP"]
    pump = box(px0, px1, py0, py1, 0, ph) + cyl_x(55, px0 - 120, px0, (py0 + py1) / 2, 100)
    hz = mz + 25
    hy = (py0 + py1) / 2
    hose = cyl_y(P["HOSE_D"] / 2, 70, hy, mx, hz) + cyl_z(P["HOSE_D"] / 2, ph, hz + P["HOSE_D"] / 2, mx, hy)
    add("pump", "Vacuum pump", pump, 29, "steel", "buy", (300, 300, 0), "outside", bought_mass=11.0)
    add("hose", "Vacuum hose", hose, 29, "epdm", "buy, cut", (300, 300, 0), "outside", bought_mass=0.8)

    # 30 control cabinet with emergency stop
    cx0_, cx1_, cy0_, cy1_, ch = P["CAB"]
    cab = box(cx0_, cx1_, cy0_, cy1_, 0, ch) + cyl_y(25, cy0_ - 30, cy0_, (cx0_ + cx1_) / 2, ch - 150)
    add("cabinet", "Control and power cabinet", cab, 30, "steel", "buy, fit out", (-200, -200, 0), "outside",
        bought_mass=45.0)
    return C


def by_key(P=PARAMS, **kw):
    return {c.key: c for c in components(P, **kw)}


def mass_kg(c, P=PARAMS):
    if c.bought_mass is not None:
        return c.bought_mass
    return c.shape.volume * 1e-9 * P["RHO"][c.material]


# ---------------------------------------------------------------- checks
def check(P=PARAMS, tol=1.0):
    """Every pair of components that overlaps by more than tol mm3, and any part with no volume."""
    C = components(P)
    bad = []
    bbs = [c.shape.bounding_box() for c in C]
    for i, a in enumerate(C):
        if a.shape.volume < 1.0:
            bad.append((a.key, "no volume", 0.0))
        for j in range(i + 1, len(C)):
            b = C[j]
            A, B = bbs[i], bbs[j]
            if A.max.X < B.min.X or B.max.X < A.min.X or A.max.Y < B.min.Y or B.max.Y < A.min.Y or \
                    A.max.Z < B.min.Z or B.max.Z < A.min.Z:
                continue
            v = (a.shape & b.shape).volume
            if v > tol:
                bad.append((a.key, b.key, round(v, 1)))
    # baffle sheet (decision 41B): at least 80 % open, and the bars between holes no thinner than the sheet
    if baffle_open(P) < P["BAF_OPEN"] - 1e-3:
        bad.append(("baffle", "open area below BAF_OPEN", round(baffle_open(P), 3)))
    if P["BAF_PITCH"] - P["BAF_HOLE"] < P["BAF_T"]:
        bad.append(("baffle", "bar between holes thinner than the sheet", P["BAF_PITCH"] - P["BAF_HOLE"]))
    return bad


def clearances(P=PARAMS):
    """Gaps that matter, mm."""
    L = levels(P)
    out = {
        "prop tip to shell inside": L["ri"] - P["PROP_D"] / 2,
        "prop tip to deck top": P["Z_AX"] - P["PROP_D"] / 2 - L["deck_top"],
        "prop plane to speed sensor face": P["PROP_X"] - 5 - 490.0,
        "prop plane to baffle": P["BAF_X"] - P["PROP_X"],
        "door ring face to prop plane": P["PROP_X"],
        "window edge off the prop plane, deg": L["burst_half_angle"],
        "feed-through edge off the prop plane, deg": L["burst_half_angle_ft"],
        "baffle to rear head tip": L["rear_tip"] - P["BAF_X"],
        "vessel inside diameter / propeller diameter": 2 * L["ri"] / P["PROP_D"],
    }
    return out


def assembly(P=PARAMS, door_open=False):
    return Compound([c.shape for c in components(P, door_open=door_open)])


def main():
    C = components()
    bad = check()
    print("overlaps:", bad if bad else "none")
    tot = 0.0
    for c in C:
        m = mass_kg(c)
        tot += m
        print(f"{c.bom:3d} {c.name:42s} {m:8.2f} kg")
    print(f"total mass {tot:.0f} kg")
    for k, v in clearances().items():
        print(f"{k}: {v:.1f}")
    if "--check" in sys.argv:
        return
    step_dir, stl_dir = ROOT / "cad" / "step", ROOT / "cad" / "stl"
    step_dir.mkdir(parents=True, exist_ok=True)
    stl_dir.mkdir(parents=True, exist_ok=True)
    export_step(Compound([c.shape for c in C]), str(step_dir / "altirig-assembly.step"))
    export_step(Compound([c.shape for c in C if c.group in ("vessel", "door", "window", "inside")]),
                str(step_dir / "altirig-vessel.step"))
    export_step(Compound([c.shape for c in C if c.group in ("stand", "test")]), str(step_dir / "altirig-stand.step"))
    export_stl(Compound([c.shape for c in C if c.group == "stand"]), str(stl_dir / "altirig-stand.stl"),
               tolerance=0.05, angular_tolerance=0.2)
    export_stl(Compound([c.shape for c in C]), str(stl_dir / "altirig-assembly.stl"), tolerance=1.0, angular_tolerance=0.35)
    print("exported STEP and STL")


if __name__ == "__main__":
    main()
