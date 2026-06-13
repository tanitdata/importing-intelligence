---
type: data-provenance
source: OpenRouter, State of AI 2025 (100T token study)
retrieved: 2026-05-04
---

# OpenRouter — State of AI 2025 (100T Token LLM Usage Study)

## Bibliographic

- **Publisher:** OpenRouter
- **URL:** https://openrouter.ai/state-of-ai
- **Data scope:** Over 100 trillion tokens of real-world LLM inference traffic through the OpenRouter platform, primarily across the most recent year up to publication.
- **Retrieved:** 2026-05-04
- **Access:** Public HTML; downloadable visualizations. No paywall. No underlying per-request microdata publicly released.

## Headline facts relevant to the essay

- OpenRouter supports **300+ active models from 60+ providers** as of 2025.
- **Over 50% of OpenRouter usage originates outside the United States.** This is a critical counter-anchor to the AImultiple 85.5–90.5% US consumer figure. The two measure different things: AImultiple = consumer web traffic to LLM products (ChatGPT, Claude.ai, Gemini); OpenRouter = developer API traffic through a specific aggregator. Essay must distinguish these carefully — both are true simultaneously.
- **Reasoning models (o1 and successors) shifted from a small slice to ~50% of total tokens across 2025**, starting from o1 release 2024-12-05.
- **Usage category mix:** creative roleplay and coding assistance dominate; productivity is not as outsized as commonly assumed.
- **Cinderella "Glass Slipper" effect:** early-cohort users show much longer retention than later cohorts — foundational cohorts matter.
- **Rise of agentic inference** — tokens consumed by agent frameworks are a growing share.

## Why this matters for the essay

- **Geographic-share tension:** the 85.5–90.5% US consumer figure (AImultiple) and the <50% US developer-API figure (OpenRouter) are both used in the sovereignty conversation, often interchangeably. The essay's flow analysis must get this right — consumer flow and developer flow are different flows with different chokepoints.
- **Aggregator layer:** OpenRouter itself is a chokepoint — a single hosted routing layer that sits between developers and 60+ providers. Worth a paragraph in Section 5.
- **Reasoning premium:** consistent with Du's 31.5× reasoning premium and partially explains persistence of flagship-tier pricing.

## Caveats

- OpenRouter is one aggregator among several (Together AI, Replicate, Fireworks, Groq, direct API calls bypass aggregators entirely). Its user base skews toward developers experimenting with multi-model workflows, which may inflate multi-homing and open-source metrics relative to enterprise production.
- "Over 50% outside US" is a weak claim without country-level breakdown. Worth emailing OpenRouter for more granular geography.
- Non-peer-reviewed; industry publication, not academic.

## Files in this folder

- `PROVENANCE.md` — this file
- `openrouter_state_of_ai_2025_facts.json` — machine-readable summary
