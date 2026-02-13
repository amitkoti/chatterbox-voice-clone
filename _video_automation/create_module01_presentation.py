"""
Generate Module 01 Presentation
Metadata-Driven Ingestion Framework - Foundation Setup
"""

from slide_composer_snowbrix import SnowbrixSlideComposer
from datetime import datetime

# Create presentation
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_file = f"Module_01_Foundation_Setup_{timestamp}.pptx"
composer = SnowbrixSlideComposer(output_file, include_logo=True)

print("\nGenerating Module 01 Presentation...")
print("=" * 70)

# Slide 1: Title Slide
print("Creating slide 1: Title...")
composer.add_title_slide(
    "Module 01: Foundation Setup",
    "Metadata-Driven Ingestion Framework"
)

# Slide 2: Architecture - 4 Databases
print("Creating slide 2: Architecture...")
composer.add_content_slide(
    "Four-Database Architecture",
    key_points=[
        "MDF_CONTROL_DB - Brain: config tables, procedures, audit logs",
        "MDF_RAW_DB - Landing zone: raw data exactly as-is from source",
        "MDF_STAGING_DB - Cleaned and validated data with quality checks",
        "MDF_CURATED_DB - Business-ready data for analyst queries"
    ],
    notes="Isolation. Security. Cost tracking. Each database serves a specific purpose in the data pipeline."
)

# Slide 3: Database Benefits
print("Creating slide 3: Database isolation benefits...")
composer.add_content_slide(
    "Why Separate Databases?",
    key_points=[
        "Isolation - Workload separation prevents interference",
        "Security - Grant analysts CURATED access without exposing RAW",
        "Cost Tracking - Track spending per database layer",
        "Data Safety - RAW layer preserves original source data"
    ],
    notes="Design decision, not accident. Security and cost control from day one."
)

# Slide 4: Warehouses
print("Creating slide 4: Warehouses...")
composer.add_content_slide(
    "Four Purpose-Specific Warehouses",
    key_points=[
        "MDF_INGESTION_WH (SMALL) - I/O heavy COPY INTO operations",
        "MDF_TRANSFORM_WH (MEDIUM) - Compute-intensive transformations",
        "MDF_MONITORING_WH (XSMALL) - Lightweight dashboard queries",
        "MDF_ADMIN_WH (SMALL) - Procedure execution and admin tasks"
    ],
    notes="Cost attribution. When CFO asks why the bill is $40K, point to exact workload."
)

# Slide 5: Resource Monitors
print("Creating slide 5: Resource monitors...")
composer.add_content_slide(
    "Financial Guardrails",
    key_points=[
        "Set resource monitors BEFORE loading data, not after the bill",
        "75% threshold - notification alert sent to admins",
        "100% threshold - warehouse auto-suspends",
        "110% threshold - force suspend with no exceptions"
    ],
    notes="Bad query with auto-resume on XL warehouse at 3 AM = $18K by morning. Real scenario."
)

# Slide 6: RBAC Roles
print("Creating slide 6: RBAC roles...")
composer.add_content_slide(
    "Five Functional Roles",
    key_points=[
        "MDF_ADMIN - Full control for framework owner",
        "MDF_DEVELOPER - Modify procedures and configs",
        "MDF_LOADER - Execute COPY INTO, write to RAW only",
        "MDF_TRANSFORMER - Read RAW, write to STAGING/CURATED",
        "MDF_READER - Read-only: monitoring views and curated data"
    ],
    notes="Functional roles, not user roles. Least-privilege access with future grants."
)

# Slide 7: RBAC Design Principles
print("Creating slide 7: RBAC principles...")
composer.add_content_slide(
    "Security Design Principles",
    key_points=[
        "Functional roles over user roles (MDF_LOADER vs JOHN_ROLE)",
        "Least-privilege access - minimum permissions needed",
        "Future grants - new objects inherit permissions automatically",
        "Blast radius containment - compromised loader only affects RAW"
    ],
    notes="Production-grade security. Same architecture we deploy for enterprise clients."
)

# Slide 8: Recap
print("Creating slide 8: Module recap...")
composer.add_content_slide(
    "Module 01 Deliverables",
    key_points=[
        "4 databases with clear multi-layer architecture",
        "4 warehouses with auto-suspend and resource monitors",
        "5 functional roles with least-privilege and future grants",
        "Production-ready foundation for metadata-driven ingestion"
    ],
    notes="25 minutes. Production-grade architecture. Scale changes, design doesn't."
)

# Slide 9: Next Steps
print("Creating slide 9: Next module preview...")
composer.add_emphasis_slide(
    "Coming Next",
    quote="Module 02: File Formats & Stages - Defining how the framework reads CSV, JSON, and Parquet files"
)

# Save
composer.save()

print("\n" + "=" * 70)
print("PRESENTATION CREATED!")
print("=" * 70)
print(f"\nFile: {output_file}")
print(f"Slides: 9 (1 title + 7 content + 1 emphasis)")
print(f"Design: Snowbrix Professional")
print(f"Logo: Bottom right corner on all slides")
print("\nFeatures:")
print("  ✓ Cream + green color scheme")
print("  ✓ Forest green and sage green numbered circles")
print("  ✓ Snowbrixai logo on every slide")
print("  ✓ Professional data engineering aesthetic")
print("\nNext steps:")
print("  1. Open the presentation")
print("  2. (Optional) Generate AI images for architecture diagrams")
print("  3. Add custom diagrams if needed")
print("  4. Export to video or use for teaching")
print("\n" + "=" * 70)
