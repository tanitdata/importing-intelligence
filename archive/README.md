# archive/

Frozen evidence for the brief's perishable claims.

## `snapshots.csv`

Manifest of Wayback Machine captures for the web pages the availability and
payment matrices rest on. Columns:

- `wayback_timestamp` — the capture timestamp (YYYYMMDDhhmmss).
- `captured_url` — the original page URL.
- `wayback_full_url` — the resolvable Wayback link; this is what to click to
  see the page as it was on the observation date.
- `cited_in` — which research note(s) in the brief's working set cite this page.
- `note` — capture provenance: research-time pin, recovered later, or a flagged
  gap (stale or missing capture).

These pins are what let a reader in 2027 check that "Yemen appears on OpenAI's,
Google's, and Microsoft's lists but not Anthropic's, as of June 2026" against
the page as it actually read on 2026-06-12, rather than against an edited live
page. Provider country lists and central-bank circulars change without notice;
the brief's own text notes that the Azure status-history page had already
dropped the September 2025 Red Sea incident by the time of writing.

### Known gaps (as of 2026-06-13)

- PayPal residence-services legal page — no Wayback capture.
- Adyen onboarding docs — no Wayback capture.
- Azure free-account FAQ — only a stale 2024 capture resolves.

The underlying claims for these are corroborated by other sources in the
matrices' notes; the missing captures should be re-pinned (Wayback "Save Page
Now") before the Zenodo deposit.

## `incidents-and-physical-layer.md`

Evidence pack for Section 4's physical-stratum claims: the September 2025
Jeddah submarine-cable cuts (SMW4, IMEWE, FALCON GCX), the Azure status notice,
the share-of-traffic figure, and the February 2026 Red Sea shipping-threat
episode.

## `legal-pack.md`

Evidence pack for Section 4's jurisdictional claims: the CLOUD Act
(18 U.S.C. § 2713), OFAC sanctions regimes (Iran ITSR, Syria EO 14312 and
Caesar Act repeal), the suspended AI Diffusion Rule, and the Remote Access
Security Act (H.R. 2683).
