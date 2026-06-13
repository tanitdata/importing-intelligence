"""Figure 0 -- "One inference request, many gates" (fig0_token_flow_map).

Schematic of the path a single hosted inference request traverses, with the
enforceable control points ("gates") that bind along each leg.

Design assumptions (documented per project conventions):
- This is a SCHEMATIC of a request/authorization pipeline, not a network map
  and not a physical-transport diagram. Nodes are logical stages, not places;
  the caption states that gate placement is illustrative.
- Gate placement follows where each control binds in practice as of June 2026:
  geo-availability and sanctions screening bind at the provider gateway;
  API key, payment rail, and rate limits bind at the account/payment layer;
  model/safety policy, contract terms, and cloud-region capacity bind at the
  hosted inference stage. Placement is a simplification: several gates are
  enforced at more than one stage (e.g., sanctions checks also occur at
  payment processors).
- One accent color (muted brick, #c45911) is used ONLY for the chokepoint
  badges; everything else is grayscale. Badges are also distinguished by a
  geometric padlock glyph and a dotted leader line, so the figure does not
  rely on hue alone and remains legible in grayscale (a *_gray.png luminance
  conversion is saved as a check).
- All caption/source text is >= 8 pt.

Outputs: drafts/version_1/figures/fig0_token_flow_map.{png,svg} and a
grayscale legibility check fig0_token_flow_map_gray.png.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc, FancyArrowPatch, FancyBboxPatch, Rectangle

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "drafts" / "version_1" / "figures"
OUT.mkdir(parents=True, exist_ok=True)

# Palette: grayscale structure + ONE accent (badges only).
ACCENT = "#c45911"      # muted brick -- chokepoint badges only
INK = "#2b2b2b"         # node borders / primary text
MIDGRAY = "#6e6e6e"     # arrows, subtitle, secondary text
FILL = "#f2f2f2"        # node fill
LEADER = "#9a9a9a"      # dotted leader lines

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.size": 9,
    "svg.fonttype": "none",
})

# Full-bleed axes with xlim/figwidth == ylim/figheight gives a 1:1 data
# aspect, so patch-drawn glyphs are not distorted.
FIG_W, FIG_H = 15.0, 7.0
fig = plt.figure(figsize=(FIG_W, FIG_H))
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, FIG_W)
ax.set_ylim(0, FIG_H)
ax.axis("off")

# ----------------------------------------------------------------------
# Pipeline nodes (logical stages, left to right)
# ----------------------------------------------------------------------
NODE_Y = 3.3            # vertical center of the pipeline
NODE_W, NODE_H = 1.70, 0.96
centers = [1.30 + i * 2.07 for i in range(7)]   # node x-centers

nodes = [
    ("User /\napplication", False),
    ("Local app /\nbackend", False),
    ("Aggregator /\nrouter\n(optional)", True),   # dashed border: optional
    ("Provider API\ngateway", False),
    ("Account / payment /\nrate-limit layer", False),
    ("Hosted model /\ninference cluster", False),
    ("Response, logging,\nbilling", False),
]

for cx, (label, optional) in zip(centers, nodes):
    box = FancyBboxPatch(
        (cx - NODE_W / 2, NODE_Y - NODE_H / 2), NODE_W, NODE_H,
        boxstyle="round,pad=0.02,rounding_size=0.12",
        facecolor=FILL, edgecolor=INK, linewidth=1.1,
        linestyle="--" if optional else "-", zorder=3)
    ax.add_patch(box)
    ax.text(cx, NODE_Y, label, ha="center", va="center", fontsize=9,
            color=INK, zorder=4, linespacing=1.25)

# Numbered stage markers above each node's top-left corner.
for i, cx in enumerate(centers, start=1):
    ax.text(cx - NODE_W / 2 + 0.10, NODE_Y + NODE_H / 2 - 0.16, str(i),
            ha="center", va="center", fontsize=8, color=MIDGRAY,
            fontweight="bold", zorder=5)

# Arrows along the path legs.
for left, right in zip(centers[:-1], centers[1:]):
    ax.add_patch(FancyArrowPatch(
        (left + NODE_W / 2 + 0.03, NODE_Y), (right - NODE_W / 2 - 0.03, NODE_Y),
        arrowstyle="-|>", mutation_scale=13, linewidth=1.3,
        color=MIDGRAY, zorder=2))


# ----------------------------------------------------------------------
# Chokepoint badges: geometric padlock glyph + label, accent color only.
# ----------------------------------------------------------------------
def draw_lock(x, y, s=0.21):
    """Simple geometric padlock: rectangle body + arc shackle (no emoji)."""
    body_h = 0.72 * s
    ax.add_patch(Rectangle((x - s / 2, y - body_h / 2), s, body_h,
                           facecolor=ACCENT, edgecolor="none", zorder=5))
    ax.add_patch(Arc((x, y + body_h / 2), 0.62 * s, 0.80 * s,
                     theta1=0, theta2=180, linewidth=1.5, color=ACCENT,
                     zorder=5))
    # Keyhole dot for legibility at small sizes / in grayscale.
    ax.add_patch(plt.Circle((x, y), 0.055 * s * 4, facecolor="white",
                            edgecolor="none", zorder=6))


# Badge spec: (label, glyph_x, glyph_y, bind_x, bind_y).
# Rows are staggered (two tiers above, two below) to keep leaders untangled.
TOP, BOT = NODE_Y + NODE_H / 2, NODE_Y - NODE_H / 2   # node edge y
HI_A, LO_A = 5.65, 4.90       # above-path badge tiers
LO_B, HI_B = 1.30, 2.00       # below-path badge tiers
c = centers

badges = [
    # Geo-availability binds at the provider gateway (node 4).
    ("Supported country /\ngeo-availability", c[3] - 0.95, HI_A, c[3], TOP),
    # API key / account status binds at the account layer (node 5).
    ("API key /\naccount status", c[4] - 0.95, LO_A, c[4] - 0.30, TOP),
    # Rate limits bind at the account layer, on the leg toward inference.
    ("Rate limit /\npriority tier", c[4] + 0.80, HI_A, c[4] + 0.55, TOP),
    # Cloud-region capacity binds at the inference cluster (node 6).
    ("Cloud-region\navailability / capacity", c[5] + 0.60, LO_A,
     c[5] + 0.30, TOP),
    # Sanctions screening binds on the gateway -> account leg.
    ("Sanctions\ncompliance", c[3] + 0.45, LO_B, (c[3] + c[4]) / 2, NODE_Y - 0.12),
    # Payment rail / billing country binds at the account layer (node 5).
    ("Payment rail /\nbilling country", c[4] - 0.35, HI_B, c[4], BOT),
    # Model availability / safety policy binds at the hosted model (node 6).
    ("Model availability /\nsafety policy", c[5] - 1.05, LO_B,
     c[5] - 0.35, BOT),
    # Contract terms bind at the hosted-model relationship (node 6).
    ("Contract / governing law /\ndata retention", c[5] + 0.55, HI_B,
     c[5] + 0.40, BOT),
]

for label, gx, gy, bx, by in badges:
    ax.plot([gx, bx], [gy, by], linestyle=(0, (2, 3)), linewidth=0.9,
            color=LEADER, zorder=1)
    draw_lock(gx, gy)
    ax.text(gx + 0.22, gy, label, ha="left", va="center", fontsize=8.5,
            color=ACCENT, zorder=5, linespacing=1.15)

# ----------------------------------------------------------------------
# Title, subtitle, caption
# ----------------------------------------------------------------------
ax.text(0.35, 6.62, "One inference request, many gates",
        fontsize=15, fontweight="bold", color=INK, ha="left", va="center")
ax.text(0.35, 6.24, "Every hosted inference request passes through "
        "enforceable gates — as of June 2026",
        fontsize=10.5, color=MIDGRAY, ha="left", va="center")
ax.text(0.35, 0.42, "A token does not travel like oil, but every hosted "
        "inference request passes through enforceable gates. "
        "Schematic; gate placement is illustrative.",
        fontsize=8.5, color=MIDGRAY, ha="left", va="center")

# ----------------------------------------------------------------------
# Save PNG (300 dpi), SVG, and a grayscale-legibility check PNG.
# ----------------------------------------------------------------------
STEM = "fig0_token_flow_map"
fig.savefig(OUT / f"{STEM}.png", dpi=300)
fig.savefig(OUT / f"{STEM}.svg")
plt.close(fig)

# Grayscale check: luminance conversion of the rendered PNG (Rec. 709).
img = plt.imread(OUT / f"{STEM}.png")
gray = (0.2126 * img[..., 0] + 0.7152 * img[..., 1] + 0.0722 * img[..., 2])
plt.imsave(OUT / f"{STEM}_gray.png", gray, cmap="gray", vmin=0, vmax=1)

print(f"wrote {STEM}.png / .svg / _gray.png to {OUT}")
