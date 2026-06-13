# Changelog

All observation dates and data snapshots for the *Importing Intelligence*
research repository. Because the brief's claims are perishable, this file is
the record of *when* each layer was observed — the diachronic frame depends on
snapshot dates being preserved rather than overwritten.

## v1.0 — 2026-06

Initial public release, accompanying policy brief TD-PB-2026-02 v1.0.

- **Availability matrix** — 19 MENA jurisdictions × 9 providers, observed
  2026-06-12. Core country-list pages (OpenAI, Anthropic, Google, Microsoft
  Foundry, AWS, OpenRouter, Cohere) pinned to Wayback captures dated
  2026-06-12 and the days immediately prior.
- **Payment matrix** — 19 jurisdictions, observed 2026-06-12. Processor and
  central-bank sources captured 2026-06-12; six payment-rail pages whose
  captures were rate-limited at research time were recovered from the Wayback
  Machine on 2026-06-13 (see `archive/snapshots.csv`).
- **Token-price milestones** — 32 points spanning 2021–2026, each with its own
  archived pricing-page source.
- **Known capture gaps at release (rechecked 2026-06-13):**
  - *Azure free-account FAQ* — a fresh Wayback capture was successfully
    submitted on 2026-06-13 (Save Page Now returned 200 OK); the new
    timestamp is pending Internet Archive indexing. The prior stale 2024
    capture remains listed until the new one resolves.
  - *PayPal residence-services legal page* — returns HTTP 523 to the Internet
    Archive's crawler (origin CDN refuses archiving); no capture obtainable.
  - *Adyen onboarding docs* — return HTTP 403 to the crawler (archiving
    blocked by the site); no capture obtainable.
  The two un-archivable pages are corroborated by independent sources in the
  matrices' notes (their underlying claims do not rest on the snapshot alone).
  The crawler-refusal status is itself documented here rather than left as a
  silent gap.

Future data refreshes should be added as new dated entries here, preserving
prior figures rather than overwriting them.
