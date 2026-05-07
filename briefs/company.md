# Tech Week Consortium

## Overview

Tech Week Consortium ("TWC") is a Philadelphia-based civic technology
cooperative specializing in public-sector software, civic engagement
platforms, and open-data infrastructure. We design and ship resilient,
accessibility-first systems for cities, transit authorities, school
districts, healthcare networks, and the nonprofits that serve them.

We are member-owned and worker-governed. Every full-time staffer is a
voting member of the cooperative. We publish every non-confidential
deliverable under an open-source license and contribute our reusable
components back to the civic-tech commons.

## Mission

To build durable digital public goods that outlast their funding cycles,
their procurement vehicles, and the political administrations that
commissioned them.

## History

TWC was founded in 2015 by ten organizers of Philadelphia's annual
"Philly Tech Week" festival, who incorporated as a Pennsylvania
worker-owned cooperative to formalize the volunteer civic-tech work
they had been doing on weekends for the City of Philadelphia and
several Greater Philadelphia nonprofits.

Notable milestones:

- **2015** — Incorporated as a worker cooperative; six founding members.
- **2016** — First municipal contract: rebuild of `phila.gov/license-and-inspect`.
- **2017** — Awarded GSA 8(a) BPA for civic technology services.
- **2019** — Expanded to 18 staff; opened satellite office in Camden, NJ.
- **2020** — Pivoted heavily to public-health response work; built
  contact-tracing intake tools for two state health departments and a
  vaccine eligibility lookup used by 4.1M residents.
- **2022** — Hit 30 staff; launched our internal `civitas` framework
  for accessible civic web apps (now MIT-licensed and used by 14
  municipalities outside our client list).
- **2024** — 35 staff; SOC 2 Type II certification across our hosting
  practice; FedRAMP Moderate authorization for our managed-service tier.
- **2025** — Surpassed $9.4M in annual revenue; 100% client renewal
  rate for engagements over six months.

## Core capabilities

### Civic web applications

Public-facing portals, license/permit applications, constituent
service request systems, and benefits-eligibility wizards. Our stack
is intentionally boring: server-rendered HTML, progressive enhancement,
no client-side framework unless the use case demands it. We test against
WCAG 2.2 AA before every deploy and publish a public accessibility
conformance report (ACR) for every shipped application.

### Open data and APIs

ETL pipelines for municipal datasets, public APIs over those datasets,
and developer portals to document them. We have shipped open-data
platforms for three cities and one regional planning commission. Our
opinionated default is to treat the API contract as the product and
the dashboard/portal as a thin viewer over it — so downstream civic
hackers, journalists, and academic researchers always have an
unmediated path to the data.

### Data engineering

Lakehouse architectures (typically Iceberg + Spark), dbt-based
transformation pipelines, and BI delivery via Metabase or Superset.
We have particular depth in healthcare data (HIPAA-compliant
warehouses for two regional payers), transit (GTFS-RT pipelines for
two transit authorities), and educational outcomes (SLDS-style
warehouses for two state education agencies).

### Community engagement and participatory design

Co-design workshops, accessibility user-testing with disabled users,
and Spanish-/Mandarin-/Vietnamese-language community feedback rounds.
Our engagement designs are reviewed and signed off by community
members before any code is written. We have run 47 such engagements
since 2017.

### Procurement and program advisory

Pre-RFP advisory work for public agencies — helping them scope, slice,
and structure technology procurements so they attract a competitive
bidder pool and avoid lock-in. We do not bid on procurements we have
advised on within the prior 24 months.

## Selected past engagements

### City of Philadelphia — Department of Licenses and Inspections (2016–present)

Rebuild of the public-facing licensing and inspections portal serving
~85,000 active business and trade licenses. Migrated from a legacy
ColdFusion/Oracle stack to a Django/PostgreSQL deployment with public
APIs. Reduced average license-renewal completion time from 19 minutes
to 4. Continuous engagement; current contract runs through 2027.

### NJ Transit — Real-Time Bus Arrivals Refactor (2019–2021)

Replaced an aging vendor system with an in-house GTFS-RT pipeline
feeding a public API and the official rider-facing app. 99.97% uptime
across the engagement. Open-sourced our `gtfs-rt-validator` tool which
is now used by 22 transit agencies in North America.

### Pennsylvania Department of Health — COVID-19 Vaccine Eligibility (2021)

Six-week sprint to deploy a multilingual eligibility-lookup tool,
later extended to a full appointment-booking system. Served 4.1M
unique users at peak. Designed for low-bandwidth and screen-reader
use; 0 critical accessibility findings on independent audit.

### Greater Philadelphia Health Information Network — Lakehouse Migration (2022–2024)

Migration of a 47TB on-prem Teradata warehouse to a HIPAA-compliant
Iceberg lakehouse on AWS. Zero patient-data downtime. BI tooling
preserved via Trino + Superset. Reduced annual infrastructure spend by
$1.1M.

### School District of Philadelphia — Family Communications Platform (2023)

Replaced four overlapping vendor tools with a unified family
communications platform supporting SMS, email, voice, and in-app
messages in 11 languages. Sub-200ms broadcast latency to 200K
recipients. WCAG 2.2 AA conformant.

### Camden County, NJ — Open Data Platform (2024)

Greenfield open-data portal exposing 80+ datasets via a public API
and CKAN-style catalog. Co-designed with three local journalism
nonprofits and the county's data-literacy program in the public
libraries.

## Team

35 staff as of January 2026:

- 3 partners / co-leads (technology, design, operations)
- 11 software engineers (full-stack, data, infra)
- 5 designers (product, accessibility, research)
- 4 data engineers / analytics engineers
- 3 community engagement leads
- 3 program managers
- 2 procurement / proposal specialists
- 4 part-time advisors (former municipal CIOs, public-health informatics, civil rights law)

Average tenure: 4.7 years. Voluntary turnover (excluding retirements):
6% over the last three years.

## How we work

- **Time-and-materials with a soft cap.** We prefer T&M billing with a
  not-to-exceed cap renegotiated quarterly. We do fixed-price when
  required by procurement vehicle and have shipped on fixed-price for
  more than 80% of those engagements without change orders.
- **Two-week iterations, public roadmaps.** Every engagement publishes
  a roadmap to a client-accessible board. Public-sector clients are
  encouraged to publish those roadmaps externally; we provide the
  templates.
- **Open by default.** All non-PII deliverables are released under MIT
  or Apache-2.0 unless the client's procurement explicitly forbids.
- **Accessibility-first.** Every shipped UI passes WCAG 2.2 AA before
  deploy. We publish ACRs publicly.
- **No "innovation theater."** We use boring, well-supported
  technology stacks. We will not propose generative AI features unless
  the use case has been validated with end users and the failure modes
  have been mapped.
- **Co-op profit share with municipalities.** When an engagement
  yields ongoing licensing revenue (rare; usually managed-services
  retainers), we share 10% of that revenue back to the municipality's
  general fund or a designated public-benefit recipient.

## Values

- **Durability over novelty.** We choose technologies our successors
  can maintain.
- **Boring is a feature.** We do not introduce dependencies for which
  we cannot identify a 10-year support story.
- **Public money, public code.** Anything paid for with tax dollars
  should be inspectable by the taxpayers.
- **Disability is a design constraint, not an afterthought.**
- **Procurement reform is part of the work.** We share what we learn
  about contracting back with the public-procurement community.

## Differentiators

1. **Worker-cooperative governance.** No private equity, no
   acquisition pressure, no growth-at-all-costs incentives. We turn
   down work that does not fit the cooperative's mission.
2. **100% client renewal rate** for engagements over six months
   (12-quarter rolling).
3. **No subcontracting layer.** Every line of code on every project is
   written by a TWC member.
4. **Open-source first.** 31 of our 47 production deliverables since
   2017 are publicly available on GitHub.
5. **Accessibility audit included.** Every engagement budget includes
   a third-party accessibility audit by a certified vendor before
   final delivery; we do not invoice for the audit cost.
6. **Local presence.** Headquartered three blocks from City Hall;
   Camden satellite office is on the PATCO line. We attend client
   working sessions in person.

## Certifications and registrations

- Pennsylvania-incorporated worker cooperative (since 2015)
- SAM.gov Unique Entity ID: ABCD-1234-EFGH (active)
- GSA Schedule 70 / 8(a) BPA (active)
- SOC 2 Type II (annual)
- FedRAMP Moderate (managed-services tier, sponsored by NJ DOH)
- Pennsylvania Small Diverse Business (SDB) — verified
- City of Philadelphia M/W/DSBE — verified

## Contact

- **Proposal lead:** R. Park, Procurement Specialist
- **Email:** proposals@techweekconsortium.coop
- **Phone:** 215-555-0119
- **Address:** 1234 Market Street, Suite 800, Philadelphia, PA 19107
