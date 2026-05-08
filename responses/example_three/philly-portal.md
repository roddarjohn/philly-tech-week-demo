# Tech Week Consortium — Proposal for City of Philadelphia Special Event Permitting Software Solution
**Project Intake #1140 | Submitted by Tech Week Consortium | March 17, 2026**

---

## Executive Summary

Tech Week Consortium (TWC) is a Philadelphia-based, worker-owned civic technology cooperative with a decade of continuous delivery for the City of Philadelphia and its regional partners. We propose **EventPath**, a configurable, open-source-first special event permitting platform purpose-built to manage the City's ~1,700 annual applications—with surge capacity engineered for the 2026 MLB All-Star Game and FIFA World Cup. This is a fixed-price, turnkey engagement. Every line of code is written by a TWC member; no subcontracting layer exists.

---

## Solution Overview

EventPath is a **COTS-configurable platform** deployed on the City's existing infrastructure. Its modular architecture supports all twelve mandatory functional requirements simultaneously:

| Requirement | EventPath Capability |
|---|---|
| Multi-application hosting (A.1.1) | Concurrent permit-type registry; unlimited application schemas |
| Permit generation & distribution (A.1.2) | Templated PDF/digital permit issuance with audit trail |
| Service request creation (A.1.3) | Applicant-input-triggered task generation routed to City departments |
| Post-submission editing & upload (A.1.4) | Version-controlled document amendments with configurable approval gates |
| Conditional logic workflows (A.1.5) | No-code rule engine for dynamic field visibility, routing, and documentation requirements |
| Real-time status tracking (A.1.6) | Applicant and staff dashboards with event-driven status push notifications |
| External communication (A.1.7) | Threaded messaging portal with full history retained per application record |
| Internal collaboration (A.1.8) | Interdepartmental comment threads, @mentions, and assignment queues |
| Centralized dashboards & calendars (A.1.9) | Unified OCRSE operations calendar; per-staff and citywide views |
| Third-party integrations (A.1.10) | REST APIs, SSO (SAML 2.0), webhooks, and scheduled file exchange for payment, GIS, and licensing systems |
| Invoice management (A.1.11) | Automated invoice generation, fee-schedule configuration, and payment-status reconciliation |
| Multi-user access & permissions (A.1.12) | Role-based access control with configurable permission tiers per department |

**Scalability for 2026 surge:** EventPath is load-tested to 5× baseline concurrency. We will document tested throughput, response times, and concurrent-user capacity against the City's existing hardware environment and clearly itemize any recommended (but separately procured) network or equipment upgrades with full specifications and cost estimates—at no additional charge to this contract.

**Integrations:** EventPath ships with pre-built connectors for Philadelphia's billing, GIS, and business licensing systems, leveraging TWC's existing integration work on the L&I portal (active contract through 2027).

---

## Technical & Compliance Standards

- **WCAG 2.1 AA (and 2.2 AA):** Every delivered UI passes automated and manual accessibility testing before deployment. A third-party certified accessibility audit is included in our fixed price; we publish a public Accessibility Conformance Report at launch.
- **City IT Standards (Appendix K):** Full compliance with data, addressing, general technical, digital, and security standards. Security architecture addresses Confidentiality, Integrity, and Availability of all City data.
- **SOC 2 Type II:** TWC holds an active SOC 2 Type II certification (annual); we will provide audit reports to the City and cooperate with any City-requested SSAE 18 SOC 2 Type II review.
- **Data breach notification:** TWC's incident response policy mandates notification within **24 hours** of discovery—meeting the City's contractual requirement.
- **Source code escrow:** As a proprietary-COTS hybrid, EventPath's source code will be deposited into an escrow arrangement satisfactory to the City at no cost, with regular updates maintained throughout the contract term.
- **AI disclosure:** No generative AI features are proposed. Any AI-assisted proposal content has been reviewed, verified, and certified by TWC subject-matter experts.

---

## Implementation Plan

| Phase | Milestone | Timeline |
|---|---|---|
| 1 — Discovery & Configuration | Requirements validation, workflow mapping, City environment assessment | Weeks 1–6 |
| 2 — Build & Integration | Platform configuration, API integrations, data migration | Weeks 7–16 |
| 3 — Testing & Accessibility Audit | UAT with OCRSE staff, third-party accessibility audit, performance benchmarking | Weeks 17–20 |
| 4 — Training & Pilot | Staff training delivery, parallel-run pilot with live applications | Weeks 21–24 |
| 5 — Go-Live & Reliability Period | Full production launch, 30-day reliability period, Final Acceptance | Weeks 25–28 |

**Target go-live:** Ahead of 2026 event season. Phased deployment prioritizes OCRSE's highest-volume permit types first, ensuring operational readiness before FIFA and MLB All-Star surge windows.

---

## Training & Support

**Training program (Appendix A.2):** TWC will deliver role-differentiated training covering system navigation, application processing, report generation, and troubleshooting across three audience groups: OCRSE administrators, City department reviewers, and help-desk staff. Formats include live instructor-led sessions (virtual and in-person at City Hall), recorded video tutorials, user manuals, and an FAQ knowledge base. A detailed training plan—including schedule, format, audience assignments, and City responsibilities—will be delivered in Week 3.

**Maintenance & support:**
- **Year 1:** Included in fixed price. Severity-classified response SLAs with best-efforts resolution within **48 hours** for all defects.
- **Years 2–5:** Priced as separate fixed-price line items in our cost proposal.
- **5-year availability:** TWC contractually guarantees platform availability and support for a minimum of five years from Final Acceptance.
- **Single point of contact:** One named TWC engagement lead holds accountability for the full turnkey scope.
- **Escalation procedures:** Documented severity tiers (P1–P4) with defined response, escalation, and fix-time targets provided in the full technical proposal.

**Warranty:** 1-year warranty included in fixed price; Years 2–3 warranty priced as optional line items. Coverage extends to all software, design, implementation, and integration deliverables on a turnkey basis.

---

## Commercial Terms

- **Pricing:** Fixed price only. Full line-item cost breakdown provided for all software, configuration, implementation, integration, training, and maintenance (Years 1–5). No time-and-materials or cost-plus elements.
- **Tax status:** City's exemption from sales, use, and federal excise taxes is reflected in all pricing.
- **Retainage:** TWC acknowledges the 20% retainage requirement and has cash-flow plans in place accordingly.
- **Bonds & insurance:** TWC will provide all required performance, labor and materialmen's, and fidelity bonds. Insurance coverages meet or exceed all City minimums, including **$1M Cyber Liability** (City named as additional insured) and **$1M Professional Liability E&O** with 2-year tail coverage.
- **Proposals binding:** This proposal remains binding for 180 days from the March 17, 2026 submission date.

---

## Qualifications & Local Impact

TWC has delivered production software to the City of Philadelphia continuously since 2016. Our current L&I portal engagement gives us direct, working knowledge of the City's infrastructure, procurement environment, and interdepartmental coordination patterns—materially reducing discovery risk and integration effort for this project.

**Relevant experience highlights:**

- **City of Philadelphia L&I Portal (2016–present):** ~85,000 active licenses; Django/PostgreSQL; public APIs; 4-minute average completion time (down from 19). Direct analog to EventPath's permitting architecture.
- **PA Dept. of Health — COVID Vaccine Eligibility (2021):** 4.1M users at peak; surge-capacity design; 0 critical accessibility findings on independent audit.
- **School District of Philadelphia — Family Communications Platform (2023):** Sub-200ms broadcast latency to 200K recipients; WCAG 2.2 AA; 11-language support.
- **Camden County Open Data Platform (2024):** Co-designed with community partners; 80+ datasets; public API.

**Technical qualifications:** TWC staff hold demonstrated experience across large-scale distributed database design, WAN/LAN integration, software design and testing, help desk operations, large-scale project management, high-availability/mission-critical systems, municipal information systems, and transition management—meeting the City's preferred 5-year experience threshold across all listed domains.

**Local Business Entity:** TWC is headquartered at 1234 Market Street—three blocks from City Hall. We are a verified City of Philadelphia M/W/DSBE and Pennsylvania Small Diverse Business. All work is performed by Philadelphia-based TWC members; no out-of-region subcontractors.

**Financial stability:** TWC surpassed $9.4M in annual revenue in 2025 with a 100% client renewal rate for engagements over six months. Three years of audited financial statements, bank reference, bonding capacity documentation, and all required Appendix H forms are included in Volume 1.

---

## Compliance Checklist

| Requirement | Status |
|---|---|
| eContract Philly registration | ✅ Registered; TIN/name verified |
| Appendix D Requirements Compliance Matrix | ✅ Completed in full |
| Fixed-price proposal | ✅ No T&M or cost-plus elements |
| Campaign contribution disclosure (Ch. 17-1400) | ✅ Completed; contribution history reviewed |
| Equal Benefits Ordinance (Ch. 17-1900) | ✅ Compliant |
| Demographic data disclosure | ✅ Submitted |
| LGBTQ Applicant Opportunity Data (Appendix M) | ✅ Voluntarily disclosed |
| Appendix H Tax & Regulatory Clearance | ✅ Included |
| AI use disclosure / human review certification | ✅ Certified |
| Years 2–5 maintenance line items | ✅ Included in cost proposal |

---

*Contact: R. Park, Procurement Specialist | proposals@techweekconsortium.coop | 215-555-0119 | 1234 Market Street, Suite 800, Philadelphia, PA 19107*