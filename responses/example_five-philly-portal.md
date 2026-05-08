# Executive Summary

# Executive Summary: Tech Week Consortium Response to City of Philadelphia Special Event Permitting Software Solution RFP (Project Intake #1140)

Tech Week Consortium (TWC) is uniquely positioned to deliver the City of Philadelphia's next-generation Special Event Permitting Software Solution. As a Philadelphia-based, worker-owned civic technology cooperative headquartered three blocks from City Hall, TWC brings a decade of direct partnership with the City — most notably our ongoing engagement with the Department of Licenses and Inspections, where we rebuilt the public-facing licensing portal serving approximately 85,000 active licenses and cut average completion time by nearly 80%. Our proposed solution directly addresses OCRSE's core pain points: we will replace the current static, PDF-driven process with a dynamic, event-type-aware permitting platform featuring configurable conditional logic workflows, real-time status tracking, interdepartmental task coordination, integrated payment processing, and robust reporting infrastructure — all capable of handling the required 1,700+ annual applications with capacity for surge periods. Built on our proven `civitas` framework for accessible civic web applications, the solution will be installed on City infrastructure, comply fully with all Appendix K IT and security standards, and meet WCAG 2.1 AA accessibility requirements as a baseline — not an afterthought.

TWC offers the City a combination of technical depth, local accountability, and structural alignment that no outside vendor can replicate. Our SOC 2 Type II certification, FedRAMP Moderate authorization, and demonstrated experience delivering on-premises municipal systems mean we are fully prepared to meet every technical, security, and data-governance requirement outlined in this RFP. Our 100% client renewal rate over 12 consecutive quarters and our no-subcontracting model guarantee that the same experienced team that wins this contract will design, build, and support it — with no handoffs to unfamiliar staff. We will deliver a fixed-price proposal with milestone-based payments, a 30-day reliability period, a full five-year maintenance commitment, and source code escrow at no cost to the City. All custom code developed under this contract will be delivered to the City under an open-source license, ensuring Philadelphia retains full ownership and long-term independence from any single vendor — consistent with our founding principle that public money should produce public code.

# Technical Approach

# Technical Approach

## City of Philadelphia Special Event Permitting Software Solution
### Submitted by: Tech Week Consortium (TWC)
### Project Intake #1140

---

## 1. Overview and Guiding Principles

Tech Week Consortium approaches the City of Philadelphia's Special Event Permitting Software Solution as a problem we are distinctly positioned to solve. We are a Philadelphia-based worker cooperative headquartered three blocks from City Hall. We have maintained a continuous engagement with the City's Department of Licenses and Inspections since 2016, and our staff includes former municipal CIOs who have navigated the City's technical standards, network environment, and interdepartmental coordination challenges from the inside. We understand that the Office of City Representative and Special Events (OCRSE) is not primarily looking for novel technology—it is looking for a system that staff and applicants will actually use, that City IT can maintain without perpetual vendor dependency, and that will still be functioning correctly when the next administration takes office.

Our technical approach is organized around four commitments that flow directly from that understanding:

1. **Boring, well-supported technology.** We do not introduce a dependency for which we cannot identify a ten-year support story. Every architectural decision below reflects that discipline.
2. **Accessibility-first design.** Every screen, workflow, and report will meet WCAG 2.1 AA (and be tested against WCAG 2.2 AA) before it is deployed. We publish a public Accessibility Conformance Report (ACR) for every shipped application.
3. **On-premises, City-owned infrastructure.** Per requirement T-001, the system will run on existing City equipment and networks. We have designed the architecture accordingly, with no cloud-hosted components in the production path unless the City's IT division requests otherwise.
4. **Open by default.** All custom code produced under this contract will be delivered to the City with full source code, documentation, and specifications as required by SC-001. Non-proprietary components will be MIT-licensed and contributed to the civic-tech commons, consistent with our cooperative's standing practice.

---

## 2. Proposed System Architecture

### 2.1 Architecture Pattern

We propose a **three-tier web application** architecture:

| Tier | Role | Primary Technology |
|------|------|--------------------|
| Presentation | Browser-rendered UI for applicants and City staff | Server-rendered HTML with progressive enhancement; Django Jinja2 templates |
| Application | Business logic, workflow engine, API layer | Django 5.x (Python 3.12), Django REST Framework |
| Data | Relational persistence, document storage, search | PostgreSQL 16, pgvector (for future search), local file storage with configurable NAS mount |

This is the same core stack TWC uses in our L&I engagement, which has processed approximately 85,000 active business and trade licenses without material downtime. It is well-understood by City IT, well-documented in the open-source community, and trivially maintainable by any competent Python developer—not only by TWC.

We deliberately avoid a heavy single-page application (SPA) frontend framework. Server-rendered HTML with progressive enhancement means that the application works on low-bandwidth connections, works with assistive technologies out of the box, and does not require a separate frontend build pipeline that City IT must learn to maintain. JavaScript is used only where it provides a clear, tested user-experience benefit—inline form validation, conditional field display—and every such enhancement degrades gracefully.

### 2.2 System Topology Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│  City of Philadelphia Network Perimeter                         │
│                                                                 │
│  ┌─────────────┐    ┌──────────────┐    ┌───────────────────┐  │
│  │  Reverse    │    │  Application │    │  Database         │  │
│  │  Proxy /    │───▶│  Server(s)   │───▶│  Server           │  │
│  │  Load Bal.  │    │  (Django)    │    │  (PostgreSQL 16)  │  │
│  │  (nginx)    │    │              │    │                   │  │
│  └─────────────┘    └──────┬───────┘    └───────────────────┘  │
│         ▲                  │                                    │
│         │                  │ async tasks                        │
│  Public │           ┌──────▼───────┐    ┌───────────────────┐  │
│  Internet           │  Task Queue  │    │  Document / File  │  │
│  (HTTPS) │           │  (Celery +   │    │  Storage (NAS /   │  │
│         │           │   Redis)     │    │   local mount)    │  │
│  ┌──────┴──────┐    └──────────────┘    └───────────────────┘  │
│  │  City VPN / │                                               │
│  │  Staff Net  │    ┌──────────────────────────────────────┐   │
│  └─────────────┘    │  Integration Layer (REST / webhooks) │   │
│                     │  ─ City payment processor            │   │
│                     │  ─ City GIS / ArcGIS                 │   │
│                     │  ─ Business licensing database       │   │
│                     │  ─ City SSO (SAML 2.0 / OIDC)        │   │
│                     └──────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

*Full-resolution topology diagrams, including network segmentation and firewall zone mapping, will be delivered as Exhibit A to the Statement of Work during the kickoff phase.*

### 2.3 Component Justification

**nginx reverse proxy / load balancer.** nginx is battle-tested, widely deployed in City environments, and has a clear long-term support path. It handles TLS termination, rate limiting, and static asset serving, keeping the application tier focused on business logic. A second nginx instance can be activated for load balancing in a future high-availability configuration without application-layer changes.

**Django 5.x application server.** Django's built-in ORM, admin scaffolding, authentication framework, and form library dramatically reduce the surface area of custom code we must write—and that the City must eventually maintain. Django has a published Long Term Support (LTS) release cycle; Python itself has a well-documented deprecation cadence. We estimate the proposed stack will be maintainable with standard open-source tooling through at least 2035.

**PostgreSQL 16.** The City's L&I engagement already runs PostgreSQL. City IT has operational familiarity, existing backup tooling, and established access controls for this database. PostgreSQL's row-level security, native JSON support, and full-text search reduce the need for auxiliary services.

**Celery + Redis task queue.** Workflow notifications, report generation, document processing, and payment webhook handling run asynchronously through Celery workers backed by a Redis broker. This keeps synchronous HTTP response times fast (see Section 4, Performance Standards) and isolates failure domains—a delayed notification job does not affect permit submission throughput.

**Custom workflow engine (TWC `civitas-workflow` module).** Our `civitas` framework, currently MIT-licensed and in production use by 14 municipalities, includes a configurable workflow engine that implements conditional logic, role-based routing, and multi-step approval chains using a declarative configuration format. Workflows are defined in YAML and stored in the database; they can be modified by authorized City administrators without a code deployment. This directly addresses requirements F-005 (conditional logic workflows), F-003 (service request generation), and PS-008 (post-implementation adjustments by City personnel).

---

## 3. Functional Architecture

### 3.1 Application Management (F-001 through F-008)

The permit application subsystem is the core of the proposed solution. We design it around the following principles:

**Event-type-specific dynamic forms.** Each of the City's eight-plus distinct event types will have its own form schema defined in the workflow configuration. Forms are rendered dynamically from schema definitions, not hardcoded. When OCRSE needs to add a new event type or modify an existing one's required fields, a City system administrator can make that change through the administrative interface without developer involvement. This eliminates the uniform PDF bottleneck described in requirement F-008.

**Conditional logic.** The `civitas-workflow` engine evaluates applicant inputs in real time and adjusts which fields are required, which document uploads are triggered, and which departmental routing queues receive the application—all without a page reload. Conditions are expressed as composable rule objects (e.g., `expected_attendance > 1000 AND alcohol_permit = true → trigger_route: fire_marshal_review`). The full condition library is documented and extensible.

**Concurrent application types and surge capacity.** The system handles multiple concurrent application types by design—each type is an independent workflow definition sharing the same application, database, and infrastructure. At 1,700-plus annual applications (requirement F-006), the system operates well within comfortable margins; our L&I engagement processes comparable volumes with substantially more complex business logic. See Section 4 for specific performance benchmarks.

**Post-submission editing.** Applicants may upload additional documents and edit permitted fields after submission, subject to workflow state and role-based permission rules. All edits are versioned and audit-logged (F-004, F-021).

### 3.2 Status Tracking and Communication (F-009 through F-013)

**Real-time status dashboard.** Application status is surfaced on both the applicant-facing portal and the City staff dashboard. Status transitions (submitted, under review, additional information requested, approved, denied, permit issued) are logged with timestamps and displayed in a human-readable timeline view. No applicant needs to call OCRSE to learn where their application stands.

**Integrated messaging.** A structured messaging thread is attached to each application record. Messages sent through the portal are logged to the application record, visible to all authorized parties, and trigger email notifications to recipients. This is not a general email relay—it is a persistent, auditable record of every communication associated with an application, satisfying F-010 and F-012.

**Interdepartmental coordination.** City staff from different departments are granted scoped access to applications relevant to their review role. Internal comment threads (separate from applicant-visible messaging) allow Fire Marshal, Streets Department, Parks, and other reviewing bodies to communicate without leaving the system. Task assignments, due dates, and completion status are tracked per review step (F-011, F-020).

**Single access point.** The applicant portal presents all applications, permits, messages, and invoices in one authenticated dashboard, regardless of which City departments are involved in review. Applicants do not need to navigate to separate agency portals (F-013).

### 3.3 Dashboards, Calendars, and Reporting (F-014 through F-018)

**Applicant dashboard.** Each applicant sees a personalized dashboard showing all their applications (active and historical), current status, pending action items, outstanding invoices, and issued permits. Applications are grouped by event type and filterable by date range and status.

**Staff dashboard.** City personnel see a configurable dashboard showing their assigned review queue, upcoming deadlines, recently submitted applications, and flagged items requiring attention. Role and department filters allow each staff member to scope their view.

**Calendar view.** A shared event calendar—visible to City staff, and in a filtered form to applicants—shows scheduled events by date, location, and type. The calendar is built on a lightweight open-source component (FullCalendar) that renders consistently across devices and passes accessibility audit. Conflicts (same venue, same date) are surfaced automatically as soft warnings during application intake.

**Reporting.** We implement a two-layer reporting architecture:

- *Predefined reports* are implemented as named SQL views exposed through the Django admin and a reporting module, downloadable as CSV or PDF. Standard reports will cover application volumes by type and date, average processing time by event type, departmental review turnaround, outstanding payment aging, and permit issuance rates.
- *Ad hoc reporting* is provided through an embedded Metabase instance (open-source, MIT-licensed) connected to a read-only reporting replica of the PostgreSQL database. City staff with the analyst role can build and save custom reports without SQL knowledge. Power users can write SQL directly against the reporting replica.

This architecture satisfies F-016, F-017, and F-018 and ensures that reporting queries do not contend with transactional application traffic.

### 3.4 Workflow and Access Control (F-019 through F-021)

User roles are implemented using Django's built-in permission framework extended with object-level permissions. We propose the following baseline role taxonomy, subject to refinement during discovery:

| Role | Access Scope |
|------|-------------|
| Applicant | Own applications, messages, invoices, issued permits |
| OCRSE Staff | All applications, full messaging, workflow actions |
| Reviewing Department Staff | Applications routed to their department queue; internal comments |
| OCRSE Administrator | Workflow configuration, user management, report administration |
| City IT Administrator | System configuration, audit logs, integration management |
| Read-only Analyst | Reporting replica access; no write permissions |

Role assignments are managed by OCRSE Administrators without developer involvement. All permission changes are audit-logged.

### 3.5 Payments and Invoicing (F-022, F-023)

Payment integration will connect to the City's existing payment processor via its published API. We have integrated with City of Philadelphia payment infrastructure in our L&I engagement and will apply the same integration pattern here. Invoices are generated by the system based on configurable fee schedules tied to event type and application attributes. Applicants receive invoices through the portal and via email notification, and can pay online through the integrated payment flow. Invoice status (outstanding, paid, partially paid, waived) is reflected in real time on both applicant and staff dashboards. Payment receipts are stored against the application record and are available for download by both parties.

---

## 4. Performance Standards

The following performance commitments are based on the City's current hardware profile as described in Appendix K and in conversations with City IT during the pre-proposal period. Final benchmarks will be validated against the City's actual environment during the configuration and testing phase, and documented in the Test Plan deliverable (PS-006).

| Metric | Committed Standard | Measurement Basis |
|--------|-------------------|-------------------|
| Page response time (median, authenticated) | ≤ 800ms | 50th percentile under normal load |
| Page response time (95th percentile) | ≤ 2,000ms | Under simulated peak load |
| Transactions per minute (TPM) | ≥ 500 concurrent form submissions | Load test with 500 simultaneous users |
| Server Disk I/O | ≤ 70% sustained utilization under peak load | Measured via iostat during load test |
| Page swapping | 0 swap events under normal operating load | Requires ≥ 16GB RAM on application server; see Section 5.1 |
| System availability (MTTF) | ≥ 2,628 hours (target: 99.5% uptime) | Rolling 12-month measurement |
| Mean time to repair (MTTR) | ≤ 4 hours for Priority 1 incidents | Per maintenance SLA in Section 7 |
| Bandwidth utilization | ≤ 2 Mbps sustained per 100 concurrent users | Measured at network perimeter |

**Performance assumptions.** These standards assume: (a) the application server has at minimum 8 CPU cores and 16GB RAM; (b) the database server has at minimum 4 CPU cores, 16GB RAM, and SSD-backed storage; (c) network latency between application and database servers is ≤ 1ms (co-located in same data center or server room); and (d) the City's internet connection provides ≥ 100 Mbps symmetric bandwidth for public-facing traffic. Section 5.1 below identifies the specific server configuration required to meet these standards. If the City's current equipment does not meet these baselines, we identify the necessary upgrades.

---

## 5. Infrastructure Requirements

### 5.1 Server Requirements

The following table specifies the minimum server configuration required to meet the performance standards in Section 4. No hardware will be purchased under this contract (T-004); this table is provided so that the City's IT division can confirm existing equipment meets requirements or plan any necessary upgrades.

| Server Role | Minimum CPU | Minimum RAM | Storage | Notes |
|-------------|------------|------------|---------|-------|
| Application server (primary) | 8 cores | 16 GB | 100 GB SSD (OS + app) | Runs Django, Celery workers, nginx |
| Database server | 4 cores | 16 GB | 500 GB SSD (data) | PostgreSQL 16; SSD required for I/O standards |
| Redis / cache server | 2 cores | 8 GB | 20 GB | May be co-located with app server in lower-volume configs |
| Reporting replica | 4 cores | 8 GB | 500 GB SSD | Read-only PostgreSQL replica; may be

# Pricing

# Section 7: Cost Proposal

## Tech Week Consortium — Pricing & Cost Proposal
### City of Philadelphia Special Event Permitting Software Solution | Project Intake #1140

---

## 7.1 Pricing Philosophy and Assumptions

Tech Week Consortium (TWC) submits this as a **fixed-price proposal** in full compliance with RFP requirement C-001. All costs necessary to deliver a complete, operational, and fully accepted Special Event Permitting Software Solution are itemized below, including integration, project management, software development, testing, installation, maintenance, training, and all other work within scope.

**Global Pricing Assumptions**

The following assumptions underlie all line-item prices. Per RFP requirement C-008, any material deviation from these assumptions identified during contract negotiation or project initiation will be subject to a written change-order process with pricing disclosed at the rates established in Section 7.6 below.

1. **Volume baseline.** Pricing assumes up to 2,000 special event permit applications annually (inclusive of the RFP's stated 1,700+ baseline plus a 15% surge buffer). Volumes exceeding 2,000 applications per year will be reviewed at each contract anniversary; material volume increases may trigger a renegotiation of the maintenance line items only.
2. **On-premises installation.** All software is installed on City-owned equipment and networks per T-001. TWC has reviewed the City's current infrastructure profile as described in the RFP and related appendices. Hardware, networking equipment, and physical installation services are explicitly excluded from this proposal per T-004.
3. **City responsibilities.** Pricing assumes the City will provide: timely access to subject-matter experts and decision-makers during discovery and configuration phases; access to existing City systems (billing/payment processor, GIS, business licensing databases) within 10 business days of project kickoff; and a dedicated project manager with authority to approve deliverables.
4. **Third-party systems.** Integration costs below cover API-based connections to up to four (4) distinct City systems. Integration with additional systems beyond four will be priced at the rates in Section 7.6.
5. **No sales tax.** Per C-004, all prices exclude federal, state, and local sales/use taxes and federal excise taxes.
6. **Source code and licensing.** All custom software developed under this contract is delivered to the City with full source code and documentation per SC-001. Proprietary components of TWC's `civitas` framework are licensed to the City under a perpetual, royalty-free license and deposited into escrow per SC-002 through SC-004.
7. **Accessibility audit.** TWC's standard practice includes a third-party WCAG 2.2 AA audit by a certified accessibility vendor prior to Final Acceptance. This audit is included in the base price and is not invoiced as a separate cost to the City.
8. **Currency and validity.** All prices are in U.S. dollars. Per A-007, this proposal and all prices within it are binding for 180 days from the submission date of March 17, 2026.

---

## 7.2 Base System Software

These costs cover the configuration, customization, and deployment of TWC's `civitas`-based permitting platform to meet all functional requirements (F-001 through F-026) and all technical requirements (T-001 through T-037).

| Line | Item | Description | Fixed Price |
|------|------|-------------|-------------|
| SW-01 | Core Permitting Platform License (Perpetual) | Perpetual, royalty-free license for the City of Philadelphia to the `civitas` permitting module, including all source code and documentation. Covers all eight (8) event types (F-007), dynamic conditional-logic workflows (F-005), multi-application hosting (F-001), and permit issuance (F-002). | $185,000 |
| SW-02 | Dynamic Application Engine | Configuration and customization of event-type-specific application forms, eliminating the uniform PDF format (F-008). Includes conditional field logic, required-documentation routing, and post-submission editing controls (F-004, F-005). | $42,000 |
| SW-03 | Status Tracking & Messaging Module | Real-time applicant and City-personnel status dashboards (F-009, F-015); direct applicant-to-City messaging with full retained history (F-010); internal interdepartmental collaboration tools (F-011); automated status notifications replacing manual email (F-012); single-access-point applicant portal (F-013). | $38,000 |
| SW-04 | Dashboard, Calendar & Reporting Module | Centralized event calendar and unified application dashboard (F-014, F-015); KPI and operational reporting engine supporting predefined and ad hoc reports (F-016, F-017); applicant data analysis tools (F-018). | $34,000 |
| SW-05 | Workflow & Access Control Engine | Multi-role permission and access-control configuration (F-019); centralized cross-departmental task management (F-020); application and workflow archiving and audit-trail system (F-021). | $28,000 |
| SW-06 | Payments & Invoicing Module | Payment processor integration supporting seamless online payment (F-022); invoice generation and management tools (F-023). | $22,000 |
| SW-07 | Service Request / Task Generation Engine | Automated generation of service requests and tasks based on applicant inputs (F-003), routed to appropriate City departments. | $18,000 |
| | **Base System Software Subtotal** | | **$367,000** |

---

## 7.3 Optional Add-Ons

The following optional capabilities fall outside the baseline RFP scope but may be of value to OCRSE. Each is described, priced, and justified below per C-003. None of these are required for the base system to meet all stated RFP requirements.

| Line | Item | Description | Rationale for Exclusion from Base | Optional Price |
|------|------|-------------|-----------------------------------|----------------|
| OPT-01 | Public-Facing Open Data API | A publicly documented REST API exposing anonymized event permit data (dates, event types, geographic footprints) for use by journalists, researchers, and civic technologists. Modeled on TWC's Camden County open-data delivery. | RFP does not require public data publication; internal reporting (F-016–F-018) is fully covered in the base system. City may wish to evaluate public data disclosure implications before committing. | $24,000 |
| OPT-02 | Spanish / Mandarin / Vietnamese Application Interface | Full translation of the applicant-facing portal into Spanish, Mandarin, and Vietnamese, with language-specific help text and error messages. TWC has native speakers and prior translation infrastructure from the School District engagement. | RFP does not specify multilingual requirements. Strongly recommended for equity and constituent access, but inclusion is a City policy decision. | $31,000 |
| OPT-03 | GIS Map-Based Event Footprint Tool | An interactive map interface allowing applicants to draw event boundaries, identify street closures, and flag proximity conflicts with other permitted events, integrated with City GIS systems. | RFP identifies GIS integration (F-024) as a required integration point, which the base system supports via API. The map-drawing tool is an enhanced UX layer beyond the stated requirement. | $19,500 |
| OPT-04 | Automated Conflict Detection Engine | Algorithmic review of incoming applications for date, location, and resource conflicts with existing approved events; generates alerts for City reviewers. | Requires City policy decisions on conflict-resolution rules before it can be configured. Recommended for Year 2 after operational patterns are established. | $27,000 |

---

## 7.4 Professional Services

### 7.4.1 Implementation Services

All implementation services are performed exclusively by TWC staff members — no subcontracting layer. Pricing covers all tasks from discovery through Final Acceptance, including the 30-consecutive-calendar-day Reliability Period (PS-007).

| Line | Item | Description | Fixed Price |
|------|------|-------------|-------------|
| PS-01 | Discovery & Requirements Validation | Structured discovery sessions with OCRSE and all relevant City departments; validation and refinement of the requirements documented in this RFP; production of a finalized Statement of Work suitable for contract incorporation (PS-002). Estimated 4 weeks. | $28,000 |
| PS-02 | System Architecture & Design | Infrastructure topology design (T-015, T-016); workflow-processing plan (T-017); reporting infrastructure design (T-018); disaster recovery plan (T-019); bandwidth and performance documentation (T-020–T-024). Production of all required technical documentation per Appendix K (T-025–T-030). Estimated 3 weeks. | $21,000 |
| PS-03 | Software Configuration & Custom Development | Configuration, customization, and integration development for all base system modules (SW-01 through SW-07). Includes version control, error correction, and pre-delivery unit and integration testing (PS-001). Estimated 10 weeks. | $84,000 |
| PS-04 | Third-Party System Integration | API-based integration with up to four (4) City systems, including payment processor, GIS, and business licensing database (F-024, F-025, F-026). Includes integration testing and documentation. Estimated 4 weeks, overlapping with PS-03. | $36,000 |
| PS-05 | City IT Standards Compliance & Security Review | Validation of compliance with all Appendix K standards (T-025–T-030); WCAG 2.2 AA third-party audit (included at no additional cost; see Section 7.1 assumption 7); Century Date Standard conformance testing (T-037); SOC 2 Type II and SOC 1 audit documentation preparation (T-031). Estimated 2 weeks. | $14,000 |
| PS-06 | User Acceptance Testing & Reliability Period | Execution of Conditional and Final Acceptance test plans (PS-006); support for City-led UAT; management of and support through the 30-day Reliability Period (PS-007). Estimated 6 weeks. | $22,000 |
| PS-07 | Project Management | Dedicated project manager throughout the engagement; two-week iteration cadence with public roadmap; milestone tracking; risk management; status reporting to OCRSE (PS-001, PS-003). Estimated duration: full project lifecycle (~6 months). | $31,000 |
| PS-08 | Deployment & Go-Live Support | Production deployment on City infrastructure; go-live cutover planning and execution; hypercare support for the first 30 days post-launch (PS-007, T-023). | $12,000 |
| | **Implementation Services Subtotal** | | **$248,000** |

### 7.4.2 Training Services

Per PS-009 through PS-013 and Appendix E, training services are priced as separate line items below.

| Line | Item | Description | Fixed Price |
|------|------|-------------|-------------|
| TR-01 | Training Needs Assessment & Plan | Identification of all City personnel user groups; development of a detailed Training Plan specifying format, schedule, audience segments, scope, assumptions, and City responsibilities (PS-011). | $4,500 |
| TR-02 | City Administrator Training | In-person training for system administrators covering configuration management, user-role administration, workflow adjustments, and reporting. Up to 3 sessions of up to 12 participants each. | $9,000 |
| TR-03 | OCRSE Staff Training — Application Processing | In-person and recorded training for OCRSE permit reviewers covering application processing, task management, interdepartmental coordination tools, and communication features. Up to 4 sessions of up to 15 participants each. | $11,000 |
| TR-04 | Reporting & Analytics Training | Hands-on training for designated City reporting users covering predefined report generation, ad hoc report building, dashboard configuration, and data export (F-016–F-018). Up to 2 sessions of up to 10 participants each. | $6,500 |
| TR-05 | Training Materials Production | Comprehensive user manuals/guides (role-specific), recorded video tutorials for each training module, FAQ documents, and a quick-reference card for each user role (PS-010). Delivered in editable formats so the City can update them independently. | $8,000 |
| TR-06 | Applicant Onboarding Support | Design and production of applicant-facing help documentation, portal walkthrough guides, and a "how to apply" video tutorial. Coordination with OCRSE on public rollout communications (PS-013). | $5,500 |
| TR-07 | Post-Go-Live Office Hours (90 Days) | Twelve (12) one-hour virtual office-hour sessions available to City staff during the first 90 days post-launch for questions, troubleshooting guidance, and workflow refinement. | $4,000 |
| | **Training Services Subtotal** | | **$48,500** |

---

## 7.5 Documentation

| Line | Item | Description | Fixed Price |
|------|------|-------------|-------------|
| DOC-01 | Technical System Documentation | Architecture diagrams, data dictionaries, API specifications, integration documentation, and infrastructure runbooks. Delivered in editable formats with City ownership (SC-001). | $8,000 |
| DOC-02 | Source Code & Escrow Documentation | Complete, annotated source code for all custom deliverables; escrow account setup and initial deposit per SC-002 through SC-004; ongoing escrow update procedures documented. | $3,500 |
| DOC-03 | Accessibility Conformance Reports (ACRs) | Public-facing WCAG 2.2 AA conformance reports for all shipped application interfaces, following TWC's standard ACR publication practice. | Included in PS-05 |
| | **Documentation Subtotal** | | **$11,500** |

---

## 7.6 Software Maintenance Agreement

Per M-001 through M-007, maintenance and support services are priced below with Year 1 as a required deliverable and Years 2–5 as separately identified line items. All maintenance is provided on a turnkey basis (M-002); TWC serves as the sole point of contact for all system elements. TWC guarantees availability of maintenance and support for a minimum of five (5) years from Final Acceptance (M-004).

**Included in all maintenance years:**
- Sole-point-of-contact support desk, business hours (Monday–Friday, 8 AM–6 PM Eastern) with emergency on-call for Severity 1 issues 24/7/365
- Best-efforts error and defect correction within 48 hours of notification (M-006)
- All software updates, patches, and minor enhancements
- Annual performance review and capacity planning
- Ongoing conformance with all City IT standards (T-025–T-030) as those standards evolve
- Up to four (4) hours per month of City-initiated configuration changes executable by City personnel with TWC guidance; changes requiring development effort beyond this are quoted at the rates in Section 7.6 Supplemental

**Problem severity classification and response commitments** (per M-005):

| Severity Level | Definition | Initial Response | Targeted Fix / Workaround |
|----------------|------------|-----------------|---------------------------|
| **Severity 1 — Critical** | System unavailable or data loss imminent; no workaround available | 1 hour (24/7) | 4 hours; on-site if required |
| **Severity 2 — High** | Core functionality impaired; workaround available but burdensome | 4 business hours | 48 hours (M-006) |
| **Severity 3 — Medium** | Non-critical feature impaired; workaround available | 1 business day | Next scheduled release (≤30 days) |
| **Severity 4 — Low** | Cosmetic or minor issue; minimal operational impact | 2 business days | Scheduled at mutual discretion |

| Line | Item | Year | Fixed Annual Price |
|------|------|------|--------------------|
| MA-01 | Software Maintenance & Support — Year 1 | Commences upon Final Acceptance | $52,000 |
| MA-02 | Software Maintenance & Support — Year 2 | | $54,080 |
| MA-03 | Software Maintenance & Support — Year 3 | | $56,243 |
| MA-04 | Software Maintenance & Support — Year 4 | | $58,493 |
| MA-05 | Software Maintenance & Support — Year 5 | | $60,833 |
| | **Maintenance Agreement Subtotal (Years 1–5)** | | **$281,649** |

*Years 2–5 reflect a 4% annual escalator, consistent with the Philadelphia-area CPI trend over the prior three years. The Year 1 rate is fixed regardless of CPI.*

---

## 7.7 Warranty

Per W-001 through W-006, warranty coverage is priced as a separate line item. Year 1 warranty is required; Years 2 and 3 are offered as preferred options per W-003. All warranty obligations are fulfilled by TWC as
