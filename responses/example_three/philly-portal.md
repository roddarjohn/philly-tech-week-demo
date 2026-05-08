# Tech Week Consortium — Proposal for Special Event Permitting Software Solution
**City of Philadelphia, OCRSE | Project Intake #1140**
*Submitted by Tech Week Consortium ("TWC") | 1234 Market Street, Suite 800, Philadelphia, PA 19107 | proposals@techweekconsortium.coop | 215-555-0119*

---

## Who We Are

Tech Week Consortium is a Philadelphia-headquartered worker cooperative with a decade of municipal technology delivery for the City of Philadelphia and peer public agencies. We are a verified City of Philadelphia M/W/DSBE, a Pennsylvania Small Diverse Business, and a GSA 8(a) BPA holder. Our 35-member staff—all worker-owners—operate three blocks from City Hall with a Camden, NJ satellite office. We carry no private-equity obligations and turn down work that conflicts with our public-benefit mission. Our 100% client renewal rate over 12 rolling quarters and our active engagement with the City's Department of Licenses & Inspections (2016–present) demonstrate the sustained, trust-based partnerships we build with Philadelphia government.

---

## Our Solution

TWC proposes **CivitasPermit**, a purpose-built special-event permitting platform derived from our production-tested `civitas` framework (MIT-licensed, deployed by 14 municipalities). The system will be installed on existing City infrastructure per technical requirements and will serve OCRSE and all coordinating departments through a single, centrally managed deployment.

**Core functionality delivered on Day 1:**

| RFP Requirement | TWC Delivery |
|---|---|
| Multi-permit hosting & permit generation (A.1.1–A.1.2) | Configurable permit templates; PDF/digital issuance from within platform |
| Conditional logic workflows & service request creation (A.1.3, A.1.5) | Visual rule engine; auto-generated task queues per applicant inputs |
| Post-submission editing & document upload (A.1.4) | Role-gated amendment workflow with full audit trail |
| Real-time status tracking (A.1.6) | Live applicant portal and City personnel dashboard |
| External messaging & internal collaboration (A.1.7–A.1.8) | Threaded message history with retention; cross-department task assignment |
| Centralized dashboards & calendar views (A.1.9) | Configurable views per role; exportable event calendar |
| Third-party integrations—billing, GIS, licensing, SSO (A.1.10) | REST/webhook API layer; pre-built connectors for City payment and GIS systems |
| Invoice management (A.1.11) | Automated invoice generation tied to permit workflow stages |
| Multi-user roles & permissions (A.1.12) | Granular RBAC configurable by City administrators without vendor involvement |

**Architecture:** Three-tier deployment (presentation / application / data) on City-owned infrastructure. PostgreSQL data layer; Django application tier; server-rendered HTML front end with progressive enhancement. We will deliver a full architecture diagram, documented DR plan with defined RTO/RPO, and performance benchmarks (disk I/O, TPM, response time, throughput, MTTF/MTTR, bandwidth) calibrated to the City's existing environment in the Volume 2 Technical Proposal. Any required infrastructure upgrades will be identified in a pre-deployment assessment with full specifications and cost estimates.

**Accessibility:** Every UI passes WCAG 2.2 AA (exceeding the RFP's WCAG 2.1 AA floor) before deployment. A third-party Accessibility Conformance Report is included in the engagement budget at no additional City cost.

**Security & compliance:** SOC 2 Type II certified; FedRAMP Moderate authorized. All data handling aligns with City standards per Appendix K—access controls, metadata, geospatial formats, retention schedules, and 24-hour breach notification. Source code for all custom components will be delivered to the City with full ownership rights; proprietary components will be escrowed at TWC's expense and updated with every release.

---

## Addressing the Timeline Risk

We recognize that the anticipated May 15, 2026 start coincides with the FIFA World Cup and MLB All-Star Game surge. Our mitigation is straightforward: we will deliver a production-ready core permitting workflow within **60 days of contract execution**, prioritizing the highest-volume permit types, with remaining configuration and integrations completed in a phased rollout. This approach is consistent with our two-week iteration cadence and has been validated on comparable high-stakes deployments (PA DOH vaccine eligibility: 4.1M users served within six weeks of launch).

---

## Training & Ongoing Support

We will deliver a structured training program covering system navigation, application processing, reporting, and troubleshooting—targeting all City personnel roles. Deliverables include role-based user manuals, recorded video tutorials, and a searchable FAQ portal. The training plan submitted in Volume 2 will specify format, schedule, audience groups, and City responsibilities.

**Maintenance & Warranty:** TWC serves as sole point of contact for all support and warranty obligations. We propose a **2-year warranty** (Year 1 included in fixed price; Year 2 priced as a separate line item) and a **5-year maintenance term** (Years 2–5 priced separately by year in the cost proposal per Appendix C). Severity classifications, response times, fix times, and escalation procedures will be fully documented. Material defects will be addressed within 48 hours of notice. Support availability is guaranteed for a minimum of 5 years from final acceptance.

---

## Cost & Compliance

Our proposal is submitted as a **fixed-price, line-item cost structure** using the Appendix C template, inclusive of implementation, integrations, training, Year 1 warranty, and Year 1 maintenance. Years 2–5 maintenance and Years 2+ warranty extensions are priced as separate line items. We carry all required insurance coverages: General Liability ($1M/$2M), Professional Liability ($1M E&O), Cyber Liability ($1M), Workers' Compensation (statutory), and Auto ($1M). Tax Clearance (Appendix H), Requirements Compliance Matrix (Appendix D), campaign contribution disclosures (Ch. 17-1400), demographic disclosure, and all other Appendix requirements will be submitted in full via eContract Philly. This proposal was prepared with human authorship and reviewed by TWC members; any AI-assisted drafting assistance has been reviewed and certified per RFP requirements. This proposal is binding for 180 days from submission.

---

*Contact: R. Park, Procurement Specialist — proposals@techweekconsortium.coop — 215-555-0119*