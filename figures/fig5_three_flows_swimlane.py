"""Figure 5 -- "Three flows, three exposure profiles" (fig5_three_flows_swimlane).

Three horizontal swimlanes (Consumer, Developer, Enterprise), each tracing
actor -> channel -> control points -> exposure as four stages, with a vertical
bracket on the right marking the correlated-constriction scenario in which a
single shock binds across all three flows at once.

Design assumptions (documented per project conventions):
- The three lanes are CHANNELS of token dependence, not market segments by
  revenue; stage labels are taken verbatim from the brief's spec.
- The fourth stage in each lane is the lane's exposure profile (where its
  distinctive chokepoints sit), so it is drawn with a dashed border to
  distinguish "exposure" from the three flow stages, without relying on hue.
- The Developer-lane annotation uses the OpenRouter State of AI 2025 figure
  (>50% of usage originating outside the U.S.), per project empirical
  anchors; it characterizes a developer-skewed aggregator platform, not
  consumer web traffic (the two flows are kept distinct per CLAUDE.md).
- One accent color (muted brick, #c45911) is used ONLY for the
  correlated-constriction bracket and its icons; lanes are grayscale.
  Grayscale legibility relies on lightness contrast, border styles, and
  geometric icons, not hue (a *_gray.png luminance conversion is saved
  as a check). All caption/source text is >= 8 pt.

Outputs: drafts/version_1/figures/fig5_three_flows_swimlane.{png,svg} and a
grayscale legibility check fig5_three_flows_swimlane_gray.png.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import (Arc, Circle, FancyArrowPatch, FancyBboxPatch,
                                Polygon, Rectangle)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "drafts" / "version_1" / "figures"
OUT.mkdir(parents=True, exist_ok=True)

# Palette: grayscale structure + ONE accent (bracket/scenario only).
ACCENT = "#c45911"      # muted brick -- correlated-constriction bracket only
INK = "#2b2b2b"         # text, box borders
MIDGRAY = "#6e6e6e"     # arrows, secondary text
FILL = "#f2f2f2"        # flow-stage fill
EXPO_FILL = "#e0e0e0"   # exposure-stage fill (darker: lightness contrast)
LANE_BG = ["#fafafa", "#f0f0f0", "#fafafa"]   # alternating lane backgrounds

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.size": 9,
    "svg.fonttype": "none",
})

# Full-bleed axes with matching data/figure aspect so patches are undistorted.
FIG_W, FIG_H = 14.0, 7.6
fig = plt.figure(figsize=(FIG_W, FIG_H))
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, FIG_W)
ax.set_ylim(0, FIG_H)
ax.axis("off")

# ----------------------------------------------------------------------
# Lane geometry
# ----------------------------------------------------------------------
LANE_X0, LANE_X1 = 1.45, 11.45         # lane band horizontal extent
LANE_H = 1.50                          # lane band height
LANE_GAP = 0.20
lane_tops = [5.95, 5.95 - (LANE_H + LANE_GAP), 5.95 - 2 * (LANE_H + LANE_GAP)]
lane_cy = [t - LANE_H / 2 for t in lane_tops]

BOX_W, BOX_H = 2.04, 1.04
stage_cx = [LANE_X0 + 0.30 + BOX_W / 2 + i * (BOX_W + 0.46) for i in range(4)]

lanes = [
    ("Consumer",
     ["End user", "App store /\nsubscription", "Consumer AI\nproduct",
      "Content & compliance\npolicy; consumer\npayment rails"]),
    ("Developer",
     ["Startup /\napplication", "API /\naggregator", "Provider API",
      "Geo-availability;\ndeveloper payment\nrails; rate limits"]),
    ("Enterprise",
     ["Organization", "Cloud contract", "Hosted model /\ninference provider",
      "Data residency;\ngoverning law;\ncompliance regimes"]),
]

for (name, stages), top, cy, bg in zip(lanes, lane_tops, lane_cy, LANE_BG):
    # Lane background band and left-edge lane label.
    ax.add_patch(Rectangle((LANE_X0, top - LANE_H), LANE_X1 - LANE_X0, LANE_H,
                           facecolor=bg, edgecolor="#d8d8d8", linewidth=0.8,
                           zorder=1))
    ax.text(LANE_X0 - 0.18, cy, name, ha="right", va="center", fontsize=11,
            fontweight="bold", color=INK, rotation=0)

    # Four stages: three flow boxes (solid) + exposure box (dashed, darker).
    for i, (cx, label) in enumerate(zip(stage_cx, stages)):
        is_exposure = (i == 3)
        ax.add_patch(FancyBboxPatch(
            (cx - BOX_W / 2, cy - BOX_H / 2), BOX_W, BOX_H,
            boxstyle="round,pad=0.02,rounding_size=0.10",
            facecolor=EXPO_FILL if is_exposure else FILL,
            edgecolor=INK, linewidth=1.0,
            linestyle="--" if is_exposure else "-", zorder=3))
        ax.text(cx, cy, label, ha="center", va="center", fontsize=8.6,
                color=INK, zorder=4, linespacing=1.2)

    # Arrows between stages.
    for left, right in zip(stage_cx[:-1], stage_cx[1:]):
        ax.add_patch(FancyArrowPatch(
            (left + BOX_W / 2 + 0.04, cy), (right - BOX_W / 2 - 0.04, cy),
            arrowstyle="-|>", mutation_scale=12, linewidth=1.2,
            color=MIDGRAY, zorder=2))

# Column headers over the four stages.
for cx, head in zip(stage_cx, ["Actor", "Channel", "Control points",
                               "Exposure"]):
    ax.text(cx, lane_tops[0] + 0.22, head, ha="center", va="center",
            fontsize=9.5, color=MIDGRAY, style="italic")

# ----------------------------------------------------------------------
# Developer-lane annotation (OpenRouter, State of AI 2025)
# ----------------------------------------------------------------------
# The annotation sits in the inter-lane gap directly ABOVE the Developer
# band, with a short straight leader pointing down into the band's empty
# left margin (above the stage boxes, which top out at cy + BOX_H/2).
# This anchors it unambiguously to the Developer lane: the previous
# placement (text at bottom-left, tip in the gap BELOW the band) read as
# pointing at the Enterprise lane.
ax.annotate(
    ">50% of OpenRouter usage originates outside the U.S. "
    "(developer-skewed platform, 2025)",
    xy=(LANE_X0 + 0.15, lane_tops[1] - 0.14),
    xytext=(LANE_X0 + 0.42, lane_tops[1] + LANE_GAP / 2),
    fontsize=8.5, color=INK, ha="left", va="center",
    arrowprops=dict(arrowstyle="->", color=MIDGRAY, linewidth=0.9),
    zorder=6)

# ----------------------------------------------------------------------
# Correlated-constriction bracket (accent color) spanning all three lanes
# ----------------------------------------------------------------------
BX = LANE_X1 + 0.30                      # bracket spine x
y_top, y_bot = lane_tops[0], lane_tops[2] - LANE_H
TICK = 0.16

ax.plot([BX, BX + TICK, BX + TICK, BX],
        [y_top, y_top, y_bot, y_bot],
        color=ACCENT, linewidth=2.0, solid_capstyle="round", zorder=4)
# Center nib pointing toward the label.
ax.plot([BX + TICK, BX + 2 * TICK], [(y_top + y_bot) / 2] * 2,
        color=ACCENT, linewidth=2.0, zorder=4)

LBL_X = BX + 2 * TICK + 0.14
mid_y = (y_top + y_bot) / 2
ax.text(LBL_X, mid_y + 1.06, "Correlated-constriction\nscenario:",
        fontsize=9.5, fontweight="bold", color=ACCENT, ha="left",
        va="center", linespacing=1.25)


# --- Small geometric icons (no emoji), accent-colored, one per shock term ---
def icon_card(x, y, s=0.30):
    """Payment card: rectangle with a magnetic stripe."""
    w, h = s, 0.62 * s
    ax.add_patch(Rectangle((x - w / 2, y - h / 2), w, h, facecolor="white",
                           edgecolor=ACCENT, linewidth=1.3, zorder=5))
    ax.add_patch(Rectangle((x - w / 2, y + h / 2 - 0.30 * h), w, 0.18 * h,
                           facecolor=ACCENT, edgecolor="none", zorder=6))


def icon_globe(x, y, s=0.30):
    """Geo rules: circle with meridian ellipse and equator line."""
    r = s / 2
    ax.add_patch(Circle((x, y), r, facecolor="white", edgecolor=ACCENT,
                        linewidth=1.3, zorder=5))
    ax.add_patch(Arc((x, y), 0.55 * s, s, linewidth=1.0, color=ACCENT,
                     zorder=6))
    ax.plot([x - r * 0.92, x + r * 0.92], [y, y], color=ACCENT,
            linewidth=1.0, zorder=6)


def icon_doc(x, y, s=0.30):
    """Contract: page outline with folded corner and text lines."""
    w, h = 0.72 * s, s
    f = 0.28 * w
    pts = [(x - w / 2, y - h / 2), (x + w / 2, y - h / 2),
           (x + w / 2, y + h / 2 - f), (x + w / 2 - f, y + h / 2),
           (x - w / 2, y + h / 2)]
    ax.add_patch(Polygon(pts, closed=True, facecolor="white",
                         edgecolor=ACCENT, linewidth=1.3, zorder=5))
    for dy in (-0.16 * h, 0.04 * h):
        ax.plot([x - 0.30 * w, x + 0.30 * w], [y + dy, y + dy],
                color=ACCENT, linewidth=0.9, zorder=6)


def icon_warning(x, y, s=0.32):
    """Compliance shock: triangle with exclamation mark."""
    h = s
    pts = [(x, y + h / 2), (x - 0.58 * s, y - h / 2),
           (x + 0.58 * s, y - h / 2)]
    ax.add_patch(Polygon(pts, closed=True, facecolor="white",
                         edgecolor=ACCENT, linewidth=1.3, zorder=5))
    ax.plot([x, x], [y + 0.10 * h, y - 0.14 * h], color=ACCENT,
            linewidth=1.4, zorder=6)
    ax.add_patch(Circle((x, y - 0.30 * h), 0.045 * s * 1.6, facecolor=ACCENT,
                        edgecolor="none", zorder=6))


shock_items = [
    (icon_card, "payment"),
    (icon_globe, "+ geo rules"),
    (icon_doc, "+ cloud contract"),
    (icon_warning, "+ compliance shock"),
]
for k, (draw, text) in enumerate(shock_items):
    y = mid_y + 0.52 - k * 0.52
    draw(LBL_X + 0.16, y)
    ax.text(LBL_X + 0.46, y, text, fontsize=9, color=ACCENT, ha="left",
            va="center")

# ----------------------------------------------------------------------
# Title and caption
# ----------------------------------------------------------------------
ax.text(0.35, 7.12, "Token dependence is not one flow but three",
        fontsize=15, fontweight="bold", color=INK, ha="left", va="center")
ax.text(0.35, 6.74, "Consumer, developer, and enterprise channels each pass "
        "through different control points",
        fontsize=10.5, color=MIDGRAY, ha="left", va="center")
ax.text(0.35, 0.40, "Three channels with different chokepoints — and some "
        "shocks can constrict all three together. "
        "Developer-lane figure: OpenRouter, State of AI 2025.",
        fontsize=8.5, color=MIDGRAY, ha="left", va="center")

# ----------------------------------------------------------------------
# Save PNG (300 dpi), SVG, and a grayscale-legibility check PNG.
# ----------------------------------------------------------------------
STEM = "fig5_three_flows_swimlane"
fig.savefig(OUT / f"{STEM}.png", dpi=300)
fig.savefig(OUT / f"{STEM}.svg")
plt.close(fig)

# Grayscale check: luminance conversion of the rendered PNG (Rec. 709).
img = plt.imread(OUT / f"{STEM}.png")
gray = (0.2126 * img[..., 0] + 0.7152 * img[..., 1] + 0.0722 * img[..., 2])
plt.imsave(OUT / f"{STEM}_gray.png", gray, cmap="gray", vmin=0, vmax=1)

print(f"wrote {STEM}.png / .svg / _gray.png to {OUT}")
