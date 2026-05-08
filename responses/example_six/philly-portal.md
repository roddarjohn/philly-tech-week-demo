# Tech Week Consortium — Proposal for City of Philadelphia Special Event Permitting Software Solution (RFP #1140)

**Submitted by:** Tech Week Consortium | 1234 Market Street, Suite 800, Philadelphia, PA 19107 | proposals@techweekconsortium.coop | 215-555-0119
**Proposal Lead:** R. Park, Procurement Specialist | **Submission Deadline:** March 17, 2026, 5:00 PM via eContract Philly

---

## Why Tech Week Consortium

Tech Week Consortium (TWC) is a Philadelphia-based, worker-owned civic technology cooperative founded in 2015 — three blocks from City Hall. We have delivered production software to the City of Philadelphia continuously since 2016, including the Department of Licenses and Inspections portal serving ~85,000 active licenses that is directly analogous to the permitting workflows described in this RFP. We bring no acquisition pressure, no subcontracting layer, and a 100% client renewal rate for engagements over six months. Every line of code is written by a TWC member.

---

## Proposed Solution

We will design, build, and maintain a **configurable, open-source special event permitting platform** deployed on City infrastructure. The system will be purpose-built for Philadelphia's event permitting process and released under an MIT license, ensuring the City retains full ownership and auditability of the codebase with no escrow dependency. Our stack — Django, PostgreSQL, server-rendered HTML with progressive enhancement — is intentionally maintainable by successor vendors and City IT staff alike.

**All twelve mandatory functional requirements (A.1.1–A.1.12) are addressed as STANDARD or CONFIGURATION capabilities**, including:

- **Multi-application hosting and conditional logic workflows** via a configurable form engine supporting Philadelphia's eight event types, with branching routing, dynamic required fields, and department-specific approval chains
- **Permit generation and distribution** with templated, digitally signed PDF issuance and applicant delivery via email and portal download
- **Real-time status tracking and external communication** through an applicant-facing portal with in-thread messaging and full message history retained
- **Internal collaboration tools and centralized dashboards** with role-based interdepartmental views, shared calendars, and task queues
- **Invoice management** integrated with the City's existing billing infrastructure via REST API
- **Third-party integrations** with City GIS (ArcGIS), business licensing databases, and payment processors via documented API connectors and webhooks; SSO via the City's existing identity provider

All web interfaces conform to **WCAG 2.1 AA** (we test to 2.2 AA as standard practice) and adhere to City Digital Standards. A third-party accessibility audit is included in our engagement budget at no additional cost to the City.

---

## Implementation Approach

We propose a **phased, 26-week implementation** from contract execution to final acceptance:

| Phase | Weeks | Activities |
|---|---|---|
| Discovery & Configuration Design | 1–6 | Stakeholder workshops, workflow mapping, integration scoping |
| Build & Integration | 7–18 | Iterative two-week sprints; City review at each sprint close |
| User Acceptance Testing | 19–22 | Parallel testing with City staff and pilot applicants |
| Training & Soft Launch | 23–25 | Staff training, applicant onboarding, go-live readiness |
| Go-Live & Stabilization | 26 | Production cutover; hypercare support |

Public roadmap boards are provided to all stakeholder departments throughout. Milestone payments align to phase completions; we will provide a detailed milestone payment schedule per Appendix C requirements.

---

## Training and Support

Training will cover system navigation, application processing, report generation, and troubleshooting across all user role groups (City reviewers, department coordinators, applicants). Deliverables include role-specific user manuals, recorded video walkthroughs, and a searchable FAQ. A detailed training plan specifying format, schedule, audience groups, and City environment responsibilities will be delivered no later than Week 4.

Post-implementation support includes **Year 1 maintenance in the fixed price**, with Years 2–5 priced as separate line items per Appendix C. We are the single point of contact for all support and warranty matters. Problem severity classifications, response SLAs, escalation procedures, and fix-time commitments will be documented in the maintenance agreement. We maintain SOC 2 Type II certification annually and will provide audit reports upon City request.

---

## Cost Structure

Our proposal will be submitted as a **fixed price** in full compliance with Appendix C, itemized across base software, professional services (implementation and training by named staff with hourly rates and estimated hours), annual maintenance (Years 1–3 with monthly and annual breakdowns), and optional add-ons. Taxes are excluded. No time-and-materials or cost-plus components are included. Post-implementation workflow and form modifications are available under a transparent subscription retainer model, documented in C.7 pricing assumptions, and can be executed by City personnel for configuration-level changes without vendor involvement.

---

## Local Impact and Cooperative Advantage

TWC is headquartered in Philadelphia, employs 35 Philadelphia-area residents, and holds verified City of Philadelphia M/W/DSBE certification and Pennsylvania Small Diverse Business status. All project staff will be TWC members — no subcontractors. As a worker cooperative, we share 10% of any ongoing licensing revenue back to the City's general fund or a designated public-benefit recipient. Every deliverable is published under an open-source license, consistent with our *public money, public code* principle. We are committed to sustaining Philadelphia jobs and contributing durable digital infrastructure to the civic commons.

---

*Tech Week Consortium looks forward to building this system with the City of Philadelphia. Full proposal volumes, compliance matrix (Appendix D), cost proposal (Appendix C), audited financials, and all required certifications will be submitted via eContract Philly by March 17, 2026, 5:00 PM.*