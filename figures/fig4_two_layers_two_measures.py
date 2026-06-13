"""Figure 4 (policy brief) — two-card concentration comparison.

Replaces a side-by-side chart that risked naive comparison of two
concentration measures. Two visually separated "cards" with deliberately
DIFFERENT visual grammars, plus a prominent central callout warning the
reader not to compare heights across cards:

  Card A  — Du (2026) proxy-estimated HHI over the broad model catalog,
            drawn as a line with HHI threshold bands. Only the two
            REPORTED endpoints (2023Q1 = 4,558; 2026Q1 = 2,086) are solid
            markers; the 2024Q1 ~3,200 point is an interpolation and is
            drawn as an open marker. The connecting line is light and
            dashed: a trend between reported endpoints, not a series.
  Card B  — Menlo Ventures (Dec 2025) enterprise API dollar-flow shares,
            drawn as a single 100% stacked horizontal bar with a bracket
            over the top three providers (88%).

Data / assumption notes:
- Card A values from data/du-2026/du_2026_key_figures.json
  (hhi_trajectory start/end). The 2024Q1 ~3,200 midpoint is treated as
  interpolated per the brief's work order, not as a reported figure.
  Du's shares are proxy-estimated; no transaction-volume data.
- Card B values from data/menlo-ventures/menlo_2025_eoy.json
  (market_share_dollars_spent). Survey-based (N=495, U.S. enterprises);
  Menlo is an Anthropic investor (vendor adjacency disclosed in-figure).
- The two cards measure DIFFERENT layers of the supply chain with
  different methods; the central callout is the message.
- Style: minimal line art, muted grays, one accent color (rust) reserved
  for the callout and the top-three bracket. Grayscale-legible: bar
  segments are distinguished by lightness and hatching, not hue; all
  in-figure source text >= 8pt.

Outputs: drafts/version_1/figures/fig4_two_layers_two_measures.{png,svg}
(PNG at 300 dpi).
"""

import json
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "drafts" / "version_1" / "figures"
OUT.mkdir(parents=True, exist_ok=True)

ACCENT = "#B5541C"
TEXT_DARK = "#2b2b2b"
TEXT_GRAY = "#6e6e6e"
CARD_A_BG = "#f7f6f3"   # warm light gray
CARD_B_BG = "#ebedef"   # cool, slightly darker gray (lightness-distinct)
CARD_EDGE = "#b8b8b8"

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.size": 9.5,
    "svg.fonttype": "none",
})

with open(DATA / "du-2026" / "du_2026_key_figures.json", encoding="utf-8") as f:
    du = json.load(f)
with open(DATA / "menlo-ventures" / "menlo_2025_eoy.json", encoding="utf-8") as f:
    menlo = json.load(f)

hhi_start = du["hhi_trajectory"]["start"]          # 4558, reported (2023Q1)
hhi_end = du["hhi_trajectory"]["end"]              # 2086, reported (2026Q1)
hhi_mid = 3200                                     # 2024Q1, interpolated (~)
share = menlo["market_share_dollars_spent"]

fig = plt.figure(figsize=(11.2, 6.3))

# --- card backgrounds -----------------------------------------------------
for (x0, w, bg) in [(0.025, 0.460, CARD_A_BG), (0.515, 0.460, CARD_B_BG)]:
    fig.add_artist(FancyBboxPatch(
        (x0, 0.10), w, 0.70, transform=fig.transFigure,
        boxstyle="round,pad=0.006,rounding_size=0.012",
        facecolor=bg, edgecolor=CARD_EDGE, linewidth=1.0, zorder=0))

# --- central callout (the message) ---------------------------------------
fig.text(0.5, 0.925,
         "Different layers, different measures — do not compare heights.",
         ha="center", va="center", fontsize=12.5, fontweight="bold",
         color=ACCENT,
         bbox=dict(boxstyle="round,pad=0.55", facecolor="white",
                   edgecolor=ACCENT, linewidth=1.6))

# ==========================================================================
# Card A — HHI line with threshold bands
# ==========================================================================
fig.text(0.045, 0.765, "Broad model catalog — proxy-estimated HHI: falling",
         fontsize=11, fontweight="bold", color=TEXT_DARK)
fig.text(0.045, 0.732,
         "Du (2026), preprint; proxy-estimated shares, "
         "no transaction-volume data",
         fontsize=8.5, color=TEXT_GRAY, style="italic")

ax_a = fig.add_axes([0.085, 0.175, 0.36, 0.50])
ax_a.set_facecolor("white")

# threshold bands (lightness only — grayscale-safe)
ax_a.axhspan(2500, 5300, color="#dedede", zorder=0)
ax_a.axhspan(1500, 2500, color="#efefef", zorder=0)
ax_a.text(2025.95, 4950, "highly concentrated (HHI > 2,500)",
          ha="right", fontsize=8, color=TEXT_GRAY)
ax_a.text(2025.95, 1620, "moderately concentrated (HHI 1,500–2,500)",
          ha="right", fontsize=8, color=TEXT_GRAY)

xs = [2023.0, 2024.0, 2026.0]
ys = [hhi_start, hhi_mid, hhi_end]
ax_a.plot(xs, ys, linestyle="--", color="#9a9a9a", linewidth=1.2, zorder=2)
# reported endpoints: solid markers
ax_a.plot([xs[0], xs[2]], [ys[0], ys[2]], "o", color=TEXT_DARK,
          markersize=7, zorder=3)
# interpolated midpoint: open marker, visibly different
ax_a.plot([xs[1]], [ys[1]], "o", markerfacecolor="white",
          markeredgecolor=TEXT_DARK, markeredgewidth=1.3, markersize=7,
          zorder=3)

ax_a.annotate(f"{hhi_start:,}\n(reported)", (xs[0], ys[0]),
              textcoords="offset points", xytext=(10, 2), fontsize=8.5,
              color=TEXT_DARK)
ax_a.annotate("≈3,200\n(interpolated)", (xs[1], ys[1]),
              textcoords="offset points", xytext=(2, -34), fontsize=8.5,
              ha="center", color=TEXT_GRAY)
ax_a.annotate(f"{hhi_end:,}\n(reported)", (xs[2], ys[2]),
              textcoords="offset points", xytext=(-14, 12), fontsize=8.5,
              ha="right", color=TEXT_DARK)
ax_a.text(2024.85, 3050, "trend between\nreported endpoints",
          fontsize=8, color=TEXT_GRAY, style="italic", ha="left",
          rotation=-14)

ax_a.set_xlim(2022.75, 2026.45)
ax_a.set_ylim(0, 5300)
ax_a.set_xticks(xs)
ax_a.set_xticklabels(["2023 Q1", "2024 Q1", "2026 Q1"])
ax_a.set_ylabel("HHI", fontsize=9)
ax_a.spines[["top", "right"]].set_visible(False)
ax_a.tick_params(labelsize=8.5)
# plain-English reading aid for the index (figure coords, inside card A)
fig.text(0.085, 0.118,
         "HHI: a concentration index; higher = more concentrated",
         fontsize=8, color=TEXT_GRAY)

# ==========================================================================
# Card B — 100% stacked horizontal dollar-flow bar
# ==========================================================================
# Title and source line wrapped to two lines each so both stay inside the
# card's right boundary (x = 0.975); words identical to v1, breaks only.
fig.text(0.535, 0.790,
         "Enterprise API dollar flow —\n"
         "Menlo estimate: 88% to three providers",
         fontsize=11, fontweight="bold", color=TEXT_DARK,
         va="top", linespacing=1.25)
fig.text(0.535, 0.722,
         "Menlo Ventures (Dec 2025); survey-based (N=495, U.S.),\n"
         "vendor-adjacent (Menlo is an Anthropic investor)",
         fontsize=8.5, color=TEXT_GRAY, style="italic",
         va="top", linespacing=1.25)

ax_b = fig.add_axes([0.545, 0.175, 0.40, 0.47])
ax_b.set_facecolor("none")

# grayscale-distinct segments: lightness ramp + hatching, no hue coding
segments = [
    ("Anthropic", share["anthropic"] * 100, "#3d3d3d", None, "white"),
    ("OpenAI", share["openai"] * 100, "#7d7d7d", "//", "white"),
    ("Google", share["google"] * 100, "#b4b4b4", None, TEXT_DARK),
    ("All others", share["remaining_long_tail"] * 100, "#e6e6e6", "..",
     TEXT_DARK),
]

BAR_Y, BAR_H = 0.42, 0.30
left = 0.0
for name, val, color, hatch, txtcolor in segments:
    ax_b.barh([BAR_Y], [val], left=left, height=BAR_H, color=color,
              hatch=hatch, edgecolor="white", linewidth=1.0)
    # solid pad behind labels on hatched segments so hatch lines do not
    # cross the text
    bbox = (dict(facecolor=color, edgecolor="none", pad=1.6)
            if hatch else None)
    ax_b.text(left + val / 2, BAR_Y, f"{name}\n{val:.0f}%", ha="center",
              va="center", fontsize=9, fontweight="bold", color=txtcolor,
              linespacing=1.2, bbox=bbox)
    left += val

# bracket over the top three (88%) — accent, the card's one emphasis
top3 = share["top_three_combined"] * 100
y_br = BAR_Y + BAR_H / 2 + 0.07
ax_b.plot([0, 0, top3, top3], [y_br, y_br + 0.05, y_br + 0.05, y_br],
          color=ACCENT, linewidth=1.5, clip_on=False)
ax_b.text(top3 / 2, y_br + 0.085, f"top three: {top3:.0f}%", ha="center",
          va="bottom", fontsize=10.5, fontweight="bold", color=ACCENT)

ax_b.set_xlim(0, 100)
ax_b.set_ylim(0, 1.0)
ax_b.set_yticks([])
ax_b.set_xticks([0, 25, 50, 75, 100])
ax_b.set_xticklabels(["0%", "25%", "50%", "75%", "100%"], fontsize=8.5)
ax_b.set_xlabel("Share of enterprise LLM API spend", fontsize=9)
ax_b.spines[["top", "right", "left"]].set_visible(False)

# --- caption --------------------------------------------------------------
fig.text(0.025, 0.030,
         "The apparent contradiction disappears once the measures are "
         "assigned to different layers of the supply chain.\n"
         "Sources: Du (2026), arXiv:2603.28576, proxy-estimated HHI over "
         "OpenRouter-available models (card A); Menlo Ventures, 2025: The "
         "State of Generative AI in the Enterprise, Dec 2025 (card B).",
         fontsize=8, color=TEXT_GRAY, va="bottom", linespacing=1.4)

for ext in ("png", "svg"):
    fig.savefig(OUT / f"fig4_two_layers_two_measures.{ext}", dpi=300,
                bbox_inches="tight")
plt.close(fig)

# Grayscale-legibility proof: Rec. 709 luminance conversion of the PNG.
img = plt.imread(OUT / "fig4_two_layers_two_measures.png")
gray = (0.2126 * img[..., 0] + 0.7152 * img[..., 1] + 0.0722 * img[..., 2])
plt.imsave(OUT / "fig4_two_layers_two_measures_gray.png", gray,
           cmap="gray", vmin=0, vmax=1)
print("wrote fig4_two_layers_two_measures.png / .svg / _gray.png to", OUT)
