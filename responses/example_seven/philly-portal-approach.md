# Technical Approach

## Tech Week Consortium Response to City of Philadelphia Project Intake #1140
### Special Event Permitting Software Solution

---

## 1. Overview and Solution Philosophy

Tech Week Consortium (TWC) proposes to design, build, deploy, and maintain a purpose-configured special event permitting platform for the City of Philadelphia's Office of City Representative and Special Events (OCRSE). Our solution replaces the current 8-page PDF/email workflow with a durable, accessible, fully integrated digital permitting system — purpose-built for Philadelphia's operational environment, its existing technology infrastructure, and the extraordinary demands of 2026.

We are not proposing a generic COTS product drop-in. We are proposing a **configurable platform built on TWC's open-source `civitas` framework**, hardened against real production load through our decade of civic application delivery in Philadelphia and across the region. Every component we propose is already in production somewhere in Philadelphia City government or in a comparable municipal environment. Nothing in this proposal is experimental.

Our approach is governed by four commitments that run through every section below:

1. **Operational continuity above all.** OCRSE manages approximately 1,700 applications per year under normal conditions. In 2026, FIFA World Cup and MLB All-Star Game events will compress that volume into a narrower window precisely as the new system goes live. Our implementation plan is sequenced so that OCRSE can process live applications in the new system before the peak begins — not after.

2. **No surprises on existing infrastructure.** The City is not purchasing hardware or network upgrades under this contract. We specify our infrastructure assumptions and performance requirements in full in Section 5, and we design our architecture to perform within them.

3. **Public money, public code.** All custom software delivered under this engagement will be licensed to the City of Philadelphia with full source code ownership and will be published under an open-source license, per our standard practice and consistent with SC.1 requirements. The City will not be locked into TWC for maintenance.

4. **Accessibility is a precondition, not a checklist item.** Every public-facing component passes WCAG 2.1 AA — and our internal standard of WCAG 2.2 AA — before it is deployed. A certified third-party accessibility audit is included in our fixed price.

---

## 2. Solution Architecture

### 2.1 Architectural Pattern

We propose a **three-tier web application architecture** deployed on the City's existing server infrastructure (or City-designated hosting environment), with clear separation among:

| Tier | Component | Technology |
|------|-----------|------------|
| Presentation | Public applicant portal; staff workflow interface; administrative configuration UI | Server-rendered Django templates with progressive enhancement; no mandatory JavaScript for core form submission |
| Application | Business logic, workflow engine, conditional routing, API layer, integration middleware | Django (Python 3.12+), Django REST Framework, Celery for async task processing |
| Data | Relational data store for application records, workflow state, user accounts, documents, audit logs | PostgreSQL 16+; MinIO or City-provisioned S3-compatible object store for document storage |

**Justification for three-tier architecture:** The separation of presentation from application logic allows the City to replace or extend the front-end (e.g., future mobile applications, department-specific dashboards) without touching business logic. The separation of application from data enables independent scaling of compute and storage — critical during 2026 surge periods — and supports a clean backup/restore boundary for disaster recovery. This architecture also aligns with the City's existing Django/PostgreSQL investment, documented in our ongoing L&I portal engagement (see Section 9, Past Experience).

We explicitly reject a two-tier (client-database) architecture for this use case. A two-tier pattern would expose database credentials to the client tier, limit our ability to implement API-based integrations, and make WCAG compliance significantly harder to achieve consistently.

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

All components are installed on existing City equipment and networks per T.1. No hardware procurement is required under this contract (see Section 5 for equipment specifications and any upgrade recommendations we identify as needed to meet performance standards).

### 2.3 Software Architecture Documentation (T.4)

The three-tier pattern is documented in full in our Software Architecture Document (SAD), delivered as a formal project deliverable at the conclusion of Phase 1 (Discovery and Architecture). The SAD includes:

- Component diagram with all services, data flows, and integration points
- Deployment diagram with server roles, network segments, and firewall rules
- Data model schema with entity-relationship diagram
- API specification (OpenAPI 3.1) for all integration endpoints
- Security architecture narrative (see Section 6)

---

## 3. Functional Capabilities (Appendix A.1 Requirements)

### 3.1 Multi-Application Hosting (A.1.1)

The platform supports an unlimited number of concurrent permit application types, each independently configurable. OCRSE currently manages eight distinct event types; we will configure all eight at launch, with the administrative tooling to create, modify, or retire application types without vendor involvement after go-live.

Each application type is defined by a configuration object specifying:

- Form fields (type, validation rules, conditional visibility)
- Required documentation (by event type and applicant-supplied inputs)
- Workflow routing (which departments receive routing, in what sequence or parallel)
- Fee schedule (flat, tiered, or calculated based on applicant inputs)
- Permit template (output format for generated permits)

Concurrent application management is enforced at the database level with row-level locking and optimistic concurrency control. Staff working on the same application from different departments see real-time state without collision.

### 3.2 Permit Generation and Distribution (A.1.2)

Permits are generated as structured PDF documents using a configurable template engine. Each permit type has an independently maintained template. Permit generation is triggered automatically upon workflow completion and final approval, or manually by authorized staff.

Generated permits are:

- Stored in the document store with a versioned record
- Delivered to the applicant via the platform's messaging interface (A.1.7) and email notification
- Available for download from the applicant's portal dashboard at any time
- Optionally delivered via configurable webhook to a City-designated endpoint

Permits carry a unique identifier and a machine-readable QR code linking to a public verification endpoint, allowing field inspection without portal access.

### 3.3 Service Request Creation (A.1.3)

When an applicant's inputs indicate a need for City services (e.g., traffic control, sanitation, police detail, street closures), the workflow engine automatically generates structured service requests and routes them to the appropriate City department queue. Each service request carries:

- Source application reference
- Event date, location (geocoded), and requested service window
- Applicant contact information
- Department-specific data fields configured per service type

Service requests are visible to both the originating department and OCRSE staff in the centralized dashboard (A.1.9). Status updates on service requests are reflected in the applicant's real-time status view (A.1.6).

### 3.4 Post-Submission Editing and Document Upload (A.1.4)

Applicants may edit submitted applications and upload supplemental documentation after submission, subject to workflow state controls. Specifically:

- Editing is permitted when the application is in any staff-configurable "open for revision" state (e.g., pending supplemental documentation, returned for correction)
- Editing is locked when the application is under active departmental review unless a staff member explicitly unlocks the record with a documented reason
- All edits are tracked in a complete, immutable audit log recording the previous value, new value, timestamp, and user identity
- Document uploads are versioned; prior uploads are retained and accessible to staff

This design gives OCRSE full control over when applicants can and cannot modify records, without requiring vendor intervention to configure those states.

### 3.5 Conditional Logic Workflows (A.1.5)

This is the core architectural feature of the platform. Our workflow engine implements a directed acyclic graph (DAG) model where each node is a workflow state and each edge is a transition condition. Conditions can reference:

- Any field value on the application form
- The output of any prior workflow stage
- Calendar conditions (date relative to event date, submission date, City holidays)
- External data lookups (e.g., business license status from the City's licensing database)
- Staff manual decision inputs

**Example — FIFA-related event routing:**
An applicant selecting "Block Party / Street Closure" within a FIFA Fan Fest impact zone automatically triggers:
1. Routing to the Streets Department queue (required for all street closures)
2. Routing to the Mayor's Office of Special Events coordination queue (FIFA impact zone flag)
3. A conditional documentation requirement for a FIFA/FIFA-affiliate coordination letter
4. A fee schedule override reflecting the surge pricing policy (if applicable)

None of these conditional branches require code changes. They are configured through the administrative UI and can be modified by trained City staff after go-live.

### 3.6 Real-Time Status Tracking (A.1.6)

Every application has a publicly visible status page (accessible without login via a unique application token, shareable by the applicant). Status updates are pushed in real time via WebSocket connections for logged-in users and via polling with a 30-second refresh maximum for unauthenticated token-based views.

Status information includes:

- Current workflow stage and responsible department
- Pending actions (items the applicant must complete)
- Estimated processing time (configurable by stage; displayed as a range, not a false-precision date)
- Message thread summary (see A.1.7)
- Service request statuses for each associated City department

Staff dashboards show application status across all active records with filter, sort, and saved-view capabilities.

### 3.7 External Communication (A.1.7)

A structured messaging interface is embedded directly in each application record. Messages are threaded by application and visible to both the applicant and authorized City staff. Key features:

- Full message history retained for the life of the application and archived per City records retention policy
- Email and optional SMS notification for new messages (applicant-configurable)
- File attachments supported in messages (with virus scanning via ClamAV or equivalent City-approved scanner)
- Staff can send messages individually or in bulk to all applicants in a filtered set (e.g., all applicants with events on a given date)
- All messages carry timestamp, sender identity, and read receipts for staff

No communication about an application leaves the system outside this channel without a staff-initiated action, creating a complete record for every application.

### 3.8 Internal Collaboration Tools (A.1.8)

The staff-facing interface includes a suite of interdepartmental collaboration tools:

- **Internal notes:** Staff can attach internal notes to any application, visible only to City personnel, with @-mention notification to specific colleagues
- **Departmental queues:** Each department has its own queue view showing only the applications and tasks assigned to it, with configurable priority flags
- **Cross-department routing history:** Every routing action is logged with timestamp, originating user, destination department, and any attached notes
- **Shared calendar:** A City-side calendar view shows all events by date, location, and current permit status, overlaid on a GIS base layer (see A.1.9, A.1.10)
- **Workload indicators:** Queue depth and average processing age are displayed to department supervisors for staffing awareness

These tools are designed specifically around multi-department coordination — the operational reality for OCRSE, which touches Parks, Streets, Police, Fire, and other agencies for major events.

### 3.9 Centralized Dashboards and Calendars (A.1.9)

Three distinct dashboard roles are provided out of the box, each configurable by OCRSE administrators:

| Dashboard | Primary Audience | Key Views |
|-----------|-----------------|-----------|
| Applicant Portal | Event organizers | My applications; pending actions; message inbox; permit downloads |
| Staff Operations | OCRSE and department reviewers | Active queue; upcoming events calendar; cross-department routing status; KPI summary |
| Administrative | OCRSE leadership and City Representative | Volume trends; processing time analytics; surge capacity indicators; exportable reports |

The events calendar supports iCal export and can be embedded in existing City intranet pages. GIS integration (A.1.10) overlays permitted event locations on a map view, allowing staff to identify geographic conflicts between concurrent events.

### 3.10 Third-Party Integrations (A.1.10)

Our integration architecture uses an API gateway pattern with a dedicated integration middleware layer. This isolates external system dependencies from core application logic — if a third-party system changes its API, only the integration adapter requires updating, not the application.

Planned integrations at launch:

| System | Integration Method | Scope |
|--------|--------------------|-------|
| City payment processor | REST API / hosted payment page redirect | Invoice generation, payment confirmation, reconciliation callbacks |
| City GIS platform (ArcGIS or equivalent) | ArcGIS REST API | Address geocoding, event location mapping, impact zone lookups |
| Business licensing database | REST API or database view (per City IT guidance) | License status verification at application submission |
| City SSO / Identity provider | SAML 2.0 or OAuth 2.0 (per City standard) | Staff single sign-on; applicant account federation where applicable |
| City email / notification infrastructure | SMTP relay or SendGrid-compatible API | Transactional notifications |

All integration endpoints are documented in the API specification deliverable. We request integration environment access during Phase 1 (Discovery) and will complete integration testing in our staging environment before any production deployment.

We have prior direct experience integrating with Philadelphia's L&I licensing database and GIS infrastructure through our ongoing portal engagement; we do not anticipate discovery risk on those integrations.

### 3.11 Invoice Management (A.1.11)

The platform includes a full invoice management module:

- Fees are calculated automatically based on applicant inputs and the configured fee schedule for each application type
- Draft invoices are generated at a configurable workflow stage and held for staff review before issuance
- Issued invoices are delivered to the applicant via the messaging interface and email
- Payment status is tracked in real time via callback from the City's payment processor
- Invoices, payment receipts, and adjustments are stored in the application record and available for export
- Reporting views show outstanding invoices, payment aging, and revenue by event type and period

The invoice module is designed to integrate with the City's existing payment processor rather than introduce a new payment channel.

### 3.12 Multi-User Access and Permissions (A.1.12)

Role-based access control (RBAC) is implemented at the application level with the following default role hierarchy:

| Role | Scope |
|------|-------|
| Applicant | Own applications only; cannot access other users' records |
| Department Reviewer | Applications routed to their department; read/write on assigned tasks |
| Department Supervisor | All applications in their department queue; user management for their department |
| OCRSE Staff | All applications across all departments; no administrative configuration |
| OCRSE Administrator | Full access including workflow configuration, form builder, fee schedules, and user management |
| System Administrator | Infrastructure-level access; managed by City IT |

Roles are configurable by OCRSE administrators without vendor involvement. Custom roles can be created with granular permission assignments. All permission changes are logged in the audit trail.

City SSO integration ensures that staff accounts are provisioned and deprovisioned in sync with the City's identity management system, eliminating the risk of orphaned accounts after staff departures.

---

## 4. Customization and Configuration Approach (A.3.2)

### 4.1 What City Staff Can Configure Without Vendor Involvement

A core design principle of our platform is that OCRSE should control its own workflows. After go-live and training, City staff with administrator-level access can independently:

- Add, modify, or retire permit application types
- Edit form fields, labels, help text, and validation rules
- Modify conditional logic routing rules
- Update fee schedules
- Edit permit templates (PDF layout and content)
- Create and modify departmental queues and assignment rules
- Generate and customize reports
- Add or modify notification templates (email/SMS)
- Create new user roles with custom permission sets

### 4.2 What Requires Vendor Involvement

Changes that involve new external system integrations, database schema migrations beyond the configuration layer, or modifications to the underlying workflow engine require TWC involvement. These changes are priced in Section 7 (Cost Structure) as a defined post-implementation services rate, under a clear change-order process. We are committed to providing a written estimate within five business days of any change request and to completing approved changes on a published timeline.

Our long-term goal is to expand the