"""Figure 2 (policy brief) — provider concentration, honesty-pass rebuild (v3).

Outputs: drafts/version_1/figures/fig2_provider_concentration.{png,svg}

Data discipline and assumptions
-------------------------------
- All shares are Menlo Ventures EOY-2025 estimates of enterprise LLM API
  DOLLAR SPEND (survey N=495, U.S. enterprises; triangulated with public
  financials). Loaded from data/menlo-ventures/menlo_2025_eoy.json.
  Never mixed with the mid-year USAGE-share figures (different definition).
- Trajectory points (Panel B):
    Anthropic: 12% (2023), 24% (2024), 40% (2025)  — all three reported.
    OpenAI:    50% (2023),  [2024 NOT reported],  27% (2025).
    Google:     7% (2023),  [2024 NOT reported],  21% (2025).
  Google's 2023 point (7%) is the EOY-report anchor documented in CLAUDE.md;
  it is not present in the on-disk EOY JSON, so it is set here as a constant
  with this comment as provenance.
- Honesty conventions: markers mark only reported values; connectors across
  unreported years are light and dashed (visual guides, not measurements).
  The 2023 top-three total (~69% = 50+12+7) is derived by summation, not
  reported by Menlo, and the in-panel footnote says so.
- Vendor adjacency disclosed in the subtitle: Menlo is an Anthropic investor.
- Grayscale legibility: distinct marker shapes per series (circle/square/
  triangle), direct series labels instead of hue-only encoding.
"""

import json
from pathlib import Path

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "drafts" / "version_1" / "figures"
OUT.mkdir(parents=True, exist_ok=True)

# Palette: muted grays + one accent (deep blue), grayscale-distinguishable.
ACCENT = "#1f4e79"   # accent — Anthropic (largest EOY share)
DARK = "#595959"     # OpenAI
MID = "#8c8c8c"      # Google
LIGHT = "#bfbfbf"    # all others
GRID = "#d9d9d9"
TEXT_GRAY = "#555555"

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.size": 10,
    "axes.titlesize": 10.5,
    "axes.labelsize": 9.5,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "svg.fonttype": "none",
})

with open(DATA / "menlo-ventures" / "menlo_2025_eoy.json", encoding="utf-8") as f:
    eoy = json.load(f)

share = eoy["market_share_dollars_spent"]
anth_hist = eoy["historical_anthropic_share"]   # 2023, 2024, 2025_eoy
oai_hist = eoy["historical_openai_share"]       # 2023, 2025_eoy (no 2024)
GOOGLE_2023 = 7.0   # % — EOY-report anchor per CLAUDE.md (see header note)
GOOGLE_2025 = share["google"] * 100

fig, (ax_a, ax_b) = plt.subplots(1, 2, figsize=(10.5, 4.8))

# ---------------------------------------------------------------- Panel A
labels = ["All others", "Google", "OpenAI", "Anthropic"]
values = [share["remaining_long_tail"] * 100, GOOGLE_2025,
          share["openai"] * 100, share["anthropic"] * 100]
colors = [LIGHT, MID, DARK, ACCENT]
bars = ax_a.barh(labels, values, color=colors, height=0.6)
for bar, v in zip(bars, values):
    ax_a.text(bar.get_width() + 0.9, bar.get_y() + bar.get_height() / 2,
              f"{v:.0f}%", va="center", fontsize=10)
ax_a.set_xlim(0, 48)
ax_a.set_xlabel("Share of enterprise LLM API dollar spend (%)")
ax_a.set_title("A. Dollar-spend shares, EOY 2025", loc="left")
ax_a.spines[["top", "right"]].set_visible(False)
ax_a.grid(axis="x", color=GRID, linewidth=0.6)
ax_a.set_axisbelow(True)
ax_a.annotate(f"Top three: {share['top_three_combined'] * 100:.0f}%",
              xy=(0.97, 0.08), xycoords="axes fraction", ha="right",
              fontsize=10.5, fontweight="bold", color=ACCENT)

# ---------------------------------------------------------------- Panel B
# Point chart: markers only at reported values. Solid connector permitted
# for Anthropic (all adjacent years reported); light dashed connectors for
# OpenAI and Google across the unreported 2024.
anth_xy = ([2023, 2024, 2025],
           [anth_hist["2023"] * 100, anth_hist["2024"] * 100,
            anth_hist["2025_eoy"] * 100])
oai_xy = ([2023, 2025], [oai_hist["2023"] * 100, oai_hist["2025_eoy"] * 100])
goog_xy = ([2023, 2025], [GOOGLE_2023, GOOGLE_2025])

# Anthropic — all points reported: solid line + solid circles (accent).
ax_b.plot(*anth_xy, color=ACCENT, linewidth=1.4, zorder=2)
ax_b.scatter(*anth_xy, marker="o", s=42, color=ACCENT, zorder=3)
# OpenAI — dashed light connector, solid square markers at reported points.
ax_b.plot(*oai_xy, color=DARK, linewidth=1.0, linestyle=(0, (4, 3)),
          alpha=0.55, zorder=2)
ax_b.scatter(*oai_xy, marker="s", s=38, color=DARK, zorder=3)
# Google — same dashed treatment, triangle markers.
ax_b.plot(*goog_xy, color=MID, linewidth=1.0, linestyle=(0, (4, 3)),
          alpha=0.55, zorder=2)
ax_b.scatter(*goog_xy, marker="^", s=46, color=MID, zorder=3)

# Direct series labels at the 2025 ends (grayscale-safe, no legend needed).
ax_b.annotate("Anthropic  40%", (2025, 40), textcoords="offset points",
              xytext=(7, -3), fontsize=9.5, color=ACCENT, fontweight="bold")
ax_b.annotate("OpenAI  27%", (2025, 27), textcoords="offset points",
              xytext=(7, -3), fontsize=9.5, color=DARK)
ax_b.annotate("Google  21%", (2025, 21), textcoords="offset points",
              xytext=(7, -3), fontsize=9.5, color=MID)
ax_b.annotate("50%", (2023, 50), textcoords="offset points", xytext=(-4, 7),
              fontsize=9, color=DARK)
ax_b.annotate("12%", (2023, 12), textcoords="offset points", xytext=(-4, 7),
              fontsize=9, color=ACCENT)
ax_b.annotate("7%", (2023, 7), textcoords="offset points", xytext=(-4, -14),
              fontsize=9, color=MID)
ax_b.annotate("24%", (2024, 24), textcoords="offset points", xytext=(0, 8),
              fontsize=9, color=ACCENT, ha="center")

# Mark the unreported year explicitly.
ax_b.annotate("2024 not reported\n(OpenAI, Google)", xy=(2024, 38.5),
              ha="center", fontsize=8.5, color=TEXT_GRAY, style="italic")

ax_b.set_xlim(2022.75, 2025.85)
ax_b.set_ylim(0, 58)
ax_b.set_xticks([2023, 2024, 2025])
ax_b.set_ylabel("Share of enterprise LLM API dollar spend (%)")
ax_b.set_title("B. Reported share points, 2023 → 2025", loc="left")
ax_b.spines[["top", "right"]].set_visible(False)
ax_b.grid(axis="y", color=GRID, linewidth=0.6)
ax_b.set_axisbelow(True)

# In-panel honesty footnote (>= 8 pt).
ax_b.text(0.0, -0.26,
          "Markers = reported values; dashed connectors are visual guides across\n"
          "unreported years, not measurements. 2023 top-three total (~69%) is\n"
          "derived by summing per-provider shares.",
          transform=ax_b.transAxes, fontsize=8, color=TEXT_GRAY, va="top")

# ------------------------------------------------------- titles + caption
fig.suptitle("Menlo-estimated U.S. enterprise LLM API dollar spend "
             "remains highly concentrated",
             fontsize=12.5, fontweight="bold", x=0.01, ha="left", y=1.06)
fig.text(0.01, 0.995,
         "EOY 2025 shares; survey/model estimate (N=495, U.S.); Menlo Ventures "
         "is vendor-adjacent and an Anthropic investor.",
         fontsize=9.5, color=TEXT_GRAY, ha="left")

fig.text(0.01, -0.13,
         "Provider shares are Menlo Ventures estimates of enterprise LLM API "
         "dollar spend. Dashed connectors span years with no reported figure.\n"
         "Source: Menlo Ventures, 2025: The State of Generative AI in the "
         "Enterprise (Dec 2025).",
         fontsize=8, color=TEXT_GRAY, va="top")

fig.tight_layout(rect=(0, 0, 1, 0.97))
for ext in ("png", "svg"):
    fig.savefig(OUT / f"fig2_provider_concentration.{ext}", dpi=300,
                bbox_inches="tight")
plt.close(fig)
print("wrote fig2_provider_concentration.png / .svg to", OUT)
