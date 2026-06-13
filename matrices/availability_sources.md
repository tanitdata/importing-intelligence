# MENA LLM-Provider Availability Matrix (R1)

**Date of record:** 2026-06-12
**Status:** v1 — all cells sourced from official provider documentation fetched 2026-06-12 (three columns reuse the Phase 0/V5 archive-pinned captures of the same date).

## Method note

- Every cell rests on an **official primary source**: provider documentation, help-center articles, terms of service, or published country/region lists. No journalism, no third-party aggregators.
- Cell = **legal/policy availability** ("may a customer located in jurisdiction X lawfully sign up for and be served by this service, per the provider's own published policy?"). It is **not** network reachability, latency, payment-rail feasibility, or local-regulator permission.
- Two evidence types are distinguished throughout (see Limitations):
  - **Positive lists** (OpenAI, Anthropic, Google, Microsoft): the provider enumerates supported countries; absence from the list is treated as exclusion.
  - **ToS exclusion lists** (Mistral, Cohere, OpenRouter, AWS): the provider restricts named jurisdictions (or none) in its terms; a ✓ means "not excluded by the provider's terms," a weaker claim than presence on a positive list.
- Cell values: **✓** officially supported (or not excluded, for exclusion-list providers — flagged in notes) / **partial** supported with restrictions or pass-through restrictions / **✗** officially excluded (by list-absence or named exclusion — distinguished in notes) / **UNKNOWN** documentation does not settle the status.
- Per author decision D6, Syria, Sudan, Iran (and Yemen, which Anthropic excludes) are grouped as a separately labeled **sanctioned/conflict-affected** category: they are the existence proof of correlated constriction, distinct from non-sanctioned importers.

## Matrix

Columns: (1) OpenAI API · (2) ChatGPT (consumer) · (3) Anthropic/Claude API · (4) Google Gemini API / AI Studio · (5) Azure OpenAI (now Microsoft Foundry) · (6) AWS Bedrock · (7) OpenRouter · (8) Mistral La Plateforme · (9) Cohere

### Non-sanctioned importers

| Jurisdiction (ISO) | OpenAI API | ChatGPT | Anthropic | Gemini API | Azure OpenAI / MS Foundry | AWS Bedrock | OpenRouter | Mistral | Cohere |
|---|---|---|---|---|---|---|---|---|---|
| Algeria (DZ) | ✓ | ✓ ⁽²⁾ | ✓ ⁽³⁾ | ✓ | ✓ ⁽⁴⁾ | ✓ ⁽⁵⁾ | partial ⁽⁶⁾ | ✓ ⁽⁷⁾ | ✓ ⁽⁸⁾ |
| Bahrain (BH) | ✓ | ✓ ⁽²⁾ | ✓ ⁽³⁾ | ✓ | ✓ ⁽⁴⁾ | ✓ ⁽⁵⁾ | partial ⁽⁶⁾ | ✓ ⁽⁷⁾ | ✓ ⁽⁸⁾ |
| Egypt (EG) | ✓ | ✓ ⁽²⁾ | ✓ ⁽³⁾ | ✓ | ✓ ⁽⁴⁾ | ✓ ⁽⁵⁾ | partial ⁽⁶⁾ | ✓ ⁽⁷⁾ | ✓ ⁽⁸⁾ |
| Iraq (IQ) | ✓ | ✓ ⁽²⁾ | ✓ ⁽³⁾ | ✓ | ✓ ⁽⁴⁾ | ✓ ⁽⁵⁾ | partial ⁽⁶⁾ | ✓ ⁽⁷⁾ | ✓ ⁽⁸⁾ |
| Jordan (JO) | ✓ | ✓ ⁽²⁾ | ✓ ⁽³⁾ | ✓ | ✓ ⁽⁴⁾ | ✓ ⁽⁵⁾ | partial ⁽⁶⁾ | ✓ ⁽⁷⁾ | ✓ ⁽⁸⁾ |
| Kuwait (KW) | ✓ | ✓ ⁽²⁾ | ✓ ⁽³⁾ | ✓ | ✓ ⁽⁴⁾ | ✓ ⁽⁵⁾ | partial ⁽⁶⁾ | ✓ ⁽⁷⁾ | ✓ ⁽⁸⁾ |
| Lebanon (LB) | ✓ ⁽¹⁾ | ✓ ⁽²⁾ | ✓ ⁽³⁾ | ✓ | ✓ ⁽⁴⁾ | ✓ ⁽⁵⁾ | partial ⁽⁶⁾ | ✓ ⁽⁷⁾ | ✓ ⁽⁸⁾ |
| Libya (LY) | ✓ ⁽¹⁾ | ✓ ⁽²⁾ | ✓ ⁽³⁾ | ✓ | ✓ ⁽⁴⁾ | ✓ ⁽⁵⁾ | partial ⁽⁶⁾ | ✓ ⁽⁷⁾ | ✓ ⁽⁸⁾ |
| Morocco (MA) | ✓ | ✓ ⁽²⁾ | ✓ ⁽³⁾ | ✓ | ✓ ⁽⁴⁾ | ✓ ⁽⁵⁾ | partial ⁽⁶⁾ | ✓ ⁽⁷⁾ | ✓ ⁽⁸⁾ |
| Oman (OM) | ✓ | ✓ ⁽²⁾ | ✓ ⁽³⁾ | ✓ | ✓ ⁽⁴⁾ | ✓ ⁽⁵⁾ | partial ⁽⁶⁾ | ✓ ⁽⁷⁾ | ✓ ⁽⁸⁾ |
| Palestine (PS) | ✓ ⁽⁹⁾ | ✓ ⁽²⁾ | ✓ ⁽³⁾ | ✓ | ✓ ⁽⁹⁾ | ✓ ⁽⁹⁾ | partial ⁽⁶⁾ | ✓ ⁽⁷⁾ | ✓ ⁽⁸⁾ |
| Qatar (QA) | ✓ | ✓ ⁽²⁾ | ✓ ⁽³⁾ | ✓ | ✓ ⁽⁴⁾ | ✓ ⁽⁵⁾ | partial ⁽⁶⁾ | ✓ ⁽⁷⁾ | ✓ ⁽⁸⁾ |
| Saudi Arabia (SA) | ✓ | ✓ ⁽²⁾ | ✓ ⁽³⁾ | ✓ | ✓ ⁽⁴⁾ | ✓ ⁽⁵⁾ | partial ⁽⁶⁾ | ✓ ⁽⁷⁾ | ✓ ⁽⁸⁾ |
| Tunisia (TN) | ✓ | ✓ ⁽²⁾ | ✓ ⁽³⁾ | ✓ | ✓ ⁽⁴⁾ | ✓ ⁽⁵⁾ | partial ⁽⁶⁾ | ✓ ⁽⁷⁾ | ✓ ⁽⁸⁾ |
| UAE (AE) | ✓ | ✓ ⁽²⁾ | ✓ ⁽³⁾ | ✓ | ✓ ⁽⁴⁾ | ✓ ⁽⁵⁾ | partial ⁽⁶⁾ | ✓ ⁽⁷⁾ | ✓ ⁽⁸⁾ |

### Sanctioned / conflict-affected (D6 group — correlated-constriction existence proof)

| Jurisdiction (ISO) | OpenAI API | ChatGPT | Anthropic | Gemini API | Azure OpenAI / MS Foundry | AWS Bedrock | OpenRouter | Mistral | Cohere |
|---|---|---|---|---|---|---|---|---|---|
| Yemen (YE) | ✓ | ✓ ⁽²⁾ | **✗** ⁽¹⁰⁾ | ✓ | ✓ ⁽⁴⁾ | ✓ ⁽⁵⁾ | partial ⁽⁶⁾ | ✓ ⁽⁷⁾ | ✓ ⁽⁸⁾ |
| Sudan (SD) | ✓ | ✓ ⁽²⁾ | ✓ ⁽³⁾ | ✓ | **✗** ⁽¹¹⁾ | UNKNOWN ⁽¹²⁾ | partial ⁽⁶⁾ | ✓ ⁽⁷⁾ | ✓ ⁽⁸⁾ |
| Syria (SY) | **✗** ⁽¹³⁾ | **✗** ⁽²⁾⁽¹³⁾ | **✗** ⁽¹⁰⁾ | **✗** ⁽¹⁴⁾ | **✗** ⁽¹¹⁾ | **✗** ⁽¹⁵⁾ | UNKNOWN ⁽¹⁶⁾ | **✗** ⁽¹⁷⁾ | UNKNOWN ⁽¹⁸⁾ |
| Iran (IR) | **✗** ⁽¹³⁾ | **✗** ⁽²⁾⁽¹³⁾ | **✗** ⁽¹⁰⁾ | **✗** ⁽¹⁴⁾ | **✗** ⁽¹¹⁾ | **✗** ⁽¹⁵⁾ | UNKNOWN ⁽¹⁶⁾ | **✗** ⁽¹⁷⁾ | UNKNOWN ⁽¹⁸⁾ |

## Notes (per non-obvious cell)

1. **OpenAI API — Lebanon, Libya.** Both appear in OpenAI's supported countries and territories list (Lebanon between Latvia and Lesotho; Libya between Liberia and Liechtenstein), confirmed against the full list text fetched 2026-06-12. An initial partial extraction of the page erroneously suggested their absence; the full-list fetch settles it. Source: https://developers.openai.com/api/docs/supported-countries, accessed 2026-06-12, archive: http://web.archive.org/web/20260612132555/ (Phase 0/V5 pin).

2. **ChatGPT (consumer) — all cells.** OpenAI maintains a dedicated help article "ChatGPT Supported Countries" (https://help.openai.com/en/articles/7947663-chatgpt-supported-countries, accessed 2026-06-12), but the article body is JavaScript-rendered and could not be captured; no Wayback snapshot exists (checked 2026-06-12). The cells therefore rest on three corroborating official pages: (a) the developers supported-countries page states that accessing or offering access to OpenAI's *services* (plural, unqualified) outside the listed countries may lead to account blocking or suspension; (b) the help article on travelling (https://help.openai.com/en/articles/9022015, accessed 2026-06-12) treats ChatGPT and the API together and points to a single supported list; (c) the help article on unsupported-country signup errors (https://help.openai.com/en/articles/8983035, accessed 2026-06-12) states OpenAI does not currently support ChatGPT *and* API access in all regions, again with one list. Conclusion: OpenAI publishes one unified country list covering both ChatGPT and the API; ChatGPT cells mirror the API column. Confidence: high but indirect — flagged in Limitations.

3. **Anthropic — all non-excluded cells.** All 19 jurisdictions except Syria, Yemen, Iran appear on Anthropic's supported-countries list. Additional ToS-level constraint applying to every ✓ cell: entities more than 50% owned by parties from unsupported regions are barred regardless of where the entity itself is located (announced 2025-09-04). A nominally supported MENA company majority-owned from, e.g., Syria or Iran is therefore excluded. Sources: https://www.anthropic.com/supported-countries, accessed 2026-06-12, archive: http://web.archive.org/web/20260612132920/ (Phase 0/V5 pin); https://www.anthropic.com/news/updating-restrictions-of-sales-to-unsupported-regions (2025-09-04).

4. **Azure OpenAI / Microsoft Foundry — product name and evidence.** The product line formerly sold as Azure OpenAI is now part of **Microsoft Foundry** (naming arc: Azure AI Studio → Azure AI Foundry → Microsoft Foundry; Azure OpenAI resources upgrade to Foundry resources with endpoints and keys preserved). Source: https://learn.microsoft.com/en-us/azure/foundry/what-is-foundry, accessed 2026-06-12, archive: http://web.archive.org/web/20260530002117/https://learn.microsoft.com/en-us/azure/foundry/what-is-foundry. The cell question is **commercial availability** ("can a customer in country X buy Azure services, including Foundry/Azure OpenAI?"), settled by two positive Microsoft lists, both including Algeria, Bahrain, Egypt, Iraq, Jordan, Kuwait, Lebanon, Libya, Morocco, Oman, Palestinian Authority, Qatar, Saudi Arabia, Tunisia, UAE, and Yemen: (a) the Microsoft Customer Agreement FAQ's table of countries where new customers can purchase Azure directly from Azure.com (doc updated 2026-05-05/2026-06-11): https://learn.microsoft.com/en-us/azure/cost-management-billing/microsoft-customer-agreement/microsoft-customer-agreement-faq, accessed 2026-06-12, archive: http://web.archive.org/web/20260217071931/ (Feb 2026 snapshot); (b) the Azure account FAQ's statement that Azure is commercially available in 140 countries/regions with an enumerated list: https://azure.microsoft.com/en-us/free/free-account-faq/, accessed 2026-06-12, no Wayback snapshot available (checked 2026-06-12). Caveat: commercial availability is country-of-billing; model-level region availability within Foundry varies by Azure region (MENA regions exist: UAE North/Central, Qatar Central, Saudi Arabia East) but any commercially served customer may deploy to any permitted region, so this does not change cell values.

5. **AWS Bedrock — evidence.** AWS publishes no single global "where we sell" list; the operative official artifacts are (a) the AWS EMEA countries list (countries whose accounts contract with Amazon Web Services EMEA SARL), which includes Algeria, Bahrain, Egypt, Iraq, Jordan, Kuwait, Lebanon, Libya, Morocco, Oman, Palestinian Territories, Qatar, Saudi Arabia, Tunisia, UAE, and Yemen: https://aws.amazon.com/legal/aws-emea-countries/, accessed 2026-06-12, archive: http://web.archive.org/web/20260501060121/https://aws.amazon.com/legal/aws-emea-countries/; and (b) the AWS Contracting Party page, which assigns any country not otherwise listed to Amazon Web Services, Inc.: https://aws.amazon.com/legal/aws-contracting-party/, accessed 2026-06-12, no Wayback snapshot available (checked 2026-06-12). Presence on the EMEA list is treated as affirmative evidence of commercial availability. Bedrock is a region-hosted service (including Middle East (Bahrain) me-south-1 and Middle East (UAE) me-central-1) usable from any AWS account, so country-level commercial availability is the binding constraint.

6. **OpenRouter — all "partial" cells.** OpenRouter's Terms of Service contain **no platform-level list of excluded countries**. The geographically relevant clauses: §5.7 states that certain Model Providers do not authorize users located in certain countries or regions to access their models ("Restricted Models") — i.e., upstream provider restrictions pass through per-model; §6.8 notes OpenRouter cannot always accurately represent a user's country of origin to providers. The privacy policy adds nothing geographic. So no MENA jurisdiction is either "officially supported" or "officially excluded" at the platform level; access to specific models from a given country may be restricted by the upstream provider. Hence "partial" rather than ✓. Source: https://openrouter.ai/terms, accessed 2026-06-12, archive: http://web.archive.org/web/20260610031424/https://openrouter.ai/terms; https://openrouter.ai/privacy, accessed 2026-06-12, no Wayback snapshot available (checked 2026-06-12).

7. **Mistral La Plateforme — all ✓ cells.** Mistral publishes no positive supported-country list. Its Commercial Terms of Service §14.13 (export/trade controls) prohibit use from jurisdictions under comprehensive sanctions regimes, naming Cuba, Iran, North Korea, Syria, and the Crimea/Donetsk/Luhansk regions, and require compliance with OFAC, U.S. Commerce, EU, and UN Security Council sanctions lists. The Usage Policy contains no geographic restriction. A ✓ therefore means "not excluded by Mistral's terms" (exclusion-list evidence type), not "affirmatively enumerated as supported." Source: https://legal.mistral.ai/terms/commercial-terms-of-service, accessed 2026-06-12, no Wayback snapshot available (checked 2026-06-12); index at https://legal.mistral.ai/terms, accessed 2026-06-12.

8. **Cohere — all ✓ cells.** Cohere's Terms of Use contain no country list and no platform-level geographic signup restriction. Geographically relevant clauses: a representation (in the Apple App Store section, i.e., scoped to mobile-app use) that the user is not located in a country under U.S. government embargo or designated terrorist-supporting; an ITAR-use prohibition; and a general obligation to comply with all applicable trade restrictions and not to export the Cohere Solution to sanctioned countries/persons. A ✓ therefore means "not excluded by Cohere's terms" (exclusion-list evidence type). Source: https://cohere.com/terms-of-use, accessed 2026-06-12, archive: http://web.archive.org/web/20260607163926/https://cohere.com/terms-of-use.

9. **Palestine — naming variance.** Listed as "Palestine" by OpenAI, "Palestinian Authority" by Microsoft (MCA FAQ and Azure account FAQ), and "Palestinian Territories (PS)" by AWS. All treated as PS. Same sources as notes 1, 4, 5.

10. **Anthropic — Syria, Yemen, Iran ✗.** Absent from Anthropic's positive supported-countries list (list-absence exclusion). Yemen's exclusion by Anthropic alone — while OpenAI, Google, Microsoft, and AWS all list Yemen — is the matrix's clearest single-provider divergence. Source as note 3.

11. **Azure — Sudan, Syria, Iran ✗.** Absent from both Microsoft positive commercial-availability lists (MCA direct-purchase table; Azure account FAQ 140-country list). This is list-absence exclusion: Microsoft does not name these jurisdictions as excluded. Caveats: (a) the Azure account FAQ wording "including those listed below" leaves formal room for unenumerated countries; (b) the MCA is also offered "through Cloud Solution Providers around the world," so indirect CSP resale into an unlisted jurisdiction is not formally foreclosed by these pages. Sudan's absence (while Sudan appears on OpenAI's, Anthropic's, and Google's lists) is the notable case — see UNVERIFIED section. Sources as note 4.

12. **AWS — Sudan UNKNOWN.** Sudan is absent from the AWS EMEA countries list, but the AWS Contracting Party page assigns accounts from any unlisted country to Amazon Web Services, Inc. by default, so list-absence here does not function as exclusion. No official AWS document fetched today affirmatively settles whether AWS opens accounts for customers located in Sudan. The AWS Customer Agreement §11.6 requires sanctions compliance generally but names no countries (and Sudan is not under comprehensive U.S. embargo). Marked UNKNOWN. Sources as notes 5 and 15.

13. **OpenAI (API and ChatGPT) — Syria, Iran ✗.** Absent from OpenAI's supported list (Suriname is followed directly by Sweden; Iraq is followed directly by Ireland). List-absence exclusion. Source as note 1; ChatGPT coupling as note 2.

14. **Gemini API / AI Studio — Syria, Iran ✗.** Absent from Google's available-regions list for the Gemini API; all other 17 jurisdictions present. Source: https://ai.google.dev/gemini-api/docs/available-regions, accessed 2026-06-12, archive: http://web.archive.org/web/20260612133451/ (Phase 0/V5 pin).

15. **AWS — Syria, Iran ✗ (ToS-level, countries not named).** AWS publishes no named country-exclusion list. The cell rests on: (a) absence from the EMEA countries list; (b) the AWS Customer Agreement's trade-compliance section, under which the customer represents that it and its payment institutions are not subject to sanctions or designated on prohibited/restricted-party lists, with OFAC economic sanctions programs expressly referenced. Iran and Syria are under comprehensive OFAC embargoes, which the agreement incorporates by reference rather than by name — so this ✗ involves one inferential step beyond the document text (applying the referenced OFAC regimes to these jurisdictions). Flagged in Limitations. Source: https://aws.amazon.com/agreement/, accessed 2026-06-12, archive: http://web.archive.org/web/20260607140527/https://aws.amazon.com/agreement/.

16. **OpenRouter — Syria, Iran UNKNOWN.** OpenRouter's public terms neither support nor exclude these jurisdictions; as a U.S.-based platform it presumably carries OFAC obligations, but its published documents do not say so, and per-model upstream restrictions (§5.7) would in practice constrict most major models. Documentation does not settle the status. Source as note 6.

17. **Mistral — Syria, Iran ✗ (named exclusion).** The only provider in this matrix that names excluded jurisdictions in its terms: Commercial ToS §14.13 names Iran and Syria (with Cuba, North Korea, and occupied Ukrainian regions) under comprehensive sanctions regimes. Notable: as an EU provider, Mistral's named list matches the U.S. comprehensive-embargo set — the EU/US divergence hypothesis finds no support at the named-exclusion level. Source as note 7.

18. **Cohere — Syria, Iran UNKNOWN.** Cohere's terms reference U.S. embargoes only in the Apple App Store clause (mobile-app scope) plus a general export-compliance obligation; no clause unambiguously bars an API customer located in Syria or Iran, and Cohere is a Canadian company (Ontario law governs). Likely excluded in practice, but the documentation does not settle it. Marked UNKNOWN. Source as note 8.

## Sources

| Provider | Page | URL | Access date | Archive snapshot |
|---|---|---|---|---|
| OpenAI | Supported countries and territories (API + services) | https://developers.openai.com/api/docs/supported-countries | 2026-06-12 | http://web.archive.org/web/20260612132555/ (Phase 0/V5 pin) |
| OpenAI | ChatGPT Supported Countries (help article; body not capturable) | https://help.openai.com/en/articles/7947663-chatgpt-supported-countries | 2026-06-12 | none exists (checked 2026-06-12) |
| OpenAI | Travelling / can't access ChatGPT or the API (help article) | https://help.openai.com/en/articles/9022015 | 2026-06-12 | none exists (checked 2026-06-12) |
| OpenAI | Why can't I sign up due to "unsupported country"? (help article) | https://help.openai.com/en/articles/8983035-why-can-t-i-sign-up-due-to-unsupported-country | 2026-06-12 | none exists (checked 2026-06-12) |
| Anthropic | Supported countries and regions | https://www.anthropic.com/supported-countries | 2026-06-12 | http://web.archive.org/web/20260612132920/ (Phase 0/V5 pin) |
| Anthropic | Updating restrictions of sales to unsupported regions (ownership rule) | https://www.anthropic.com/news/updating-restrictions-of-sales-to-unsupported-regions | 2026-06-12 | — (2025-09-04 announcement) |
| Google | Gemini API / AI Studio available regions | https://ai.google.dev/gemini-api/docs/available-regions | 2026-06-12 | http://web.archive.org/web/20260612133451/ (Phase 0/V5 pin) |
| Microsoft | Microsoft Customer Agreement FAQ (direct-purchase country table) | https://learn.microsoft.com/en-us/azure/cost-management-billing/microsoft-customer-agreement/microsoft-customer-agreement-faq | 2026-06-12 | http://web.archive.org/web/20260217071931/ |
| Microsoft | Azure account FAQ ("commercially available in 140 countries") | https://azure.microsoft.com/en-us/free/free-account-faq/ | 2026-06-12 | none exists (checked 2026-06-12) |
| Microsoft | What is Microsoft Foundry? (product-name confirmation) | https://learn.microsoft.com/en-us/azure/foundry/what-is-foundry | 2026-06-12 | http://web.archive.org/web/20260530002117/ |
| AWS | AWS Europe (EMEA SARL) countries and territories | https://aws.amazon.com/legal/aws-emea-countries/ | 2026-06-12 | http://web.archive.org/web/20260501060121/ |
| AWS | AWS Contracting Party | https://aws.amazon.com/legal/aws-contracting-party/ | 2026-06-12 | none exists (checked 2026-06-12) |
| AWS | AWS Customer Agreement (trade compliance §11.6) | https://aws.amazon.com/agreement/ | 2026-06-12 | http://web.archive.org/web/20260607140527/ |
| OpenRouter | Terms of Service | https://openrouter.ai/terms | 2026-06-12 | http://web.archive.org/web/20260610031424/ |
| OpenRouter | Privacy Policy | https://openrouter.ai/privacy | 2026-06-12 | none exists (checked 2026-06-12) |
| Mistral | Commercial Terms of Service (§14.13 export/trade controls) | https://legal.mistral.ai/terms/commercial-terms-of-service | 2026-06-12 | none exists (checked 2026-06-12) |
| Mistral | Legal terms index / Usage Policy | https://legal.mistral.ai/terms ; https://legal.mistral.ai/terms/usage-policy | 2026-06-12 | none checked/found |
| Cohere | Terms of Use | https://cohere.com/terms-of-use | 2026-06-12 | http://web.archive.org/web/20260607163926/ |

## Limitations

1. **Two evidence types, not one.** Positive country lists (OpenAI, Anthropic, Google, Microsoft) and ToS exclusion lists (Mistral, Cohere, OpenRouter, AWS) are different kinds of evidence. A ✓ from a positive list means the provider affirmatively names the jurisdiction; a ✓ from an exclusion-list provider only means the terms do not exclude it. An ✗ by list-absence (e.g., Azure–Sudan) is weaker than an ✗ by named exclusion (e.g., Mistral–Iran). The notes distinguish these case by case.
2. **Commercial availability ≠ guaranteed individual signup.** A country's presence on a billing/commercial list does not guarantee that any given individual or entity can complete signup: payment-instrument requirements (non-prepaid cards, SMS-capable phone numbers), entity-level sanctions screening, and Anthropic's >50%-ownership rule all bite below the country level. The converse also holds: ToS-level permission says nothing about local-regulator posture or network-level blocking.
3. **Perishability.** All cells are "as of 2026-06-12." Provider lists change without notice (OpenAI's help articles were updated within the past 10–24 days of access; Microsoft's MCA FAQ was updated 2026-06-11). The archive snapshots pin what was claimed and when; several key pages (Mistral commercial ToS, Azure account FAQ, OpenAI help articles, AWS contracting party, OpenRouter privacy) had **no Wayback snapshot** as of today and should be re-pinned (e.g., via Save Page Now) before publication.
4. **ChatGPT column is indirect.** The dedicated ChatGPT help-center country list could not be machine-captured (JS-rendered, no archive snapshot); the column rests on OpenAI's unified-list language across three official pages (note 2). Low risk, but the consumer list should be eyeballed in a browser before the brief ships.
5. **One inferential step in AWS ✗ cells.** AWS names no excluded countries; the Syria/Iran ✗ applies the OFAC regimes that the AWS Customer Agreement incorporates by reference (note 15). This is standard compliance reading, but it is interpretation, not quotation.
6. **Region availability vs. country availability.** For Azure/Foundry and Bedrock, model availability differs by datacenter region; cells answer only the commercial "can a customer in X buy it" question, not which models are deployable where.

## UNVERIFIED / UNKNOWN cells

| Cell | Status | Why |
|---|---|---|
| AWS Bedrock × Sudan (SD) | UNKNOWN | Absent from the EMEA SARL country list, but the contracting-party catch-all ("any other country → AWS Inc.") means list-absence is not exclusion; no AWS document affirmatively settles Sudanese customer eligibility. |
| OpenRouter × Syria (SY) | UNKNOWN | No platform-level country restrictions in ToS or privacy policy; US-sanctions exposure unaddressed in public terms; upstream model restrictions pass through per-model. |
| OpenRouter × Iran (IR) | UNKNOWN | Same as above. |
| Cohere × Syria (SY) | UNKNOWN | Terms reference U.S. embargoes only in mobile-app (Apple App Store) scope plus a general export-compliance clause; no clause unambiguously bars an API customer located in Syria. |
| Cohere × Iran (IR) | UNKNOWN | Same as above. |
| ChatGPT column (all rows) | verified-indirect | Cells mirror the unified OpenAI list per note 2; the dedicated consumer help-article body could not be captured. Treat as ✓/✗ with a residual capture caveat, not as UNKNOWN. |
| Azure × Sudan (SD) | ✗ with caveat | List-absence from two positive Microsoft lists, but the account FAQ's "including those listed below" wording and worldwide CSP channel leave formal residual ambiguity. Kept as ✗ (consistent with list-absence treatment elsewhere), flagged here for transparency. |
