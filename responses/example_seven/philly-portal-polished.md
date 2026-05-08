```markdown
# Executive Summary

## Tech Week Consortium Response to RFP Project Intake #1140
### Special Event Permitting Software Solution — City of Philadelphia, Office of City Representative and Special Events

---

## Philadelphia's Moment. Built by Philadelphia.

The City of Philadelphia is preparing to welcome the world. With FIFA World Cup matches beginning in June 2026 and the MLB All-Star Game following in July, the Office of City Representative and Special Events (OCRSE) is faced with an undeniable challenge: the current 8-page PDF email workflow managing over 1,700 annual permit applications cannot cope with the impending influx. **Tech Week Consortium (TWC) proposes to replace this outdated system — on time, on budget, and designed to serve well beyond 2026.**

We are not a vendor coming from another location. We are a Philadelphia-headquartered, worker-owned civic technology cooperative, located just three blocks from City Hall. Our ongoing engagement with the City's Department of Licenses and Inspections, which began in 2016 and will continue through 2027, has provided us with deep insight into the City's systems, procurement culture, and infrastructure. We have successfully delivered production software on the City's networks before, and we stand ready to do so again — with a fixed-price contract, on an expedited timeline, and without subcontractors or surprises.

---

## What We Are Proposing

TWC proposes to design, build, configure, deploy, and maintain a tailored special event permitting platform for OCRSE — a **fully custom, open-source-licensed solution** developed on our proven `civitas` civic application framework. This platform will be deployed on the existing City infrastructure and delivered under a fixed-price contract with milestone-based payments.

Our solution comprehensively addresses every mandatory functional requirement outlined in Appendix A.1:

| Requirement | TWC Solution Capability |
|---|---|
| Multi-application hosting (A.1.1) | Configurable application registry supporting all eight OCRSE event types concurrently |
| Permit generation and distribution (A.1.2) | Automated PDF/digital permit issuance with audit trail |
| Service request creation (A.1.3) | Rule-based task generation routed to relevant City departments |
| Post-submission editing (A.1.4) | Workflow-controlled amendment portal with version history |
| Conditional logic workflows (A.1.5) | Field-level and section-level conditional logic; no irrelevant questions shown to applicants |
| Real-time status tracking (A.1.6) | Applicant-facing status dashboard and City staff queue views, updated on every workflow transition |
| External communication (A.1.7) | Threaded messaging with full retained history; exportable for records requests |
| Internal collaboration (A.1.8) | Interdepartmental task assignments, comment threads, and @-mentions |
| Centralized dashboards and calendars (A.1.9) | Unified event calendar and application pipeline views by department and event type |
| Third-party integrations (A.1.10) | REST API and webhook architecture; documented integration paths for payment, GIS, and business licensing systems |
| Invoice management (A.1.11) | Configurable fee schedules with invoice generation, tracking, and status |
| Multi-user access and permissions (A.1.12) | Role-based access control with department-scoped permission sets |

The platform will be delivered as **City-owned source code**, fully documented, MIT-licensed, and deposited in escrow at no cost to the City — consistent with our founding principle that public money produces public code.

---

## Why TWC for This Procurement

### 1. We Have Done This Work, in This City, on These Systems

Our decade-long partnership with the Department of Licenses and Inspections, which involved migrating an 85,000-license legacy ColdFusion/Oracle stack to a modern Django/PostgreSQL portal, is the most relevant experience for this RFP's evaluation criteria. We possess comprehensive knowledge of the City's network environment, identity and authentication schemes, GIS platforms, and business licensing databases. We are not making estimates regarding integration complexity; we have already resolved most of it.

### 2. We Can Meet the Timeline

We recognize the stakes involved. A system that is not operational before the FIFA Group Stage matches commence signifies failure, not partial success. Our proposed implementation timeline targets a **production go-live by May 15, 2026**, aligning with the City's anticipated project start date and ensuring a 30-day reliability period ahead of peak FIFA event activities. Our project team is already local, fully staffed, and familiar with the City's technical environment; we are not building a team for this project; we already have one.

### 3. We Are Philadelphia

TWC is a certified M/W/DSBE, Small Diverse Business, and worker-owned cooperative located in Philadelphia. Every team member engaged in this project lives and works within the Philadelphia area, pays the local wage tax, and participates in client working sessions in person. When OCRSE staff have questions at 7:00 AM during the All-Star Game week, they will connect directly with a TWC member, not an out-of-state helpdesk.

This alignment directly responds to the City's preference for local business entities under Executive Order 04-12 and its commitments under the PHL Open for Business initiative. Awarding this contract to TWC would exemplify a commitment to Mayor Parker's vision of economically inclusive growth for Philadelphia.

### 4. We Are Structured to Protect the City's Interests

Our cooperative governance model ensures stability. There are no external investors applying pressure for profit, which allows us to focus on quality delivery and client satisfaction. Our 100% client renewal rate for engagements exceeding six months speaks to the positive outcomes of our stable environment. Over 80% of our procurement-required engagements are shipped under fixed-price contracts without change orders. We recognize the City's 20% retainage structure and have structured our pricing accordingly, ensuring no surprises in future billing cycles.

### 5. Our Open-Source Approach Eliminates Long-Term Lock-In

Every line of code produced by TWC belongs to the City from the moment it is committed. Our `civitas` framework is already MIT-licensed and employed by 14 municipalities. This enables the City's staff to engage any qualified developer for future maintenance, extension, or replacement of components without being hindered by proprietary systems. This is the true essence of durable digital public infrastructure.

---

## Compliance Commitments

TWC confirms full compliance with all legal and regulatory requirements detailed in this RFP, including:

- **Fixed-price proposal** — Fully itemized by deliverable as per Appendix C 
- **WCAG 2.1 AA** — We adhere to WCAG 2.2 AA standards (a superset) before every deployment; a third-party accessibility audit is included at no extra cost
- **SOC 2 Type II and FedRAMP Moderate** — Current certifications; documentation available upon request
- **Chapter 17-1400 campaign contribution disclosures** — Completed and included in Volume 1
- **Equal Benefits Ordinance (Chapter 17-1900)** — We extend equal benefits to domestic partners in line with cooperative policy
- **Philadelphia M/W/DSBE and SDB certifications** — Verified and active
- **Source code ownership and escrow** — Full ownership of custom source code is transferred to the City, with escrow arrangements at no cost
- **AI use certification** — Any AI-assisted drafting in this proposal has undergone review and validation by TWC subject-matter experts; TWC holds the appropriate licenses for all submitted content
- **Minimum 5-year maintenance commitment** — Guaranteed, with separate pricing for Years 2–5
- **Cyber Liability Insurance** — Coverage of $1M per claim/aggregate, with the City named as an additional insured; certificate included in Volume 1

---

## Proposal Organization

This response is organized into two volumes as mandated by the RFP:

- **Volume 1 — Qualifications:** Overview of company history, governance structure, Philadelphia experience, technical qualifications, financials, references, and relevant certifications 
- **Volume 2 — Technical and Cost Proposal:** Detailed solution architecture, implementation methodology, project timeline, staffing plan, integration approach, disaster recovery plan, performance specifications, training plan, statement of work, Requirements Compliance Certification (Appendix D), and fixed-price cost proposal (Appendix C)

---

## Our Commitment to OCRSE

The Office of City Representative and Special Events is pioneering a significant transformation — shifting from a paper-based system to a modern, accountable permitting operation with a timeline markedly compressed by international events beyond the City’s control. Director Jazelle Jones and her team deserve a technology partner who understands the urgency, brings relevant experience to bear, and maintains the values necessary to be a responsible steward of this system long after the World Cup concludes.

That is our commitment through Tech Week Consortium.

We welcome the opportunity to discuss our approach further in-person and are available for any pre-award conversations the Office would like to schedule.

---

*Submitted by:*
**R. Park, Procurement Specialist**  
Tech Week Consortium  
1234 Market Street, Suite 800, Philadelphia, PA 19107  
proposals@techweekconsortium.coop | 215-555-0119  

*This proposal is binding for 180 days from the submission date of March 17, 2026.*

# Technical Approach

## Tech Week Consortium Response to City of Philadelphia Project Intake #1140
### Special Event Permitting Software Solution

---

## 1. Overview and Solution Philosophy

Tech Week Consortium (TWC) proposes to design, build, deploy, and maintain a dedicated special event permitting platform for the City of Philadelphia's Office of City Representative and Special Events (OCRSE). Our solution supersedes the current 8-page PDF/email workflow with a sustainable, accessible, fully integrated digital permitting system—specifically crafted for Philadelphia's operational environment and existing technology infrastructure, as well as the exceptional demands expected in 2026.

We are not merely proposing a generic commercial off-the-shelf product. Instead, our **configurable platform built on TWC's open-source `civitas` framework** is hardened through a decade of delivering civic applications within Philadelphia and the surrounding region. Every component within this proposal is already utilized in production within Philadelphia City government or similar municipal environments. Nothing we propose is experimental.

Our approach is guided by four core commitments that resonate throughout every section of this proposal:

1. **Operational continuity above all.** OCRSE processes approximately 1,700 applications annually under standard conditions. In 2026, the FIFA World Cup and MLB All-Star Game events will compress that volume into a shorter time frame, coinciding with the deployment of the new system. Our implementation plan ensures OCRSE can process live applications in the new system before peak activity begins — rather than afterward.

2. **No surprises based on existing infrastructure.** The City does not intend to purchase new hardware or network upgrades under this contract. We clearly outline our infrastructure assumptions and performance requirements in Section 5, and we design our architecture to work seamlessly within those parameters.

3. **Public money, public code.** All custom software delivered under this engagement will be licensed to the City of Philadelphia with full source code ownership and will be published under an open-source license, aligning with our standard practices and meeting SC.1 requirements. The City will not face vendor lock-in for maintenance.

4. **Accessibility is a precondition, not a checklist item.** Every public-facing component will comply with WCAG 2.1 AA and our internal standard of WCAG 2.2 AA, thoroughly vetted before deployment. A certified third-party accessibility audit is factored into our fixed-price proposal at no additional cost to the City.

---

## 2. Solution Architecture

### 2.1 Architectural Pattern

We recommend a **three-tier web application architecture** deployed on the City's existing server infrastructure (or a City-designated hosting environment), with a distinct separation among:

| Tier | Component | Technology |
|------|-----------|------------|
| Presentation | Public applicant portal; staff workflow interface; administrative configuration UI | Server-rendered Django templates with progressive enhancement; no mandatory JavaScript for core form submission |
| Application | Business logic, workflow engine, conditional routing, API layer, integration middleware | Django (Python 3.12+), Django REST Framework, Celery for asynchronous task processing |
| Data | Relational data store for application records, workflow states, user accounts, documents, audit logs | PostgreSQL 16+; MinIO or City-provisioned S3-compatible document storage |

**Justification for a three-tier architecture:** This separation of presentation from application logic enables future replacements or extensions of the front-end without affecting the underlying business logic. Separating application logic from data allows independent scaling of computing power and storage—which is critical during surge periods in 2026—and facilitates a clear backup/restore procedure for disaster recovery. Additionally, this structure aligns with the City of Philadelphia's existing Django/PostgreSQL investment, as documented in our ongoing L&I portal engagement (refer to Section 9, Past Experience).

We categorically reject a two-tier (client-database) structure for this use case. A two-tier model exposes database credentials to clients, restricts our ability to implement API-based integrations, and complicates compliance with WCAG standards.

### 2.2 Deployment Topology

```
[Public Internet]
       │
  [City Firewall / Load Balancer]
       │
  [Web/Application Servers]          ← Django application; Celery workers
  [Reverse Proxy: nginx]             ← TLS termination; static asset serving
       │
  [Application Database]             ← PostgreSQL primary + replica
  [Document Store]                   ← MinIO / City S3-compatible endpoint
  [Message Broker]                   ← Redis (Celery broker + cache layer)
       │
  [Integration Middleware]           ← API gateway for external system calls
       │
  [City External Systems]
    ├── Payment processor (A.1.11)
    ├── GIS platform (A.1.10)
    ├── Business licensing database (A.1.10)
    └── City SSO / Identity provider (A.1.12)
```

All components will be installed on existing City equipment and networks, per T.1. No hardware procurement is required under this contract (we will provide equipment specifications and any necessary upgrade recommendations in Section 5).

### 2.3 Software Architecture Documentation (T.4)

The three-tier architecture is documented in our Software Architecture Document (SAD), which will be delivered as a formal project deliverable at the conclusion of Phase 1 (Discovery and Architecture). The SAD includes:

- Component diagram illustrating all services, data flows, and integration points
- Deployment diagram detailing server roles, network segments, and firewall rules
- Data model schema with an entity-relationship diagram
- API specification (OpenAPI 3.1) for all integration endpoints
- Security architecture narrative (see Section 6).

---

## 3. Functional Capabilities (Appendix A.1 Requirements)

### 3.1 Multi-Application Hosting (A.1.1)

The platform supports an unlimited number of concurrent permit application types, each independently configurable. OCRSE currently manages eight distinct event types; we will configure all eight at launch, with tools for administrators to create, modify, or retire application types without vendor involvement post-launch.

Each application type will be defined by a configuration object specifying:

- Form fields (type, validation rules, conditional visibility)
- Required documentation (by event type and applicant-supplied inputs)
- Workflow routing (which departments receive routing, in what order)
- Fee schedule (flat, tiered, or based on applicant inputs)
- Permit template (output format for generated permits)

Concurrent application management will be enforced at the database level using row-level locking and optimistic concurrency control. Staff working on the same application from different departments will access real-time state information without conflict.

### 3.2 Permit Generation and Distribution (A.1.2)

Permits will be generated as structured PDF documents through a configurable template engine. Each permit type will have a specifically maintained template. Permit generation will occur automatically upon the completion of workflows or may be initiated manually by authorized staff.

Generated permits will:

- Be stored in the document store with version history
- Be delivered to the applicant via the platform's messaging interface (A.1.7) and email notifications
- Be available for download from the applicant's portal dashboard at any time
- Optionally be sent via configurable webhook to a City-designated endpoint

Each permit will carry a unique identifier and a machine-readable QR code linking to a public verification endpoint, allowing inspectors to access the information without logging in.

### 3.3 Service Request Creation (A.1.3)

When an applicant’s entries imply a need for City services (e.g., traffic control, sanitation, police detail, street closures), the workflow engine will automatically generate structured service requests routed to the appropriate City department queue. Each service request will contain:

- A source application reference
- Event date, location (geocoded), and requested service window
- Applicant contact information
- Department-specific fields configurable per service type

Service requests will be visible to both the originating department and OCRSE staff in a central dashboard (A.1.9). Status updates on service requests will be reflected in the applicant's real-time status view (A.1.6).

### 3.4 Post-Submission Editing and Document Upload (A.1.4)

Applicants will have the ability to edit submitted applications and upload additional documentation post-submission, subject to workflow state controls. Specifically:

- Editing will be permitted when the application is in any staff-configurable "open for revision" state (e.g., pending supplemental documentation, returned for correction)
- Editing will be locked during active departmental review unless a staff member explicitly unlocks the record with justification
- All edits will be logged in a full, immutable audit trail documenting previous values, new values, timestamps, and user identities
- Document uploads will be versioned; earlier uploads will remain accessible to staff

This structural approach gives OCRSE complete control over when applicants can modify records, all without needing vendor intervention.

### 3.5 Conditional Logic Workflows (A.1.5)

This function embodies the platform's core capability. Our workflow engine follows a directed acyclic graph (DAG) model, where each node represents a workflow state and each edge reflects a transition condition. Conditions can reference:

- Any field value on the application form
- The output from any preceding workflow stage
- Calendar conditions (dates relative to event date, submission date, City holidays)
- External data lookups (e.g., business license status from the City's licensing database)
- Staff manual decision inputs

**Example — FIFA-related event routing:**
Selecting "Block Party / Street Closure" in a FIFA Fan Fest impact zone automatically triggers:

1. Routing to the Streets Department queue (mandatory for all street closures)
2. Routing to the Mayor's Office of Special Events coordination queue (due to FIFA impact)
3. A conditional documentation requirement for a FIFA coordination letter
4. A fee schedule override reflecting applicable surge pricing policies

None of these conditional branches necessitate code changes; they are configurable via the administrative UI, enabling trained City staff to adapt processes post-go-live.

### 3.6 Real-Time Status Tracking (A.1.6)

Each application will have a publicly visible status page (accessible without login via a unique application token, shareable by the applicant). Status updates will be pushed in real time via WebSocket for logged-in users and via polling with a 30-second refresh maximum for unauthenticated views.

Status information will include:

- Current workflow stage and responsible department
- Pending actions (items the applicant must complete)
- Estimated processing time (configurable by stage; displayed as a range)
- Message thread summaries (see A.1.7)
- Service request statuses associated with each relevant City department

Staff dashboards will display application status across all active records, complementing filter, sort, and saved-view capabilities.

### 3.7 External Communication (A.1.7)

A structured messaging interface will be integral to each application record. Messages will be threaded per application and visible to both the applicant and authorized City staff. Key features will include:

- A complete message history retained for the application's lifetime, archived per City records retention policy
- Email and optional SMS notifications for new messages (configurable by applicants)
- File attachments supported in messages (with virus scanning via ClamAV or another City-approved scanner)
- Staff capability to send messages en masse to applicants with similar event dates
- All messages will include timestamps, sender identity, and read receipts for staff

No communication regarding an application will leave the system outside this channel unless initiated by staff, thereby ensuring a comprehensive record for each application.

### 3.8 Internal Collaboration Tools (A.1.8)

The staff-facing interface will feature a suite of interdepartmental collaborative tools including:

- **Internal notes:** Staff can attach notes to any application, visible only to City personnel, with @-mention notifications to specific colleagues
- **Departmental queues:** Each department will have its own queue view showing only assigned applications and tasks, including configurable priority flags
- **Cross-department routing history:** Every routing action will be logged with timestamps, user identities, and any notes attached
- **Shared calendar:** A central calendar view will present all events sorted by date, location, and current permit statuses, overlaying a GIS base layer (see A.1.9 and A.1.10)
- **Workload indicators:** Queue depth and average processing time will be displayed for department supervisors to monitor staffing levels

These tools are purposefully designed to enhance the collaborative reality of OCRSE, which necessarily interacts with Parks, Streets, Police, Fire, and other agencies for major events.

### 3.9 Centralized Dashboards and Calendars (A.1.9)

The system will provide three configurable dashboard roles out of the box:

| Dashboard | Primary Audience | Key Views |
|-----------|-----------------|-----------|
| Applicant Portal | Event organizers | My applications; pending actions; message inbox; permit downloads |
| Staff Operations | OCRSE and department reviewers | Active queue; upcoming events calendar; inter-department routing status; KPI summary |
| Administrative | OCRSE and City Representative leadership | Volume trends; processing time analytics; surge capacity indicators; exportable reporting |

The events calendar will support iCal export capabilities and can be embedded into existing City intranet pages. GIS integration (A.1.10) will overlay permitted event locations on a map view, enabling staff to identify concurrent event conflicts geographically.

### 3.10 Third-Party Integrations (A.1.10)

We propose an API gateway architecture accompanied by an integration middleware layer. This effectively isolates external system dependencies from core application logic — if an external system alters its API, only the integration adapter will require adjustments, minimizing disruption to the broader application.

Proposed integrations at launch will include:

| System | Integration Method | Scope |
|--------|--------------------|-------|
| City payment processor | REST API / hosted payment page redirect | Invoice generation, payment confirmation, and reconciliation callbacks |
| City GIS platform (ArcGIS or equivalent) | ArcGIS REST API | Address geocoding, event location mapping, and impact zone lookups |
| Business licensing database | REST API or database view (as guided by City IT) | License status verification during application submission |
| City SSO / Identity provider | SAML 2.0 or OAuth 2.0 (as per City standards) | Staff single sign-on; applicant account federation where applicable |
| City email/notification infrastructure | SMTP relay or SendGrid-compatible API | Transactional notifications |

All integration points will be fully documented in the accompanying API specification. We request access to the integration environment during Phase 1 (Discovery) and will complete integration testing in our staging environment before moving any component to production.

Our previous experience with the City’s L&I licensing database and GIS infrastructure through ongoing portal engagement suggests a low-risk discovery phase for these integrations.

### 3.11 Invoice Management (A.1.11)

The platform features a comprehensive invoice management module:

- Fees will be automatically calculated based on applicant inputs and the configured fee schedule for each application type
- Draft invoices will be generated at designated workflow stages and held for staff review prior to issuance
- Issued invoices will be dispatched to the applicant via the messaging interface and email
- Payment status will be tracked in real-time through callbacks from the City’s payment processor
- Invoices, payment receipts, and modifications will all be securely stored in the application record and available for export
- Reporting features will allow tracking of outstanding invoices, payment aging, and revenue by event type and period

The invoice module is specifically designed to integrate with the City’s existing payment processor instead of introducing a separate payment channel.

### 3.12 Multi-User Access and Permissions (A.1.12)

Role-based access control (RBAC) will be implemented with the following default role hierarchy:

| Role | Scope |
|------|-------|
| Applicant | Own applications only; cannot access others' records |
| Department Reviewer | Assigned applications for their department; read/write on tasks assigned |
| Department Supervisor | All applications in their department’s queue; user management specific to their department |
| OCRSE Staff | Access to applications across all departments; limited to no administrative configuration rights |
| OCRSE Administrator | Full access, including workflow configuration, form builder, fee scheduling, and user management |
| System Administrator | Infrastructure-level access; managed by City IT |

Roles can be modified by OCRSE administrators without the need for vendor involvement. Custom roles can be created with granular permission specifications. All permission changes will be recorded in the audit trail to maintain oversight and accountability.

Integration with City SSO will ensure that staff accounts are provisioned and decommissioned in accordance with the City's identity management system, reducing the likelihood of lingering accounts following staff departures.

---

## 4. Customization and Configuration Approach (A.3.2)

### 4.1 What City Staff Can Configure Without Vendor Involvement

A primary design tenet of our platform is that OCRSE should be empowered to control its workflows. Once live and after training, City personnel with administrator-level access will be able to independently:

- Add, modify, or retire permit application types
- Edit form fields, labels, help text, and validation rules
- Adjust conditional logic routing rules
- Update fee schedules
- Modify permit templates (PDF layout and content)
- Create and change departmental queues and assignment rules
- Generate and customize reports
- Add or change notification templates (email/SMS)
- Establish new user roles with custom permission sets

### 4.2 What Requires Vendor Involvement

Changes necessitating new external system integrations, significant database schema migrations beyond standard configuration, or alterations to the underlying workflow engine will require TWC involvement. These revisions will be priced in Section 7 (Cost Structure) under a defined post-implementation service rate, accompanied by a transparent change-order process. We are committed to providing a written estimate within five business days of any change request and will complete authorized changes on an established timeline.

Our long-term objective is to expand the...

# Qualifications

## Section 4: Qualifications and Past Performance

## Tech Week Consortium | Project Intake #1140
### City of Philadelphia Special Event Permitting Software Solution

---

## 4.1 Company Overview and Corporate Structure

**Tech Week Consortium (TWC)** is a Philadelphia-based, worker-owned civic technology cooperative incorporated in Pennsylvania in 2015. Our headquarters is located at 1234 Market Street, Suite 800, Philadelphia, PA 19107—just three blocks from City Hall and well within the City of Philadelphia's geographical boundaries. Our Camden, New Jersey satellite office is accessible via the PATCO line.

As of January 2026, TWC employs 35 full-time staff members. We operate under a member-owned and worker-governed model; every full-time employee holds a voting membership in the cooperative, maintaining a lack of private equity, external investors, and growth pressures. Our governance structure minimizes the misaligned incentives often seen in vendor relationships, providing a substantial advantage for a client like the City of Philadelphia, especially for a minimum five-year engagement.

**Corporate Structure at a Glance:**

| Attribute | Detail |
|---|---|
| Legal name | Tech Week Consortium |
| Entity type | Pennsylvania worker-owned cooperative |
| Year incorporated | 2015 |
| Headquarters | 1234 Market Street, Suite 800, Philadelphia, PA 19107 |
| Satellite office | Camden, NJ |
| Total staff | 35 full-time (January 2026) |
| Annual revenue (2025) | $9.4M+ |
| Client renewal rate | 100% for engagements over six months (12-quarter rolling) |
| Voluntary turnover | 6% over the last three years |
| Average staff tenure | 4.7 years |

---

## 4.2 Organizational History and Growth

TWC was founded in 2015 by ten organizers of Philadelphia's annual Philly Tech Week festival. The founding members incorporated as a worker cooperative to formalize volunteer civic technology work they had previously performed for the City of Philadelphia and regional nonprofits. From the beginning, our mission has been to build durable digital public goods that endure beyond their funding cycles, procurement vehicles, and the political administrations that commissioned them.

**Organizational Milestones:**

| Year | Milestone |
|---|---|
| 2015 | Incorporated as a Pennsylvania worker cooperative; six founding members |
| 2016 | Secured our first municipal contract: rebuild of phila.gov/license-and-inspect for the City of Philadelphia Department of Licenses and Inspections |
| 2017 | Awarded GSA 8(a) Blanket Purchase Agreement for civic technology services |
| 2019 | Expanded staff to 18 and opened Camden, NJ satellite office |
| 2020 | Pivoted for public-health response: built contact-tracing and vaccine eligibility tools for two state health departments, aiding 4.1M residents |
| 2022 | Grew to 30 staff members; launched the MIT-licensed `civitas` accessibility framework, currently in active use by 14 municipalities |
| 2024 | Achieved SOC 2 Type II certification across our hosting practice; attained FedRAMP Moderate authorization for managed service tier |
| 2025 | Surpassed $9.4M in annual revenue while maintaining a 100% client renewal rate for engagements over six months |

This trajectory exemplifies sustained, mission-aligned growth in public-sector technology delivery—not speculative expansion. Every significant capability we have introduced since 2015 has been driven by documented needs from public-sector clients, not growth theories.

---

## 4.3 Certifications, Registrations, and Compliance Standing

TWC holds the following active certifications and registrations relevant to this procurement:

| Certification / Registration | Status |
|---|---|
| SAM.gov Unique Entity ID: ABCD-1234-EFGH | Active |
| GSA Schedule 70 / 8(a) BPA | Active |
| SOC 2 Type II (annual recertification) | Current |
| FedRAMP Moderate — managed-services tier (sponsored by NJ DOH) | Active |
| Pennsylvania Small Diverse Business (SDB) | Verified |
| City of Philadelphia M/W/DSBE certification | Verified |
| Pennsylvania worker cooperative incorporation | Since 2015 |

TWC qualifies as a **certified City of Philadelphia M/W/DSBE** and a verified **Pennsylvania Small Diverse Business**. Under Mayor Parker's Executive Order 04-12, these certifications qualify TWC as a Local Business Entity granted significant positive preference factors in evaluations. We maintain a permanent office within Philadelphia, employing local residents across multiple roles, and we expect this engagement will sustain and enhance that presence.

We are entirely compliant with all Philadelphia tax and regulatory mandates. The Philadelphia Tax and Regulatory Status and Clearance Statement (Appendix H) will be submitted with our proposal. We have no history of bankruptcy, insolvency proceedings, or federal government audits yielding adverse findings. Comprehensive audited financial statements and requisite financial disclosures are included in Section 6 of this proposal.

---

## 4.4 Core Technical Qualifications

The RFP highlights twenty technical experience areas, each requiring a minimum of five years of demonstrated experience. TWC’s qualifications in each area are summarized as follows.

### 4.4.1 Technical Experience Matrix

| RFP Experience Area | TWC Qualification | Years |
|---|---|---|
| Large-scale distributed database design and implementation | PostgreSQL and Oracle-integrated deployments across City of Philadelphia L&I, PA DOH, GPHIN lakehouse (47TB), and SDP platforms; three open data platform builds | 9+ |
| Software design, integration, testing, and support | Continuous delivery practice across all 47 production deployments since 2017; bi-weekly iteration cycles with automated test suites, version control, and staging environments on every engagement | 9+ |
| Large-scale project management | Multi-agency, multi-department engagements including PA DOH COVID vaccine eligibility (six-week sprint to 4.1M users), GPHIN migration, and SDP family communications platform | 7+ |
| High availability / mission-critical systems | 99.97% uptime on NJ Transit GTFS-RT pipeline; SOC 2 Type II and FedRAMP Moderate certifications; formal MTTF/MTTR documentation on all managed-service engagements | 6+ |
| Previous permitting software installations | City of Philadelphia L&I portal serving ~85,000 active business and trade licenses; conditional workflow logic, multi-user access, document upload, and permit generation fully in scope since 2016 | 9+ |
| Municipal, state, or federal information systems experience | City of Philadelphia (active since 2016), NJ Transit, PA Department of Health, School District of Philadelphia, Camden County, NJ; GSA 8(a) BPA | 9+ |
| Oracle-based application/database experience | L&I portal migrated from ColdFusion/Oracle legacy stack; ongoing Oracle integration maintained under 2027 contract | 9+ |
| Managing environment transitions | L&I ColdFusion-to-Django migration; GPHIN 47TB Teradata-to-Iceberg migration with zero patient-data downtime; NJ Transit vendor-system-to-in-house GTFS-RT migration | 7+ |
| Help desk operations | Tier 1/2 support included in all managed-service retainers; incident classification, SLA-based response times, and escalation procedures documented for each engagement | 7+ |
| Computer-based training development | User documentation, video tutorials, and training materials delivered for the L&I portal, SDP family communications platform, and Camden County open-data portal | 7+ |
| Architecture and design services | Three-tier web application architecture standard across all civic application deployments; documented in architecture decision records (ADRs) for each engagement | 9+ |
| Network monitoring and management | Infrastructure monitoring via Prometheus and Grafana on all managed-service engagements; bandwidth and I/O metrics tracked against defined thresholds | 6+ |
| Wide Area Network and Local Area Network integration | On-premises-to-cloud hybrid deployments for City of Philadelphia L&I and GPHIN; configured to function within existing client network environments | 7+ |
| Wireless technology development and implementation | Mobile-responsive progressive web applications tested on cellular and low-bandwidth connections; PA DOH vaccine tool designed for low-bandwidth use | 5+ |
| Peripheral device management | Field-facing mobile interfaces for L&I inspectors; scanner-compatible document upload workflows | 6+ |
| Web Content Accessibility | WCAG 2.2 AA testing before every deployment; published Accessibility Conformance Reports (ACRs) for every shipped application; third-party accessibility audit included in every engagement budget; zero critical findings on PA DOH independent audit | 9+ |
| Network infrastructure and procurement | Advisory and specification support for City of Philadelphia and PA DOH network environments; bandwidth requirements documentation standard practice | 7+ |
| Operations Support Systems services | Monitoring, alerting, and incident-response runbooks across all managed-service accounts | 6+ |
| PC and mainframe operating system management | Comprehensive QA and deployment on City-provided hardware configurations; on-premises deployment documentation for existing client equipment | 7+ |
| Installation services | All TWC deployments are installed on client-controlled infrastructure or client-designated cloud tenants; no proprietary hosting lock-in | 9+ |

TWC meets or exceeds the City’s preferred five-year threshold in all twenty technical experience areas.

---

## 4.5 Directly Relevant Capability: Philadelphia Permitting and Licensing

The most compelling qualification for this engagement stems from our **ten-year active relationship with the City of Philadelphia Department of Licenses and Inspections (L&I)**.

Since 2016, TWC has designed, built, and continuously maintained the public-facing licensing and inspections portal that serves approximately 85,000 active business and trade licenses. Key features include:

- **Multiple application types** with distinct conditional workflows routing applicants based on license category, business type, and submitted information—offering direct analogies to OCRSE's eight distinct event types
- **Permit and license generation and distribution** directly via the system
- **Post-submission document upload** and application modification governed by workflow controls
- **Real-time status tracking** for both applicants and L&I staff
- **Integration** with billing, payment processing, and City business licensing databases
- **Multi-user access** with configurable role-based permissions for L&I staff, supervisors, and external applicants
- Deployment on **City of Philadelphia infrastructure and networks**, optimized for existing City equipment and networks, avoiding the need for new hardware procurement under the contract
- **Compliance with City of Philadelphia addressing standards**, Century Date Standard, and WCAG 2.1/2.2 AA accessibility requirements

Our understanding of Philadelphia's permitting environment is grounded not in theoretical claims but in nine years of active and continuous delivery work with the L&I team, which currently continues through 2027. We have profound insights into the City's network operations, procurement processes, interdepartmental coordination dynamics, and integrations with payment processors, GIS systems, and business licensing processes.

No other bidder in this procurement can match our level of familiarity with Philadelphia's specific permitting infrastructure.

---

## 4.6 Past Performance References

The engagements outlined below represent our most directly comparable past performances. Contact information for references is provided below each engagement description and is also available in Appendix [_] of this proposal.

---

### 4.6.1 City of Philadelphia — Department of Licenses and Inspections Portal
**Contract period:** 2016–present (current contract through 2027)  
**Contract value:** Available upon request; over $100K annually; continuous engagement  
**Scope:** Full rebuild and ongoing maintenance of the public-facing licensing and inspections portal. Migrated from legacy ColdFusion/Oracle stack to Django/PostgreSQL with public APIs. Reduced average license-renewal completion time from 19 minutes to 4 minutes. Serves ~85,000 active business and trade licenses. Includes multi-application hosting, permit generation and distribution, real-time status tracking, document upload, conditional workflows, role-based access control, and payment integration, with deployment on the City's infrastructure.

**Relevance to this RFP:** Direct analog to all twelve mandatory functional requirements (A.1.1–A.1.12). Demonstrates ability to operate within the City of Philadelphia's network environment, adherence to City data standards, and delivery of multi-year maintenance and support.

**Reference:**  
> *Contact information to be confirmed and provided; City of Philadelphia Department of Licenses and Inspections, Philadelphia, PA*

---

### 4.6.2 Pennsylvania Department of Health — COVID-19 Vaccine Eligibility and Appointment Booking
**Contract period:** 2021  
**Contract value:** Available upon request  
**Scope:** Six-week sprint deployment of a multilingual eligibility-lookup tool, later extended to a full appointment-booking system. Served 4.1M unique users at peak demand. Designed for low-bandwidth and screen-reader use, with 0 critical accessibility findings on the independent audit. Required extensive coordination with county health systems across Pennsylvania.

**Relevance to this RFP:** Demonstrates rapid delivery of a high-stakes, high-volume public-facing application for a state government client. This experience is particularly relevant given the compressed implementation timeline leading up to the FIFA World Cup and MLB All-Star Game events in 2026. Highlights real-time intake management capabilities under surge-demand conditions that mirror OCRSE's anticipated permitting surge.

**Reference:**  
> *Contact information to be confirmed and provided; Pennsylvania Department of Health, Harrisburg, PA*

---

### 4.6.3 NJ Transit — Real-Time Bus Arrivals Refactor
**Contract period:** 2019–2021  
**Contract value:** Available upon request  
**Scope:** Replacement of an outdated vendor system with an in-house GTFS-RT pipeline feeding a public API and the official rider-facing application, achieving 99.97% uptime across the engagement. Open-sourced the `gtfs-rt-validator` tool, which is now employed by 22 transit agencies across North America.

**Relevance to this RFP:** Demonstrates the design and delivery of a mission-critical, high-availability system for a large regional public-sector client. Relevant to RFP requirements related to uptime metrics (T.7), performance indicators (T.8), and disaster recovery (T.5). Displays capabilities in managing vendor transitions while maintaining operational continuity.

**Reference:**  
> *Contact information to be confirmed and provided; NJ Transit, Newark, NJ*

---

### 4.6.4 School District of Philadelphia — Family Communications Platform
**Contract period:** 2023  
**Contract value:** Available upon request; City of Philadelphia affiliated entity; over $100K  
**Scope:** Consolidation of four overlapping vendor tools into a unified family communications platform supporting SMS, email, voice, and in-app messaging in 11 languages. Achieved sub-200ms broadcast latency to 200,000 recipients. Conformed to WCAG 2.2 AA standards. Integrated with existing School District of Philadelphia identity and directory systems.

**Relevance to this RFP:** Highlights internal communication capabilities including threaded message histories (relevant to A.1.7), multi-department coordination within a significant Philadelphia public institution, and SSO and legacy system integration. This project showcases our local institutional relationships and knowledge.

**Reference:**  
> *Contact information to be confirmed and provided; School District of Philadelphia, Philadelphia, PA*

---

### 4.6.5 Greater Philadelphia Health Information Network — Lakehouse Migration
**Contract period:** 2022–2024  
**Contract value:** Available upon request  
**Scope:** Migration of a 47TB on-premises Teradata warehouse to a HIPAA-compliant Iceberg lakehouse on AWS, ensuring zero downtime for patient data. BI tools were preserved via Trino and Apache Superset. Generated annual infrastructure cost savings of $1.1M for the client.

**Relevance to this RFP:** Demonstrates capacity for large-scale data migration and management of environmental transitions, directly relevant to shifting from OCRSE's current PDF-based process to the digital platform. Showcases effectiveness in cost-reduction outcomes, pertinent to the City’s interest in long-term cost efficiency (Evaluation Factor 10).

**Reference:**  
> *Contact information to be confirmed and provided; Greater Philadelphia Health Information Network, Philadelphia, PA*

---

### 4.6.6 Camden County, NJ — Open Data Platform
**Contract period:** 2024  
**Contract value:** Available upon request  
**Scope:** Development of a greenfield open data portal providing access to 80+ datasets through a public API and CKAN-style catalog, co-designed with three local journalism nonprofits and the county's data-literacy program. Delivered on schedule within a fixed-price contract.

**Relevance to this RFP:** Reflects our commitment to fixed-price delivery for municipal government clients, fulfilling the City's fixed-price proposal requirement (L.1). Highlights GIS-related data publishing, API design, and integration pertinent to A.1.10.

**Reference:**  
> *Contact information to be confirmed and provided; Camden County, NJ*

---

## 4.7 Philadelphia Regional Experience — Projects Over $100,000 (Last Five Years)

In accordance with Section 2.3 of the RFP's evaluation criteria, the following table summarizes all TWC engagements...
```
