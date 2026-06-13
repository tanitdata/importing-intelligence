---
type: data-provenance
source: Menlo Ventures
retrieved: 2026-05-04
captured_by: research-engineering workflow
---

# Menlo Ventures — enterprise LLM market share

Two reports in scope. The figures differ because definitions and survey waves differ. Both should be cited where used.

## Report A — 2025 Mid-Year LLM Market Update

- **Publisher:** Menlo Ventures
- **Published:** 2025-07-31
- **Canonical URL:** https://menlovc.com/2025-mid-year-llm-market-update/
- **Press release (figures):** https://www.globenewswire.com/news-release/2025/07/31/3125037/0/en/Enterprise-LLM-Spend-Reaches-8-4B-as-Anthropic-Overtakes-OpenAI-According-to-New-Menlo-Ventures-Report-on-LLM-Market.html
- **Survey base:** 150 technical leaders across AI startups and large enterprises.
- **Definition:** "proportion of production AI usage" (share of API calls/usage, NOT dollars). Responses weighted by each enterprise and startup application's scale.
- **Headline figures:**
  - Anthropic: 32%
  - OpenAI: 25% (down from 50% in 2023)
  - Google: 20% (up from 7% in 2023)
  - Meta (Llama): 9%
  - DeepSeek: 1%
  - Enterprise LLM spend: $8.4B (up from $3.5B in Nov 2024, i.e. doubled in ~6 months).
  - Inference has overtaken training as primary compute workload.
- **Methodology caveat:** self-reported production API usage share; weighted by scale but survey-dependent; no public underlying microdata.

## Report B — 2025: The State of Generative AI in the Enterprise

- **Publisher:** Menlo Ventures
- **Published:** 2025-12-09
- **Canonical URL:** https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/
- **PDF URL:** https://menlovc.com/wp-content/uploads/2025/12/menlo_ventures_enterprise_ai_report-2025.pdf
- **Definition shift:** market share reframed as "estimated dollars spent based on proportion of production API usage"; now triangulated with publicly reported financials. This is a *different* metric than Report A.
- **Headline figures:**
  - Anthropic: 40% (up from 24% in 2024 and 12% in 2023)
  - OpenAI: 27% (down from 50% in 2023)
  - Google: 21% (up from 7% in 2023)
  - Top three combined: 88% of enterprise LLM API usage.
  - Remaining 12% spread across Meta (Llama), Cohere, Mistral, long tail.
  - Coding vertical: Anthropic 54% (up from 42% six months prior), OpenAI 21%. Attributed substantially to Claude Code adoption.
  - 10 products generating >$1B ARR; 50 products generating >$100M ARR.

## How to cite in the essay

- For **mid-2025 snapshot and usage-share framing:** Report A.
- For **end-of-2025 snapshot, dollar-spend framing, and concentration claim (88% top-three):** Report B.
- Do not mix the two headline percentages in a single sentence — the definitions are different (usage vs. dollars).
- When making the concentration argument (central to the essay's LLM regime section), Report B is the stronger anchor because it is dollar-weighted and more recent.

## Known limitations

- Both reports are vendor-adjacent (Menlo Ventures is an LLM investor, holds positions in Anthropic). Disclose this caveat in the essay when citing.
- Sample is self-selected technical leaders responding to a survey; generalizability to non-US enterprises is unclear.
- "Enterprise API usage" excludes consumer traffic, on-premise deployments, and non-API integration paths. The figures describe a specific slice of the market.

## Files in this folder

- `PROVENANCE.md` — this file
- `menlo_2025_midyear.json` — key figures from Report A, machine-readable
- `menlo_2025_eoy.json` — key figures from Report B, machine-readable
- (PDF of Report B to be captured into refs/ on next pass; license terms to verify before any redistribution)
