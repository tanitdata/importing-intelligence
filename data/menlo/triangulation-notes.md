# R4 — Independent Triangulation of the Menlo EOY-2025 Enterprise LLM Concentration Estimate

**Task:** Audit triangulation for the brief's headline claim — 88% of enterprise LLM API dollar spend to Anthropic (40%) / OpenAI (27%) / Google (21%) at end-2025, per Menlo Ventures EOY-2025 survey (N=495, U.S.-only, vendor-adjacent: Menlo is an Anthropic investor).

**Date of research:** 2026-06-12. All figures below were retrieved on 2026-06-12 from the URLs listed, via direct fetch (WebFetch) or full-content web search retrieval (Exa). All figures are paraphrased. Anything not directly retrievable today is marked UNVERIFIED.

---

## 1. Summary verdict

**No independent source replicates Menlo's exact metric (share of enterprise LLM API dollar spend by model provider). The 40/27/21 split therefore remains a single-source point estimate.** However, the triangulation is not empty — it produces three findings:

1. **One independent survey-based spend-share estimate exists, and it disagrees with Menlo on shares while agreeing on concentration.** a16z's third annual Global 2000 CIO survey (published 2026-01-30, N=100) reports OpenAI at ~56% of enterprise model *wallet share*, with Anthropic and Google gaining; respondents project ~53% OpenAI / ~18% Anthropic / ~18% Google for 2026 — a combined top-3 of ~89–92%. This **confirms high top-3 concentration (~90%)** but **inverts Menlo's within-top-3 ordering** (OpenAI majority vs. Menlo's Anthropic lead). Note the symmetry: Menlo is an Anthropic investor and finds Anthropic first; a16z is an OpenAI investor (disclosed) and finds OpenAI first. Sample frames also differ: a16z surveys only Global 2000-scale enterprises ($500M+ revenue, 88% over $1B); Menlo's N=495 spans a broader U.S. enterprise definition.

2. **Independent spend panels (Ramp, Brex) and revenue disclosures are consistent with (a) extreme top-2/top-3 concentration and (b) Anthropic ≥ OpenAI in enterprise/business *API and model* spend specifically by late 2025–spring 2026.** Ramp's 70K-business card/bill-pay panel shows Anthropic passing OpenAI in paid business adoption in April 2026 (34.4% vs. 32.3%), with all other model providers marginal (Google ~4.7%, xAI <2% as of Feb 2026). Revenue arithmetic points the same way: Anthropic's ~$9B end-2025 run-rate was ~80% business-driven (i.e., roughly $7B annualized enterprise/API), against OpenAI's consumer-dominated $13.1B full-year 2025 with API revenue estimated by financial press in the $1.6–3B range. On the *API-dollar* axis Menlo measures, Anthropic > OpenAI at EOY-2025 is the ordering the independent evidence supports — if anything more lopsided than 40:27.

3. **The Google 21% share is the least verifiable leg.** Alphabet disclosed Q1-2026 Google Cloud revenue of $20.0B with gen-AI-product revenue up ~800% YoY and 16B tokens/minute of direct first-party-model API use, but publishes no Gemini-API dollar breakout. No independent source decomposes Google's enterprise LLM API revenue. **UNVERIFIED as a share.**

**Bottom line for the brief:** the 88% top-3 concentration figure is directionally corroborated by one independent survey (~90% top-3) and by panel data showing a two-to-three-vendor market; the specific 40/27/21 split is *not* independently confirmed, and the only comparable independent estimate (a16z wallet share) reverses the Anthropic/OpenAI ordering for the largest enterprises. The metric difference matters: Menlo measures API dollars (where Anthropic's revenue mix concentrates); a16z measures total model wallet share among Global 2000 firms (where OpenAI's enterprise-seat products weigh more).

---

## 2. Per-source findings

### 2.1 Ramp AI Index / Ramp Economics Lab (business spend panel)

- **What it measures:** Paid adoption rate — share of U.S. businesses on Ramp with a positive transaction for a given AI vendor in a month, from corporate-card and bill-pay data. From the June 2026 revision it also tracks intensity (spend per employee; subscriptions vs. coding agents vs. tokens/APIs), but **publishes no vendor-level dollar-share split**. Adoption % ≠ spend share.
- **Panel:** Originally 50,000+ (now "more than 70K") U.S. businesses; $100B+ annual spend tracked. U.S.-only, skews SMB/mid-market/startup (Ramp's customer base), so not representative of Global 2000 procurement.
- **Figures (access 2026-06-12):**
  - June 2026 update (data ~May 2026, methodology revised "to better capture enterprise spend on OpenAI and Anthropic"): Anthropic 41.0% of businesses (+2.5pp), OpenAI 39.5% (−0.1pp). URL: https://ramp.com/leading-indicators/ai-index-june-2026 (published 2026-06-09).
  - May 13, 2026 release (April data): first-ever crossover — Anthropic 34.4% (+3.8pp), OpenAI 32.3% (−2.9pp); overall AI adoption 50.6%. Over the prior year Anthropic quadrupled adoption while OpenAI grew 0.3pp. URL: https://ramp.com/leading-indicators/ai-index-may-2026.
  - March 2026 release (Feb data): overall adoption 47.6%; Anthropic 24.4%; Google 4.7%; xAI <2%; OpenAI fell 1.5pp (largest single-month decline recorded for any model company on the panel). Anthropic won ~70% of head-to-head first-purchase matchups vs. OpenAI. URL: https://ramp.com/leading-indicators/ai-index-march-2026 (retrieved via search-result content, 2026-06-12).
  - February 2026 release (Jan data): Anthropic 19.5%, OpenAI 35.9%, Google 4.5%. ~79% of Anthropic's business customers also pay for OpenAI; 16% of all businesses pay for both (vs. 8% a year earlier); churn ~4%/month for both. URL: https://ramp.com/leading-indicators/ai-index-february-2026 (retrieved via search-result content, 2026-06-12).
  - Spring 2026 Business Spending Report: Anthropic's share of *paid AI customers* jumped 16.7% → 30.6% in a quarter; OpenAI 36.8% → 35.2%. URL: https://ramp.com/reports/2026-spring-spending-benchmarks (retrieved via search-result content, 2026-06-12).
  - Index methodology page: https://ramp.com/data/ai-index (direct fetch returned truncated content on 2026-06-12; panel description retrieved via search-result content same day).
- **Consistency vs. Menlo:** Consistent with (a) top-2/3 dominance — Google's paid-adoption footprint on card/bill-pay rails is tiny (~4.7%), and everything outside the top three is marginal; and with (b) Anthropic ≥ OpenAI — but only from April 2026 onward, i.e., *after* Menlo's EOY-2025 reference period, and on an adoption-count metric, not dollars. Caveat: Google enterprise AI spend frequently rides Workspace/GCP invoices rather than card spend, so Ramp likely understates Google — which also cautions against reading Ramp as confirming Google's 21%.

### 2.2 Brex Benchmark (business spend panel)

- **What it measures:** Top software/AI vendors by dollar spend on Brex card + bill pay; rankings and relative magnitudes, no published share percentages. Startups = <250 employees; enterprises = 250+.
- **Panel:** 30,000–35,000+ Brex customers, billions in monthly spend. U.S.-centric, startup-heavy.
- **Figures (access 2026-06-12):**
  - May 2025: Anthropic led startup AI spend at >2x OpenAI; OpenAI outpaced Anthropic ~4x in enterprise (250+ employees). URL: https://www.brex.com/journal/brex-benchmark-may-2025 (retrieved via search-result content).
  - September 2025: Anthropic, OpenAI, Cursor together captured "the lion's share" of startup AI spend; enterprise Anthropic spend +25% MoM; Anthropic's penetration relative to OpenAI up ~1.5x since Jan 2025. URL: https://www.brex.com/journal/brex-benchmark-september-2025 (direct fetch).
  - October 2025: OpenAI spend on Brex +80% Jan–Oct 2025; enterprise OpenAI spend +20% MoM; enterprises "consolidating around a few core AI vendors like OpenAI and Anthropic." URL: https://www.brex.com/journal/brex-benchmark-october-2025 (retrieved via search-result content).
- **Consistency vs. Menlo:** Consistent with (a) — model-provider spend concentrates in OpenAI + Anthropic with a thin tail. Mixed on (b): within calendar 2025 the ordering was segment-dependent (Anthropic dominant among startups, OpenAI dominant among 250+-employee firms on this panel), with Anthropic converging fast. Does not contradict Menlo's dollar-weighted 40/27 (which is usage-dollar-weighted across a broader enterprise sample), but does not independently confirm it either.
- **Mercury:** No equivalent published AI-vendor spend benchmark found in searches on 2026-06-12. Absence documented.

### 2.3 Revenue disclosures and press-reported company figures

**Anthropic** (company disclosures + press-reported company figures):
- Run-rate trajectory: ~$1B (Jan 2025) → ~$7B (Oct 2025) → ~$9B at end-2025 (some accounts say $8–10B) → $14B (Feb 2026, Series G announcement) → $19B (Mar 2026, Bloomberg-reported) → $30B (Apr 2026, company disclosure of 2026-04-07). Sources: Reuters via TradingView, https://www.tradingview.com/news/reuters.com,2025:newsml_L2N3VW0U5:0-inside-anthropic-s-ambitious-2026-revenue-goal/ (direct fetch, 2026-06-12; original Reuters reporting Oct 2025); The Deep Dive, https://thedeepdive.ca/anthropic-revenue-run-rate-surpasses-30-billion-as-enterprise-demand-accelerates/ (direct fetch, 2026-06-12); VentureBeat, https://venturebeat.com/technology/anthropic-says-it-hit-a-30-billion-revenue-run-rate-after-crazy-80x-growth (direct fetch returned HTTP 429; figures retrieved via search-result content, 2026-06-12).
- Mix: businesses contributed ~80% of revenue; 300,000+ companies on the API (Reuters, Oct 2025). Third-party trackers (Sacra, reported secondhand) put the mix around 70–75% API — treat as estimate, not disclosure. 1,000+ customers spending $1M+/yr by April 2026 (company); Claude Code >$2.5B annualized.
- Dispute flag: press reports that OpenAI internally argues Anthropic's $30B figure is overstated by ~$8B on gross-vs-net accounting for AWS/Google Cloud distribution (press-reported, unresolved; would also apply proportionally to earlier figures). Treat all Anthropic run-rates as company-asserted, non-GAAP.

**OpenAI** (company statement + press-reported company figures):
- ~$2B/month (~$24B annualized) as of end-March 2026, per company statement reported 2026-04-01; enterprises ≈ 40% of total revenue; 900M weekly ChatGPT users, 50M paying subscribers; API throughput >15B tokens/minute. URL: https://finance.yahoo.com/sectors/technology/articles/openai-says-making-2-billion-132500739.html (direct fetch, 2026-06-12).
- Full-year 2025 revenue ≈ $13.1B; ~$25B annualized by Feb 2026 (press-reported company figures; secondary sources vary). URLs: https://www.humai.blog/openai-makes-25-billion-a-year-and-is-preparing-for-an-ipo-here-is-what-the-numbers-actually-mean/ and https://uk.investing.com/analysis/openais-real-ipo-risk-is-financial-transparency-200624570 (retrieved via search-result content, 2026-06-12).
- Consumer/API split: no audited disclosure. Financial-press estimates of 2025 API revenue range $1.6B (Meridian48, citing The Information/Bloomberg reporting: https://meridian48.com/business/how-openai-makes-money-2026-revenue-breakdown) to ~$3B (valueaddvc.com: https://valueaddvc.com/blog/openai-revenue-2026-20b-arr-4b-month-path-to-profitability) — both retrieved via search-result content 2026-06-12; both are estimate blogs synthesizing press reporting, so treat as a range, not a figure. Consumer subscriptions ≈ 60–70% of mix across all estimates.

**Google** (SEC filing + earnings call):
- Q1 2026: Google Cloud revenue $20.0B (+63% YoY); enterprise AI solutions the largest growth contributor; gen-AI-product revenue +~800% YoY (no dollar level disclosed); first-party models processing >16B tokens/minute via direct customer API use (up from 10B prior quarter); backlog $462B. URLs: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000043/googexhibit991q12026.htm and https://s206.q4cdn.com/479360582/files/doc_events/2026/Apr/29/2026_Q1_Earnings_Transcript.pdf (retrieved via search-result content, 2026-06-12; filed/published 2026-04-29).
- **No Gemini API revenue dollar figure exists publicly.** Google's enterprise LLM API revenue cannot be isolated from GCP infrastructure, Workspace, and Vertex bundling. UNVERIFIED as a share input.

**What the revenue arithmetic implies for Menlo's ordering (computed, not sourced):**
- At Menlo's EOY-2025 reference point: Anthropic ~$9B run-rate × ~75–80% business/API ≈ **$6.5–7B annualized enterprise/API**. OpenAI full-year-2025 API revenue ≈ **$1.6–3B** (press-estimate range); even using OpenAI's late-2025 ~$21B run-rate × ~25% API ≈ $5B as a generous upper bound, Anthropic's enterprise-API dollars plausibly exceeded OpenAI's at EOY-2025.
- **Relative ordering: consistent with Menlo's Anthropic (40%) > OpenAI (27%).** If anything, the raw revenue ratio (roughly 2:1 or wider on central estimates) is more extreme than Menlo's 40:27 ≈ 1.5:1 — plausibly because Menlo's survey frame includes enterprise spend routed through ChatGPT Enterprise/business seats and excludes some of Anthropic's non-survey-visible revenue. Caution: this is an order-of-magnitude consistency check on non-GAAP, partly disputed figures — not an independent estimate of shares. Total revenue ≠ enterprise API revenue on both sides, and the Anthropic gross-vs-net dispute could move its figure materially.

### 2.4 Cloud marketplace / procurement signals

- **Canalys (now Omdia), "Now and next for hyperscaler marketplaces":** third-party marketplace sales $16B (2023), forecast >$45B (2025), $85B (2028); private offers >70% of AWS Marketplace sales. **No AI-model-provider spend breakout published.** URLs: https://omdia.tech.informa.com/insights/2025/now-and-next-for-hyperscaler-marketplaces and the report PDF (retrieved via search-result content, 2026-06-12).
- **Tackle, State of Cloud GTM 2025:** cloud committed spend >$460B (2025, citing Canalys); marketplace mechanics only — **no model-provider split**. URL: https://tackle.io/wp-content/uploads/2025/11/SOCGTM-Report-2025.pdf (retrieved via search-result content, 2026-06-12).
- **U.S. government procurement (GSA OneGov, Aug 2025):** ChatGPT Enterprise at $1/agency (2025-08-06), Claude for Enterprise/Government at $1 across all three branches (2025-08-12), Gemini for Government at $0.47/agency (2025-08-21). Because pricing is nominal and API access is largely excluded from these agreements (per Federal News Network reporting, https://federalnewsnetwork.com/contractsawards/2025/08/gsas-1-awards-for-ai-tools-come-under-protest/), **federal procurement records carry no usable spend-share signal** — only an adoption-breadth signal that the same three vendors constitute the government-recognized market. URLs: https://www.gsa.gov/about-gsa/newsroom/news-releases/gsa-announces-new-partnership-with-openai-delivering-deep-discount-to-chatgpt-08062025 ; https://www.gsa.gov/about-gsa/newsroom/news-releases/gsa-strikes-onegov-deal-with-anthropic-08122025 ; https://www.gsa.gov/about-gsa/newsroom/news-releases/gsa-google-announce-gemini-onegov-agreement-08212025 (all retrieved via search-result content, 2026-06-12).
- **Verdict for this family: documented absence.** No published marketplace or procurement dataset breaks out enterprise LLM API spend by model provider.

### 2.5 Independent enterprise surveys, 2025–2026

**a16z third annual Enterprise CIO survey (the key independent comparator):**
- **What it measures:** Self-reported model usage and *wallet share of AI model spend* among very large enterprises.
- **Sample/period:** N=100 VP/C-level at Global 2000 firms ($500M+ revenue; 88% >$1B; >50% with 10,000+ employees); published 2026-01-30; fielding window not stated in the public post (references changes "since May 2025," implying late-2025 fielding — overlapping Menlo's EOY-2025 window).
- **Figures (direct fetch, 2026-06-12):** OpenAI in production at 78% of enterprises; Anthropic 44% in production (63%+ incl. testing), the largest share gain of any lab since May 2025. **Wallet share: OpenAI ~56% of model spend, majority but declining; respondents project 2026 at ~53% OpenAI / ~18% Anthropic / ~18% Google** (projection figures via The Decoder's report of the same survey, https://the-decoder.com/openai-still-leads-enterprise-ai-but-anthropic-is-gaining-fast-according-to-new-study/, and eMarketer, https://www.emarketer.com/content/openai-leads--anthropic-surges-enterprise-ai-shifts-multi-model-reality, both retrieved 2026-06-12). Average enterprise LLM spend: ~$4.5M (2024) → ~$7M (2025) → ~$11.6M expected (2026). 81% of enterprises use 3+ model families. The post also cites Yipit panel data (~1,000 mid-market/enterprise companies) showing OpenAI ~85% and Anthropic ~55% *adoption*. **Disclosure: a16z states it is an investor in OpenAI.** URL: https://a16z.com/leaders-gainers-and-unexpected-winners-in-the-enterprise-ai-arms-race/.
- **Consistency vs. Menlo:** Top-3 combined ≈ 89–92% — **strongly consistent with Menlo's 88% concentration claim**. Within-top-3 shares — **inconsistent**: OpenAI majority (~56%) vs. Menlo's OpenAI 27%/Anthropic 40%. Reconciliation candidates: (i) metric — a16z's wallet share covers *all* model spend including enterprise ChatGPT-type contracts, Menlo isolates API dollars; (ii) sample — Global 2000 incumbment-heavy vs. Menlo's broader 495-firm U.S. panel; (iii) opposite vendor adjacency. Neither estimate can adjudicate the other; together they bracket the plausible range.

**Wharton–GBK "Accountable Acceleration" 2025 AI Adoption Report:**
- N≈800 senior U.S. leaders (1,000+ employees, $50M+ revenue), fielded 2025-06-26 → 2025-07-11. Measures usage frequency, budgets, ROI — **no model-provider spend-share question reported**. Useful only as corroboration that enterprise gen-AI budgets are large and growing (two-thirds budgeting $5M+; 88% expect increases). URLs: https://ai.wharton.upenn.edu/wp-content/uploads/2025/10/2025-Wharton-GBK-AI-Adoption-Report_Full-Report.pdf and https://knowledge.wharton.upenn.edu/special-report/2025-ai-adoption-report/ (retrieved via search-result content, 2026-06-12). **Documented absence of a provider-share estimate.**

**YipitData (ERP-derived B2B spend panel, 1,300+ mid-market/enterprise companies, ~250K vendors):**
- Publishes adoption and growth analyses (e.g., mid-market AI early adopters grew core-AI spend >300% YoY to Dec 2025) and the adoption rates cited in the a16z post (OpenAI ~85%, Anthropic ~55%), but **no public model-provider dollar-share estimate**. URL: https://www.yipitdata.com/resources/blog/is-ai-replacing-saas (retrieved via search-result content, 2026-06-12). Proprietary data could in principle answer the question; the public record does not.

**ETR / Morgan Stanley CIO surveys; Bain/BCG/McKinsey adoption reports:** No 2025–2026 public report found on 2026-06-12 that quantifies model-provider *spend share* among enterprises (BCG's sovereignty piece and consultancy adoption studies measure adoption/maturity, not vendor dollars). UNVERIFIED whether paywalled ETR data contains such a breakout; the public record does not. **Documented absence.**

---

## 3. Convergence test (assembled)

| Independent signal | Metric | (a) High top-3 concentration? | (b) Anthropic ≥ OpenAI in enterprise API? |
|---|---|---|---|
| a16z CIO survey (Jan 2026) | Wallet share, model spend, Global 2000 | **Yes** (~89–92% top-3) | **No** (OpenAI ~56% majority) |
| Ramp AI Index (Feb–Jun 2026) | Paid adoption %, 70K US businesses | Yes (top-2 dominant; Google ~5%, xAI <2%, thin tail) | **Yes, from April 2026** (34.4 vs 32.3; 41.0 vs 39.5 in May data) — adoption, not dollars |
| Brex Benchmark (2025) | Dollar-spend rankings, 30–35K customers | Yes (OpenAI+Anthropic+Cursor dominate AI spend) | Mixed in 2025: yes for startups (>2x), no for 250+-employee firms (OpenAI 4x), gap closing fast |
| Revenue disclosures + press (EOY 2025) | Company run-rates and mix | Yes (three firms' disclosed/reported revenue dwarfs all other model providers) | **Yes** on API dollars: Anthropic ~$6.5–7B enterprise/API annualized vs. OpenAI API ~$1.6–3B (press-estimate range) |
| Google disclosures (Q1 2026) | Cloud segment revenue, token throughput | Uninformative on shares | Uninformative; Gemini API dollars UNVERIFIED |
| Marketplace data (Canalys/Tackle) | Marketplace GMV | No provider breakout — absence | No provider breakout — absence |
| Federal procurement (GSA OneGov) | Contract awards | Same three vendors only — weak qualitative support | No spend signal ($1 nominal pricing; API excluded) |

**Reading:** Concentration (a) is corroborated from every angle that can speak to it. The Anthropic-first ordering (b) is supported on the API-dollar axis (revenue arithmetic) and on paid business adoption from spring 2026, but contradicted on total-model-wallet share among the largest enterprises (a16z). The two surveys plausibly measure genuinely different things, and each carries opposite-signed vendor adjacency.

---

## 4. What this licenses the brief to say (draft for Section 3.1)

> No independent source replicates Menlo's metric — share of enterprise LLM API spend in dollars — so the 40/27/21 split should be read as the only published point estimate of that quantity, not a consensus figure. The concentration claim itself, however, triangulates well: a16z's January 2026 Global 2000 CIO survey independently puts roughly ninety percent of enterprise model spend with the same three providers, and corporate-card spend panels from Ramp and Brex show paid business adoption and AI dollar spend collapsing onto OpenAI and Anthropic with a thin tail. The within-top-three ordering is the contested part: a16z's large-enterprise sample still gives OpenAI a ~56% wallet-share majority, while company revenue disclosures (Anthropic's ~$9B end-2025 run-rate, roughly 80% business-driven, against OpenAI's consumer-heavy $13.1B 2025 revenue with API revenue press-estimated at $1.6–3B) and Ramp's spring-2026 adoption crossover support Menlo's finding that Anthropic leads specifically in enterprise API dollars. It is worth stating plainly that the two available survey estimates are vendor-adjacent in opposite directions — Menlo is an Anthropic investor, a16z an OpenAI investor — and each finds its portfolio company ahead; the honest summary is high and rising top-three concentration (~88–92%), with the Anthropic-versus-OpenAI ordering dependent on whether one measures API dollars or total enterprise model wallet share.

---

## 5. Limitations

1. **Metric incommensurability.** Adoption rate (Ramp, Brex penetration, Yipit), wallet share of all model spend (a16z), and API dollar share (Menlo) are three different quantities. None of the independent sources isolates Menlo's exact object (enterprise LLM **API** dollars), so "consistency" judgments here are directional, not quantitative.
2. **Period drift.** Menlo's reference point is EOY 2025. The strongest independent panel signals (Ramp's Anthropic-passes-OpenAI crossover) date from April–May 2026 and cannot retroactively confirm the EOY-2025 split; in Jan–Feb 2026 Ramp still showed OpenAI well ahead on adoption (35.9% vs 19.5%).
3. **Non-GAAP, partly disputed revenue figures.** All Anthropic and OpenAI revenue numbers are annualized run-rates from company statements or financial press, not audited revenue. The press-reported OpenAI challenge to Anthropic's gross-vs-net accounting (~$8B of the April-2026 $30B) could compress the Anthropic-over-OpenAI API-dollar gap if it applies proportionally to the EOY-2025 figure. OpenAI's consumer/API split is an estimate range, not a disclosure.
4. **Panel composition biases.** Ramp and Brex panels skew U.S. SMB/startup/mid-market and undercount spend routed through hyperscaler invoices and enterprise agreements — likely understating Google (Workspace/GCP bundling) and large-enterprise OpenAI contracts. a16z's panel is the opposite skew (Global 2000 only) and a16z is an OpenAI investor; Yipit's figures reach the public record mainly through a16z's post.
5. **Google is the weakest leg.** No source — company, panel, or survey — yields an independent dollar figure for Gemini enterprise API revenue; Menlo's 21% for Google is the least triangulable of the three shares. UNVERIFIED.
6. **Retrieval caveat.** Figures marked "retrieved via search-result content" came through the Exa search tool's full-text extraction on 2026-06-12 rather than a direct page fetch (two direct fetches failed: ramp.com/data/ai-index returned truncated content; the VentureBeat article rate-limited with HTTP 429). Content was still retrieved today; flagged for audit completeness.
