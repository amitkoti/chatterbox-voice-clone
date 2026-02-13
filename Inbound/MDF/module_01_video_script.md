# Module 01 — Foundation Setup | Snowbrix Slide Deck

**Duration:** ~25 minutes
**Type:** Architecture + Hands-On
**Deliverable:** 4 databases, 4 warehouses, 5 RBAC roles

---

## Presentation Structure for /snowbrixSlides

Use this command:
```
/snowbrixSlides Create a presentation from this module outline
```

---

## Slide 1: Title Slide

**Layout:** Title Slide
**Title:** Module 01: Foundation Setup
**Subtitle:** Building the Metadata-Driven Ingestion Framework

---

## Slide 2: Agenda

**Layout:** Agenda Slide
**Title:** Today's Agenda

**Items:**
- **01** | Database Architecture | 8 min
- **02** | Warehouses & Cost Controls | 7 min
- **03** | Security & RBAC | 8 min
- **04** | Verification & Next Steps | 2 min

---

## Slide 3: Section Divider

**Layout:** Section Divider
**Title:** The Foundation

---

## Slide 4: The Challenge

**Layout:** Content Slide (3 points)
**Title:** What We're Building Today

**Points:**
- 4 databases with multi-layer architecture
- 4 purpose-specific warehouses with cost controls
- 5 functional roles with security built-in

---

## Slide 5: Why This Matters

**Layout:** Quote Slide
**Title:** (Quote)
**Quote:** "Everything we build in the next 10 modules sits on top of what we create here."
**Author:** Module Foundation Principle

---

## Slide 6: Section Divider

**Layout:** Section Divider
**Title:** Database Architecture

---

## Slide 7: Four-Database Structure

**Layout:** Content Slide (4 points)
**Title:** The Four-Database Architecture

**Points:**
- MDF_CONTROL_DB — The brain (config, procedures, monitoring)
- MDF_RAW_DB — Landing zone (data exactly as-is)
- MDF_STAGING_DB — Cleaned and validated data
- MDF_CURATED_DB — Business-ready data for analysts

---

## Slide 8: Why Separate Databases?

**Layout:** Three-Column Slide
**Title:** Benefits of Database Separation

**Column 1: Isolation**
**Points:**
- Workload separation
- Independent scaling
- Clear boundaries

**Column 2: Security**
**Points:**
- Granular access control
- Blast radius limitation
- Role-based permissions

**Column 3: Cost Tracking**
**Points:**
- Attribution by layer
- Budget monitoring
- Chargeback capabilities

---

## Slide 9: Control Database Schemas

**Layout:** Content Slide (4 points)
**Title:** MDF_CONTROL_DB — Four Schemas

**Points:**
- CONFIG — Configuration tables and settings
- AUDIT — Run history and error logs
- PROCEDURES — All stored procedures
- MONITORING — Dashboard views and metrics

---

## Slide 10: The RAW Layer Rule

**Layout:** Emphasis/Quote Slide
**Quote:** "Never transform data in RAW. It's your safety net."
**Author:** Data Engineering Best Practice

---

## Slide 11: Section Divider

**Layout:** Section Divider
**Title:** Warehouses & Cost Controls

---

## Slide 12: Four Warehouses

**Layout:** Content Slide (4 points)
**Title:** Purpose-Specific Warehouses

**Points:**
- MDF_INGESTION_WH (SMALL) — COPY INTO operations
- MDF_TRANSFORM_WH (MEDIUM) — Staging transformations
- MDF_MONITORING_WH (XSMALL) — Dashboard queries
- MDF_ADMIN_WH (SMALL) — Procedure execution

---

## Slide 13: Why Separate Warehouses?

**Layout:** Two-Column Slide
**Title:** Cost Attribution & Performance

**Left Column: Without Separation**
**Points:**
- One warehouse for everything
- No cost visibility
- Resource contention
- Hard to optimize

**Right Column: With Separation**
**Points:**
- Clear cost attribution
- Independent scaling
- Workload isolation
- Actionable insights

---

## Slide 14: Warehouse Configuration

**Layout:** Content Slide (3 points)
**Title:** Key Warehouse Settings

**Points:**
- AUTO_SUSPEND = 60 seconds (optimal for bursty loads)
- INITIALLY_SUSPENDED = TRUE (no immediate billing)
- MAX_CLUSTER_COUNT = 2 (parallel load capacity)

---

## Slide 15: Resource Monitors

**Layout:** Emphasis/Quote Slide
**Quote:** "Set resource monitors BEFORE you start loading data, not after you get the bill."
**Author:** Production Lesson

---

## Slide 16: Resource Monitor Thresholds

**Layout:** Content Slide (3 points)
**Title:** Financial Guardrails

**Points:**
- 75% usage — Notification alert sent
- 100% usage — Warehouse suspends automatically
- 110% usage — Force suspend, no exceptions

---

## Slide 17: Section Divider

**Layout:** Section Divider
**Title:** Security & RBAC

---

## Slide 18: Five Functional Roles

**Layout:** Content Slide (5 points)
**Title:** Role-Based Access Control

**Points:**
- MDF_ADMIN — Full control (framework owner)
- MDF_DEVELOPER — Modify procedures and configs
- MDF_LOADER — Execute COPY INTO, write to RAW
- MDF_TRANSFORMER — Read RAW, write STAGING/CURATED
- MDF_READER — Read-only access (monitoring + curated)

---

## Slide 19: Functional vs User Roles

**Layout:** Two-Column Slide
**Title:** Design Philosophy

**Left Column: Wrong Approach**
**Points:**
- User-specific roles (JOHN_ROLE)
- Everyone gets SYSADMIN
- Manual grants per object
- Unsustainable at scale

**Right Column: Right Approach**
**Points:**
- Functional roles (MDF_LOADER)
- Least-privilege access
- Future grants enabled
- Scales automatically

---

## Slide 20: Role Hierarchy

**Layout:** Paragraph Slide
**Title:** Inheritance Model

**Paragraphs:**
- "MDF_READER is the base role. MDF_LOADER inherits from READER. MDF_TRANSFORMER inherits from LOADER. MDF_ADMIN inherits from everything."
- "This hierarchical structure means granting permissions to the base role automatically propagates up the chain. Grant once, inherited everywhere."

---

## Slide 21: Future Grants

**Layout:** Content Slide (3 points)
**Title:** Why Future Grants Matter

**Points:**
- New tables automatically inherit permissions
- No manual grants for each object
- Set once, works forever

---

## Slide 22: Blast Radius Limitation

**Layout:** Two-Column Slide
**Title:** Security Isolation

**Left Column: If MDF_LOADER Compromised**
**Points:**
- Only RAW database affected
- Cannot modify STAGING
- Cannot touch CURATED
- Limited damage potential

**Right Column: Protection Layers**
**Points:**
- Role-based boundaries
- Database-level isolation
- Least-privilege design
- Defense in depth

---

## Slide 23: Section Divider

**Layout:** Section Divider
**Title:** Verification

---

## Slide 24: What We Built

**Layout:** Three-Column Slide
**Title:** Module 01 Deliverables

**Column 1: Databases**
**Points:**
- CONTROL (4 schemas)
- RAW
- STAGING
- CURATED

**Column 2: Warehouses**
**Points:**
- INGESTION (SMALL)
- TRANSFORM (MEDIUM)
- MONITORING (XSMALL)
- ADMIN (SMALL)

**Column 3: Security**
**Points:**
- 5 functional roles
- Future grants enabled
- Least-privilege access
- Resource monitors

---

## Slide 25: Production Architecture

**Layout:** Emphasis/Quote Slide
**Quote:** "This foundation is the same architecture we deploy for production clients. The scale changes. The design doesn't."
**Author:** Framework Principle

---

## Slide 26: Section Divider

**Layout:** Section Divider
**Title:** Next Steps

---

## Slide 27: Module 02 Preview

**Layout:** Content Slide (3 points)
**Title:** Coming Up Next: File Formats & Stages

**Points:**
- Define how framework reads different file types
- Configure stages for CSV, JSON, Parquet
- Set up external stage connections

---

## Slide 28: Action Items

**Layout:** Content Slide (3 points)
**Title:** Before Module 02

**Points:**
- Run all SQL scripts from Module 01
- Verify databases, warehouses, and roles
- Review the architecture diagram

---

## Slide 29: Thank You

**Layout:** Thank You Slide
**Title:** Thank You!
**Contact:** course@snowbrix.ai | snowbrix.ai/mdf

---

## Technical Notes for AI Image Generation

If using `--generate-images` flag:

**Slide 7 (Four-Database Architecture):**
- Type: architecture
- Prompt context: Four-layer database architecture, stacked layers

**Slide 12 (Four Warehouses):**
- Type: architecture
- Prompt context: Compute resources, warehouse sizing comparison

**Slide 18 (Five Functional Roles):**
- Type: architecture
- Prompt context: Role hierarchy pyramid, security layers

**Slide 24 (What We Built):**
- Type: features
- Prompt context: Three-pillar architecture (databases, compute, security)

---

## B-Roll Integration Notes

For video production, these slides sync with:

| Slides | B-Roll Type | Timestamp |
|--------|-------------|-----------|
| 1-5 | Architecture diagrams | 0:00-1:30 |
| 6-11 | Live SQL execution (databases) | 1:30-7:00 |
| 12-16 | Live SQL execution (warehouses) | 7:00-14:00 |
| 17-22 | Live SQL execution (roles) | 14:00-22:00 |
| 23-29 | Verification queries + recap | 22:00-25:00 |

---

## Usage Instructions

**Option 1: Generate entire deck**
```
/snowbrixSlides Create presentation from Module 01 Foundation Setup outline above
```

**Option 2: Generate with AI images**
```
/snowbrixSlides Create presentation with AI-generated backgrounds for architecture slides (7, 12, 18, 24)
```

**Option 3: Generate specific sections**
```
/snowbrixSlides Create slides 6-11 (Database Architecture section) from outline
```

---

## Presentation Metadata

- **Total Slides:** 29
- **Section Dividers:** 5
- **Content Slides:** 14
- **Two-Column Slides:** 3
- **Three-Column Slides:** 2
- **Quote/Emphasis Slides:** 4
- **Special Slides:** 1 (Agenda)

**Estimated Presentation Time:** 25-30 minutes (with speaker notes)
