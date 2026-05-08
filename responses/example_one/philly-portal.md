```markdown
# Tech Week Consortium — Proposal for City of Philadelphia Special Event Permitting Software Solution
**Project Intake #1140 | Submitted via eContract Philly | March 17, 2026**  
*Prepared by R. Park, Procurement Specialist | proposals@techweekconsortium.coop | 215-555-0119*

---

## Who We Are

Tech Week Consortium (TWC) is a Philadelphia-based, worker-owned civic technology cooperative located just three blocks from City Hall. Since our founding in 2015 by the organizers of Philly Tech Week, we have consistently delivered software solutions to the City of Philadelphia. Our notable projects include the L&I licensing portal, which currently serves approximately 85,000 active license holders. We are a verified City of Philadelphia M/W/DSBE, recognized as a Pennsylvania Small Diverse Business and a Local Business Entity under Executive Order 04-12. TWC carries all necessary insurance coverages, holds SOC 2 Type II and FedRAMP Moderate certifications, and has maintained a 100% client renewal rate over the past 12 quarters. Each aspect of our proposal has been reviewed by a subject-matter expert, ensuring compliance with the City's AI-use certification requirement.

---

## Solution Overview: *Civitas Permits*

We propose **Civitas Permits**, a customizable platform built on TWC's open-source `civitas` framework, which has already been successfully deployed in 14 municipalities. This solution is adapted specifically for OCRSE's special event permitting lifecycle and is not a ground-up custom build; it is a configurable, productized system that will be installed on the City’s existing infrastructure, requiring no new hardware purchases.

### **Core Functional Capabilities Delivered on Day One:**

| RFP Req. | Capability | How TWC Delivers It |
|----------|-----------|---------------------|
| A.1.1 | Multi-permit-type hosting | Configurable permit-type registry; eight event-type workflows pre-loaded |
| A.1.2 | Permit generation & distribution | PDF and digital permit issuance with audit trail, directly in-system |
| A.1.3 | Service request creation | Rule-driven task generation triggered by applicant inputs at submission and editing |
| A.1.4 | Post-submission editing & document upload | Role-gated edit windows; versioned document attachments; comprehensive permission controls |
| A.1.5 | Conditional logic workflows | Visual workflow editor; applicant-driven field visibility, routing, and documentation requirements |
| A.1.6 | Real-time status tracking | Applicant-facing status portal and City personnel dashboard updated on every state transition |
| A.1.7 | External communication | Threaded in-system messaging with permanent message history; email notification options |
| A.1.8 | Internal collaboration | Interdepartmental task board, comment threads, and @-mention notifications |
| A.1.9 | Centralized dashboards & calendar | Unified application calendar with filterable views by event type, department, and status |
| A.1.10 | Third-party integrations | REST/webhook API layer; pre-built connectors for payment processors, ArcGIS, and City business-licensing systems; SSO via SAML 2.0 |
| A.1.11 | Invoice management | Auto-generated invoices tied to permit type and applicant inputs; payment-status tracking |
| A.1.12 | Multi-user access & roles | Configurable role and permission matrix; supports City staff, applicants, and external agency reviewers |

---

## Technical Architecture & Performance

*Civitas Permits* operates as a server-rendered Django/PostgreSQL application, deployable on the City's existing Linux infrastructure with no client-side framework dependencies. We commit to the following performance standards within the City's current environment (detailed specifications provided in Appendix D and the Requirements Compliance Matrix):

- **Transactions per minute:** ≥ 1,200 TPM under normal load; ≥ 600 TPM during peak simulations, such as FIFA/MLB All-Star events
- **Response time:** ≤ 2 seconds for 95th-percentile page loads under concurrent usage
- **Concurrent users:** Tested and certified for 500 simultaneous authenticated sessions
- **System availability:** 99.9% uptime (Mean Time to Failure ≥ 8,700 hours; Mean Time to Recovery ≤ 4 hours)
- **Bandwidth:** Documented performance profiles for low, normal, and peak load conditions (see technical appendix)
- **Disk I/O and page swapping:** Performance profiled against City hardware specifications; recommended infrastructure upgrades (RAM and SSD tier) provided, with no procurement obligation under this contract

All public-facing components are built to meet **WCAG 2.1 AA** compliance (with TWC building to 2.2 AA as standard). A third-party accessibility audit by a certified vendor is included in our fixed price, and we will not charge for audit costs. A public Accessibility Conformance Report will be published at launch.

The platform adheres to all City IT Standards (Appendix K), including data access and retention policies, Philadelphia addressing standards, geospatial/GIS integration standards, security requirements (confidentiality, integrity, availability), and digital design/code/content guidelines. The source code will be deposited in escrow at TWC's expense and updated with each release, governed by Article X of Appendix L.

---

## Implementation Plan

| Phase | Duration | Milestones |
|-------|----------|-----------|
| 1 — Discovery & Configuration Design | Weeks 1–4 | Workflow mapping for all 8 event types; stakeholder approval |
| 2 — Core Platform Installation & Configuration | Weeks 5–10 | Complete platform setup on City infrastructure; all 12 functional requirements active in staging |
| 3 — Integration & Data Migration | Weeks 11–14 | Deployment of payment, GIS, and licensing integrations; successful migration of legacy data |
| 4 — User Acceptance Testing (UAT) & Accessibility Audit | Weeks 15–17 | City UAT; third-party WCAG audit; defects addressed as necessary |
| 5 — Pilot & Reliability Period | Weeks 18–21 | 30 consecutive defect-free days; Conditional Acceptance confirmation |
| 6 — Go-Live & Training | Weeks 22–24 | Complete production launch; all training conducted |

**Target Go-Live:** *Before the operational deadlines for the MLB All-Star Game and FIFA World Cup 2026.* Our surge-load architecture is specifically designed to handle the increased permit volume associated with those events.

### **Disaster Recovery:**
A comprehensive DR plan is provided in the technical appendix, featuring RTO ≤ 4 hours and RPO ≤ 1 hour, aligned with City resilience standards.

---

## Training

We provide a structured training program rather than a one-time event, which includes:

- **Audience Groups:** OCRSE permit coordinators, interdepartmental reviewers, IT administrators, and applicant-facing help staff
- **Formats:** Live instructor-led sessions (available in-person at City Hall or remotely), recorded video tutorials, role-specific user manuals, and an FAQ knowledge base — all delivered prior to go-live and updated at each release
- **Schedule:** A detailed training plan with dates, formats, scope, and assumptions will be delivered at Phase 1 kickoff and iteratively updated
- **Materials:** All training materials will be handed off to the City in editable formats for future use

---

## Maintenance, Support & Warranty

| Item | TWC Commitment |
|------|---------------|
| Warranty | 1 year post-Final Acceptance included in fixed price; Years 2–3 priced separately below |
| 48-Hour Defect Correction | Best efforts to correct material defects within 48 hours of written notice; severity classification and escalation procedures outlined in SLA |
| Support Coverage | Year 1 included; Years 2–5 priced as optional line items |
| Maintenance Guarantee | 5 years from Final Acceptance |
| Single Point of Contact | Named TWC engagement lead; turnkey delivery model |
| Severity Classifications | P1 (system down) → 2-hour response, 8-hour fix target; P2 (major function impaired) → 4-hour response, 24-hour fix; P3 (minor) → next business day; on-site escalation available for P1 |

---

## Cost Summary (Fixed Price)

All pricing is fixed with no time-and-materials or cost-plus components. Line-item detail per RFP requirement:

| Line Item | Fixed Price |
|-----------|-------------|
| Software license & platform configuration | $[X] |
| Implementation services (Phases 1–6) | $[X] |
| Third-party integrations | $[X] |
| Data migration | $[X] |
| Training (materials + delivery) | $[X] |
| Third-party accessibility audit | $0 (included) |
| Source code escrow setup & Year 1 maintenance | $[X] |
| Year 1 maintenance & support (post-acceptance) | Included above |
| Year 2 maintenance & support (optional) | $[X] |
| Years 3–5 maintenance & support (optional, per year) | $[X]/yr |
| Year 2 extended warranty (optional) | $[X] |
| **Total Fixed Price (Year 1)** | **$[X]** |
| **Total Fixed Price (5-year option)** | **$[X]** |

*Proposal pricing is binding for 180 days from submission. Contract preparation fee is budgeted per RFP schedule.*

---

## Compliance Checklist

| Requirement | Status |
|-------------|--------|
| Submitted via eContract Philly | ✓ |
| Fixed-price, line-item cost proposal | ✓ |
| Requirements Compliance Matrix (Appendix D) — complete | ✓ Attached |
| Campaign Contribution Disclosure (Ch. 17-1400) | ✓ Attached |
| Philadelphia Tax & Regulatory Clearance Statement | ✓ Attached |
| DBE Participation Plan | ✓ Attached |
| Equal Benefits Ordinance Compliance (Ch. 17-1900) | ✓ TWC extends equal benefits to all domestic partners |
| Local Business Entity Certification | ✓ Attached (significant evaluation factor) |
| AI Use Certification — Human SME Review Completed | ✓ |
| Insurance Certificates Meeting All Appendix L, Article XV Minimums | ✓ Attached |
| Audited Financials (3 years) | ✓ Attached |
| WCAG 2.1 AA Compliance Commitment | ✓ (TWC builds to 2.2 AA) |
| Source Code Escrow at Vendor Expense | ✓ |
| 180-Day Proposal Binding Period Accepted | ✓ |

---

*Tech Week Consortium | 1234 Market Street, Suite 800, Philadelphia, PA 19107 | proposals@techweekconsortium.coop | 215-555-0119*
```