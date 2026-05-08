# Tech Week Consortium — Proposal: City of Philadelphia Special Event Permitting Software Solution
**Project Intake #1140 | Submitted via eContract Philly | March 17, 2026**
*Prepared by R. Park, Procurement Specialist | proposals@techweekconsortium.coop | 215-555-0119*

---

## Who We Are

Tech Week Consortium (TWC) is a Philadelphia-based, worker-owned civic technology cooperative founded three blocks from City Hall in 2015 — by the same organizers who built Philly Tech Week into a civic institution. We have held a continuous contract with the City's Department of Licenses and Inspections since 2016, reducing license-renewal completion time from 19 minutes to 4 minutes across ~85,000 active accounts. We carry SOC 2 Type II certification, FedRAMP Moderate authorization, Pennsylvania Small Diverse Business (SDB) verification, and City of Philadelphia M/W/DSBE certification. Our 35 member-staff average 4.7 years of tenure; voluntary turnover over three years is 6%. We have never used a subcontracting layer — every line of code is written by a TWC member, and the City will have a single point of contact for every obligation under this contract.

---

## Proposed Solution

We will configure and deploy **CivitasPermit**, our MIT-licensed, production-proven permitting platform, on the City's existing infrastructure. CivitasPermit is a COTS-configurable system — not custom-only — built on our open-source `civitas` framework, currently in production use by 14 municipalities. It is not an experimental product; it ships on boring, well-supported technology (Django, PostgreSQL, server-rendered HTML with progressive enhancement) that City staff and successor vendors can maintain without vendor lock-in.

| Requirement | How We Meet It |
|---|---|
| **A.1.1 – Multi-application hosting** | Unlimited concurrent permit types; event-type templates configurable by City staff without code changes |
| **A.1.2 – Permit generation & distribution** | PDF/digital permit issuance baked into core; bulk and individual distribution supported |
| **A.1.3 – Service request creation** | Applicant inputs trigger automated task generation routed to designated City units |
| **A.1.4 – Post-submission editing & document upload** | Workflow-gated editing and document upload; audit trail preserved on every revision |
| **A.1.5 – Conditional logic workflows** | Visual workflow builder with field-level conditional logic; no-code configuration for City administrators |
| **A.1.6 – Real-time status tracking** | Live status dashboard for applicants and staff; webhook-driven status push available |
| **A.1.7 – External communication** | Threaded applicant–City messaging with full message history retained and exportable |
| **A.1.8 – Internal collaboration** | Interdepartmental task threads, @-mentions, and shared review queues |
| **A.1.9 – Centralized dashboards & calendars** | Unified event calendar and application pipeline view; configurable per role |
| **A.1.10 – Third-party integrations** | REST API, SSO (SAML 2.0/OIDC), webhooks, and file-exchange connectors for City GIS, payment, and business licensing systems; integration scope confirmed during kick-off discovery |
| **A.1.11 – Invoice management** | Invoice generation, line-item customization, and payment-status tracking built in |
| **A.1.12 – Multi-user access & permissions** | Role-based access control with configurable permission tiers; unlimited user profiles |
| **WCAG 2.1 AA** | We test against WCAG 2.2 AA (superset of 2.1 AA) before every deploy and publish a public ACR; a third-party accessibility audit by a certified vendor is included in our fixed price at no additional charge to the City |
| **Security & data standards** | SOC 2 Type II controls; 24-hour breach notification; forensic response included; data formatted to City master-data, metadata, date, geospatial, and addressing standards |
| **System architecture** | Three-tier deployment (presentation / application / data); workflow engine on application tier; reporting and archiving infrastructure documented in our Architecture Specification deliverable |
| **Disaster recovery** | Written DR plan delivered at project kickoff; tested recovery procedure with documented RTO/RPO targets |
| **Source code** | CivitasPermit is MIT-licensed; the City receives full source code ownership of all City-specific configuration and customization. No escrow complexity — the code is already public |
| **Performance standards** | We will document throughput, processing volumes, and response-time benchmarks against the City's current environment during a pre-deployment load assessment; any required infrastructure upgrades will be identified in writing within 30 days of project start so the City can procure separately without schedule impact |
| **Scalability for 2026 event surge** | CivitasPermit's stateless application tier scales horizontally; our vaccine-eligibility platform served 4.1M users at peak with zero downtime. We will conduct surge-capacity testing simulating FIFA World Cup and MLB All-Star Game permit volumes before go-live |

---

## Implementation Plan

**Phase 1 — Discovery & Configuration (Weeks 1–4):** Kick-off, stakeholder mapping across City departments, integration scoping with GIS/payment/licensing teams, infrastructure assessment, and workflow design workshops. Deliverables: Architecture Specification, Integration Scope Document, DR Plan, Performance Benchmark Baseline.

**Phase 2 — Build & Integration (Weeks 5–10):** Workflow configuration, third-party integrations, role and permission setup, data migration from existing PDF-based process, and internal QA including accessibility audit.

**Phase 3 — User Acceptance & Reliability Period (Weeks 11–14):** City staff UAT, defect resolution (material defects corrected within 48 hours of notice), third-party accessibility audit, and the required 30-consecutive-day reliability period. Any defect that resets the clock is corrected at TWC's expense with no schedule-day billing.

**Phase 4 — Training & Go-Live (Weeks 13–16, overlapping):** Role-segmented training sessions (City administrators, departmental reviewers, public-facing staff); delivery of user manuals, recorded video tutorials, and a searchable FAQ library. Training plan specifying format, schedule, audience groups, scope, assumptions, and City responsibilities delivered at end of Phase 1.

**Milestone Payment Schedule:** Tied to Phase completion and City sign-off, structured to account for the City's 20% retainage policy; cash-flow assumptions disclosed in full in Volume 2.

---

## Maintenance, Support & Warranty

TWC will serve as the sole point of contact — no subcontractor layer, no escalation to a third party. We commit to:

- **Warranty:** 2 years post-Final Acceptance included in fixed price; Years 3–5 priced as optional line items in Volume 2
- **Maintenance & support:** 1 year included; Years 2–5 priced separately with monthly and annual options
- **Response:** Best-efforts correction within 48 hours of notice; severity classifications (Critical / High / Medium / Low), response times, fix times, and escalation procedures detailed in our Support Plan deliverable
- **System availability:** Guaranteed minimum 5 years from Final Acceptance
- **Key personnel:** Any substitution requires City approval; TWC's 6% voluntary turnover rate and cooperative governance structure make mid-project departures rare

---

## Pricing & Administrative Compliance

Our fixed-price proposal with mandatory line-item breakdown is submitted in Volume 2 covering: base system software, optional add-ons, implementation professional services, training professional services, documentation, software maintenance agreement (Years 1–5, monthly and annual), third-party accessibility audit, and all assumptions stated explicitly. No time-and-materials components.

TWC is in full compliance with all administrative requirements: City of Philadelphia Tax and Regulatory Clearance (current), Chapter 17-1400 campaign contribution disclosures (no disqualifying contributions), Equal Benefits Ordinance (Chapter 17-1900, applicable as member-cooperative with equivalent domestic-partner benefits policy), demographic data transparency disclosures, and required insurance coverage (Workers' Comp; General Liability $1M/$2M; Auto $1M; Professional Liability $1M; Cyber Liability $1M). This proposal was drafted with staff assistance from AI writing tools; all content has been reviewed, verified, and approved by a TWC subject-matter expert, and TWC warrants lawful ownership of all proposal content. Our proposal remains binding for 180 days from the submission date.

As a **Philadelphia-headquartered Local Business Entity** (1234 Market Street, Suite 800, Philadelphia, PA 19107) and a certified Pennsylvania Small Diverse Business and City M/W/DSBE vendor, TWC meets the Local Business/Local Impact criteria identified as a significant evaluation factor under Section 3.5.

---

*TWC's 100% client renewal rate for engagements over six months, decade-long relationship with the City of Philadelphia, open-source deliverables, and cooperative governance — with no acquisition pressure and no growth-at-all-costs incentives — make us the partner best positioned to deliver a permitting system that will serve Philadelphia residents durably, accessibly, and transparently well beyond the 2026 event season.*