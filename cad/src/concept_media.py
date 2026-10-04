"""AltiRig concept media (TRL 3, constructable design ALR-DDR-002), generated from the parametric model.

Run from the repo root:  python cad/src/concept_media.py
Takes every component from cad/src/model.py and renders the media set with .kit/concept.py: hero
with the 1.75 m figure, cutaway (window side removed), exploded view with BOM numbers, blueprint
sheet ALR-DWG-010, energy flow of one full-power test point, and the web model (model.glb with
viewer.html) at a coarse tessellation. Figures come from docs/04-calcs/sizing.py (ALR-CAL-001).
CONCEPT, NOT FOR FABRICATION.
"""
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / ".kit"), str(ROOT / "cad" / "src")]
from build123d import Compound, Color, export_gltf  # noqa: E402
import matplotlib.colors as mc  # noqa: E402
from concept import Part, render_all, _render  # noqa: E402
from model import components  # noqa: E402

COLOR = {"shell": "#4B6584", "shell_ring": "#3B4F6B", "rear_head": "#4B6584", "win_nozzle": "#3B4F6B",
         "ft_nozzle": "#3B4F6B", "man_stub": "#3B4F6B", "saddle1": "#374151", "saddle2": "#374151",
         "rail_p": "#6B7280", "rail_n": "#6B7280", "tabs": "#6B7280", "hinge_fixed": "#1F2937",
         "door_ring": "#3B4F6B", "door_head": "#5B7594", "door_lugs": "#1F2937", "pin": "#111827",
         "gasket": "#111827", "latches": "#B45309", "win_gasket": "#111827", "window": "#93C5FD",
         "win_spacer": "#475569", "win_clamp": "#334155", "ft_gasket": "#111827", "ft_plate": "#A8B3C2",
         "deck": "#CBD5E1", "baffle": "#94A3B8", "stand_base": "#0F766E", "leaves": "#D4A017",
         "clamps": "#115E59", "carriage": "#14B8A6", "anchor": "#115E59", "thrust_cell": "#2563EB",
         "hanger": "#115E59", "housing": "#0D9488", "bearings": "#6B7280", "shaft": "#9CA3AF", "mplate": "#64748B",
         "arm": "#0F766E", "torque_cell": "#2563EB", "tc_bracket": "#115E59", "speed_post": "#7C3AED",
         "motor": "#111827", "prop": "#1F2937", "sensors": "#F59E0B", "manifold": "#B91C1C", "pump": "#DC2626",
         "hose": "#111827", "cabinet": "#E5E7EB"}

C = components()
parts = [Part(c.name, c.shape, COLOR[c.key], c.bom, c.explode) for c in C]
# exploded view: the stand, the deck and the test article lifted out through the top so they are not hidden
LIFT = {"stand": (-250, 0, 750), "test": (-250, 0, 750)}
exploded = []
for c in C:
    off = c.explode
    if c.group in LIFT or c.key in ("deck", "sensors"):
        add = LIFT.get(c.group, (-250, 0, 600))
        off = tuple(a + b for a, b in zip(off, add))
    exploded.append(Part(c.name, c.shape, COLOR[c.key], c.bom, off))


def exploded_view():
    _render(exploded, ROOT / "media" / "exploded.png", offsets=True, labels=True, title="AltiRig: exploded view",
            note="Seen from the front right and above, 24 deg elevation; the stand, deck and test article lifted out "
                 "above the vessel; numbers match bom/bom.csv")


if "--exploded-only" in sys.argv:
    exploded_view()
    sys.exit(0)

outs = render_all(
    parts, project="AltiRig", title="Altitude test chamber with a thrust stand, concept", dwg_no="ALR-DWG-010",
    key_figures=["Holds 5,000 m air density (0.736 kg/m3): 61.9 kPa at 20 C",
                 "Steel vessel 813 mm OD x 1.5 m, 0.93 m3 inside; propellers to 380 mm",
                 "Designed for full vacuum: shell collapse factor 6.7, window 7.1 on yield",
                 "Pump-down to 54 kPa in about 4 min with a 170 L/min pump",
                 "Flexure stand: thrust 0 to 50 N within 0.27 %, torque to 2 N m",
                 "Air holds the door shut: 24 kN at the 5,000 m point",
                 "Estimated USD 3,920 against a USD 1,000 target",
                 "Not certified pressure equipment or test equipment"],
    cut_exclude=("Control and power cabinet", "Vacuum pump", "Vacuum hose", "Valve manifold"),
    web_model=False,
    flow={"title": "energy at one full-power test point, W (ALR-CAL-001 estimates); all of it ends as heat in the steel walls",
          "unit": "W",
          "stages": [("Mains into the supply", 1650), ("Supply to the speed controller", 1500), ("Motor shaft", 1200),
                     ("Ideal power in the propeller jet", 720)],
          "losses": [(0, "Supply loss (estimate)", 150), (1, "Speed controller and motor losses (estimate)", 300),
                     (2, "Blade drag and swirl (estimate)", 480)]},
)

exploded_view()
md = ROOT / "media"
kids = []
for p in parts:
    sh = p.shape
    sh.color = Color(*mc.to_rgb(p.color))
    sh.label = p.name
    kids.append(sh)
export_gltf(Compound(kids), str(md / "model.glb"), binary=True, linear_deflection=1.0, angular_deflection=0.35)
(md / "viewer.html").write_text("""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>AltiRig: altitude test chamber with a thrust stand, concept</title>
<script type="module" src="https://cdn.jsdelivr.net/npm/@google/model-viewer@3/dist/model-viewer.min.js"></script>
<style>body{margin:0;font-family:system-ui,sans-serif;background:#F9FAFB}model-viewer{width:100vw;height:100vh}
.tag{position:fixed;left:12px;top:10px;font-size:12px;color:#B45309;letter-spacing:.06em}</style></head>
<body><div class="tag">CONCEPT, NOT FOR FABRICATION</div>
<model-viewer src="model.glb" poster="hero.png" alt="AltiRig: altitude test chamber with a thrust stand, concept" camera-controls auto-rotate shadow-intensity="0.6"
  exposure="1.0" camera-orbit="-35deg 70deg auto" interaction-prompt="auto"></model-viewer></body></html>
""")
print({k: str(v) for k, v in outs.items()}, "model.glb", round((md / "model.glb").stat().st_size / 1e6, 2), "MB")
