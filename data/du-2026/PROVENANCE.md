---
type: data-provenance
source: Du 2026, Tiered Super-Moore's Law (arXiv)
retrieved: 2026-05-04
---

# Du (2026) — Tiered Super-Moore's Law

## Bibliographic

- **Author:** Mingdeng Du
- **Title:** Tiered Super-Moore's Law: Price Evolution, Production Frontiers, and Market Competition in Large Language Model Inference Services
- **Version:** v1
- **Submitted:** 2026-03-30
- **arXiv ID:** 2603.28576
- **Abstract URL:** https://arxiv.org/abs/2603.28576
- **PDF URL:** https://arxiv.org/pdf/2603.28576
- **DOI:** 10.48550/arXiv.2603.28576

## Dataset structure (per paper)

Three integrated data sources:

1. **OpenRouter API cross-section (318 models).** Collected 2026-03-28 via OpenRouter API. Fields: model id, vendor, input price ($/M tokens), output price ($/M tokens), context window. Covers OpenAI, Anthropic, Google, DeepSeek, Meta, xAI, Alibaba/Qwen, Mistral, others. Standardized to $/M tokens.
2. **Epoch AI panel (3,237 models).** From Epoch AI's Notable AI Models database. Fields: training cost (USD), training compute (FLOP), parameter count, hardware configuration, frontier status, open-weight status, region (US/EU vs. China). Covers 2020–2026.
3. **Cross-validated milestones (62 records, time series).** Manually compiled from vendor pricing pages, OpenRouter quotes, industry reports. Distribution: OpenAI 22, Anthropic 14, Google 8, DeepSeek 5, Meta 5, xAI 4, Alibaba/Qwen 4.

## Headline findings relevant to the essay

- **~600-fold decline in token prices, 2020–2026.**
- **Tiered decline:** economy half-life 1.10 years, mid-tier 1.55 years — both faster than Moore's Law's 2-year benchmark. Flagship tier defies exponential decay (R² = 0.031) due to reasoning premium averaging **31.5× non-reasoning prices**.
- **Chow structural break test identifies May 2024** as the critical market inflection point (F = 5.74, p = 0.005). Transition from technology-driven to competition-driven price acceleration.
- **Cost decomposition:** TFP residuals ≈ 103.7% of cost reduction, GPU hardware contribution ≈ −0.9%. Software/architectural innovation, not hardware, drives the decline. (Relevant for production-vs-flow argument.)
- **US-China training cost gap:** 63×, statistically attributable to architectural innovation, not factor-price differentials ($/FLOP difference insignificant, p = 0.228).
- **Market concentration:** HHI fell from 4,558 to 2,086 over three years. Concentration is declining on this metric — worth engaging carefully, since the Menlo Ventures data shows top-three capturing 88% of enterprise spend. These are *different* concentration metrics (provider-model HHI across OpenRouter vs. enterprise API dollar share). The tension is methodological, not substantive. Flag in essay.

## Data access

- **OpenRouter API (live):** https://openrouter.ai/ — no API key needed for public price data via `/api/v1/models`, cross-section cheap to replicate at any future date.
- **Epoch AI Notable Models:** https://epochai.org/data/notable-ai-models (CC BY 4.0).
- **62 milestones + replication code:** per paper, "available in accompanying replication package" — to verify whether this is arXiv ancillary files, a GitHub repo, or a separate archive. ACTION: download v1 PDF and check for ancillary files; if absent, email the author.

## Files in this folder

- `PROVENANCE.md` — this file
- `du_2026_key_figures.json` — machine-readable headline figures
- (Dataset files pending — retrieve replication package in Week 2)
