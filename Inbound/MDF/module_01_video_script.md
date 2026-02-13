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

If using `--generate-images` flag, use these detailed prompts:

### Slide 7: Four-Database Architecture

**Full Prompt:**
```
Modern data engineering architecture diagram showing four stacked horizontal layers representing databases in a vertical flow.

Layer 1 (Top): MDF_CONTROL_DB - Control layer with icons for configuration, procedures, and monitoring. Use deep forest green (#2D5F3F) for this layer.

Layer 2: MDF_RAW_DB - Raw data landing zone with file/folder icons showing incoming data streams. Use sage green (#6B9080) for this layer.

Layer 3: MDF_STAGING_DB - Staging/transformation layer with data quality check symbols and validation icons. Use lighter sage green with terracotta (#C97D60) accents for processing elements.

Layer 4 (Bottom): MDF_CURATED_DB - Business-ready data layer with analytics icons, dashboard symbols, and user access indicators. Use cream (#FDF8F3) with forest green borders.

Connect layers with downward-flowing arrows in sage green showing data progression. Soft cream background (#FDF8F3). Clean, minimalist design with clear separation between layers. Professional, warm, educational aesthetic. 16:9 widescreen format.

Style: Modern data architecture diagram, isometric or 2.5D perspective, clean lines, no gradients, flat design with subtle shadows for depth.
```

### Slide 8: Benefits of Database Separation (Alternative Image)

**Full Prompt:**
```
Split-screen comparison diagram showing three benefits of database separation.

Left third: "Isolation" - Show separate containers or boxes representing different workloads, with clear boundaries between them. Forest green (#2D5F3F) boxes with white icons inside.

Center third: "Security" - Display a shield icon with lock symbols, access control gates, and user role indicators. Sage green (#6B9080) shield with terracotta (#C97D60) security elements.

Right third: "Cost Tracking" - Show a clean bar chart or pie chart with cost attribution arrows pointing to different layers. Mix of forest green and sage green bars with terracotta accent highlights.

Soft cream background (#FDF8F3). Each section clearly labeled. Modern, professional iconography. Balanced composition with equal spacing. 16:9 format. Warm, educational aesthetic with Snowbrix color palette throughout.
```

### Slide 9: Control Database Schemas (Alternative Image)

**Full Prompt:**
```
Four-quadrant layout representing the four schemas within MDF_CONTROL_DB database.

Top-left quadrant: CONFIG - Database icon with gear/settings symbols. Forest green (#2D5F3F) background.

Top-right quadrant: AUDIT - Magnifying glass over document icons, checklist symbols. Sage green (#6B9080) background.

Bottom-left quadrant: PROCEDURES - Code brackets { } or function icons, stored procedure symbols. Lighter sage green background.

Bottom-right quadrant: MONITORING - Dashboard with charts, metrics, alert bells. Terracotta (#C97D60) accents on cream background.

All quadrants connected by subtle lines showing relationships. Cream (#FDF8F3) overall background. Professional database schema visualization. Clean, modern iconography. 16:9 widescreen. Educational, approachable style.
```

### Slide 12: Four Warehouses Architecture

**Full Prompt:**
```
Four compute warehouse visualization showing different sizes and purposes.

Left section: MDF_INGESTION_WH (SMALL) - Show a compact server/warehouse icon with data ingestion arrows (files flowing in). Label "SMALL" clearly. Forest green (#2D5F3F) with size indicator "S".

Center-left: MDF_TRANSFORM_WH (MEDIUM) - Larger server icon with transformation symbols (gears, data processing icons). Label "MEDIUM". Sage green (#6B9080) with size indicator "M".

Center-right: MDF_MONITORING_WH (XSMALL) - Very small server icon with dashboard/monitoring symbols. Label "XSMALL". Light sage green with size indicator "XS".

Right section: MDF_ADMIN_WH (SMALL) - Compact server with admin tools icons (wrench, settings). Forest green with size indicator "S".

Show visual size differentiation - XSMALL should look noticeably smaller than SMALL, which should be smaller than MEDIUM. Include AUTO_SUSPEND clock icons below each warehouse. Soft cream background (#FDF8F3). Clean, modern server/compute icons. Cost meter or billing symbol at bottom showing different consumption levels. 16:9 format.

Style: Technical but approachable, modern data warehouse visualization, clear size hierarchy, professional coloring using Snowbrix palette.
```

### Slide 13: Cost Attribution Comparison (Alternative Image)

**Full Prompt:**
```
Side-by-side before/after comparison showing warehouse cost visibility.

LEFT HALF - "Without Separation":
- Single large gray blob representing one warehouse
- Question marks and confusion symbols around it
- Overlapping resource indicators showing contention
- Red warning triangle for "No visibility"
- Dark, chaotic appearance

RIGHT HALF - "With Separation":
- Four distinct color-coded warehouses in organized grid:
  * INGESTION (forest green #2D5F3F) - 20%
  * TRANSFORM (sage green #6B9080) - 50%
  * MONITORING (light sage) - 5%
  * ADMIN (terracotta #C97D60) - 25%
- Clear percentage labels showing cost attribution
- Clean pie chart or stacked bar showing breakdown
- Green checkmark for "Clear visibility"
- Organized, clean appearance

Center divider with arrow showing transformation from chaos to clarity. Soft cream background (#FDF8F3). Professional data visualization style. 16:9 widescreen format.
```

### Slide 18: Five Functional Roles Hierarchy

**Full Prompt:**
```
Role hierarchy pyramid diagram showing five levels of access control.

TOP (Apex): MDF_ADMIN - Crown or administrator icon, full access symbol. Forest green (#2D5F3F). Label: "Full Control"

LEVEL 2: MDF_DEVELOPER - Code/dev tools icon. Darker sage green. Label: "Modify Procedures & Configs"

LEVEL 3: MDF_TRANSFORMER - Data transformation symbol, ETL icon. Sage green (#6B9080). Label: "Read RAW, Write STAGING/CURATED"

LEVEL 4: MDF_LOADER - Upload/copy icons, file transfer symbols. Lighter sage green. Label: "Execute COPY INTO, Write RAW"

BOTTOM (Base): MDF_READER - Eye/view icon, read-only symbol. Terracotta (#C97D60) or light green. Label: "Read-Only Access"

Show inheritance arrows flowing upward from base to apex (READER → LOADER → TRANSFORMER → DEVELOPER → ADMIN). Each level progressively wider at base creating stable pyramid shape. Add permission icons at each level (lock open/closed, read/write symbols).

Soft cream background (#FDF8F3). Clean, modern security hierarchy visualization. Side annotation showing "Least Privilege" at bottom, "Full Access" at top. 16:9 widescreen format.

Style: Enterprise security diagram, professional iconography, clear visual hierarchy, Snowbrix color palette, educational aesthetic.
```

### Slide 22: Security Isolation Visualization (Alternative Image)

**Full Prompt:**
```
Security blast radius limitation diagram showing contained breach scenario.

LEFT SIDE - "If MDF_LOADER Compromised":
- Show RAW database layer highlighted in red warning color
- Breach/crack symbol on RAW layer
- STAGING and CURATED layers shown as protected/locked (green checkmarks)
- Visual barrier or firewall between RAW and other layers
- Limited blast radius indicated by red circle only around RAW

RIGHT SIDE - "Protection Layers":
- Four concentric security rings/shields:
  * Inner ring: Database-level isolation (forest green #2D5F3F)
  * Second ring: Role-based boundaries (sage green #6B9080)
  * Third ring: Least-privilege design (lighter sage)
  * Outer ring: Defense in depth (terracotta #C97D60)
- Each ring labeled clearly
- Shield icons at each layer

Center shows secured data vault symbol. Soft cream background (#FDF8F3). Professional security architecture diagram. Clear visual separation between compromised vs protected areas. 16:9 widescreen format.

Style: Enterprise security visualization, modern threat modeling diagram, reassuring color scheme emphasizing protection.
```

### Slide 24: Module 01 Deliverables - Three Pillars

**Full Prompt:**
```
Three-pillar architecture showing Module 01 complete deliverables in an ancient Greek temple style (metaphorical).

LEFT PILLAR - "Databases":
- Four stacked blocks representing 4 databases
- Top block: CONTROL (4 schemas icon) - forest green (#2D5F3F)
- Three blocks below: RAW, STAGING, CURATED - sage green gradient (#6B9080)
- Label: "4 Databases" at base

CENTER PILLAR - "Warehouses":
- Four server/compute icons of different sizes
- INGESTION (S), TRANSFORM (M) - forest green
- MONITORING (XS), ADMIN (S) - sage green
- Resource meter showing different sizes
- Label: "4 Warehouses" at base

RIGHT PILLAR - "Security":
- Shield icon with 5 role badges/emblems
- Lock symbols, key icons
- "Future Grants" checkmark
- Resource monitor gauge
- Terracotta (#C97D60) accents on sage green base
- Label: "5 Roles + Monitors" at base

All three pillars support a roof/capstone labeled "Production-Ready Foundation". Soft cream background (#FDF8F3). Professional, classical-modern hybrid style. Clean lines, organized structure. 16:9 widescreen format.

Style: Architectural metaphor showing stability and solid foundation, modern professional icons, Snowbrix color palette, educational and inspiring tone.
```

### General Guidelines for All Images:

**Color Palette (MUST USE):**
- Primary: #2D5F3F (forest green) - for main elements, emphasis
- Secondary: #6B9080 (sage green) - for supporting elements, accents
- Accent: #C97D60 (terracotta) - for highlights, warnings, important items
- Background: #FDF8F3 (soft cream) - always use as base
- Text: #4A4A4A (warm gray) or #FFFFFF (white on dark backgrounds)

**Style Requirements:**
- Aspect ratio: Always 16:9 widescreen
- Design style: Modern, clean, minimalist, professional
- Mood: Warm, educational, trustworthy, approachable
- Avoid: Gradients, shadows (except subtle), 3D effects, stock photo aesthetic
- Prefer: Flat design, line icons, clear hierarchy, plenty of white space

**Technical Specifications:**
- Resolution: 1920x1080 pixels minimum
- Format: PNG with transparency support
- Compression: Medium quality (good for presentations)
- Text: Avoid text in images (will be added in slide)

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
