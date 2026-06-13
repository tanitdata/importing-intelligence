"""Figure 1 (policy brief) — framework diagram: "Where concentration migrates".

Replaces a dense table in the brief body. A 3-column x 4-row schematic:
columns are the three computing regimes (internet, cloud, LLM); rows are the
four analytical categories (commodity, form of flow, main control points,
concentration layer). The key visual element is a thick accent-colored band
that rises across the "Concentration layer" row, tracing the migration of
concentration: network connectivity -> platform hosting -> model / API layer.

Assumptions / data notes:
- This is a framework diagram, not a data chart. Cell contents are the
  brief's own regime characterizations (per the work order), drawing on
  Mitchell (2011) for the framework and Srnicek (2017), Narayan (2022),
  Demirer et al. (2025) for the regime characterizations. No quantitative
  data are encoded.
- Style: minimal line art, muted grays, ONE accent color (rust) reserved
  for the migrating band — the band is the message. Grayscale-legible:
  the accent is a mid-dark tone carrying white bold text; everything else
  is distinguished by lightness, not hue. In-figure source text >= 8pt.

Outputs: drafts/version_1/figures/fig1_framework_migration.{png,svg}
(PNG at 300 dpi).
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Polygon

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "drafts" / "version_1" / "figures"
OUT.mkdir(parents=True, exist_ok=True)

# Palette: muted grays + one accent (rust). Accent lightness ~45% so white
# text on it survives grayscale conversion.
ACCENT = "#B5541C"
CELL_FILL = "#f4f4f4"
CELL_EDGE = "#c8c8c8"
TEXT_DARK = "#2b2b2b"
TEXT_GRAY = "#6e6e6e"

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.size": 9.5,
    "svg.fonttype": "none",
})

fig, ax = plt.subplots(figsize=(10.5, 6.6))
ax.set_xlim(0, 11.6)
ax.set_ylim(0, 7.6)
ax.set_aspect("auto")
ax.axis("off")

# --- geometry -----------------------------------------------------------
LABEL_X = 1.55                       # right edge of the row-label gutter
COL_W, COL_GAP = 3.05, 0.18
col_x0 = [LABEL_X + 0.15 + i * (COL_W + COL_GAP) for i in range(3)]
col_cx = [x + COL_W / 2 for x in col_x0]

Y_HEADER = (6.55, 7.30)
Y_COMMODITY = (5.55, 6.35)
Y_FORM = (4.40, 5.38)
Y_CONTROL = (3.22, 4.22)
Y_CONC = (1.35, 3.02)                # taller row: hosts the migrating band

HEADERS = [
    "Internet regime\n(1990s–2000s)",
    "Cloud regime\n(2010s)",
    "LLM regime\n(2022–present)",
]

# rows: (left label, y-extent, [three cell texts])
ROWS = [
    ("Commodity", Y_COMMODITY, [
        "Connectivity",
        "Rented compute\n& storage",
        "Metered reasoning\n(per token)",
    ]),
    ("Form of flow", Y_FORM, [
        "Packets over\nopen-protocol mesh",
        "Workloads in hyperscale\ndata centers",
        "API request → router →\nhosted model →\nmetered response",
    ]),
    ("Main control\npoints", Y_CONTROL, [
        "Backbones, IXPs,\ncables, DNS root",
        "Contracts, data gravity,\negress pricing",
        "API endpoints, payment\nrails, rate limits,\ngeo-availability",
    ]),
]

CONC_LABELS = ["Network\nconnectivity", "Platform\nhosting", "Model / API\nlayer"]


def cell(x, y0, y1, text, fontsize=9):
    ax.add_patch(FancyBboxPatch(
        (x + 0.07, y0 + 0.05), COL_W - 0.14, (y1 - y0) - 0.10,
        boxstyle="round,pad=0.04,rounding_size=0.08",
        facecolor=CELL_FILL, edgecolor=CELL_EDGE, linewidth=0.8))
    ax.text(x + COL_W / 2, (y0 + y1) / 2, text, ha="center", va="center",
            fontsize=fontsize, color=TEXT_DARK, linespacing=1.25)


# --- column headers ------------------------------------------------------
for x, cx, h in zip(col_x0, col_cx, HEADERS):
    ax.text(cx, sum(Y_HEADER) / 2, h, ha="center", va="center",
            fontsize=10.5, fontweight="bold", color=TEXT_DARK,
            linespacing=1.2)
    ax.plot([x + 0.15, x + COL_W - 0.15], [Y_HEADER[0] - 0.04] * 2,
            color="#9a9a9a", linewidth=1.0)

# --- ordinary rows -------------------------------------------------------
for label, (y0, y1), cells in ROWS:
    ax.text(LABEL_X - 0.08, (y0 + y1) / 2, label, ha="right", va="center",
            fontsize=9.5, fontweight="bold", color=TEXT_GRAY,
            linespacing=1.2)
    for x, txt in zip(col_x0, cells):
        cell(x, y0, y1, txt)

# --- the migrating band (the message) ------------------------------------
# A thick accent band rises across the "Concentration layer" row from the
# internet column to the LLM column, ending in an arrowhead: concentration
# does not disappear across regimes, it migrates to the layer the dominant
# flow must pass through.
ax.text(LABEL_X - 0.08, sum(Y_CONC) / 2, "Concentration\nlayer", ha="right",
        va="center", fontsize=9.5, fontweight="bold", color=ACCENT,
        linespacing=1.2)

x_start = col_x0[0] + 0.07
x_neck = col_x0[2] + COL_W - 0.55    # where the arrowhead begins
x_tip = col_x0[2] + COL_W + 0.12
y_c0 = Y_CONC[0] + 0.52              # band centerline, left end (low)
y_c1 = Y_CONC[1] - 0.52              # band centerline, right end (high)
HALF = 0.40                          # band half-thickness
HEAD = 0.26                          # extra arrowhead flare


def band_cy(x):
    """Centerline height of the rising band at horizontal position x."""
    return y_c0 + (y_c1 - y_c0) * (x - x_start) / (x_tip - x_start)


ax.add_patch(Polygon([
    (x_start, band_cy(x_start) + HALF),
    (x_neck, band_cy(x_neck) + HALF),
    (x_neck, band_cy(x_neck) + HALF + HEAD),
    (x_tip, band_cy(x_tip)),
    (x_neck, band_cy(x_neck) - HALF - HEAD),
    (x_neck, band_cy(x_neck) - HALF),
    (x_start, band_cy(x_start) - HALF),
], closed=True, facecolor=ACCENT, edgecolor="none", zorder=3))

for cx, txt in zip(col_cx, CONC_LABELS):
    ax.text(cx, band_cy(cx), txt, ha="center", va="center", fontsize=9.5,
            fontweight="bold", color="white", linespacing=1.15, zorder=4)

# small accent chevrons in the column gaps to reinforce direction
for gap_x in [(col_x0[1] - COL_GAP / 2), (col_x0[2] - COL_GAP / 2)]:
    ax.text(gap_x, band_cy(gap_x), "›", ha="center", va="center",
            fontsize=15, fontweight="bold", color="white", zorder=4)

ax.text((x_start + x_tip) / 2, Y_CONC[0] - 0.02,
        "concentration migrates with the dominant flow",
        ha="center", va="top", fontsize=8.5, style="italic", color=ACCENT)

# --- title and caption ----------------------------------------------------
ax.text(0.0, 7.55, "Concentration migrates; it does not disappear",
        ha="left", va="top", fontsize=13.5, fontweight="bold",
        color=TEXT_DARK)

fig.text(0.012, 0.045,
         "Across three computing regimes, control concentrates at the layer "
         "through which the dominant flow must pass.\n"
         "Framework: Mitchell (2011), adapted; regime characterizations per "
         "Srnicek (2017), Narayan (2022), Demirer et al. (2025).",
         fontsize=8, color=TEXT_GRAY, va="bottom", linespacing=1.4)

fig.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.13)

for ext in ("png", "svg"):
    fig.savefig(OUT / f"fig1_framework_migration.{ext}", dpi=300,
                bbox_inches="tight")
plt.close(fig)
print("wrote fig1_framework_migration.png / .svg to", OUT)
