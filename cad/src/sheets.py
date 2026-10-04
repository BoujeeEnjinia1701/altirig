"""AltiRig general arrangement sheet ALR-DWG-001, Rev P3 (TRL 3, constructable design ALR-DDR-002; decisions ALR-DDR-003).

Run from the repo root:  python cad/src/sheets.py
Writes cad/drawings/ALR-DWG-001.svg, .pdf and .png from the parametric model in cad/src/model.py
with .kit/drawing.py: the chamber with its door closed, window, feed-through, valve manifold,
saddles, the stand inside (hidden lines) and the vacuum pump beside it; three views with overall
sizes, an isometric view and the main dimensions, all taken from PARAMS. The control cabinet
stands apart and is not drawn. The concept blueprint in media/ is ALR-DWG-010; the making sketches
are ALR-DWG-101 onward.
"""
import shutil
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / ".kit"), str(ROOT / "cad" / "src")]
from build123d import Compound  # noqa: E402
from drawing import Sheet, project_views  # noqa: E402
from model import PARAMS as P, components, levels  # noqa: E402

DATE = "2026-10-03"


def main():
    L = levels(P)
    comps = [c for c in components(P) if c.key not in ("cabinet",)]
    asm = Compound([c.shape for c in comps])
    work = ROOT / "cad" / "drawings" / "_views"
    views = project_views(asm, work)
    s = Sheet(project="AltiRig", title="Altitude test chamber with a thrust stand: general arrangement",
              dwg_no="ALR-DWG-001", rev="P3", author="Amish Chadha", date=DATE, theme="technical",
              material="Per bom/bom.csv: carbon steel vessel (pipe, plate, tank heads), polycarbonate window, "
                       "6082 aluminium stand. PRELIMINARY, NOT FOR FABRICATION",
              revisions=[("P1", "General arrangement of the TRL 3 concept", DATE, "AC"),
                         ("P2", "Constructable design (ALR-DDR-002)", DATE, "AC"),
                         ("P3", "80 % open baffle (decision 41B)", DATE, "AC")])
    s.add_ortho(views)
    s.add_svg(views["iso"], 276, 32, 140, 82, label="Isometric view", sublabel="Not to scale; control cabinet not shown")
    s.add_notes("Main dimensions and interfaces (mm)", [
        f"Shell (1): pipe {P['SH_OD']:.0f} OD x {P['SH_T']} wall, {P['SH_L']:.0f} long; axis {P['Z_AX']:.0f} above floor",
        f"Heads (3): 2:1 ellipsoidal, {P['SH_OD']:.0f} OD; rear welded, door on a flange ring",
        f"Flange rings (2): {P['RING_OD']:.0f} OD x {P['SH_OD']:.0f} ID x {P['RING_T']:.0f}; gasket {P['GASKET_T']:.0f} sponge",
        f"Window (13): polycarbonate {P['WIN_D']:.0f} dia x {P['WIN_T']:.0f}, centre {P['WIN_X']:.0f} from flange face",
        f"Window nozzle (4): {P['WN_OD']} x {P['WN_T']}; feed-through (5): {P['FN_OD']} x {P['FN_T']}",
        f"Propeller plane {P['PROP_X']:.0f} from flange face; up to {P['PROP_D']:.0f} dia",
        f"Baffle (17): {P['BAF_D']:.0f} dia, 80 % open, {P['BAF_X']:.0f} from flange face",
        f"Deck (16) top {L['deck_top']:.0f} above floor; saddles (7) at {P['SAD_X'][0]:.0f} and {P['SAD_X'][1]:.0f}",
        "Vessel designed for full vacuum; relief valve opens at 55 kPa below atmosphere",
        "Hinge (10) on the far side; door swings open to +Y",
        "Third-angle; top view from +Z; (n) = BOM line",
    ], x=276, y=132, width=146)
    s.save(ROOT / "cad" / "drawings" / "ALR-DWG-001")
    shutil.rmtree(work, ignore_errors=True)
    print("wrote cad/drawings/ALR-DWG-001")


if __name__ == "__main__":
    main()
