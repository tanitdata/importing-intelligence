---
type: note
created: 2026-06-12
tags: [inference-share, evidence-replacement, R6, capacity-constraints, datacenter-energy, aws-90-percent]
links: [data/menlo/PROVENANCE.md]
---

# R6 — Replacement evidence: "inference, not training, is where the volume sits"

Task: replace the dated AWS 2021–2022 "up to 90% of ML compute cost is inference" anchor with current (2025–2026) LLM-specific evidence. Three legs assembled below. All URLs accessed **2026-06-12** unless noted. All figures paraphrased from sources; short quoted phrases are reproduced only where the exact framing is load-bearing (executive statements).

Verified constraint carried over from Phase 0: Menlo's mid-year 2025 report does NOT state a dollar crossover; it reports a spend shift toward inference plus workload-majority survey statistics (74% of startup builders majority-inference, up from 48%; 49% of large enterprises most/nearly-all-inference, up from 29%). Author-approved wording for that leg already exists; cite as **Menlo 2025b**. This file supplies the other two legs plus the AWS footnote.

---

## Leg 1 — Provider capacity and rate-limit disclosures as evidence of inference-demand pressure (2025–2026)

These are official statements (earnings-call transcripts, company announcements) showing that serving capacity — not training capacity — has been the binding constraint providers publicly manage. Note the scope caveat at the end of this section.

### OpenAI (model provider — serving-specific)

1. **"Out of GPUs" — GPT-4.5 staggered rollout.** Altman stated on X (2025-02-27) that OpenAI had to stagger the GPT-4.5 rollout because the company was out of GPUs, promising to add tens of thousands of GPUs the following week before extending access to the Plus tier; he attributed the shortage to growth surges that are hard to predict. This is a serving/availability constraint, not a training one.
   - Source: TechCrunch, "OpenAI CEO Sam Altman says the company is 'out of GPUs'," 2025-02-27. https://techcrunch.com/2025/02/27/openai-ceo-sam-altman-says-the-company-is-out-of-gpus/ (accessed 2026-06-12)
2. **"Our GPUs are melting" — emergency rate limits on image generation.** Altman announced (2025-03-27/28) temporary rate limits on ChatGPT image generation because demand was overwhelming serving infrastructure; free-tier generation was capped at three per day.
   - Source: Fortune, 2025-03-28. https://fortune.com/2025/03/28/sam-altman-chatgpt-gpus-melting-ai-images/ (accessed 2026-06-12)
3. **Capacity issues causing deferred product rollouts.** Altman warned (2025-03-31, reported 2025-04-01) that users should expect new OpenAI releases to be delayed, services to break, and responses to slow while the company dealt with capacity challenges; OpenAI delayed the image tool for free users and temporarily disabled Sora video generation for new users to ease load.
   - Source: TechCrunch, "Sam Altman says that OpenAI's capacity issues will cause product delays," 2025-04-01. https://techcrunch.com/2025/04/01/sam-altman-says-that-openais-capacity-issues-will-cause-product-delays/ (accessed 2026-06-12)

### Anthropic (model provider — serving-specific)

4. **Unannounced tightening of Claude Code usage limits.** In mid-July 2025 heavy users (especially $200/month Max subscribers) hit abruptly restrictive limits; Anthropic confirmed degraded service without detailing changes. Claude Code had suffered repeated partial outages in the preceding month.
   - Source: TechCrunch, 2025-07-17. https://techcrunch.com/2025/07/17/anthropic-tightens-usage-limits-for-claude-code-without-telling-users/ (accessed 2026-06-12)
5. **Formal weekly rate limits, citing demand exceeding capacity.** On 2025-07-28 Anthropic announced weekly rate limits (effective 2025-08-28) on Pro and Max plans, on top of existing 5-hour limits. The company's framing: Claude Code had seen "unprecedented demand since launch," and patterns like running Claude continuously 24/7 were "impacting system capacity for all"; weekly limits would help "maintain reliable service" while affecting under 5% of subscribers. Overage purchasable at standard API rates — i.e., the constraint was explicitly priced.
   - Sources: TechCrunch, 2025-07-28, https://techcrunch.com/2025/07/28/anthropic-unveils-new-rate-limits-to-curb-claude-code-power-users/ ; VentureBeat, 2025-07-28, https://venturebeat.com/orchestration/anthropic-throttles-claude-rate-limits-devs-call-foul (both accessed 2026-06-12)

### Microsoft / Azure (hyperscaler — earnings-call language, by quarter)

6. **FY2025 Q2 call (2025-01-29).** CFO Amy Hood: "we expect to be AI capacity constrained in Q3," and "We have been short power and space." She noted Azure AI results beat expectations partly because delivery dates were pulled in by weeks — "When you're capacity constrained, weeks matter."
   - Source: Microsoft FY25 Q2 earnings call transcript, https://www.microsoft.com/en-us/investor/events/fy-2025/earnings-fy-2025-q2 (accessed 2026-06-12). Coverage: CFO Dive, 2025-01-30, https://www.cfodive.com/news/microsoft-azure-cloud-capacity-constraints-openai/739151/
7. **FY2025 Q4 call (2025-07-30).** Hood: even with additional datacenter capacity online, "demand remains higher than supply"; Microsoft expected to "remain capacity constrained through the first half of our fiscal year" (i.e., through December 2025), against a $368B contracted backlog. She noted the supply-demand balance she had expected by June was now hoped for "by December."
   - Source: https://www.microsoft.com/en-us/investor/events/fy-2025/earnings-fy-2025-q4 (accessed 2026-06-12)
8. **FY2026 Q1 call (2025-10-29).** Hood: "demand again exceeded supply across workloads even as we brought more capacity online"; Microsoft now expected to be "capacity constrained through at least the end of our fiscal year" (mid-2026), and acknowledged Azure revenue "could be higher" absent the capacity shortfall.
   - Source: https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q1 (accessed 2026-06-12). Coverage: Benzinga, 2025-10-30, https://www.benzinga.com/markets/tech/25/10/48518415/microsoft-cfo-amy-hood-says-cloud-revenue-figures-could-be-higher-but-azure-is-short-on-capacity-as-ai-demand-soars

### Alphabet / Google Cloud (hyperscaler — earnings-call language, by quarter)

9. **Q1 2025 call (2025-04-24).** CFO Anat Ashkenazi: Google Cloud was in a "tight demand/supply environment" and had exited 2024 "with more customer demand than we had capacity" — a condition that persisted in Q1.
   - Source: Alphabet IR Q1 2025 call, https://www.youtube.com/watch?v=SySgINoaI9A ; coverage: Cloud Wars, 2025-04-28, https://cloudwars.com/cloud/google-cloud-customer-demand-outstrips-data-center-capacity-as-q1-growth-slips-to-28/ (accessed 2026-06-12)
10. **Q2 2025 call (2025-07-23).** Ashkenazi: "We expect to remain in a tight demand-supply environment going into 2026"; capex raised from $75B to ~$85B, primarily to meet cloud customer demand.
    - Source: Motley Fool transcript, https://www.fool.com/earnings/call-transcripts/2025/07/23/alphabet-googl-q2-2025-earnings-call-transcript/ (accessed 2026-06-12)
11. **Q3 2025 call (2025-10-29).** Ashkenazi: "We have more demand than we have supply," with tightness expected through Q4 and 2026; cloud backlog reached $155B (+82% YoY), with demand for both TPU- and GPU-based AI infrastructure cited as a key growth driver.
    - Source: Alphabet IR Q3 2025 call, https://www.youtube.com/watch?v=hA1OEi6TRYU (accessed 2026-06-12)
12. **Q4 2025 call (2026-02-03/04).** CEO Sundar Pichai: "we've been supply-constrained, even as we've been ramping up our capacity," and "I do expect to go through the year in a supply-constrained way" (2026). He identified compute capacity — power, land, supply chain — as the top operational question.
    - Source: Alphabet IR, https://abc.xyz/investor/events/event-details/2026/2025-Q4-Earnings-Call-2026-Dr_C033hS6/default.aspx ; Motley Fool transcript, https://www.fool.com/earnings/call-transcripts/2026/02/04/alphabet-googl-q4-2025-earnings-call-transcript/ (both accessed 2026-06-12)

### Amazon / AWS (hyperscaler)

13. **Q2 2025 call (2025-07-31).** CEO Andy Jassy: "We have more demand than we have capacity right now," with resolution expected to take "several quarters"; he named power as the "single biggest constraint," followed by chips. He also noted customers moving production workloads toward inference care intensely about price-performance.
    - Sources: CRN, https://www.crn.com/news/ai/2025/amazon-q2-2025-earnings-ceo-jassy-dismisses-ai-concerns-microsoft-cloud-growth-rate ; Latitude Media, 2025-08-05, https://www.latitudemedia.com/news/power-is-aws-single-biggest-constraint/ (both accessed 2026-06-12)
14. **Q3 2025 call (2025-10-30).** Jassy: AWS added 3.8 GW of power in 12 months, expects to double total capacity by end-2027, and "as fast as we're adding capacity right now, we're monetizing it."
    - Source: Insider Monkey transcript, https://www.insidermonkey.com/blog/amazon-com-inc-nasdaqamzn-q3-2025-earnings-call-transcript-1638154/ (accessed 2026-06-12)
15. **Q4 2025 call (2026-02-05).** Jassy: "every provider would tell you, including us, that we could actually grow faster if we had all the supply that we could take"; Trainium described as "fully subscribed."
    - Source: The Register, 2026-02-06, https://www.theregister.com/2026/02/06/amazon_earnings_q4_2025/ ; transcript: https://www.earningscall.ai/stock/transcript/AMZN-2025-Q4 (both accessed 2026-06-12)

**Scope caveat for the brief.** The OpenAI and Anthropic episodes are inference/serving-specific by construction (rate limits and staggered rollouts gate model *use*). The hyperscaler "capacity constrained" statements cover AI workloads in aggregate (training + inference + first-party products) and should be framed as evidence of demand-side pressure on AI compute generally, with the rate-limit episodes carrying the inference-specific weight. Microsoft's "demand exceeded supply across workloads" (Oct 2025) and Amazon's customer-shift-to-inference remark partially bridge the gap, but no hyperscaler discloses a training/inference revenue split.

---

## Leg 2 — Institutional datacenter-energy evidence (IEA, LBNL, others)

### IEA, *Energy and AI* (published 2025-04-10)

- Global data centre electricity consumption ~415 TWh in 2024 (~1.5% of global electricity); projected to more than double to ~945 TWh by 2030 (Base Case), with AI the most important growth driver. Accelerated (AI) servers' electricity consumption projected to grow ~30%/year, accounting for almost half of the net increase in data-centre electricity demand.
- The report covers "training and deploying" AI together and does **not** publish a headline training-vs-inference split; it explicitly notes that lack of data on commercial models' energy consumption inhibits assessment.
- URLs: https://www.iea.org/reports/energy-and-ai ; demand chapter: https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai (accessed 2026-06-12)

### IEA, *Key Questions on Energy and AI* (2026 update; published 2026-04-16)

- Data centre electricity demand grew 17% in 2025; **electricity consumption of AI-focused data centres surged ~50% in 2025**. Major model providers reported a threefold increase in active users and a fivefold increase in revenue over the past year — the IEA's own proxy for usage (inference) growth in the absence of comprehensive usage statistics.
- Updated projection: data centre consumption roughly doubles from 485 TWh (2025) to ~950 TWh (2030); AI-focused data centre consumption roughly **triples** in this period to ~465 TWh by 2030.
- The report defines inference as "the day-to-day use of deployed AI models" and discusses inference optimisation (batching, caching, speculative decoding, quantisation) as a key efficiency lever, noting industry reporting that cost per token of inference has fallen by orders of magnitude. It also flags new energy-intensive inference-side uses (reasoning, agentic tasks, video generation) as demand drivers. Still no headline percentage split.
- URLs: https://www.iea.org/reports/key-questions-on-energy-and-ai ; PDF: https://iea.blob.core.windows.net/assets/3179f7f8-01f6-4dd6-bffa-c9f7b73f1dc9/KeyQuestionsonEnergyandAI.pdf ; news release: https://www.iea.org/news/data-centre-electricity-use-surged-in-2025-even-with-tightening-bottlenecks-driving-a-scramble-for-solutions (accessed 2026-06-12)

### IEA, data centres & networks tracking page (operational-data split — older underlying data)

- The IEA's tracking page reports that data from Meta and Google indicate the **training phase accounts for ~20–40% of ML-related energy use, inference (use of models) 60–70%, and model development ~10%**. Underlying corporate data is from roughly 2019–2022 (pre-/early-LLM operations) — use with that dating caveat.
- URL: https://www.iea.org/energy-system/buildings/data-centres-and-data-transmission-networks (accessed 2026-06-12)

### LBNL, *2024 United States Data Center Energy Usage Report* (published 2024-12-19/20, LBNL-2001637)

- US data centres consumed ~176 TWh in 2023 (4.4% of US electricity), up from 58–60 TWh in 2014; projected 325–580 TWh by 2028 (6.7–12% of US electricity; 74–132 GW power demand at 50% utilisation). Growth driver: multi-GPU AI servers — AI servers grow from ~1.6M units (2020) to a projected 8–12M of a ~37M total server installed base by 2028.
- The report models AI server load in aggregate and does **not** publish a training/inference split; the author team (Shehabi et al.) lists GPU-server operational practices among key data gaps.
- URLs: report page https://eta-publications.lbl.gov/publications/2024-lbnl-data-center-energy-usage-report ; PDF https://eta-publications.lbl.gov/sites/default/files/2024-12/lbnl-2024-united-states-data-center-energy-usage-report_1.pdf ; DOE release (2024-12-20) https://www.energy.gov/articles/doe-releases-new-report-evaluating-increase-electricity-demand-data-centers (accessed 2026-06-12). No 2025–2026 LBNL update located as of access date (the 2024 report remains the current congressionally mandated edition) — UNVERIFIED whether an update is in preparation.

### Analyst / research-lab estimates of the inference share (label as such)

- **Epoch AI** (research org; "How much power will frontier AI training demand in 2030?", 2025-08-11): currently AI power demand is "split roughly equally between training, experiments, and inference" — i.e., inference ≈ one-third of AI *power capacity*, with the future split explicitly uncertain. https://epoch.ai/publications/power-demands-of-frontier-ai-training (accessed 2026-06-12)
- **Epoch AI** ("Is a compute crunch coming?", late 2025/2026): global inference capacity is more than tripling each year (compute capacity ~3.4x/year), with a possible inference "compute crunch" for long-context agentic workloads. https://epoch.ai/gradient-updates/is-a-compute-crunch-coming (accessed 2026-06-12)
- **Google** (production measurement, 2025-08-21): first published full-stack measurement of production *inference* — median Gemini Apps text prompt 0.24 Wh, with a 33x per-prompt energy reduction May 2024→May 2025. Demonstrates both that serving is the measured continuous flow and that per-unit efficiency gains coexist with aggregate demand growth. Paper: https://arxiv.org/pdf/2508.15734 ; blog: https://cloud.google.com/blog/products/infrastructure/measuring-the-environmental-impact-of-ai-inference/ (accessed 2026-06-12)
- **EPRI** (*Scaling Intelligence* review): cites Meta operational data (Wu et al.) showing an experiments/training/inference power split of roughly 10:20:70 — inference over 3x training — while noting this predates Meta's largest LLM training pushes; also cites Erdil (2024) arguing theoretically for roughly balanced training/inference compute allocation. https://restservice.epri.com/publicattachment/94532 (accessed 2026-06-12)
- **SemiAnalysis** (analyst; March 2024, pre-window but directionally cited widely): inference "is eventually a larger workload than training" and can be geographically distributed. https://newsletter.semianalysis.com/p/ai-datacenter-energy-dilemma-race (accessed 2026-06-12)

**What the credible range looks like (as of June 2026):** institutional and analyst estimates of inference's share of AI compute/energy span roughly **one-third (Epoch AI, power-capacity basis, 2025) to 60–70% (Meta/Google operational energy data as reported by the IEA; older corporate data)**, with the pre-LLM AWS cost claim (80–90%, infrastructure-cost basis) at the high end. No authority publishes a current LLM-specific split; what is well-evidenced for 2025–2026 is the *direction and pressure*: AI-focused datacenter electricity grew ~50% in 2025 (IEA), model-provider usage roughly tripled (IEA), inference capacity is tripling annually (Epoch), and providers rationed serving throughout 2025–2026 (Leg 1).

---

## Leg 3 — The AWS original (for the historical footnote)

The "up to 90%" claim originates with the **December 2019 launch of AWS Inferentia-based EC2 Inf1 instances at re:Invent 2019**, not with the 2021–2022 Architecture Blog material the brief currently cites (those were later repetitions). Documented instances:

1. **AWS News Blog (Jeff Barr), 2019-12-03** — "Amazon EC2 Update – Inf1 Instances with AWS Inferentia Chips...": customers report that inference "can account for up to 90% of the cost of their machine learning work." (Customer-attributed, cost basis.) https://aws.amazon.com/blogs/aws/amazon-ec2-update-inf1-instances-with-aws-inferentia-chips-for-high-performance-cost-effective-inferencing/ (accessed 2026-06-12)
2. **Amazon press release, 2019-12-03** — "AWS Announces Nine New Compute and Networking Innovations for Amazon EC2": inference accounts for the majority of the cost of production ML — "for every dollar spent on training, up to nine are spent on inference." https://press.aboutamazon.com/2019/12/aws-announces-nine-new-compute-and-networking-innovations-for-amazon-ec2 (accessed 2026-06-12)
3. **Andy Jassy, re:Invent 2019 keynote (2019-12-03)** — for ML at scale in production, 80–90% of compute cost is inference; his worked example was Alexa (model retrained roughly twice a week vs. inference on every request from every device). Keynote video: https://www.youtube.com/watch?v=7-31KgImGgU ; contemporaneous coverage: EE Times, 2019-12-13, https://www.eetimes.com/aws-rolls-out-ai-inference-chip/ ; CRN, https://www.crn.com/news/cloud/aws-launches-new-ec2-arm-based-machine-learning-inference-instances (accessed 2026-06-12)
4. **Subsequent AWS repetitions (2020–present):** AWS ML Blog, 2020-08-13 ("In many cases, up to 90% of the infrastructure spent on developing and running an ML application is on inference"), https://aws.amazon.com/blogs/machine-learning/amazon-ec2-inf1-instances-featuring-aws-inferentia-chips-now-available-in-five-new-regions-and-with-improved-performance/ ; AWS ML Blog, 2020-09-28, https://aws.amazon.com/blogs/machine-learning/aws-inferentia-is-now-available-in-11-aws-regions-with-best-in-class-performance-for-running-object-detection-models-at-scale/ ; EC2 Inf1 product page (still live, undated), https://aws.amazon.com/ec2/instance-types/inf1/ ; AWS Well-Architected ML Lens MLCOST05-BP02 (still live), https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlcost05-bp02.html (all accessed 2026-06-12)
5. **UNVERIFIED:** a distinct 2021–2022 AWS *Architecture Blog* post making this claim was not located in this pass; the claim circulated across multiple AWS properties in that period using the same boilerplate. If the brief's current citation points to a specific Architecture Blog URL, retain it as one instance; the canonical origin remains the December 2019 launch materials above.

**Character of the claim (for the footnote):** pre-LLM (re:Invent 2019; example workloads were Alexa, vision, speech, recommendations); *infrastructure-cost* basis, not energy or FLOPs; "up to" framing; customer-reported in the blog version, asserted by Jassy in the keynote; made in service of marketing a new inference chip (vendor adjacency worth disclosing, consistent with project disclosure conventions).

---

## Synthesis — what the brief can now say

### Draft replacement passage (3 sentences, each leg with "as of" framing)

> As of mid-2025, the volume in the LLM regime sat decisively on the inference side: in Menlo Ventures' mid-year enterprise survey, 74% of startup builders and 49% of large enterprises reported workloads that were majority- or nearly-all-inference, up from 48% and 29% a year earlier (Menlo 2025b). The pressure of that continuous flow is legible in the providers' own disclosures across 2025 and into 2026 — OpenAI staggered its GPT-4.5 rollout because it was, in Altman's words, "out of GPUs" (February 2025), Anthropic imposed weekly rate limits citing unprecedented serving demand (July 2025), and every major hyperscaler told investors it was capacity-constrained on AI, from Microsoft's "demand remains higher than supply" (July 2025) to Alphabet's expectation of operating "supply-constrained" through 2026 (February 2026). The energy ledger tells the same story: the IEA reported in April 2026 that electricity consumption by AI-focused data centres surged roughly 50% in 2025 while model providers' active users tripled, and current institutional estimates attribute somewhere between one-third (Epoch AI, on a power-capacity basis) and 60–70% (Meta and Google operational data reported by the IEA, on an energy basis) of AI compute to inference — a wide range that reflects definitional spread, not doubt about the direction.

(If three sentences is too long for the slot, the second sentence can be cut to its first two clauses without losing the leg.)

### Draft AWS historical footnote

> The familiar claim that inference accounts for "up to 90%" of machine-learning compute cost is an AWS marketing figure from the December 2019 launch of its Inferentia inference chip: Amazon's press release stated that "for every dollar spent on training, up to nine are spent on inference," the AWS launch blog attributed to customers the estimate that inference "can account for up to 90% of the cost of their machine learning work," and AWS CEO Andy Jassy's re:Invent 2019 keynote put 80–90% of at-scale production ML compute cost in inference, using Alexa as the example (Amazon press release and AWS News Blog, 3 December 2019; Jassy keynote, re:Invent 2019). The figure was recycled across AWS product pages and blogs through 2020–2022, which is where it is usually encountered. It describes pre-LLM production machine learning, measures infrastructure cost rather than energy or floating-point operations, and carries an "up to" qualifier — useful as evidence that inference dominance predates the LLM era, not as a current estimate for LLM workloads.

---

## Limitations

1. **Definitional spread.** The inference-share estimates measure different things: infrastructure **cost** (AWS 2019: 80–90%), **energy** in operational corporate fleets (Meta/Google via IEA: 60–70%, data from ~2019–2022), **power capacity** (Epoch 2025: roughly one-third each for training/experiments/inference), **workload composition by survey** (Menlo 2025b), and **server fleet composition** (LBNL, no split). These are not interconvertible; the brief should never blend them in one figure.
2. **No current authoritative LLM-specific split.** Neither IEA (2025, 2026) nor LBNL (2024) publishes a training-vs-inference percentage for the LLM era; both flag operational-practice data gaps. Any single percentage the brief quotes for "inference share today" would overstate the state of knowledge — hence the range-plus-direction formulation above.
3. **Hyperscaler statements are aggregate.** "Capacity constrained" earnings language covers training, inference, and first-party AI products together; only the model-provider rate-limit episodes (OpenAI, Anthropic) are unambiguously serving-side.
4. **Vendor adjacency.** The AWS 90% figure marketed an inference chip; Google's 0.24 Wh paper is self-published and not independently verified; Menlo is an LLM investor (already disclosed in project conventions); Epoch and SemiAnalysis are think-tank/analyst estimates and labeled as such.
5. **Efficiency-vs-volume tension.** Per-prompt inference energy is falling fast (Google: 33x in one year; IEA: order-of-magnitude annual declines per task) even as aggregate inference demand grows — the brief's claim should rest on aggregate flow and capacity rationing, not per-query intensity.
6. **The 2021–2022 AWS Architecture Blog citation** in the current brief draft was not independently located; the December 2019 launch materials are the verifiable origin (see Leg 3, item 5).
