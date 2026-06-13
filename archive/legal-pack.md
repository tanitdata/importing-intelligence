---
type: note
created: 2026-06-12
tags: [legal-precision, cloud-act, export-controls, sanctions, AUD-RISK-02, D7]
links: [section-4, r-series-research]
---

# R7 — Legal-Precision Pack: CLOUD Act, Export Controls on Inference, Sanctions Layer

Prepared 2026-06-12 for the brief's Section 4 (LLM access geography). Supports audit item AUD-RISK-02 and author decision D7 (export controls on inference framed as EVOLVING/foreseeable, not currently binding). All sources paraphrased; URL + access date given for each. All access dates are 2026-06-12 unless noted.

---

## Component 1 — CLOUD Act (18 U.S.C. § 2713)

### Verified statutory scope

Statute text verified against the Legal Information Institute mirror of 18 U.S.C. § 2713 (added by the CLOUD Act, Pub. L. 115-141, Div. V, March 2018). Verified elements:

- **Covered entities:** providers of *electronic communication service* (ECS) or *remote computing service* (RCS) — i.e., the categories regulated by the Stored Communications Act (SCA), 18 U.S.C. §§ 2701–2713. Major cloud and LLM-API providers subject to U.S. jurisdiction fall within RCS/ECS as applied in practice.
- **Obligation:** comply with SCA obligations to preserve, back up, or disclose the contents of wire or electronic communications and records or other information pertaining to a customer or subscriber.
- **Data scope:** information within the provider's *possession, custody, or control*.
- **Geographic scope:** the obligation applies regardless of whether the data is located inside or outside the United States. Foreign storage location is not a defense.
- **Process:** the obligation is triggered by lawful process under the SCA (warrant under § 2703 on probable cause for content; subpoena or § 2703(d) court order for other categories). It is not a free-standing access power.
- **Limits built into the Act:** the CLOUD Act added a statutory comity mechanism — a provider may move to quash or modify legal process where the target is not a U.S. person and does not reside in the U.S., and disclosure would create a material risk of violating the law of a "qualifying foreign government" (one with a CLOUD Act executive agreement); courts then apply a codified comity analysis (18 U.S.C. § 2703(h)). The Act's second part authorizes bilateral executive agreements letting qualifying foreign governments serve process directly on U.S. providers.

Sources:
- Statute text: https://www.law.cornell.edu/uscode/text/18/2713 (accessed 2026-06-12).
- CRS, Stephen P. Mulligan, *Cross-Border Data Sharing Under the CLOUD Act*, R45173 (Apr. 23, 2018): https://www.congress.gov/crs-product/R45173 (accessed 2026-06-12). Confirms the two-part structure: (1) the SCA amendment requiring disclosure of data in the provider's possession, custody, or control regardless of storage location (mooting *United States v. Microsoft*); (2) the executive-agreement framework for foreign-government access.
- DOJ white paper, *Promoting Public Safety, Privacy, and the Rule of Law Around the World: The Purpose and Impact of the CLOUD Act* (April 2019): https://www.justice.gov/criminal/cloud-act-resources (resource page; PDF at https://www.justice.gov/d9/press-releases/attachments/2019/04/10/department_of_justice_cloud_act_white_paper_2019_04_10_final_0.pdf) (accessed 2026-06-12). DOJ's own framing emphasizes that the Act clarified existing SCA obligations and operates through legal process.

### What the CLOUD Act does NOT do (overclaim guardrails)

The brief must not present the CLOUD Act as a blanket U.S. access right to globally stored data. Specifically:

1. **Not a general surveillance or seizure authority.** It operates only through ordinary SCA legal process (warrant/subpoena/court order), with the warrant standard (probable cause, judicial approval) governing content. No process, no obligation.
2. **Not applicable to non-covered entities.** It binds ECS/RCS providers subject to U.S. jurisdiction. It does not reach entities outside SCA categories or outside U.S. jurisdiction (a purely foreign provider with no U.S. nexus is not covered).
3. **Not a repeal of comity.** The Act *added* a statutory comity/quash procedure for conflicts with qualifying foreign law, and common-law comity analysis remains available for other conflicts.
4. **Not new in kind.** DOJ and CRS both characterize § 2713 as codifying the government's long-asserted reading of the SCA (the position litigated in *Microsoft*), not creating a novel data-grab power.
5. **The executive-agreement part runs the other way:** it is a mechanism for *foreign* governments to obtain data from U.S. providers under their own law, subject to certification requirements — not an expansion of U.S. reach.

The accurate claim for the brief's purposes: the CLOUD Act means that *jurisdiction over the provider, not the location of the server or the user, determines exposure to U.S. legal process* — which is exactly the flow-side point Section 4 needs, and it needs nothing stronger.

---

## Component 2 — Export controls on AI model weights / inference: current status as of 2026-06-12

### (a) The AI Diffusion Rule (January 2025)

BIS interim final rule, *Framework for Artificial Intelligence Diffusion*, 90 Fed. Reg. 4544 (Jan. 15, 2025; effective Jan. 13, 2025; main compliance date May 15, 2025). It (i) created ECCN 4E091 controlling the weights of closed-weight AI models trained on more than 10^26 computational operations, with a worldwide license requirement and a new foreign-direct-product rule for weights; (ii) imposed a three-tier country framework with compute thresholds and license exceptions (incl. License Exception AIA); (iii) notably for inference: License Exception AIA certifications required consignees to agree not to provide IaaS access sufficient to *train* 4E091 models for entities outside trusted destinations — i.e., even at its high-water mark, the rule's services hook targeted training-by-IaaS, not inference-as-a-service. Open-weight models were expressly out of scope.

Sources: BIS press release (Jan. 13, 2025): https://www.bis.gov/press-release/biden-harris-administration-announces-regulatory-framework-responsible-diffusion-advanced-artificial ; Federal Register PDF: https://www.govinfo.gov/content/pkg/FR-2025-01-15/pdf/2025-00636.pdf ; Hogan Lovells alert: https://www.hoganlovells.com/en/publications/us-department-of-commerce-expands-controls-on-advanced-semiconductors-and-establishes (all accessed 2026-06-12).

### (b) Rescission announced May 13, 2025 — and its unresolved legal status

On May 13, 2025, Commerce announced it was initiating rescission of the AI Diffusion Rule, two days before its compliance date; Under Secretary Kessler instructed BIS enforcement officials not to enforce it. BIS said it would publish a Federal Register rule formalizing rescission and "issue a replacement rule in the future." Concurrently BIS issued three guidance documents: (1) a presumption that Huawei Ascend 910B/910C/910D (and PRC 3A090-class ICs generally) violate the EAR, triggering General Prohibition 10; (2) a policy statement that exporting advanced computing ICs — including to foreign IaaS providers — with knowledge they will be used to *train* AI models for parties headquartered in D:5 countries (China) or Macau may require a license under catch-all end-use controls; (3) anti-diversion red-flag guidance. The BIS press release also warned generally about "allowing U.S. AI chips to be used for training and inference of Chinese AI models" — but as guidance keyed to chip exports and WMD/military-intelligence end uses, not as a new control on inference services.

**Critical nuance (as of June 2026):** the formal rescission rule has still not been published. The rule remains codified in the CFR but is unenforced. On May 12, 2026, GAO (B-337935) held that Commerce's *non-enforcement policy* is itself a "rule" under the Congressional Review Act that should have been submitted to Congress, while finding the planned rescission not ripe for review because the rulemaking steps had not been taken. Practical upshot: ECCN 4E091 model-weight controls exist on paper, are not enforced, and have no announced replacement — a genuinely indeterminate state.

Sources: BIS press release (May 13, 2025): https://www.bis.gov/press-release/department-commerce-announces-rescission-biden-era-artificial-intelligence-diffusion-rule-strengthens ; BIS policy statement on AI-training catch-all controls (May 13, 2025): https://www.bis.gov/media/documents/ai-policy-statement-training-ai-models-may-13-2025 ; Akin alert: https://www.akingump.com/en/insights/ai-law-and-regulation-tracker/bis-rescinds-ai-diffusion-rule-and-issues-new-guidance ; Baker McKenzie: https://sanctionsnews.bakermckenzie.com/bis-begins-rescinding-ai-diffusion-rule-and-issues-guidance-on-huawei-ics-and-on-ics-and-commodities-used-to-train-ai-models/ ; GAO B-337935: https://www.gao.gov/products/b-337935 ; Pillsbury on the GAO decision (May 28, 2026): https://www.pillsburylaw.com/en/news-and-insights/gao-commerce-non-enforcement-ai-diffusion-rule-congressional-review-act.html (all accessed 2026-06-12).

### (c) Subsequent 2025–2026 BIS actions touching this space

- **January 2026 chip-licensing rule:** BIS final rule effective Jan. 15, 2026, *Revision to License Review Policy for Advanced Computing Commodities* (91 Fed. Reg., doc. 2026-00789), moved license review for certain sub-frontier AI chips (H200-class) exported to China/Macau from presumption-of-denial to case-by-case, with supply-share, independent-testing, and KYC/end-use conditions. This is a **chip** rule; it does not control model weights or inference services. Sources: https://www.federalregister.gov/documents/2026/01/15/2026-00789/revision-to-license-review-policy-for-advanced-computing-commodities ; Lexology summary: https://www.lexology.com/library/detail.aspx?g=15809152-dc5f-44b8-b730-6d3a308a51c7 ; IST, *A Changing Export Control Landscape* (Feb. 2026): https://securityandtechnology.org/wp-content/uploads/2026/02/A-Changing-Export-Control-Landscape.pdf (all accessed 2026-06-12).
- **No new model-weight rule.** As of 2026-06-12 no replacement rule restoring or reworking 4E091-style weight controls has been published (per the GAO decision record and the Pillsbury alert above; also CRS R48642, *U.S. Export Controls and China: Advanced Semiconductors*: https://www.congress.gov/crs-product/R48642, accessed 2026-06-12).

### (d) Is inference-as-a-service restricted today? — No general restriction; the channel is legislative and foreseeable

Three findings, each load-bearing for D7:

1. **No EAR control on inference services.** BIS does not currently treat the provision of cloud/remote computing services — including LLM inference access — as an "export" under the EAR. The Carnegie Endowment's May 2026 survey of the cloud-controls debate states this plainly: BIS has limited tools to restrict remote access to U.S.-located compute, and the chip-license-condition authority for foreign data centers has not historically been exercised. Source: Carnegie, *The Geopolitical Debates Over Controlling Cloud Compute* (May 5, 2026): https://carnegieendowment.org/research/2026/05/the-geopolitical-debates-over-controlling-cloud-compute (accessed 2026-06-12).
2. **The IaaS KYC proposed rule was never finalized.** The January 29, 2024 BIS NPRM (89 Fed. Reg. 5698, implementing EO 13984 and EO 14110) would have required U.S. IaaS providers and foreign resellers to run Customer Identification Programs and report foreign training of large AI models. It was a *proposed* rule only; comments closed April 29, 2024. EO 14110 — one of its two legal bases — was revoked on January 20, 2025 (with EO 14179, Jan. 23, 2025, directing review/rescission of implementing actions). No final rule has issued as of June 2026, and the 2026 policy literature treats KYC-for-cloud as something RASA *would* require, not something in force. Even as proposed, it targeted KYC and training-run reporting, not inference restrictions. Sources: NPRM: https://www.govinfo.gov/content/pkg/FR-2024-01-29/html/2024-01580.htm ; BIS press release (Jan. 29, 2024): https://www.bis.gov/press-release/commerce-proposes-rule-advance-u.s.-national-security-interests-implement-biden-harris-administrations-ai ; Skadden alert: https://www.skadden.com/insights/publications/2024/02/know-your-iaas-customer ; Wiley on EO 14179: https://www.wiley.law/alert-Trump-Administration-Issues-New-AI-Executive-Order (all accessed 2026-06-12). Status-of-rule finding is partly verification-by-absence; see Limitations.
3. **The foreseeable channel is the Remote Access Security Act (RASA).** H.R. 2683 passed the House 369–22 on January 12, 2026. It would amend the Export Control Reform Act of 2018 to define "remote access" to controlled items (via internet or cloud computing services) as a controlled activity, giving BIS authority to license and penalize remote access — i.e., it would for the first time bring cloud compute, and potentially inference services running on controlled hardware, inside export-control jurisdiction. A Senate companion (S. 3519, McCormick/Wyden/Cotton/Coons) is pending; a 2024 predecessor passed the House and died in the Senate. As of 2026-06-12 RASA is **not law**. Sources: bill text: https://www.govinfo.gov/content/pkg/BILLS-119hr2683rfs/pdf/BILLS-119hr2683rfs.pdf ; Select Committee press release (Jan. 12, 2026): http://chinaselectcommittee.house.gov/media/press-releases/house-passes-bipartisan-legislation-to-limit-adversaries-remote-access-to-critical-technology ; S. 3519: https://www.govinfo.gov/content/pkg/BILLS-119s3519is/html/BILLS-119s3519is.htm ; Carnegie May 2026 (above); Mondaq/Crowell summary: https://www.mondaq.com/unitedstates/export-controls-trade-investment-sanctions/1732508/house-passes-remote-access-security-act-to-limit-adversaries-remote-access-to-critical-technology (all accessed 2026-06-12).

**Conclusion for D7:** As of June 12, 2026, no U.S. export-control rule restricts the provision of LLM inference-as-a-service to any jurisdiction as such. The control surface today consists of (i) chip-export licensing (including the Jan. 2026 case-by-case China policy with KYC conditions), (ii) unenforced-but-codified model-weight controls in regulatory limbo, and (iii) end-use catch-alls and guidance aimed at *training* for Chinese/D:5-linked entities. The movement — RASA's House passage by an overwhelming bipartisan margin, the pending Senate companion, and BIS's promised replacement rule — makes controls reaching remote access a foreseeable scenario channel, which is precisely the register D7 requires.

---

## Component 3 — Sanctions layer (recap)

**Iran:** comprehensively embargoed and bindingly relevant to LLM access today. The Iranian Transactions and Sanctions Regulations (ITSR), 31 CFR Part 560, prohibit (inter alia) the exportation of goods, services, or technology from the United States to Iran (§ 560.204) — which captures U.S.-provider LLM API and consumer access. The program is active and intensifying: OFAC issued new Iran designations and a Strait of Hormuz-related alert as recently as May 1, 2026. Sources: eCFR 31 CFR Part 560: https://www.ecfr.gov/current/title-31/subtitle-B/chapter-V/part-560 ; OFAC Iran program page: https://ofac.treasury.gov/sanctions-programs-and-country-information/iran-sanctions ; OFAC recent action 2026-05-01: https://ofac.treasury.gov/recent-actions/20260501 (all accessed 2026-06-12).

**Syria — posture changed fundamentally in 2025–2026; the brief must not describe Syria as comprehensively sanctioned.** Sequence: GL 24 (Jan. 6, 2025) → GL 25 (May 23, 2025, broadly authorizing transactions otherwise prohibited by the Syrian Sanctions Regulations, 31 CFR Part 542) plus a 180-day Caesar Act waiver (May 23, 2025) → Executive Order 14312 (June 30, 2025, effective July 1, 2025) revoking the six foundational Syria EOs, terminating the national emergency, delisting ~518 SDN entries, and converting the program into the targeted PAARSS framework (Assad-linked persons, human-rights abusers, captagon traffickers, proliferation-linked persons, ISIS/al-Qa'ida, Iranian proxies) → Caesar Act **repealed** by the FY2026 NDAA (signed Dec. 18, 2025), removing the secondary-sanctions overhang. **What remains as of 2026-06-12:** Syria is still designated a State Sponsor of Terrorism (1979 designation; EO 14312 directed a review; rescission has not occurred — confirmed by Lawfare, June 11, 2026). The SST designation keeps SST-linked export controls operative (EAR Country Group E:1 consequences, NDAA FY2019 § 1754(c), Arms Export Control Act § 40, Foreign Assistance Act § 620A), although EO 14312 waived Syria Accountability Act and CBW Act export-control requirements. Net for LLM access: the OFAC services embargo on Syria is gone; residual friction is SST/EAR-based and compliance-cultural, not comprehensive-sanctions-based. Sources: EO 14312: https://www.whitehouse.gov/presidential-actions/2025/06/providing-for-the-revocation-of-syria-sanctions/ ; OFAC implementation notice (June 30, 2025): https://ofac.treasury.gov/recent-actions/20250630 ; OFAC Syria archived-program page: https://ofac.treasury.gov/sanctions-programs-and-country-information/syria-sanctions-inactive-and-archived ; Just Security, Alpert & Salzman (Dec. 19, 2025): https://www.justsecurity.org/125619/removing-syria-state-sponsor-terrorism-designation/ ; Curtis client alert on Caesar repeal (Dec. 19, 2025): https://www.curtis.com/our-firm/news/u-s-repeals-the-caesar-act-in-latest-move-to-ease-syria-sanctions ; Lawfare on the SST designation (June 11, 2026): https://www.lawfaremedia.org/article/syria-s-state-sponsor-of-terrorism-designation-is-blocking-its-recovery (all accessed 2026-06-12).

(North Korea, 31 CFR Part 510, and Cuba, 31 CFR Part 515, remain the other comprehensively/near-comprehensively sanctioned jurisdictions if the brief lists the category; not researched in depth here.)

---

## Component 4 — Draft language for the brief

### (a) CLOUD Act sentence (+ optional clarifying clause)

> Under the CLOUD Act (18 U.S.C. § 2713), providers of electronic communication and remote computing services subject to U.S. jurisdiction must preserve and disclose data within their possession, custody, or control in response to lawful U.S. process — warrants, subpoenas, and court orders under the Stored Communications Act — regardless of where the data is physically stored, subject to statutory comity procedures and the Act's framework of bilateral executive agreements.

Optional clarifying clause (recommended, for AUD-RISK-02):

> The Act is narrower than its reputation: it confers no blanket access to foreign-held data, binds only covered providers, and operates through case-by-case legal process rather than unilateral seizure — its significance for flow analysis is that it ties exposure to jurisdiction over the provider rather than to the location of the server.

### (b) Export controls as evolving (D7 register)

> As of June 2026, no U.S. export-control rule restricts the provision of LLM inference as a service to any jurisdiction. The Biden administration's January 2025 AI Diffusion Rule — which created the first export control on AI model weights (ECCN 4E091) — was suspended by the Commerce Department in May 2025 before its compliance date and sits in regulatory limbo: still codified, formally unenforced, with a promised replacement rule yet to appear. The direction of travel, however, is legible: the Remote Access Security Act, which passed the House 369–22 in January 2026 and awaits Senate action, would extend export-control jurisdiction to remote access to controlled items via cloud services — the statutory predicate under which inference access itself could become a licensable flow. Controls on inference are therefore best read as a foreseeable policy channel rather than a binding regime today.

### (c) Sanctions layer (current Syria posture)

> The bindingly closed jurisdictions for U.S.-provider LLM access are those under comprehensive OFAC embargoes — above all Iran, where the Iranian Transactions and Sanctions Regulations (31 CFR Part 560) prohibit the export of services from the United States. Syria no longer belongs in that category: the comprehensive Syria sanctions program was revoked by executive order effective July 2025 and the Caesar Act repealed in December 2025, leaving a targeted sanctions framework plus residual export-control friction tied to Syria's still-extant State Sponsor of Terrorism designation, which remained under review as of June 2026.

---

## What changed recently / perishability warnings

1. **AI Diffusion Rule limbo is unstable.** The May 12, 2026 GAO CRA decision (B-337935) increases pressure on BIS either to formally rescind (Federal Register rule) or to submit its non-enforcement policy to Congress. Either step, or the promised replacement rule, could land at any time. Re-verify before publication.
2. **RASA could move.** Senate companion S. 3519 is pending with bipartisan sponsorship; the House margin (369–22) suggests enactment is plausible within the brief's shelf life. If RASA becomes law, the D7 sentence must be rewritten — the authority (though not necessarily implementing regulations) would then exist.
3. **Syria SST rescission is actively in play.** State Department review ongoing (Lawfare, June 11, 2026; The National, April 21, 2026, reporting Syrian-US talks). Delisting plus a follow-on BIS rule (removal from Country Group E:1) would eliminate most remaining Syria export-control friction. The Syria sentence carries an "as of June 2026" stamp for this reason.
4. **Iran posture is escalating, not relaxing** (May 2026 designations; Hormuz-related OFAC alert) — directionally stable for the brief but designation details churn weekly.
5. **The January 2026 chip rule is being litigated politically** (CRA challenges to the H200 policy were debated in the Senate in May 2026 per the Congressional Record); chip-layer facts should be re-checked at publication.

## Limitations

- The IaaS KYC NPRM's status ("never finalized") rests on (i) absence of any final rule in searched sources, (ii) revocation of EO 14110 (one of its two legal bases; EO 13984 remains), and (iii) 2026 expert commentary (Carnegie, IST) treating cloud KYC as prospective. I found no BIS document formally withdrawing the NPRM, so the precise docket status is UNVERIFIED — "proposed in January 2024 and not finalized as of June 2026" is the defensible formulation.
- Reported section numbers for the Caesar Act repeal in the FY2026 NDAA conflict across sources (Just Security: § 8369; Curtis: § 6211). The repeal itself is multiply confirmed; cite the NDAA without a section number, or verify against the enrolled bill before print.
- Whether providing inference access to Syria today raises residual EAR issues (E:1 software/technology controls as applied to a hosted service) is a genuinely unsettled compliance question; the pack's claim is limited to the OFAC layer, which is the defensible one.
- 18 U.S.C. § 2713 was verified via law.cornell.edu only; uscode.house.gov was not separately checked (Cornell LII mirrors the official U.S. Code and the CRS report corroborates the operative language).
- DOJ white paper (2019) and CRS R45173 (2018) predate any later CLOUD Act executive agreements (UK, Australia); the pack does not inventory which agreements are in force as of 2026 — flag if the brief needs that.
