# RFP Analysis: City of Philadelphia Special Event Permitting Software Solution

## PROJECT OVERVIEW
- **Issuing Agency:** Office of City Representative and Special Events (OCRSE)
- **Project Intake #:** 1140
- **Proposal Deadline:** March 17, 2026, 5:00 PM
- **Anticipated Project Start:** May 15, 2026
- **Volume:** ~1,700 special event applications annually

---

## SECTION 1: REQUIREMENTS

### 1.1 Functional Requirements (Appendix A.1)

| Req # | Requirement | Description |
|-------|-------------|-------------|
| A.1.1 | Multi-application hosting | Support multiple permit application types and concurrent management |
| A.1.2 | Permit generation and distribution | Create, manage, and issue permits directly through the system |
| A.1.3 | Service request creation | Generate service requests/tasks based on applicant inputs |
| A.1.4 | Post-submission editing | Allow modification of submitted applications and document uploads (with workflow controls) |
| A.1.5 | Conditional logic workflows | Configurable workflows with conditional logic adapting routing, required fields, and documentation |
| A.1.6 | Real-time status tracking | Transparent real-time status updates for applicants and City personnel |
| A.1.7 | External communication | Direct messaging between applicants and City with retained message history |
| A.1.8 | Internal collaboration tools | Communication/collaboration features for interdepartmental coordination |
| A.1.9 | Centralized dashboards and calendars | Unified views of applications, events, and schedules |
| A.1.10 | Third-party integrations | Integration with billing/payment, GIS, business licensing, supplemental applications via API, SSO, webhooks, file exchange |
| A.1.11 | Invoice management | Tools for generating and managing invoices |
| A.1.12 | Multi-user access and permissions | Multiple user profiles with configurable permission levels/roles |

### 1.2 Training and Support Requirements (Appendix A.2)

| Req # | Requirement | Description |
|-------|-------------|-------------|
| A.2.1 | Training delivery | Comprehensive sessions covering: system navigation, application processing, report generation, troubleshooting |
| A.2.2 | Training materials | User manuals/guides, video tutorials/session recordings, FAQs |
| A.2.3 | Training plan | Detailed plan specifying format, schedule, scope, audience groups, and assumptions |

### 1.3 Technical/Infrastructure Requirements

| Category | Requirement |
|----------|-------------|
| Deployment | Installed on existing City equipment and networks |
| Performance standards | Must specify throughput, processing volumes, response times on City's current environment |
| Equipment upgrades | Must identify any necessary upgrades with detailed specifications and dual performance standards (with/without upgrades) |
| Hardware/network services | NOT included in contract scope; City will procure separately |
| Solution type | COTS, configurable, custom, or hybrid acceptable |
| Architecture | Must describe software architecture (2-tier/3-tier), workflow processing, reporting infrastructure, archiving/auditing plan |
| Disaster recovery | Must outline disaster recovery plan |
| Bandwidth | Must specify anticipated bandwidth requirements |

### 1.4 Performance Standards Required in Proposal (Vol. 2, Sec. 3)

- Server Disk I/O
- Transactions Per Minute (TPM)
- Page Swapping
- Response Time
- Throughput
- System Availability (mean time to failure / mean time to repair)
- Bandwidth utilization (bytes per second under all load conditions)

### 1.5 IT Standards Compliance (Appendix K)

| Standard | Requirement |
|----------|-------------|
| Data Requirements | Data access, master data, metadata standards, date formats, geospatial data, data protection and retention |
| Addressing Standards | All database systems maintaining property addresses |
| General Technical Standards | Resilience and security for IT systems |
| Digital Standards | Design, code, and content guidelines for web applications |
| Web Accessibility | WCAG 2.1 AA compliance required for all City-facing web content |
| Security | Confidentiality, integrity, and availability protections for all City Data |

### 1.6 Contract/Legal Requirements

| Requirement | Details |
|-------------|---------|
| Fixed price proposal | All costs must be fixed price; no time-and-materials or cost-plus |
| Maintenance and support | Minimum 1 year included; pricing required for years 2–5; 5-year availability guarantee |
| Warranty | Minimum 1-year turnkey warranty from final acceptance; City prefers 2+ years |
| Source code | Delivery and ownership of custom code; escrow required for proprietary code at no expense to City |
| Insurance – General Liability | $1M per occurrence; $2M aggregate |
| Insurance – Professional Liability | $1M with ≤$50K deductible; 2-year tail coverage |
| Insurance – Cyber Liability | $1M per claim/aggregate; 2-year extended discovery |
| Insurance – Workers' Comp | Statutory limits |
| Insurance – Auto | $1M per occurrence |
| Retainage | 20% withheld until final acceptance |
| Proposal binding period | 180 days from submission date |
| Data breach notification | Within 24 hours of discovery |
| Security audits | SSAE 18, SOC 2 Type II and SOC 1 reports, up to once per year |
| Equal Benefits Ordinance | Required for contracts >$250K (Chapter 17-1900) |
| Campaign contribution disclosure | Required per Chapter 17-1400 |
| Tax clearance | Must submit Philadelphia Tax and Regulatory Status and Clearance Statement |
| Document preparation fee | Per schedule (e.g., $1,500 for for-profit contracts >$1M) |

### 1.7 Proposal Submission Requirements

| Component | Requirement |
|-----------|-------------|
| Submission platform | eContract Philly (electronic only) |
| Volume 1 | Qualifications (company description, technical qualifications, financial qualifications) |
| Volume 2 | Technical approach and cost proposal (5 sections) |
| Requirements Compliance Matrix | Excel spreadsheet per Appendix D; must be completed for all A.1 and A.2 requirements |
| Implementation plan | Detailed methodology, SOW, project schedule, milestone payment schedule |
| Cost proposal | Line-item fixed pricing per Appendix C template |
| AI use certification | Must certify human expert review and lawful ownership of AI-assisted content |

---

## SECTION 2: EVALUATION CRITERIA

### 2.1 Formal Evaluation Factors (Section 2.11.4)

| Factor | Description |
|--------|-------------|
| 1 | **Project understanding and methodology** – Detail and accuracy of proposed scope, SOW, and implementation plan |
| 2 | **Campaign contribution eligibility** – Compliance with Chapter 17-1400 |
| 3 | **Prior experience** – References from comparable projects; demonstrated ability to deliver |
| 4 | **Solution quality and fitness** – Impact on department operations; demonstrated operational efficiency |
| 5 | **Skill, reputation, timeliness** – Financial and technical qualifications; commitment to project timeline |
| 6 | **Incumbent transition benefit** – Operational continuity considerations |
| 7 | **Small/new business development** – Promotion of competitive development and experience for smaller firms |
| 8 | **Cost** – Lower overall cost; material but not sole or determining factor |
| 9 | **Administrative efficiency** – Requires less City oversight |
| 10 | **Long-term cost effectiveness** – Anticipated total cost of ownership |
| 11 | **Prequalification requirements** – Meets all RFP qualification criteria |
| 12 | **Local Business Entity/Local Impact** – Certification per Executive Order 04-12 |

> ⚠️ **Note:** No weighting or priority order is assigned to these factors. The City retains sole discretion in evaluation and award.

### 2.2 Volume 1 Evaluation (Qualifications)

| Area | Details |
|------|---------|
| Technical qualifications | Minimum 5 years preferred in: large-scale database design, WAN/LAN integration, software design/testing, help desk, CBT development, large-scale project management, high availability systems, wireless technology, municipal information systems, Oracle-based applications, network infrastructure, architecture/design |
| Financial capacity | Audited financial statements (3 years), bank reference, bankruptcy disclosures, SEC filings (10-K, 8-K) |
| References | Comparable size, complexity, and scope; must include current owner contact and reason for reference |
| Philadelphia experience | Projects >$100K in Philadelphia in last 5 years; City contracts; government contracts |

### 2.3 Volume 2 Evaluation (Technical and Cost)

| Section | Evaluation Focus |
|---------|-----------------|
| Organization & Management | Org charts, key personnel resumes, system development methodology |
| Scope of Work Plan | Task completeness, effort estimates, personnel assignments, assumptions |
| Technical Proposal | Architecture, infrastructure, performance standards, disaster recovery, bandwidth, security |
| Cost Proposal | Line-item pricing per Appendix C; fixed price; no taxes |
| Requirements Compliance Matrix | Complete, accurate response to all A.1 and A.2 requirements |

### 2.4 Responsiveness Standards

A proposal may be deemed non-responsive and rejected without evaluation if:
- Not submitted via eContract Philly by deadline
- Requirements Compliance Matrix is missing or materially incomplete
- Does not provide fixed-price proposal
- Does not identify each work item by line item
- Applicant fails to demonstrate required qualifications
- Campaign contributions exceed permissible thresholds

---

## SECTION 3: RISKS

### 3.1 Timeline and Scheduling Risks

| Risk | Description | Severity |
|------|-------------|----------|
| **Compressed timeline** | RFP issued February 17; project start anticipated May 15 – only ~3 months from RFP to contract | High |
| **2026 major events pressure** | MLB All-Star Game and FIFA World Cup create hard deadlines for system readiness | High |
| **Schedule slippage** | Milestone payment schedule tied to acceptance; delays affect cash flow and project completion | Medium |
| **30-day reliability period** | Must operate 30 consecutive days without material defect before final acceptance; failure restarts clock | Medium |

### 3.2 Technical Risks

| Risk | Description | Severity |
|------|-------------|----------|
| **Legacy infrastructure compatibility** | System must run on existing City equipment; performance may be constrained | High |
| **Integration complexity** | Required integrations with payment processing, GIS, business licensing, SSO create multiple failure points | High |
| **Eight event types with different workflows** | Complex conditional logic required; misconfiguration could break routing | Medium |
| **Multi-department coordination** | Cross-departmental workflows increase change management complexity | Medium |
| **Performance standards on current hardware** | Must specify performance with and without upgrades; risk of underperformance if City does not procure upgrades | Medium |
| **Data migration** | Transition from PDF-based process; historical data may need to be migrated or reconciled | Medium |

### 3.3 Contractual and Legal Risks

| Risk | Description | Severity |
|------|-------------|----------|
| **20% retainage held until final acceptance** | Significant cash flow impact for vendor; final acceptance may be delayed | High |
| **Broad City discretion** | City may reject any proposal, modify terms, negotiate with multiple vendors, or cancel RFP without obligation | High |
| **Proposal binding for 180 days** | Vendor locked into pricing and terms for 6 months without guarantee of award | Medium |
| **Turnkey warranty and support obligation** | Vendor solely responsible for all elements including third-party components | High |
| **Source code escrow obligations** | Proprietary software must be escrowed at vendor's expense; ongoing update obligations | Medium |
| **Intellectual property indemnification** | Vendor must defend and indemnify against any third-party IP claims at its own expense | High |
| **Data breach liability** | 24-hour notification requirement; recreation of lost data at no charge; breach response obligations | High |
| **Campaign contribution ineligibility** | Contributions exceeding Chapter 17-1404(1) thresholds render vendor ineligible | Medium |
| **Liquidated damages** | 10% of contract value for campaign contribution violations or material disclosure misstatements | High |

### 3.4 Financial Risks

| Risk | Description | Severity |
|------|-------------|----------|
| **Fixed price requirement** | All costs must be fixed; scope changes handled via Change Order only; risk of scope creep | High |
| **Document preparation fee** | Up to $1,500 for contracts over $1M (plus potential double fee for extensive negotiation) | Low |
| **Post-implementation modification costs** | Vendor must disclose pricing model for changes after go-live; City may prefer self-service configuration | Medium |
| **Hardware upgrade costs not in scope** | If City does not procure recommended hardware upgrades, performance risk falls to vendor's contractual standards | Medium |

### 3.5 Compliance and Regulatory Risks

| Risk | Description | Severity |
|------|-------------|----------|
| **WCAG 2.1 AA compliance** | Public-facing components must meet accessibility standards; retrofitting is costly | Medium |
| **Philadelphia tax compliance** | Vendor and all subcontractors must be in tax compliance; non-compliance can disqualify | Medium |
| **Equal Benefits Ordinance** | Contracts >$250K require equal benefits for domestic partners; non-compliance is material breach | Medium |
| **Chapter 17-1400 disclosures** | Quarterly campaign contribution disclosures required throughout contract term | Low |
| **Transparency demographic disclosures** | Contracts ≥$94K require workforce and board demographic data submission before conformance | Low |

### 3.6 Operational and Organizational Risks

| Risk | Description | Severity |
|------|-------------|----------|
| **Change management across departments** | Multiple City agencies must adopt new workflows; resistance may slow adoption | High |
| **Training adequacy** | Insufficient training for City personnel could undermine system effectiveness | Medium |
| **Applicant onboarding** | Public users (event organizers) must transition from PDF submissions; may require outreach | Medium |
| **Key personnel substitution** | City must approve any substitution of key personnel proposed in the winning bid | Medium |
| **Subcontractor vetting** | All subcontractors subject to City approval; non-compliant subcontractors must be replaced | Low |

---

## SUMMARY MATRIX

| Category | Count |
|----------|-------|
| Functional requirements | 12 |
| Training/support requirements | 3 |
| Technical/infrastructure requirements | 8+ |
| Evaluation factors | 12 |
| Identified risks | 28 |