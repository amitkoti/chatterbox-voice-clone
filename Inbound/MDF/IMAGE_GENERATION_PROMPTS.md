# Module 01 - Image Generation Prompts for Google Imagen

Use these prompts with Google AI Studio: https://aistudio.google.com/

**Settings:**
- Model: Imagen 3.0
- Aspect Ratio: 16:9 (widescreen)
- Quality: High
- Safety: Default

**IMPORTANT:** Add this to ALL prompts:
```
NO TEXT IN IMAGE. NO LABELS. NO WATERMARKS. Visual elements only.
```

**Save images to:** `Inbound/MDF/images/`

**Note:** If generated images contain unwanted text, regenerate with the "NO TEXT" instruction emphasized.

---

## Slide 7: Four-Database Architecture

**Filename:** `slide_07_four_database_architecture.png`

**Prompt:**
```
Modern data engineering architecture diagram showing four stacked horizontal layers representing databases in a vertical flow.

Layer 1 (Top): MDF_CONTROL_DB - Control layer with icons for configuration, procedures, and monitoring. Use deep forest green (#2D5F3F) for this layer.

Layer 2: MDF_RAW_DB - Raw data landing zone with file/folder icons showing incoming data streams. Use sage green (#6B9080) for this layer.

Layer 3: MDF_STAGING_DB - Staging/transformation layer with data quality check symbols and validation icons. Use lighter sage green with terracotta (#C97D60) accents for processing elements.

Layer 4 (Bottom): MDF_CURATED_DB - Business-ready data layer with analytics icons, dashboard symbols, and user access indicators. Use cream (#FDF8F3) with forest green borders.

Connect layers with downward-flowing arrows in sage green showing data progression. Soft cream background (#FDF8F3). Clean, minimalist design with clear separation between layers. Professional, warm, educational aesthetic. 16:9 widescreen format.

Style: Modern data architecture diagram, isometric or 2.5D perspective, clean lines, no gradients, flat design with subtle shadows for depth.
```

---

## Slide 12: Four Warehouses Architecture

**Filename:** `slide_12_four_warehouses.png`

**Prompt:**
```
Four compute warehouse visualization showing different sizes and purposes.

Left section: MDF_INGESTION_WH (SMALL) - Show a compact server/warehouse icon with data ingestion arrows (files flowing in). Label "SMALL" clearly. Forest green (#2D5F3F) with size indicator "S".

Center-left: MDF_TRANSFORM_WH (MEDIUM) - Larger server icon with transformation symbols (gears, data processing icons). Label "MEDIUM". Sage green (#6B9080) with size indicator "M".

Center-right: MDF_MONITORING_WH (XSMALL) - Very small server icon with dashboard/monitoring symbols. Label "XSMALL". Light sage green with size indicator "XS".

Right section: MDF_ADMIN_WH (SMALL) - Compact server with admin tools icons (wrench, settings). Forest green with size indicator "S".

Show visual size differentiation - XSMALL should look noticeably smaller than SMALL, which should be smaller than MEDIUM. Include AUTO_SUSPEND clock icons below each warehouse. Soft cream background (#FDF8F3). Clean, modern server/compute icons. Cost meter or billing symbol at bottom showing different consumption levels. 16:9 format.

Style: Technical but approachable, modern data warehouse visualization, clear size hierarchy, professional coloring using Snowbrix palette.
```

---

## Slide 18: Five Functional Roles Hierarchy

**Filename:** `slide_18_role_hierarchy.png`

**Prompt:**
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

---

## Slide 24: Three-Pillar Architecture

**Filename:** `slide_24_three_pillars.png`

**Prompt:**
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

---

## Optional Alternative Images

### Slide 8: Benefits of Database Separation

**Filename:** `slide_08_database_benefits.png`

**Prompt:**
```
Split-screen comparison diagram showing three benefits of database separation.

Left third: "Isolation" - Show separate containers or boxes representing different workloads, with clear boundaries between them. Forest green (#2D5F3F) boxes with white icons inside.

Center third: "Security" - Display a shield icon with lock symbols, access control gates, and user role indicators. Sage green (#6B9080) shield with terracotta (#C97D60) security elements.

Right third: "Cost Tracking" - Show a clean bar chart or pie chart with cost attribution arrows pointing to different layers. Mix of forest green and sage green bars with terracotta accent highlights.

Soft cream background (#FDF8F3). Each section clearly labeled. Modern, professional iconography. Balanced composition with equal spacing. 16:9 format. Warm, educational aesthetic with Snowbrix color palette throughout.
```

### Slide 13: Cost Attribution Comparison

**Filename:** `slide_13_cost_comparison.png`

**Prompt:**
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

---

## Generation Checklist

- [ ] Go to https://aistudio.google.com/app/prompts/new_freeform
- [ ] Set model to Imagen 3.0
- [ ] Set aspect ratio to 16:9
- [ ] Copy prompt from above
- [ ] Generate image
- [ ] Download image
- [ ] Save to `Inbound/MDF/images/` with correct filename
- [ ] Repeat for all 4-6 images

---

## Quality Check

After generation, verify each image has:
- ✅ 16:9 aspect ratio (1920x1080 or similar)
- ✅ Snowbrix colors visible (#2D5F3F, #6B9080, #C97D60, #FDF8F3)
- ✅ Clean, professional appearance
- ✅ Clearly readable elements
- ✅ No unwanted text (text added in slides separately)
- ✅ Appropriate mood (warm, educational, professional)

If image doesn't meet criteria, regenerate with adjusted prompt.

---

## Next Steps

After generating all images:
1. Save to `Inbound/MDF/images/` folder
2. Run: `python update_presentation_with_images.py`
3. Review updated presentation
4. Adjust as needed
