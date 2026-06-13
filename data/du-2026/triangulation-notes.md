---
type: note
created: 2026-06-12
tags: [triangulation, token-economics, du-2026, pricing, figure-2]
links: [du-2026-tiered-super-moore, demirer-fradkin-2025, epoch-ai-price-trends]
---

# R5 — Triangulation of Du (2026) Tiered Price-Decline Findings

Task: verify the DIRECTION (not precision) of Du's tiered finding — steep price decline at economy/mid tiers, resistance at flagship/reasoning tier — against independent sources, and assemble raw milestone price points for the Figure 2 overlay. All access dates 2026-06-12. Note: Firecrawl search returned auth errors (401) this session; searches ran via Exa, fetches via WebFetch and curl against Wayback Machine.

## Verdict (per tier)

| Du claim | Direction independently supported? | Strength |
|---|---|---|
| ~600-fold overall decline 2020–2026 | YES — raw milestones span GPT-3 davinci $60/M (Dec 2021) to sub-$0.30/M commodity models (2025–26), a 200–600x range depending on endpoint choice; Epoch reports capability-constant declines of 9x–900x/yr | Strong on direction; the "600-fold" scalar is endpoint-sensitive |
| Economy-tier half-life 1.10y / mid-tier 1.55y (faster than Moore) | YES on direction — Epoch median 50x/yr (200x/yr post-Jan 2024) at fixed capability implies half-lives far under 1 year, i.e., even faster than Du; Demirer et al. confirm declines driven by new cheaper entrants | Strong. Note Epoch's series is capability-constant (model substitution allowed); Du's tiers are price-band cohorts — different constructions that agree on direction |
| Flagship tier resists exponential decay (R² = 0.031) | YES, with one material counterexample — top-of-market list prices rose 2024→2025 (Claude 3 Opus $75/M output → GPT-4.5 $150/M → o1-pro $600/M, per Artificial Analysis commentary); Demirer et al.: usage-weighted prices stayed flat/rose in 2025 and closed-source models rarely reprice. COUNTEREXAMPLE: o3's 80% cut (June 2025) | Moderate. Supported as a statement about the price *frontier*, not about every flagship model |
| Reasoning premium ≈31.5x | DIRECTIONALLY plausible, magnitude unverified — o1 output $60/M vs. market median $8.05/M (≈7.5x list); o1 emitted ~8x the tokens of GPT-4o on identical benchmarks (Artificial Analysis), so effective cost premium reaches ~20–60x; o1-pro at $600/M output is 40x GPT-4o's $15/M | Order of magnitude consistent; the specific 31.5x multiple is Du's estimate and should be attributed as such. COUNTEREXAMPLE: DeepSeek-R1 priced reasoning at $2.19/M output |
| Software/TFP ≈103.7%, hardware ≈−0.9% | NOT independently confirmed — Epoch's published commentary lists hardware cost-effectiveness among plausible drivers and explicitly says several drivers are opaque from public data | Weak external support. Treat as model-dependent preprint decomposition, not a triangulated fact |
| May 2024 Chow break | Consistent with Epoch's observation that decline rates accelerated post-January 2024 (median 50x → 200x/yr) and with GPT-4o's May 2024 price cut ($5/$15 vs. GPT-4-turbo $10/$30); exact break date not independently testable from our sources | Directionally consistent |

Bottom line for the brief: the tiered DIRECTION survives triangulation. Commodity-tier collapse is the best-supported claim in Du; flagship resistance is supported as a frontier-of-pricing phenomenon with at least one large counterexample (o3); the TFP/hardware decomposition has no independent corroboration and should be quarantined behind attribution.

## Source 1 — Epoch AI, "LLM inference prices have fallen rapidly but unequally across tasks"

- URL: https://epoch.ai/data-insights/llm-inference-price-trends (accessed 2026-06-12). Authors Ben Cottier, Ben Snodin, David Owen, Tom Adamczewski; published 2025-03-12.
- Construction: capability-constant price series. They find, at each date, the cheapest model matching or beating a fixed benchmark score (MMLU, GPQA Diamond, HumanEval, etc., at thresholds like "GPT-3.5 level," "GPT-4 level," "GPT-4o level"), then fit log-linear regressions on those prices. Data combine Artificial Analysis and Epoch AI records over roughly Oct 2021–early 2025.
- Headline rates: decline of 9x to 900x per year depending on benchmark and threshold; median ≈50x/yr; post-January 2024 median ≈200x/yr. GPT-4-level performance on GPQA Diamond: ~40x/yr decline. Slowest (~9x/yr): GPT-3.5-level MMLU.
- Companion summary (Epoch trends page, https://epoch.ai/trends, accessed 2026-06-12): cost to inference at fixed performance "has been halving every 2 months" / fell ~2 OOMs per year. Year-in-review (https://epoch.ai/latest/top-10-data-insights-and-gradient-updates-of-2025, accessed 2026-06-12): >10x drop in price per token at equivalent performance, April 2023–March 2025.
- Caveats they state: reasoning models excluded from the headline analysis (token-count inflation); fastest declines rest on under-a-year windows and may not persist; per-token price trends and total-evaluation-cost trends agree within ~2x.
- Relation to Du: stronger declines than Du's tier half-lives (because substitution to newer cheaper models is allowed, where Du tracks tier cohorts), same direction; their reasoning-model exclusion implicitly corroborates that the reasoning tier behaves differently.

## Source 2 — Artificial Analysis (current cross-section + reasoning-cost commentary)

- Model pages and methodology: https://artificialanalysis.ai/models, https://artificialanalysis.ai/models/o3, https://artificialanalysis.ai/models/o1 (accessed 2026-06-12). Prices in USD per 1M tokens; "blended" figures use a 7:2:1 cache-hit:input:output ratio.
- Current anchors (accessed 2026-06-12): market medians ≈ $1.55–1.60/M input and $8.05–8.10/M output across tracked models. o3: $2 input / $8 output. o1 (legacy): $15 / $60 — "expensive" relative to medians. Cheapest tracked models: Qwen3.5 0.8B ≈$0.01–0.02/M blended; Gemma 3n E4B ≈$0.02–0.03/M blended. 364 models tracked.
- Reasoning-premium evidence (via Artificial Analysis data reported in TechCrunch, 2025-04-10, https://techcrunch.com/2025/04/10/the-rise-of-ai-reasoning-models-is-making-benchmarking-more-expensive/, and deeplearning.ai The Batch, https://www.deeplearning.ai/the-batch/reasoning-llms-are-pricey-to-test, both accessed 2026-06-12): benchmarking o1 cost $2,767 vs. GPT-4o $109 (≈25x) on the same suite; o1 generated 44M tokens vs. ~5.5M for GPT-4o (≈8x). An Epoch researcher (Denain) is quoted: the most expensive models have gotten more expensive per token over time — Claude 3 Opus $75/M output (2024) was the price ceiling at release; GPT-4.5 reached $150/M and o1-pro $600/M output (early 2025).
- Relation to Du: the 25x effective evaluation-cost gap and the 8x token-inflation factor bracket Du's 31.5x reasoning premium from below and above; the rising price ceiling directly supports flagship-tier resistance to decline.

## Source 3 — Demirer, Fradkin, Tadelis, Peng (NBER WP 34608)

- Abstract/metadata: https://www.nber.org/papers/w34608 and https://ideas.repec.org/p/nbr/nberwo/34608.html (accessed 2026-06-12). Data: OpenRouter + Microsoft Azure API usage.
- Findings relevant here (from the published abstract): price declines with persistent price heterogeneity across and within intelligence tiers; open-source models ≈90% cheaper than comparable closed-source models at the same intelligence; frequent leadership turnover; short-run price elasticities just above one; multi-homing rising but most firms concentrate on one model.
- From the authors' seminar abstract (Stanford Digital Economy Lab event page, https://events.stanford.edu/event/andrey-fradkin-the-emerging-market-for-intelligence-the-supply-demand-and-usage-of-llms, accessed 2026-06-12): usage-weighted prices remain relatively flat even as the price per unit of intelligence has fallen — i.e., demand migrates toward more expensive, higher-quality models even as constant-quality prices collapse. Secondary readings of the paper (whoisnnamdi notes, https://whoisnnamdi.com/notes/@demirerEmergingMarketIntelligence/, accessed 2026-06-12) add: most of the decline comes from new cheaper models, not incumbent repricing; closed-source models rarely change list price; token-weighted prices actually rose during 2025. A LinkedIn summary circulating the paper claims GPT-4-class capability fell ~1,000x in two years — UNVERIFIED against the paper text; do not cite that figure without checking the working paper itself.
- Relation to Du: independently supports both halves of the tiered picture — constant-intelligence prices collapse (commodity dynamics) while the usage-weighted and frontier price level holds or rises (flagship stickiness). Quarter-by-quarter decline rates at constant intelligence tier: not extractable from the abstract; UNVERIFIED pending full-text read.

## Source 4 — Raw milestone price points (Figure 2 overlay)

All archived snapshots fetched via web.archive.org on 2026-06-12; live pages accessed 2026-06-12. Prices are USD per 1M tokens (provider list prices; original 2020–2023 OpenAI prices were quoted per 1K tokens and are converted x1000). GPT-3-era models billed one rate for prompt+completion combined.

| # | Model | Date (price effective/observed) | Input $/M | Output $/M | Source (URL) | Access date |
|---|---|---|---|---|---|---|
| 1 | GPT-3 Davinci | 2021-12-04 (observed) | 60.00 (combined) | 60.00 (combined) | https://web.archive.org/web/20211204021218/https://openai.com/api/pricing/ | 2026-06-12 |
| 2 | GPT-3 Curie | 2021-12-04 (observed) | 6.00 (combined) | 6.00 (combined) | same snapshot | 2026-06-12 |
| 3 | text-davinci (base Davinci) | 2023-03-16 (observed; post-Sept-2022 cut) | 20.00 (combined) | 20.00 (combined) | https://web.archive.org/web/20230316024934/https://openai.com/pricing | 2026-06-12 |
| 4 | gpt-3.5-turbo | 2023-03-16 (observed; launched 2023-03-01) | 2.00 (combined) | 2.00 (combined) | same snapshot | 2026-06-12 |
| 5 | GPT-4 (8K context) | 2023-03-16 (observed; launched 2023-03-14) | 30.00 | 60.00 | same snapshot | 2026-06-12 |
| 6 | GPT-4 (32K context) | 2023-03-16 (observed) | 60.00 | 120.00 | same snapshot | 2026-06-12 |
| 7 | Claude 3 Opus | 2024-03-04 (launch) | 15.00 | 75.00 | https://www.anthropic.com/news/claude-3-family | 2026-06-12 |
| 8 | Claude 3 Sonnet | 2024-03-04 (launch) | 3.00 | 15.00 | same page | 2026-06-12 |
| 9 | Claude 3 Haiku | 2024-03-04 (announced) | 0.25 | 1.25 | same page | 2026-06-12 |
| 10 | gpt-4-turbo | 2024-05-31 (observed; launched 2024-04) | 10.00 | 30.00 | https://web.archive.org/web/20240531225017/https://openai.com/api/pricing/ | 2026-06-12 |
| 11 | gpt-4o | 2024-05-31 (observed; launched 2024-05-13) | 5.00 | 15.00 | same snapshot | 2026-06-12 |
| 12 | gpt-3.5-turbo-0125 | 2024-05-31 (observed) | 0.50 | 1.50 | same snapshot | 2026-06-12 |
| 13 | Claude 3.5 Sonnet | 2024-06-21 (launch) | 3.00 | 15.00 | https://www.anthropic.com/news/claude-3-5-sonnet | 2026-06-12 |
| 14 | Gemini 1.5 Flash (≤128K prompts) | 2024-07-12 (observed) | 0.35 | 1.05 | https://web.archive.org/web/20240712071622/https://ai.google.dev/pricing | 2026-06-12 |
| 15 | Gemini 1.5 Pro (≤128K prompts) | 2024-07-12 (observed) | 3.50 | 10.50 | same snapshot | 2026-06-12 |
| 16 | DeepSeek-V3 (standard, cache miss) | 2024-12-26 announced; standard rate from 2025-02-08 | 0.27 | 1.10 | https://api-docs.deepseek.com/news/news1226 | 2026-06-12 |
| 17 | DeepSeek-R1 (cache miss) | 2025-01-20 (launch) | 0.55 | 2.19 | https://api-docs.deepseek.com/news/news250120 | 2026-06-12 |
| 18 | OpenAI o3 (pre-cut) | 2025-04 launch to 2025-06-10 | 10.00 | 40.00 | https://venturebeat.com/ai/openai-announces-80-price-drop-for-o3-its-most-powerful-reasoning-model + https://community.openai.com/t/o3-is-80-cheaper-and-introducing-o3-pro/1284925 | 2026-06-12 |
| 19 | OpenAI o3 (post-cut) | 2025-06-10 | 2.00 | 8.00 | same sources; confirmed live at https://artificialanalysis.ai/models/o3 | 2026-06-12 |
| 20 | OpenAI o1 | observed 2026-06-12 (launch-era list price) | 15.00 | 60.00 | https://artificialanalysis.ai/models/o1 | 2026-06-12 |
| 21 | GPT-5.5 | live 2026-06-12 | 5.00 | 30.00 | https://developers.openai.com/api/docs/pricing | 2026-06-12 |
| 22 | GPT-5.5-pro | live 2026-06-12 | 30.00 | 180.00 | same page | 2026-06-12 |
| 23 | GPT-5.4-mini | live 2026-06-12 | 0.75 | 4.50 | same page | 2026-06-12 |
| 24 | GPT-5.4-nano | live 2026-06-12 | 0.20 | 1.25 | same page | 2026-06-12 |
| 25 | Claude Fable 5 | live 2026-06-12 | 10.00 | 50.00 | https://platform.claude.com/docs/en/docs/about-claude/pricing | 2026-06-12 |
| 26 | Claude Opus 4.8 | live 2026-06-12 | 5.00 | 25.00 | same page | 2026-06-12 |
| 27 | Claude Sonnet 4.6 | live 2026-06-12 | 3.00 | 15.00 | same page | 2026-06-12 |
| 28 | Claude Haiku 4.5 | live 2026-06-12 | 1.00 | 5.00 | same page | 2026-06-12 |
| 29 | Gemini 3.1 Pro Preview (≤200K) | live 2026-06-12 | 2.00 | 12.00 | https://ai.google.dev/gemini-api/docs/pricing | 2026-06-12 |
| 30 | Gemini 2.5 Flash-Lite | live 2026-06-12 | 0.10 | 0.40 | same page | 2026-06-12 |
| 31 | DeepSeek-V4-Flash | live 2026-06-12 | 0.14 (cache miss) | 0.28 | https://api-docs.deepseek.com/quick_start/pricing | 2026-06-12 |
| 32 | DeepSeek-V4-Pro | live 2026-06-12 | 0.435 (cache miss) | 0.87 | same page | 2026-06-12 |

```json
{
  "dataset": "fig2_overlay_milestones",
  "units": "USD per 1M tokens",
  "collected": "2026-06-12",
  "notes": "GPT-3-era OpenAI prices were single-rate (prompt+completion combined), recorded in both input and output fields with combined=true. Dates marked observed are archive-snapshot dates, not launch dates.",
  "points": [
    {"model": "GPT-3 Davinci", "date": "2021-12-04", "input": 60.0, "output": 60.0, "combined": true, "tier": "flagship", "source": "https://web.archive.org/web/20211204021218/https://openai.com/api/pricing/", "date_type": "observed"},
    {"model": "GPT-3 Curie", "date": "2021-12-04", "input": 6.0, "output": 6.0, "combined": true, "tier": "mid", "source": "https://web.archive.org/web/20211204021218/https://openai.com/api/pricing/", "date_type": "observed"},
    {"model": "text-davinci (base)", "date": "2023-03-16", "input": 20.0, "output": 20.0, "combined": true, "tier": "flagship-legacy", "source": "https://web.archive.org/web/20230316024934/https://openai.com/pricing", "date_type": "observed"},
    {"model": "gpt-3.5-turbo", "date": "2023-03-16", "input": 2.0, "output": 2.0, "combined": true, "tier": "economy", "source": "https://web.archive.org/web/20230316024934/https://openai.com/pricing", "date_type": "observed"},
    {"model": "GPT-4 8K", "date": "2023-03-16", "input": 30.0, "output": 60.0, "combined": false, "tier": "flagship", "source": "https://web.archive.org/web/20230316024934/https://openai.com/pricing", "date_type": "observed"},
    {"model": "GPT-4 32K", "date": "2023-03-16", "input": 60.0, "output": 120.0, "combined": false, "tier": "flagship", "source": "https://web.archive.org/web/20230316024934/https://openai.com/pricing", "date_type": "observed"},
    {"model": "Claude 3 Opus", "date": "2024-03-04", "input": 15.0, "output": 75.0, "combined": false, "tier": "flagship", "source": "https://www.anthropic.com/news/claude-3-family", "date_type": "launch"},
    {"model": "Claude 3 Sonnet", "date": "2024-03-04", "input": 3.0, "output": 15.0, "combined": false, "tier": "mid", "source": "https://www.anthropic.com/news/claude-3-family", "date_type": "launch"},
    {"model": "Claude 3 Haiku", "date": "2024-03-04", "input": 0.25, "output": 1.25, "combined": false, "tier": "economy", "source": "https://www.anthropic.com/news/claude-3-family", "date_type": "launch"},
    {"model": "gpt-4-turbo", "date": "2024-05-31", "input": 10.0, "output": 30.0, "combined": false, "tier": "flagship", "source": "https://web.archive.org/web/20240531225017/https://openai.com/api/pricing/", "date_type": "observed"},
    {"model": "gpt-4o", "date": "2024-05-31", "input": 5.0, "output": 15.0, "combined": false, "tier": "flagship", "source": "https://web.archive.org/web/20240531225017/https://openai.com/api/pricing/", "date_type": "observed"},
    {"model": "gpt-3.5-turbo-0125", "date": "2024-05-31", "input": 0.5, "output": 1.5, "combined": false, "tier": "economy", "source": "https://web.archive.org/web/20240531225017/https://openai.com/api/pricing/", "date_type": "observed"},
    {"model": "Claude 3.5 Sonnet", "date": "2024-06-21", "input": 3.0, "output": 15.0, "combined": false, "tier": "mid", "source": "https://www.anthropic.com/news/claude-3-5-sonnet", "date_type": "launch"},
    {"model": "Gemini 1.5 Flash (<=128K)", "date": "2024-07-12", "input": 0.35, "output": 1.05, "combined": false, "tier": "economy", "source": "https://web.archive.org/web/20240712071622/https://ai.google.dev/pricing", "date_type": "observed"},
    {"model": "Gemini 1.5 Pro (<=128K)", "date": "2024-07-12", "input": 3.5, "output": 10.5, "combined": false, "tier": "mid", "source": "https://web.archive.org/web/20240712071622/https://ai.google.dev/pricing", "date_type": "observed"},
    {"model": "DeepSeek-V3 (cache miss, standard)", "date": "2025-02-08", "input": 0.27, "output": 1.1, "combined": false, "tier": "economy", "source": "https://api-docs.deepseek.com/news/news1226", "date_type": "effective"},
    {"model": "DeepSeek-R1 (cache miss)", "date": "2025-01-20", "input": 0.55, "output": 2.19, "combined": false, "tier": "reasoning-economy", "source": "https://api-docs.deepseek.com/news/news250120", "date_type": "launch"},
    {"model": "OpenAI o3 (pre-cut)", "date": "2025-04-16", "input": 10.0, "output": 40.0, "combined": false, "tier": "reasoning-flagship", "source": "https://community.openai.com/t/o3-is-80-cheaper-and-introducing-o3-pro/1284925", "date_type": "launch"},
    {"model": "OpenAI o3 (post-cut)", "date": "2025-06-10", "input": 2.0, "output": 8.0, "combined": false, "tier": "reasoning-flagship", "source": "https://community.openai.com/t/o3-is-80-cheaper-and-introducing-o3-pro/1284925", "date_type": "effective"},
    {"model": "OpenAI o1", "date": "2026-06-12", "input": 15.0, "output": 60.0, "combined": false, "tier": "reasoning-flagship", "source": "https://artificialanalysis.ai/models/o1", "date_type": "observed"},
    {"model": "GPT-5.5", "date": "2026-06-12", "input": 5.0, "output": 30.0, "combined": false, "tier": "flagship", "source": "https://developers.openai.com/api/docs/pricing", "date_type": "observed"},
    {"model": "GPT-5.5-pro", "date": "2026-06-12", "input": 30.0, "output": 180.0, "combined": false, "tier": "reasoning-flagship", "source": "https://developers.openai.com/api/docs/pricing", "date_type": "observed"},
    {"model": "GPT-5.4-mini", "date": "2026-06-12", "input": 0.75, "output": 4.5, "combined": false, "tier": "mid", "source": "https://developers.openai.com/api/docs/pricing", "date_type": "observed"},
    {"model": "GPT-5.4-nano", "date": "2026-06-12", "input": 0.2, "output": 1.25, "combined": false, "tier": "economy", "source": "https://developers.openai.com/api/docs/pricing", "date_type": "observed"},
    {"model": "Claude Fable 5", "date": "2026-06-12", "input": 10.0, "output": 50.0, "combined": false, "tier": "flagship", "source": "https://platform.claude.com/docs/en/docs/about-claude/pricing", "date_type": "observed"},
    {"model": "Claude Opus 4.8", "date": "2026-06-12", "input": 5.0, "output": 25.0, "combined": false, "tier": "flagship", "source": "https://platform.claude.com/docs/en/docs/about-claude/pricing", "date_type": "observed"},
    {"model": "Claude Sonnet 4.6", "date": "2026-06-12", "input": 3.0, "output": 15.0, "combined": false, "tier": "mid", "source": "https://platform.claude.com/docs/en/docs/about-claude/pricing", "date_type": "observed"},
    {"model": "Claude Haiku 4.5", "date": "2026-06-12", "input": 1.0, "output": 5.0, "combined": false, "tier": "economy", "source": "https://platform.claude.com/docs/en/docs/about-claude/pricing", "date_type": "observed"},
    {"model": "Gemini 3.1 Pro Preview (<=200K)", "date": "2026-06-12", "input": 2.0, "output": 12.0, "combined": false, "tier": "flagship", "source": "https://ai.google.dev/gemini-api/docs/pricing", "date_type": "observed"},
    {"model": "Gemini 2.5 Flash-Lite", "date": "2026-06-12", "input": 0.1, "output": 0.4, "combined": false, "tier": "economy", "source": "https://ai.google.dev/gemini-api/docs/pricing", "date_type": "observed"},
    {"model": "DeepSeek-V4-Flash (cache miss)", "date": "2026-06-12", "input": 0.14, "output": 0.28, "combined": false, "tier": "economy", "source": "https://api-docs.deepseek.com/quick_start/pricing", "date_type": "observed"},
    {"model": "DeepSeek-V4-Pro (cache miss)", "date": "2026-06-12", "input": 0.435, "output": 0.87, "combined": false, "tier": "mid", "source": "https://api-docs.deepseek.com/quick_start/pricing", "date_type": "observed"}
  ]
}
```

What the raw points show: along the economy/mid track, the price of "a capable general model" fell from $60/M (davinci, 2021) to $2/M (gpt-3.5-turbo, 2023) to $0.10–0.28/M (Flash-Lite, DeepSeek V4-Flash, 2026) — two-plus orders of magnitude, consistent with Du's super-Moore tiers. Along the flagship track, the launch-price band has not collapsed: GPT-4 output was $60–120/M in 2023, Claude 3 Opus output $75/M in 2024, o1 output $60/M in late 2024, GPT-5.5-pro output $180/M in 2026, Claude Fable 5 output $50/M with fast-mode Opus at $150/M. The frontier price level oscillates in a $50–180/M output band rather than decaying — Du's flagship non-decay claim describes this band well, even though individual flagship models (gpt-4o, o3, Opus 4.5+) do undergo discrete repricing.

## Source 5 — Reasoning-premium check (independent of Du)

- Artificial Analysis current data (accessed 2026-06-12): o1 list price 7.5x the market median on output; effective evaluation cost o1 vs. GPT-4o ≈25x (via TechCrunch 2025-04-10); token inflation ≈8x. o1-pro and GPT-4.5 reached $600/M and $150/M output (early 2025) versus a $8/M output median.
- These bracket Du's 31.5x premium without confirming it precisely. Two complications cut against a clean premium story: (1) DeepSeek-R1 launched reasoning at $2.19/M output (Jan 2025), within commodity range; (2) o3 was repriced down 80% in June 2025 with OpenAI attributing the cut to inference-stack optimization on the identical model — evidence that even reasoning-tier prices are contestable when serving efficiency improves.

## Contradictions and tensions to report honestly

1. **o3's 80% cut (2025-06-10)** is the sharpest counterexample to "flagship/reasoning prices resist decline." A frontier reasoning model went from $10/$40 to $2/$8 in about two months, with no model change. Du's flagship non-decay finding should be framed as "no smooth exponential trend at the frontier" — which is consistent with step repricing — not as "flagship prices do not fall."
2. **Epoch vs. Du magnitudes differ by construction.** Epoch's capability-constant series (substitution allowed) declines far faster than Du's tier half-lives; both cannot be quoted as the same quantity. The brief should never present Epoch's 50x/yr and Du's 1.10y half-life as corroborating the same number — they corroborate the same direction.
3. **Hardware decomposition.** Du attributes ≈−0.9% to GPU hardware; Epoch's public commentary treats hardware cost-effectiveness as one plausible driver among several and flags driver attribution as opaque. Du's decomposition is unreplicated.
4. **Gemini Flash drift.** Gemini 1.5 Flash (2024) at $0.35/$1.05 vs. Gemini 3.5 Flash (2026) at $1.50/$9.00 — the "Flash" brand migrated up-tier and up-price. Tier labels are not stable model identities; any tier-cohort series (including Du's) inherits this classification risk.
5. **Demirer et al. on usage-weighted prices** (flat or rising in 2025) supports flagship stickiness but also complicates the brief's "prices collapse" headline: what buyers actually pay per token has not collapsed, because demand shifts to premium models. Both facts should appear together.

## Hedging language for the brief (CON-05)

Suggested formulations: "Du (2026) estimates an approximately 600-fold decline in token prices between 2020 and 2026, with tier-specific half-lives of roughly 1.1 years (economy) and 1.6 years (mid-tier); the direction of these findings — rapid commoditization below the frontier, sticky pricing at it — is independently consistent with Epoch AI's capability-constant price series and with Demirer et al.'s finding that usage-weighted prices remained flat even as the price of constant intelligence fell." And: "Du's decomposition attributing the decline almost entirely to software and architectural innovation, with a near-zero hardware contribution, is a model-dependent result from a single preprint and has not been independently replicated; we cite it as Du's estimate rather than as an established fact." Where the flagship tier is discussed: "flagship prices have resisted smooth exponential decline, although discrete repricing events — most notably OpenAI's 80% cut to o3 in June 2025 — show the frontier is not immune to competitive pressure."

## Limitations

- Demirer et al. triangulation rests on the published abstract, a seminar abstract, and secondary notes; the full working-paper text (quarterly decline rates at constant tier, exact open/closed gap construction) was not read this session — the PDF exceeded the fetch size limit. The circulating "~1,000x in two years for GPT-4-class" figure is UNVERIFIED.
- Wayback coverage is uneven; several milestone dates are snapshot-observation dates rather than launch dates (flagged in the table). Wayback availability API rate-limited aggressively during collection; four snapshots were retrieved, others substituted with provider announcement pages.
- Current "June 2026" prices are list prices from provider documentation pages; negotiated, batch, and cached rates run 50–90% lower, and Artificial Analysis blended rates use a cache-heavy 7:2:1 ratio that is not comparable to simple input/output averages.
- Reasoning-premium magnitudes conflate two channels (higher per-token list price and higher token counts per task); Du's 31.5x is a per-token price ratio, while the strongest independent evidence (Artificial Analysis evaluation costs) measures the combined effect.
- Firecrawl search was unavailable (401 auth errors); search coverage relied on Exa, which may have different recall.
