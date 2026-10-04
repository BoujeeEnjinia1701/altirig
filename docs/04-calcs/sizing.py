"""AltiRig sizing calculations (ALR-CAL-001), TRL 3.

Run from the repo root:  python docs/04-calcs/sizing.py
Prints every result and writes docs/04-calcs/results.csv. Dimensions come from cad/src/model.py
(PARAMS and levels()), prices from bom/bom.csv. Every assumption is stated where it is used.
Hand calculations for a concept on paper; not a pressure vessel design to any code.
"""
from __future__ import annotations

import csv
import math
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "cad" / "src"))
from model import PARAMS as P, levels  # noqa: E402

L = levels(P)
R_AIR = 287.05          # J/(kg K), dry air
P0 = 101325.0           # Pa, sea-level standard pressure
G = 9.81
E_ST, NU_ST, SY_ST = 200e9, 0.3, 235e6      # S235/A36-class steel: modulus, Poisson, minimum yield (assumption)
E_PC, NU_PC, SY_PC = 2.3e9, 0.37, 62e6      # polycarbonate (assumption, typical sheet data)
rows = []


def out(sec, name, value, unit, req="", note=""):
    rows.append(dict(section=sec, quantity=name, value=value, unit=unit, requirement=req, note=note))
    v = f"{value:,.4g}" if isinstance(value, float) else str(value)
    print(f"[{sec}] {name}: {v} {unit} {('(' + req + ')') if req else ''} {note}")
    return value


def isa(h):
    T = 288.15 - 0.0065 * h
    p = P0 * (T / 288.15) ** 5.25588
    return T, p, p / (R_AIR * T)


# ------------------------------------------------------------------ A. density targets (R1)
T5, p5, rho5 = isa(5000.0)
T6, p6, rho6 = isa(6000.0)
rho_sl = isa(0.0)[2]
out("A", "ISA 5,000 m: temperature", T5 - 273.15, "C")
out("A", "ISA 5,000 m: pressure", p5 / 1000, "kPa")
out("A", "ISA 5,000 m: density", rho5, "kg/m3", "R1")
out("A", "ISA 6,000 m: density", rho6, "kg/m3")
out("A", "5,000 m density as a share of sea level", rho5 / rho_sl * 100, "%")
for tc in (15.0, 20.0, 25.0, 30.0):
    out("A", f"Chamber pressure for 5,000 m density at {tc:.0f} C", rho5 * R_AIR * (tc + 273.15) / 1000, "kPa", "R1")
p_r1 = rho5 * R_AIR * 293.15
out("A", "Density at 54.0 kPa and 20 C (pressure match, not density match)", p5 / (R_AIR * 293.15), "kg/m3",
    note="equals about 6,100 m: matching pressure at room temperature overshoots the density")
p_6k30 = rho6 * R_AIR * 303.15
out("A", "Chamber pressure for 6,000 m density at 30 C (lowest working pressure needed)", p_6k30 / 1000, "kPa")
dp_r1 = P0 - p_r1
dp_work = P0 - 46.3e3
dp_design = P0
out("A", "Pressure difference at the R1 point (5,000 m density, 20 C)", dp_r1 / 1000, "kPa")
out("A", "Relief valve setting: lowest chamber pressure 46.3 kPa, difference", dp_work / 1000, "kPa", "R12")
out("A", "Design pressure difference for the vessel (full vacuum)", dp_design / 1000, "kPa", "R7",
    "conservative: the pump can reach near full vacuum if the relief valve sticks")

# ------------------------------------------------------------------ B. vessel strength (R7)
D, t, Ls = P["SH_OD"] / 1000, P["SH_T"] / 1000, P["SH_L"] / 1000
h_head = (P["HEAD_DEPTH"] + P["SH_T"]) / 1000
L_eff = Ls + 2 * P["HEAD_SKIRT"] / 1000 + 2 * h_head / 3      # ASME practice: skirt plus a third of each head depth
td = t / D
p_el = 2.42 * E_ST * td ** 2.5 / ((1 - NU_ST ** 2) ** 0.75 * (L_eff / D - 0.45 * td ** 0.5))
p_long = 2 * E_ST / (1 - NU_ST ** 2) * td ** 3
p_y = 2 * SY_ST * td
KD = 0.5      # knock-down for out-of-roundness up to 1 % and residual weld stresses (assumption)
p_col = min(KD * p_el, p_y)
out("B", "Shell: unsupported length used (skirts plus a third of each head)", L_eff * 1000, "mm")
out("B", "Shell: elastic buckling pressure (Windenburg and Trilling)", p_el / 1000, "kPa")
out("B", "Shell: long-cylinder lower bound (no end support)", p_long / 1000, "kPa")
out("B", "Shell: plastic collapse pressure 2 x yield x t/D", p_y / 1000, "kPa")
out("B", "Shell: predicted collapse with 0.5 knock-down", p_col / 1000, "kPa")
sf_shell = out("B", "Shell: collapse factor at full vacuum", p_col / dp_design, "", "R7", "target at least 4")
sf_shell_long = out("B", "Shell: factor at full vacuum even with no end support at all (long-cylinder bound x 0.5)",
                    0.5 * p_long / dp_design, "")
R_sph = 0.9 * D
p_head = 0.25 * 1.21 * E_ST * (t / R_sph) ** 2       # classical sphere x 0.25 knock-down (assumption)
p_head_y = 2 * SY_ST * t / R_sph
out("B", "Heads: equivalent sphere radius 0.9 D", R_sph * 1000, "mm")
sf_head = out("B", "Heads: collapse factor at full vacuum", min(p_head, p_head_y) / dp_design, "", "R7")
# opening reinforcement (area replacement, simplified UG-37 for external pressure), heavy-wall set-in nozzles
t_r = t * (dp_design * 4 / p_col) ** (1 / 2.5)    # shell thickness that would just give a factor 4
out("B", "Openings: shell thickness needed for factor 4", t_r * 1000, "mm")
for label, od, tn_ in (("Window", P["WN_OD"], P["WN_T"]), ("Feed-through", P["FN_OD"], P["FN_T"])):
    d_open = (od - 2 * tn_) / 1000
    A_req = 0.5 * d_open * t_r
    A_shell = d_open * (t - t_r)
    h_out = min(2.5 * t, 2.5 * tn_ / 1000)
    h_in = min(2.5 * t, (math.sqrt(L["ri"] ** 2 - (od / 2) ** 2) - P["SET_IN"]) / 1000)   # shortest set-in length
    A_noz = 2 * (h_out + max(h_in, 0.0)) * tn_ / 1000
    out("B", f"{label} opening: area to replace", A_req * 1e6, "mm2")
    out("B", f"{label} opening: area available (shell excess, nozzle wall outside and set-in) / needed",
        (A_shell + A_noz) / A_req, "", "R7", "at least 1; no pad needed")
# window plate
a_w = P["WG_OD"] / 2 / 1000         # simply supported at the gasket's outer edge (conservative)
tw = P["WIN_T"] / 1000
sig_w = 3 * (3 + NU_PC) * dp_design * a_w ** 2 / (8 * tw ** 2)
Dw = E_PC * tw ** 3 / (12 * (1 - NU_PC ** 2))
w_w = dp_design * a_w ** 4 * (5 + NU_PC) / (64 * Dw * (1 + NU_PC))
out("B", "Window: span radius (gasket outer edge, simply supported)", a_w * 1000, "mm")
out("B", "Window: bending stress at full vacuum", sig_w / 1e6, "MPa")
sf_win = out("B", "Window: factor on yield at full vacuum", SY_PC / sig_w, "", "R7", "rule used: at least 6 for plastic windows")
out("B", "Window: centre deflection at full vacuum", w_w * 1000, "mm")
# feed-through plate (aluminium, simply supported)
a_f = (P["FF_ID"] / 2 + 6) / 1000
sig_f = 3 * (3 + 0.33) * dp_design * a_f ** 2 / (8 * (P["FP_T"] / 1000) ** 2)
out("B", "Feed-through plate: bending stress at full vacuum (holes ignored)", sig_f / 1e6, "MPa", note="6082-T6 yield 250 MPa")
# door load and gasket
r_g = (P["GASKET_ID"] + P["GASKET_OD"]) / 4 / 1000
A_g = math.pi * r_g ** 2
F_r1 = dp_r1 * A_g
F_full = dp_design * A_g
out("B", "Door: area inside the gasket line", A_g, "m2")
out("B", "Door: force holding it shut at the R1 point", F_r1 / 1000, "kN", "R11", "about 2.5 t: it cannot be opened under vacuum")
out("B", "Door: force at full vacuum", F_full / 1000, "kN")
out("B", "Door: force at only 2 kPa below atmosphere", 2000 * A_g / 1000, "kN", "R11")
A_gk = math.pi * ((P["GASKET_OD"] / 2000) ** 2 - (P["GASKET_ID"] / 2000) ** 2)
out("B", "Door gasket: bearing stress at full vacuum", F_full / A_gk / 1e6, "MPa", note="sponge closes fully; rings take the load")
F_seal = 0.05e6 * A_gk          # closed-cell sponge, about 25 % compression at 0.05 MPa (assumption)
out("B", "Latches: force to compress the sponge 25 % for the first seal", F_seal / 1000, "kN")
out("B", "Latches: force each (3 latches)", F_seal / 3000, "kN", note="latches rated at least 3 kN")
# hinge
m_door = 72.0
M_h = m_door * G * (P["PIN_Y"] / 1000)
F_lug = M_h / 0.395
out("B", "Hinge: door mass carried", m_door, "kg")
out("B", "Hinge: horizontal force at each lug pair", F_lug, "N", note="20 mm pin and 15 mm lugs: stresses under 10 MPa")

# ------------------------------------------------------------------ C. volume and pump-down (R8)
ri = L["ri"] / 1000
V_cyl = math.pi * ri ** 2 * Ls
V_heads = 2 * (2 / 3) * math.pi * ri ** 2 * (P["HEAD_DEPTH"] / 1000)
V_sk = 2 * math.pi * ri ** 2 * (P["HEAD_SKIRT"] / 1000) + math.pi * ri ** 2 * P["GASKET_T"] / 1000
V_noz = math.pi * ((P["WN_OD"] / 2 - P["WN_T"]) / 1000) ** 2 * 0.13 + math.pi * ((P["FN_OD"] / 2 - P["FN_T"]) / 1000) ** 2 * 0.11
V = V_cyl + V_heads + V_sk + V_noz - 0.012            # less the volume of the parts inside (about 12 L)
out("C", "Chamber free volume", V, "m3")
S_nom = 170.0 / 60000                                 # 6 CFM pump, m3/s
S_eff = 0.85 * S_nom                                  # speed at 50 to 100 kPa inlet, after hose and filter (assumption)
t54 = V / S_eff * math.log(P0 / p5)
t62 = V / S_eff * math.log(P0 / p_r1)
out("C", "Pump speed used (85 % of 170 L/min)", S_eff * 60000, "L/min")
out("C", "Pump-down time to 54.0 kPa", t54 / 60, "min", "R8")
out("C", "Pump-down time to the R1 density at 20 C (61.9 kPa)", t62 / 60, "min")
leak = 0.2 / 60000 * 1                                # allowed leak inflow 0.2 L/min of free air (assumption)
out("C", "Leak allowance (free air)", 0.2, "L/min", note="equivalent pressure rise about 0.3 kPa/min at 54 kPa")
Cd, A_b = 0.6, math.pi * 0.003 ** 2
mdot = Cd * A_b * P0 * math.sqrt(1.4 / (R_AIR * 293.15)) * (2 / 2.4) ** 3
dm = V * (P0 - p5) / (R_AIR * 293.15)
out("C", "Vent time through the 6 mm bleed orifice from 54 kPa to ambient", dm / mdot, "s", "R11")

# ------------------------------------------------------------------ D. air heating and density control (R2)
P_el_max = 1500.0
A_wall = math.pi * D * Ls + 2 * 1.084 * D ** 2
h_c = 30.0                                            # W/(m2 K), recirculating flow over the wall (assumption)
m_air = rho5 * V
dT_air = P_el_max / (h_c * A_wall)
tau_air = m_air * 1005 / (h_c * A_wall)
m_steel = 470.0
out("D", "Inside wall area", A_wall, "m2")
out("D", "Air mass at 5,000 m density", m_air, "kg")
out("D", "Air temperature rise above the wall at 1,500 W", dT_air, "K")
out("D", "Air thermal time constant", tau_air, "s")
out("D", "Wall warming rate at 1,500 W", P_el_max / (m_steel * 460) * 60, "K/min")
out("D", "Pressure rise the controller must make to hold density as the air warms", dT_air / 293.15 * 100, "%")
e_p = 50.0 / p_r1 * 100
e_T = 0.15 / 293.15 * 100
e_nu = 1.5 / 293.15 * 100            # spatial spread of air temperature in the wake, +/- 1.5 K (assumption)
e_rh = 0.07
e_ctl = 0.3                           # control band of the bleed valve loop (assumption)
e_tot = math.sqrt(e_p ** 2 + e_T ** 2 + e_nu ** 2 + e_rh ** 2 + e_ctl ** 2)
out("D", "Density error: pressure sensor (50 Pa)", e_p, "%")
out("D", "Density error: temperature probe (0.15 K)", e_T, "%")
out("D", "Density error: air temperature spread (1.5 K)", e_nu, "%")
out("D", "Density error: humidity correction", e_rh, "%")
out("D", "Density error: control band", e_ctl, "%")
out("D", "Density error: root sum square", e_tot, "%", "R2", "target within 1 %")

# ------------------------------------------------------------------ E. propeller loads and the stand (R3, R4, R5)
Dp = P["PROP_D"] / 1000
CT0, CP0 = 0.10, 0.042        # static coefficients of a 15 x 5 two-blade propeller (assumption, UIUC static data range)
A_p = math.pi * Dp ** 2 / 4
rho_room = isa(0.0)[1] / (R_AIR * 293.15)
for label, rho in (("sea level, 20 C", rho_room), ("5,000 m density", rho5)):
    n = math.sqrt(50.0 / (CT0 * rho * Dp ** 4))
    Pm = CP0 * rho * n ** 3 * Dp ** 5
    Q = Pm / (2 * math.pi * n)
    out("E", f"50 N with the example propeller, {label}: speed", n * 60, "rpm")
    out("E", f"50 N with the example propeller, {label}: shaft power", Pm, "W")
    out("E", f"50 N with the example propeller, {label}: torque", Q, "N m", "R4")
    out("E", f"50 N, {label}: tip speed", math.pi * Dp * n, "m/s")
n5 = math.sqrt(50.0 / (CT0 * rho5 * Dp ** 4))
P5 = CP0 * rho5 * n5 ** 3 * Dp ** 5
eta = 0.80
T_supply = 50.0 * (P_el_max * eta / P5) ** (2 / 3)
out("E", "Electrical power for 50 N at 5,000 m density (motor and ESC 80 %)", P5 / eta, "W")
out("E", "Thrust the 1,500 W supply allows with the example propeller at 5,000 m density", T_supply, "N",
    note="stand range is 50 N; a larger supply is needed only for the heaviest propellers")
n_ex = 6000 / 60
c75 = 0.030
mu = 1.81e-5
for label, rho in (("sea level", rho_room), ("5,000 m", rho5)):
    Re = rho * (0.75 * math.pi * Dp * n_ex) * c75 / mu
    out("E", f"Blade Reynolds number at 0.75 R, 6,000 rpm, {label}", Re, "")
# flexure stand
E_sp = 200e9
b_l, t_l, L_l = P["LEAF_W"] / 1000, P["LEAF_T"] / 1000, P["LEAF_FREE"] / 1000
I_l = b_l * t_l ** 3 / 12
k_leaf = 12 * E_sp * I_l / L_l ** 3
k_flex = 2 * k_leaf
k_cell = 98.1 / 0.25e-3          # 10 kg bar cell, about 0.25 mm full-scale deflection (assumption)
share = k_flex / (k_flex + k_cell)
x_fs = 50.0 / (k_flex + k_cell)
sig_l = 3 * E_sp * t_l * x_fs / L_l ** 2
m_carried = 4.7
P_cr = 2 * math.pi ** 2 * E_sp * I_l / L_l ** 2
out("E", "Flexures: stiffness of the two leaves together", k_flex / 1000, "N/mm")
out("E", "Flexures: share of thrust carried by the leaves (calibrated out)", share * 100, "%", "R3")
out("E", "Flexures: carriage movement at 50 N", x_fs * 1000, "mm")
out("E", "Flexures: leaf bending stress at 50 N", sig_l / 1e6, "MPa")
out("E", "Flexures: buckling load of the leaves / weight carried", P_cr / (m_carried * G), "")
M_pitch = 50.0 * (P["Z_AX"] - (L["sb_top"] + 3 + 70)) / 1000
out("E", "Flexures: pitching moment from thrust above the cell", M_pitch, "N m", note="taken as tension and compression in the leaves")
e3 = math.sqrt((0.05 / 100 * 98.1) ** 2 + 0.1 ** 2 + (0.02 / 100 * 98.1) ** 2 + 0.05 ** 2 + (0.1 / 100 * 50) ** 2)
out("E", "Thrust error budget (cell 0.05 % of 98 N, cable drag 0.1 N, zero drift, masses, flexure 0.1 %)", e3, "N", "R3")
out("E", "Thrust error as a share of 50 N", e3 / 50 * 100, "%", "R3", "target no more than 1 %")
r_arm = P["ARM_REACH"] / 1000
F_tc = 2.0 / r_arm
out("E", "Torque cell load at 2 N m", F_tc, "N", "R4", "5 kg cell, 49 N")
Q_brg = 0.0015 * 50.0 * 0.015 / 2 * 2
e4 = math.sqrt((0.05 / 100 * 49.05 * r_arm) ** 2 + Q_brg ** 2 + 0.005 ** 2 + (0.1 / 100 * 2) ** 2)
out("E", "Bearing friction torque at 50 N thrust", Q_brg, "N m")
out("E", "Torque error budget", e4, "N m", "R4")
out("E", "Torque error as a share of 2 N m", e4 / 2 * 100, "%", "R4", "target within 2 %")
f_pulse = 2 * 11000 / 60
out("E", "Speed: blade-pass rate at 11,000 rpm", f_pulse, "Hz")
out("E", "Speed: timing error with a 1 microsecond timer, one revolution", 1e-6 * 11000 / 60 * 100, "%", "R4")
out("E", "Propeller tip to shell inside", L["ri"] - P["PROP_D"] / 2, "mm", "R5")
out("E", "Propeller tip to deck", P["Z_AX"] - P["PROP_D"] / 2 - L["deck_top"], "mm", "R5")
out("E", "Window edge from the propeller plane", L["burst_half_angle"], "deg", "R11", "outside the 15 deg fragment zone")
out("E", "Feed-through edge from the propeller plane", L["burst_half_angle_ft"], "deg", "R11")
tip_max = math.pi * Dp * n5
m_frag = 0.025
out("E", "Energy of a half blade (25 g) released at 50 N, 5,000 m density", 0.5 * m_frag * (0.6 * tip_max) ** 2, "J",
    note="6.35 mm steel shell contains it")

# ------------------------------------------------------------------ F. chamber effect (R6)
Av = math.pi * ri ** 2
ar = A_p / Av
f = P["BAF_OPEN"]
K_plate = (0.707 * (1 - f) ** 0.375 + 1 - f) ** 2 / f ** 2      # thin perforated plate (Idelchik)
K_baf = 2 * K_plate * ar ** 2                                  # crossed twice, referred to disc velocity
K_turn = 2 * 1.0 * (ar / (1 - ar)) ** 2                        # two 180 deg turns at the return velocity
out("F", "Disc area / chamber section", ar, "")
out("F", "Vessel inside diameter / propeller diameter", 2 * ri / Dp, "")
out("F", f"Baffle loss coefficient ({f * 100:.0f} % open, at the section velocity; ALR-DDR-003)", K_plate, "")


def chamber_effect(Kx, rho=rho_room, n=None):
    """Thrust ratio chamber / open air at the same speed (linear blade model) and at the same power."""
    n = n or math.sqrt(50.0 / (CT0 * rho * Dp ** 4))
    T0 = 50.0
    v0 = math.sqrt(T0 / (2 * rho * A_p))
    vb = n * P["PROP_PITCH_IN"] * 0.0254 * 1.0      # blades unload near the pitch speed (assumption)
    Tb = T0 / (1 - v0 / vb)
    a = (2 + Kx / 2) * rho * A_p
    v = (-Tb / vb + math.sqrt((Tb / vb) ** 2 + 4 * a * Tb)) / (2 * a)
    same_speed = a * v ** 2 / T0
    same_power = (1 + Kx / 4) ** (1 / 3)
    return same_speed, same_power


for label, Kx in (("with the baffle", K_baf + K_turn), ("baffle removed", K_turn)):
    r_s, r_p = chamber_effect(Kx)
    out("F", f"Extra loop loss, {label}", Kx, "dynamic heads")
    out("F", f"Chamber thrust excess, {label}: same power model", (r_p - 1) * 100, "%", "R6")
    out("F", f"Chamber thrust excess, {label}: same speed model", (r_s - 1) * 100, "%", "R6", "target within 5 %")
f63 = 0.63                                                    # the TRL 3 baffle replaced by ALR-DDR-003
K63 = (0.707 * (1 - f63) ** 0.375 + 1 - f63) ** 2 / f63 ** 2
r_s63, r_p63 = chamber_effect(2 * K63 * ar ** 2 + K_turn)
out("F", "Superseded 63 % open baffle, same power model", (r_p63 - 1) * 100, "%", "R6", "for comparison")
out("F", "Superseded 63 % open baffle, same speed model", (r_s63 - 1) * 100, "%", "R6", "for comparison")
ri40 = (1016.0 / 2 - 7.9) / 1000
ar40 = A_p / (math.pi * ri40 ** 2)
K40 = 2 * K63 * ar40 ** 2 + 2 * (ar40 / (1 - ar40)) ** 2
r_s40, r_p40 = chamber_effect(K40)
out("F", "Reserve (option C): 1,016 mm vessel with the 63 % baffle, same power model", (r_p40 - 1) * 100, "%", "R6",
    "only if the TRL 4 comparison shows more than 5 %")
out("F", "Reserve (option C): 1,016 mm vessel with the 63 % baffle, same speed model", (r_s40 - 1) * 100, "%", "R6",
    "only if the TRL 4 comparison shows more than 5 %")
v_ret = math.sqrt(50.0 / (2 * rho_room * A_p)) * ar / (1 - ar)
out("F", "Return flow speed along the wall at 50 N", v_ret, "m/s")

# ------------------------------------------------------------------ G. data (R9)
out("G", "Logging rate", 20.0, "Hz", "R9", "load-cell amplifiers sample at 80 Hz")

# ------------------------------------------------------------------ H. cost (R10)
total = 0.0
with (ROOT / "bom" / "bom.csv").open() as fh:
    for r in csv.DictReader(fh):
        total += float(r["qty"]) * float(r["unit_cost_usd"])
target = 1000.0
out("H", "Estimated cost of the constructable design", total, "USD", "R10")
out("H", "Value-engineering target", target, "USD", "R10")
out("H", "Over the value-engineering target by", total - target, "USD", "R10")
# ALR-DDR-003 (R10 option B): surplus pipe and heads, host lab's supply and workshop pump. New prices from the
# TRL 3 bill of materials, used if a condition fails: pipe USD 420, heads 2 x USD 260, supply USD 320, pump USD 220 more.
out("H", "Cost if the surplus pipe and heads fail their checks and are bought new", total + (420 - 210) + 2 * (260 - 130),
    "USD", "R10")
out("H", "Cost if, in addition, the supply and pump have to be bought", total + 210 + 260 + 320 + 220, "USD", "R10",
    "the TRL 3 estimate plus the 80 % baffle")

with (Path(__file__).parent / "results.csv").open("w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=["section", "quantity", "value", "unit", "requirement", "note"])
    w.writeheader()
    for r in rows:
        r = dict(r)
        if isinstance(r["value"], float):
            r["value"] = f"{r['value']:.4g}"
        w.writerow(r)
print("wrote docs/04-calcs/results.csv")
