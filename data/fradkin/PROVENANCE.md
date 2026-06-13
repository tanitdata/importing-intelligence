---
type: data-provenance
source: Fradkin et al. 2025, Emerging Market for Intelligence
retrieved: 2026-05-04
---

# Fradkin, Demirer, Tadelis, Peng (2025) — The Emerging Market for Intelligence

## Superseding note

CLAUDE.md references this work as "Fradkin et al., 'The Emerging Market for Intelligence' (2025)." Two versions exist:

1. **Earlier working paper:** Fradkin solo, "Demand for LLMs: Descriptive Evidence on Substitution, Market Expansion, and Multi-Homing" (April 2025). PDF: https://andreyfradkin.com/assets/demandforllm.pdf. OpenRouter data, Jan–April 2025. Three stylized facts.
2. **Current, superseding:** Demirer, Fradkin, Tadelis, Peng, "The Emerging Market for Intelligence: Pricing, Supply, and Demand for LLMs." NBER Working Paper **34608** (Dec 2025). Accepted at *Journal of Economic Perspectives*. Data: OpenRouter + Microsoft Azure API usage. Six stylized facts.

**Cite the NBER WP 34608 version.** The andreyfradkin.com PDF is the superseded precursor.

## Bibliographic (current version)

- **Authors:** Mert Demirer, Andrey Fradkin, Nadav Tadelis, Sida Peng
- **Title:** The Emerging Market for Intelligence: Pricing, Supply, and Demand for LLMs
- **Venue:** NBER Working Paper 34608 (2025); forthcoming *Journal of Economic Perspectives*
- **URL:** https://www.nber.org/papers/w34608
- **DOI:** 10.3386/w34608
- **Authors' affiliations at time of writing:** Demirer (MIT Sloan; prior Microsoft postdoc), Fradkin (Amazon; work not conducted as Amazon employee), Tadelis, Peng (Microsoft, equity holder). Disclose in essay.

## Six stylized facts (directly relevant)

1. Rapid growth in number of models, creators, inference providers. Open-source entrants drive the growth.
2. Price declines and **persistent price heterogeneity** across and within intelligence tiers. **Open-source models ≈90% cheaper than comparable closed-source models at the same intelligence tier.**
3. Market dynamism — frequent turnover among leading models and creators.
4. Horizontal and vertical differentiation — no single model dominates across use cases.
5. Short-run price elasticities just above 1 — limited scope for Jevons-paradox effects.
6. Share of firms using multiple models increased over time, but **most firms concentrate usage on a single model**, consistent with experimentation rather than persistent multi-homing.

## Why this matters for the essay

- Fact 2 (open-source 90% cheaper at same intelligence tier) is load-bearing for the resilience sketch in Section 7. If consumer countries can access open-source at 10% the cost of closed-source for equivalent capability, the production-vs-flow argument needs to address why they still face meaningful chokepoint exposure. Likely answer: inference-hosting, legal/jurisdictional access, payment rails, updates. Worth thinking through carefully.
- Fact 6 tension with Menlo Ventures "11% vendor switching": Menlo says switching is rare; Fradkin says multi-homing is increasing but most firms still single-model. These are consistent but framed differently. Essay should cite both and note concordance.
- Fact 4 (no single model dominates across use cases) complicates simple "top-three = 88%" chokepoint framing. Need to distinguish concentration at the API layer (high) from concentration at the task/use-case layer (differentiated).

## Data access

- **OpenRouter:** public via https://openrouter.ai/api/v1/models and state-of-AI pages.
- **Microsoft Azure API usage:** proprietary, not redistributable. Essay can only cite, not replicate.
- **OpenRouter State of AI 2025 (100T tokens, 2024–2025 data):** https://openrouter.ai/state-of-ai — captured separately in data/openrouter/.

## Files in this folder

- `PROVENANCE.md` — this file
- `fradkin_2025_six_facts.json` — machine-readable summary
- (PDF of NBER WP to be captured into refs/ in Week 1 or Week 2; NBER permits academic use)
