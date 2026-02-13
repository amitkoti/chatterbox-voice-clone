"""
Generate Module 01 Foundation Setup presentation using Snowbrix layouts.
"""
import sys
import os

# Add video automation to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "_video_automation"))

from snowbrix_layouts_complete import SnowbrixLayoutsComplete

def main():
    # Output file
    output_file = "Inbound/MDF/Module_01_Foundation_Setup.pptx"

    print("Creating Module 01 Foundation Setup presentation...")

    # Initialize composer with logo and page numbers
    composer = SnowbrixLayoutsComplete(output_file, include_logo=True, include_page_numbers=True)

    # Slide 1: Title
    composer.add_title_slide(
        "Module 01: Foundation Setup",
        "Building the Metadata-Driven Ingestion Framework"
    )

    # Slide 2: Agenda
    composer.add_agenda_slide("Today's Agenda", [
        {"number": "01", "title": "Database Architecture", "duration": "8 min"},
        {"number": "02", "title": "Warehouses & Cost Controls", "duration": "7 min"},
        {"number": "03", "title": "Security & RBAC", "duration": "8 min"},
        {"number": "04", "title": "Verification & Next Steps", "duration": "2 min"}
    ])

    # Slide 3: Section Divider
    composer.add_section_divider("The Foundation")

    # Slide 4: What We're Building
    composer.add_content_slide("What We're Building Today", [
        "4 databases with multi-layer architecture",
        "4 purpose-specific warehouses with cost controls",
        "5 functional roles with security built-in"
    ])

    # Slide 5: Why This Matters
    composer.add_emphasis_slide(
        "Module Foundation Principle",
        "Everything we build in the next 10 modules sits on top of what we create here."
    )

    # Slide 6: Section Divider
    composer.add_section_divider("Database Architecture")

    # Slide 7: Four-Database Structure
    composer.add_content_slide("The Four-Database Architecture", [
        "MDF_CONTROL_DB — The brain (config, procedures, monitoring)",
        "MDF_RAW_DB — Landing zone (data exactly as-is)",
        "MDF_STAGING_DB — Cleaned and validated data",
        "MDF_CURATED_DB — Business-ready data for analysts"
    ])

    # Slide 8: Why Separate Databases?
    composer.add_three_column_slide(
        "Benefits of Database Separation",
        "Isolation",
        ["Workload separation", "Independent scaling", "Clear boundaries"],
        "Security",
        ["Granular access control", "Blast radius limitation", "Role-based permissions"],
        "Cost Tracking",
        ["Attribution by layer", "Budget monitoring", "Chargeback capabilities"]
    )

    # Slide 9: Control Database Schemas
    composer.add_content_slide("MDF_CONTROL_DB — Four Schemas", [
        "CONFIG — Configuration tables and settings",
        "AUDIT — Run history and error logs",
        "PROCEDURES — All stored procedures",
        "MONITORING — Dashboard views and metrics"
    ])

    # Slide 10: RAW Layer Rule
    composer.add_emphasis_slide(
        "Data Engineering Best Practice",
        "Never transform data in RAW. It's your safety net."
    )

    # Slide 11: Section Divider
    composer.add_section_divider("Warehouses & Cost Controls")

    # Slide 12: Four Warehouses
    composer.add_content_slide("Purpose-Specific Warehouses", [
        "MDF_INGESTION_WH (SMALL) — COPY INTO operations",
        "MDF_TRANSFORM_WH (MEDIUM) — Staging transformations",
        "MDF_MONITORING_WH (XSMALL) — Dashboard queries",
        "MDF_ADMIN_WH (SMALL) — Procedure execution"
    ])

    # Slide 13: Why Separate Warehouses?
    composer.add_two_column_slide(
        "Cost Attribution & Performance",
        [
            "One warehouse for everything",
            "No cost visibility",
            "Resource contention",
            "Hard to optimize"
        ],
        [
            "Clear cost attribution",
            "Independent scaling",
            "Workload isolation",
            "Actionable insights"
        ],
        left_title="Without Separation",
        right_title="With Separation"
    )

    # Slide 14: Warehouse Configuration
    composer.add_content_slide("Key Warehouse Settings", [
        "AUTO_SUSPEND = 60 seconds (optimal for bursty loads)",
        "INITIALLY_SUSPENDED = TRUE (no immediate billing)",
        "MAX_CLUSTER_COUNT = 2 (parallel load capacity)"
    ])

    # Slide 15: Resource Monitors
    composer.add_emphasis_slide(
        "Production Lesson",
        "Set resource monitors BEFORE you start loading data, not after you get the bill."
    )

    # Slide 16: Resource Monitor Thresholds
    composer.add_content_slide("Financial Guardrails", [
        "75% usage — Notification alert sent",
        "100% usage — Warehouse suspends automatically",
        "110% usage — Force suspend, no exceptions"
    ])

    # Slide 17: Section Divider
    composer.add_section_divider("Security & RBAC")

    # Slide 18: Five Functional Roles
    composer.add_content_slide("Role-Based Access Control", [
        "MDF_ADMIN — Full control (framework owner)",
        "MDF_DEVELOPER — Modify procedures and configs",
        "MDF_LOADER — Execute COPY INTO, write to RAW",
        "MDF_TRANSFORMER — Read RAW, write STAGING/CURATED",
        "MDF_READER — Read-only access (monitoring + curated)"
    ])

    # Slide 19: Functional vs User Roles
    composer.add_two_column_slide(
        "Design Philosophy",
        [
            "User-specific roles (JOHN_ROLE)",
            "Everyone gets SYSADMIN",
            "Manual grants per object",
            "Unsustainable at scale"
        ],
        [
            "Functional roles (MDF_LOADER)",
            "Least-privilege access",
            "Future grants enabled",
            "Scales automatically"
        ],
        left_title="Wrong Approach",
        right_title="Right Approach"
    )

    # Slide 20: Role Hierarchy
    composer.add_paragraph_slide("Inheritance Model", [
        "MDF_READER is the base role. MDF_LOADER inherits from READER. MDF_TRANSFORMER inherits from LOADER. MDF_ADMIN inherits from everything.",
        "This hierarchical structure means granting permissions to the base role automatically propagates up the chain. Grant once, inherited everywhere."
    ])

    # Slide 21: Future Grants
    composer.add_content_slide("Why Future Grants Matter", [
        "New tables automatically inherit permissions",
        "No manual grants for each object",
        "Set once, works forever"
    ])

    # Slide 22: Blast Radius Limitation
    composer.add_two_column_slide(
        "Security Isolation",
        [
            "Only RAW database affected",
            "Cannot modify STAGING",
            "Cannot touch CURATED",
            "Limited damage potential"
        ],
        [
            "Role-based boundaries",
            "Database-level isolation",
            "Least-privilege design",
            "Defense in depth"
        ],
        left_title="If MDF_LOADER Compromised",
        right_title="Protection Layers"
    )

    # Slide 23: Section Divider
    composer.add_section_divider("Verification")

    # Slide 24: What We Built
    composer.add_three_column_slide(
        "Module 01 Deliverables",
        "Databases",
        ["CONTROL (4 schemas)", "RAW", "STAGING", "CURATED"],
        "Warehouses",
        ["INGESTION (SMALL)", "TRANSFORM (MEDIUM)", "MONITORING (XSMALL)", "ADMIN (SMALL)"],
        "Security",
        ["5 functional roles", "Future grants enabled", "Least-privilege access", "Resource monitors"]
    )

    # Slide 25: Production Architecture
    composer.add_emphasis_slide(
        "Framework Principle",
        "This foundation is the same architecture we deploy for production clients. The scale changes. The design doesn't."
    )

    # Slide 26: Section Divider
    composer.add_section_divider("Next Steps")

    # Slide 27: Module 02 Preview
    composer.add_content_slide("Coming Up Next: File Formats & Stages", [
        "Define how framework reads different file types",
        "Configure stages for CSV, JSON, Parquet",
        "Set up external stage connections"
    ])

    # Slide 28: Action Items
    composer.add_content_slide("Before Module 02", [
        "Run all SQL scripts from Module 01",
        "Verify databases, warehouses, and roles",
        "Review the architecture diagram"
    ])

    # Slide 29: Thank You
    composer.add_thank_you_slide("Thank You!", "course@snowbrix.ai | snowbrix.ai/mdf")

    # Save presentation
    composer.save()

    print(f"\n✅ Presentation created successfully!")
    print(f"   Location: {output_file}")
    print(f"   Total slides: 29")
    print(f"   - Section dividers: 5")
    print(f"   - Content slides: 14")
    print(f"   - Two-column slides: 3")
    print(f"   - Three-column slides: 2")
    print(f"   - Quote slides: 4")
    print(f"   - Special slides: 1 (Agenda)")

if __name__ == "__main__":
    main()
