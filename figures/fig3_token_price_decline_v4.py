"""Figure 3 (policy brief) — token-price decline, v4 (candidate B1 final).

Author-selected redesign (2026-06-12): single panel, TWO visual groups.
Replaces the v3 four-marker design (code/fig3_token_price_decline_v3.py,
retained for provenance). Regenerates from source data at runtime — the
fig2_overlay_milestones JSON block in
drafts/version_1/research/r5-du-triangulation.md. Never drawn by eye.

Message (ten-second read): commodity-tier token prices collapsed;
frontier-tier prices did not follow — they oscillate in a band with no
smooth exponential trend.

Design decisions (author rails, 2026-06-12 figure-revision task):
- Two groups: commodity = economy + mid tiers POOLED (light blue-gray
  circles); frontier = flagship + reasoning POOLED (near-black squares).
  Pooling is a presentation choice, disclosed verbatim in the caption.
- Milestones thinned 32 -> 15 (selection rule in fig3_redesign_candidates
  history / checkpoint figures-fix.md): davinci $60 anchor; cheapest
  current commodity points; o3 repricing pair; band-defining frontier
  high/low; minimum spine per group. Full set stays in the research file.
- ONE stylized guide curve: Du economy-tier half-life 1.10 y, anchored
  exactly through gpt-3.5-turbo $2.00/M (2023-03-16). Drawn from 2021.5
  (earliest archived observation epoch). Mid tier (1.55 y) pooled under
  the same guide — disclosed in caption.
- Frontier as shaded $50-180/M band, 2023-2026; label uses the BINDING
  phrase "no smooth exponential trend" (never "flat"/"prices don't fall").
- Exactly two annotations: o3 -80% repricing arrow (binding
  counterexample) and the GPT-3 davinci anchor. May 2024 structural
  break lives in the caption.
- Log scale, explainer in subtitle; stylized-vs-raw separated by dashed
  line vs. markers; groups separated by lightness + shape (grayscale-safe).

v4 collision fixes (author note on B1 draft):
- Band label moved from the band's center (2024.7, y=96 — where it
  crowded the o3 pre-cut square and the GPT-4/Opus points) to the band's
  empty upper-middle region (centered 2024.55, y=148): no frontier point
  in that x-range sits above $120, so the two text lines clear all
  markers.
- o3 annotation text moved from (2024.35, 2.6) — where it crowded the
  2024 commodity circles at $1.05-1.25 — to the empty region right of
  them (2024.95, 2.3).
"""

import json
import re
from datetime import date
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
RESEARCH_MD = ROOT / "drafts" / "version_1" / "research" / "r5-du-triangulation.md"
OUT = ROOT / "drafts" / "version_1" / "figures"
OUT.mkdir(parents=True, exist_ok=True)

COMMODITY_C = "#9aa7b5"   # light blue-gray circles
FRONTIER_C = "#2b2b2b"    # near-black squares (lightness separates groups)
GUIDE_C = "#54708c"       # guide curve (dashed = stylized, not raw)
BAND_C = "#c9c9c9"
TEXT_GRAY = "#555555"

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.size": 11,
    "axes.labelsize": 10.5,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "legend.fontsize": 9.5,
    "svg.fonttype": "none",
})


def decimal_year(iso: str) -> float:
    d = date.fromisoformat(iso)
    start = date(d.year, 1, 1)
    days = (date(d.year + 1, 1, 1) - start).days
    return d.year + (d - start).days / days


# ------------------------------------------------------------------ data
text = RESEARCH_MD.read_text(encoding="utf-8")
m = re.search(r"```json\s*(\{.*?\})\s*```", text, re.DOTALL)
if not m:
    raise SystemExit("fig2_overlay_milestones JSON block not found")
points = {p["model"]: p for p in json.loads(m.group(1))["points"]}

KEEP_COMMODITY = [
    "GPT-3 Davinci", "gpt-3.5-turbo", "Claude 3 Sonnet", "Claude 3 Haiku",
    "Gemini 1.5 Flash (<=128K)", "GPT-5.4-mini", "Gemini 2.5 Flash-Lite",
    "DeepSeek-V4-Flash (cache miss)",
]
KEEP_FRONTIER = [
    "GPT-4 8K", "GPT-4 32K", "Claude 3 Opus", "OpenAI o3 (pre-cut)",
    "OpenAI o3 (post-cut)", "GPT-5.5-pro", "Claude Fable 5",
]

cx = [decimal_year(points[k]["date"]) for k in KEEP_COMMODITY]
cy = [points[k]["output"] for k in KEEP_COMMODITY]
fx = [decimal_year(points[k]["date"]) for k in KEEP_FRONTIER]
fy = [points[k]["output"] for k in KEEP_FRONTIER]

t_anchor = decimal_year("2023-03-16")
years = np.linspace(2021.5, 2026.45, 300)
guide = 2.00 * 0.5 ** ((years - t_anchor) / 1.10)

# ------------------------------------------------------------------ plot
fig, ax = plt.subplots(figsize=(10.0, 6.0))

# Frontier band, with its label in the band's empty upper-middle region
# (no frontier marker above $120 between 2023.4 and 2025.7).
ax.fill_between([2023.0, 2026.45], 50, 180, color=BAND_C, alpha=0.5,
                linewidth=0, zorder=1)
ax.text(2024.55, 148,
        "frontier output prices oscillate in a band:\n"
        "no smooth exponential trend (Du 2026)",
        ha="center", va="center", fontsize=10, color="#3a3a3a",
        style="italic", zorder=2)

ax.plot(years, guide, color=GUIDE_C, linewidth=1.8, linestyle=(0, (6, 3)),
        zorder=3, label="stylized guide: Du economy-tier half-life (1.10 y)")
ax.scatter(cx, cy, marker="o", s=58, facecolors=COMMODITY_C,
           edgecolors="#6b7785", linewidths=0.7, zorder=4,
           label="commodity-tier milestones (raw)")
ax.scatter(fx, fy, marker="s", s=58, facecolors=FRONTIER_C,
           edgecolors="black", linewidths=0.7, zorder=5,
           label="frontier-tier milestones (raw)")

# Annotation 1: o3 repricing (binding counterexample). Text in the empty
# region right of the 2024 commodity cluster.
pre, post = points["OpenAI o3 (pre-cut)"], points["OpenAI o3 (post-cut)"]
ax.annotate("", xy=(decimal_year(post["date"]), post["output"]),
            xytext=(decimal_year(pre["date"]), pre["output"]),
            arrowprops=dict(arrowstyle="->", color="#1a1a1a",
                            linewidth=1.3), zorder=6)
ax.annotate("o3 −80% repricing (Jun 2025)",
            xy=(decimal_year(post["date"]), post["output"]),
            xytext=(2024.95, 2.3), fontsize=9.5, color="#1a1a1a",
            arrowprops=dict(arrowstyle="-", color="#999999",
                            linewidth=0.7), zorder=6)

# Annotation 2: davinci anchor (tier reassignment disclosed in the label).
dav = points["GPT-3 Davinci"]
ax.annotate("GPT-3 davinci $60 (2021) — then the frontier",
            xy=(decimal_year(dav["date"]), dav["output"]),
            xytext=(2020.15, 215), fontsize=9.5, color="#1a1a1a",
            arrowprops=dict(arrowstyle="-", color="#999999",
                            linewidth=0.7), zorder=6)

ax.set_yscale("log")
ax.set_xlim(2020, 2026.6)
ax.set_ylim(0.12, 420)
ax.set_yticks([0.25, 1, 4, 16, 60, 180])
ax.set_yticklabels(["$0.25", "$1", "$4", "$16", "$60", "$180"])
ax.set_ylabel("USD per 1M output tokens (log scale)")
ax.set_xticks([2020, 2021, 2022, 2023, 2024, 2025, 2026])
ax.spines[["top", "right"]].set_visible(False)
ax.grid(axis="y", color="#e2e2e2", linewidth=0.6)
ax.set_axisbelow(True)
ax.legend(frameon=False, loc="lower left", handlelength=2.4)

fig.suptitle("Commodity-tier token prices collapsed; frontier prices did "
             "not follow",
             fontsize=14, fontweight="bold", x=0.01, ha="left", y=1.02)
fig.text(0.01, 0.965,
         "Raw price milestones with one stylized reconstruction from Du's "
         "estimated half-lives — illustrative, not fitted. "
         "Log scale: equal vertical steps are equal percentage changes.",
         fontsize=9.5, color=TEXT_GRAY, ha="left")
fig.text(0.01, -0.02,
         "Economy and mid tiers pooled as “commodity”; flagship and "
         "reasoning as “frontier” (presentation pooling — Du estimates "
         "the tiers separately: economy half-life 1.10 y, mid 1.55 y; "
         "guide curve shows the economy rate).\nMilestones: 15 of 32 "
         "collected points shown; full set with sources in "
         "r5-du-triangulation.md (archived pricing pages and launch "
         "announcements, accessed June 12, 2026).\nSources: Du (2026), "
         "arXiv:2603.28576 (preprint) — half-lives and the May 2024 "
         "structural break (technology-driven → competition-driven "
         "decline) are Du's estimates; band spans observed frontier "
         "output prices $50–180/M, 2023–2026.",
         fontsize=8, color=TEXT_GRAY, va="top", linespacing=1.45)

fig.tight_layout(rect=(0, 0, 1, 0.94))
for ext in ("png", "svg"):
    fig.savefig(OUT / f"fig3_token_price_decline.{ext}", dpi=300,
                bbox_inches="tight")
plt.close(fig)

# Grayscale-legibility proof (Rec. 709 luminance).
img = plt.imread(OUT / "fig3_token_price_decline.png")
gray = (0.2126 * img[..., 0] + 0.7152 * img[..., 1] + 0.0722 * img[..., 2])
plt.imsave(OUT / "fig3_token_price_decline_gray.png", gray, cmap="gray",
           vmin=0, vmax=1)
print("wrote fig3_token_price_decline.png / .svg / _gray.png to", OUT)
