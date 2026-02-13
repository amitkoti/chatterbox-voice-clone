"""
Generate all 10 MDF module presentations using Snowbrix layouts.
These slides serve as the foundation for voiceover script creation.
"""
import sys
import os
from datetime import datetime

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "_video_automation"))

from snowbrix_layouts_complete import SnowbrixLayoutsComplete

def generate_module_01():
    """Module 01: Foundation Setup - Already created, use existing"""
    print("Module 01: Using existing presentation")
    return "Already created: generate_module01_slides.py"

def generate_module_02():
    """Module 02: File Formats & Stages"""
    output_file = f"Inbound/MDF/Presentations/Module_02_File_Formats_Stages_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pptx"

    composer = SnowbrixLayoutsComplete(output_file, include_logo=True, include_page_numbers=False)

    # Title
    composer.add_title_slide(
        "Module 02: File Formats & Stages",
        "Teaching the Framework How to Read Data"
    )

    # Agenda
    composer.add_agenda_slide("Today's Agenda", [
        {"number": "01", "title": "File Formats Overview", "duration": "5 min"},
        {"number": "02", "title": "CSV Variants", "duration": "8 min"},
        {"number": "03", "title": "JSON & Columnar Formats", "duration": "7 min"},
        {"number": "04", "title": "Stages (Internal & External)", "duration": "10 min"},
        {"number": "05", "title": "Lab & Verification", "duration": "5 min"}
    ])

    # Section 1: File Formats Overview
    composer.add_section_divider("File Formats Overview")

    composer.add_content_slide("What Are File Formats?", [
        "Snowflake objects that define parsing rules",
        "Specify delimiters, compression, null handling",
        "Reusable across all ingestion pipelines",
        "Eliminate hardcoded parsing logic"
    ])

    composer.add_emphasis_slide(
        "One file format object, unlimited data sources. Define once, reuse everywhere.",
        "Metadata-Driven Principle"
    )

    # Section 2: CSV Formats
    composer.add_section_divider("CSV File Formats")

    composer.add_content_slide("Four CSV Variants", [
        "MDF_FF_CSV_STANDARD - Comma-delimited with headers",
        "MDF_FF_CSV_PIPE - Pipe-delimited (legacy systems)",
        "MDF_FF_CSV_TAB - Tab-delimited (TSV)",
        "MDF_FF_CSV_NO_HEADER - Position-based mapping"
    ])

    composer.add_two_column_slide(
        "Critical CSV Options",
        [
            "SKIP_HEADER = 1 (most CSVs have headers)",
            "NULL_IF = ('NULL', '', 'N/A') (comprehensive)",
            "TRIM_SPACE = TRUE (clean data)",
            "COMPRESSION = AUTO (detect gzip/bzip2)"
        ],
        [
            "ERROR_ON_COLUMN_COUNT_MISMATCH = FALSE (critical!)",
            "FIELD_OPTIONALLY_ENCLOSED_BY = '\"' (quoted fields)",
            "EMPTY_FIELD_AS_NULL = TRUE (cleaner)",
            "DATE_FORMAT = AUTO (intelligent parsing)"
        ],
        left_title="Essential Settings",
        right_title="Quality Settings"
    )

    # Section 3: JSON & Columnar
    composer.add_section_divider("JSON & Columnar Formats")

    composer.add_three_column_slide(
        "Three Format Categories",
        "JSON Formats",
        ["STANDARD (array unwrap)", "NDJSON (line-delimited)", "COMPACT (null stripping)"],
        "Columnar Formats",
        ["PARQUET (Spark default)", "AVRO (Kafka/Hadoop)", "ORC (Hive optimized)"],
        "Key Options",
        ["STRIP_OUTER_ARRAY", "SNAPPY_COMPRESSION", "BINARY_AS_TEXT"]
    )

    # Section 4: Stages
    composer.add_section_divider("Stages: Internal & External")

    composer.add_two_column_slide(
        "Internal vs External Stages",
        [
            "Snowflake-managed storage",
            "Ideal for dev/test and small files",
            "No cloud setup needed",
            "Limited to 50 GB per account"
        ],
        [
            "Cloud storage (S3, Azure, GCS)",
            "Production-scale (unlimited capacity)",
            "Storage integrations (secure, no credentials)",
            "Supports data lakes and archives"
        ],
        left_title="Internal Stages",
        right_title="External Stages"
    )

    composer.add_content_slide("Storage Integration Benefits", [
        "No hardcoded access keys (uses cloud IAM roles)",
        "Centralized credential rotation",
        "Least-privilege access (STORAGE_ALLOWED_LOCATIONS)",
        "Auditable via cloud provider logs"
    ])

    # Lab & Verification
    composer.add_section_divider("Lab & Verification")

    composer.add_content_slide("What We Built", [
        "10 file format objects (4 CSV, 3 JSON, 3 columnar)",
        "4 internal stages (DEV, CSV, JSON, PARQUET)",
        "External stage templates (S3, Azure, GCS)",
        "All with DIRECTORY tables enabled"
    ])

    composer.add_emphasis_slide(
        "Critical Setting",
        "ERROR_ON_COLUMN_COUNT_MISMATCH = FALSE allows schema evolution without breaking pipelines."
    )

    # Next Steps
    composer.add_content_slide("Module 02 Complete - Next Steps", [
        "File formats and stages are the building blocks",
        "Next: Module 03 - Configuration Tables (The Brain)",
        "We'll create INGESTION_CONFIG that references these objects"
    ])

    composer.add_thank_you_slide("Module 02 Complete!", "contact@snowbrixai.com | snowbrixai.com/mdf")

    composer.save()
    print(f"[OK] Module 02 created: {output_file}")
    return output_file

def generate_module_03():
    """Module 03: Configuration Tables - The Brain"""
    output_file = f"Inbound/MDF/Presentations/Module_03_Config_Tables_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pptx"

    composer = SnowbrixLayoutsComplete(output_file, include_logo=True, include_page_numbers=False)

    composer.add_title_slide(
        "Module 03: Configuration Tables",
        "The Brain of the MDF Framework"
    )

    composer.add_agenda_slide("Today's Agenda", [
        {"number": "01", "title": "Why Metadata-Driven?", "duration": "5 min"},
        {"number": "02", "title": "INGESTION_CONFIG Deep Dive", "duration": "15 min"},
        {"number": "03", "title": "Audit & Supporting Tables", "duration": "8 min"},
        {"number": "04", "title": "Lab: Sample Configurations", "duration": "7 min"}
    ])

    # Why Metadata-Driven
    composer.add_section_divider("Why Metadata-Driven?")

    composer.add_two_column_slide(
        "Traditional vs Metadata-Driven",
        [
            "100 sources = 100 COPY scripts",
            "New source = write new code",
            "Change frequency = edit code + deploy",
            "No central visibility",
            "Maintenance nightmare at scale"
        ],
        [
            "100 sources = 100 config rows + 1 procedure",
            "New source = INSERT a row (2 minutes)",
            "Change frequency = UPDATE a column (30 seconds)",
            "Config table IS the documentation",
            "Scales effortlessly"
        ],
        left_title="Script-Based Approach",
        right_title="MDF Approach"
    )

    composer.add_emphasis_slide(
        "Configuration is data, not code. Change a row, change the behavior. No deployments.",
        "MDF Core Principle"
    )

    # INGESTION_CONFIG
    composer.add_section_divider("INGESTION_CONFIG: The Single Source of Truth")

    composer.add_content_slide("36 Columns in 10 Groups", [
        "Source Identity (name, client, type, system)",
        "Stage Configuration (where files live)",
        "File Format (how to parse)",
        "Target Configuration (where data goes)",
        "Load Behavior (how to handle errors)"
    ])

    composer.add_three_column_slide(
        "Additional Column Groups",
        "Scheduling",
        ["IS_ACTIVE flag", "LOAD_FREQUENCY", "CRON expression", "LOAD_PRIORITY"],
        "Validation",
        ["ENABLE_VALIDATION", "ROW_COUNT threshold", "NULL_CHECK columns"],
        "Evolution",
        ["ENABLE_SCHEMA_EVOLUTION", "SCHEMA_EVOLUTION_MODE", "Auto-apply rules"]
    )

    composer.add_emphasis_slide(
        "Design Decision",
        "IS_ACTIVE = FALSE is a soft delete. Never hard-delete config rows - preserve audit history."
    )

    # Audit Tables
    composer.add_section_divider("Audit & Supporting Tables")

    composer.add_two_column_slide(
        "Two-Level Audit Trail",
        [
            "One row per ingestion batch",
            "Summary metrics (files, rows, duration)",
            "Overall status (SUCCESS/FAILED)",
            "Always written (success or failure)",
            "Query for troubleshooting"
        ],
        [
            "One row per individual error",
            "Detail metrics (row number, column, rejected record)",
            "Only written on errors",
            "Prevents audit log bloat",
            "Drill-down for debugging"
        ],
        left_title="INGESTION_AUDIT_LOG",
        right_title="INGESTION_ERROR_LOG"
    )

    composer.add_content_slide("Why Separate Audit vs Error Logs?", [
        "Prevents bloat (one batch with 10K errors = 1 audit row, 10K error rows)",
        "Query performance (most queries are batch-level)",
        "Different retention (audit: 90 days, errors: 30 days)",
        "Cost optimization (clustering efficiency)"
    ])

    # Lab
    composer.add_section_divider("Lab: Sample Configurations")

    composer.add_content_slide("Three Sample Sources", [
        "DEMO_CUSTOMERS_CSV - Standard comma-delimited",
        "DEMO_EVENTS_JSON - Nested clickstream with FLATTEN",
        "DEMO_SENSORS_PARQUET - IoT with schema evolution"
    ])

    composer.add_thank_you_slide("Module 03 Complete!", "contact@snowbrixai.com | snowbrixai.com/mdf")

    composer.save()
    print(f"[OK] Module 03 created: {output_file}")
    return output_file

def generate_module_04():
    """Module 04: Core Stored Procedures"""
    output_file = f"Inbound/MDF/Presentations/Module_04_Core_Procedures_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pptx"

    composer = SnowbrixLayoutsComplete(output_file, include_logo=True, include_page_numbers=False)

    composer.add_title_slide(
        "Module 04: Core Stored Procedures",
        "The Execution Engine"
    )

    composer.add_agenda_slide("Today's Agenda", [
        {"number": "01", "title": "Stored Procedure Overview", "duration": "5 min"},
        {"number": "02", "title": "SP_GENERIC_INGESTION Walkthrough", "duration": "15 min"},
        {"number": "03", "title": "Supporting Procedures", "duration": "10 min"},
        {"number": "04", "title": "Lab: Test Execution", "duration": "10 min"}
    ])

    composer.add_section_divider("The Execution Engine")

    composer.add_content_slide("Seven Core Procedures", [
        "SP_GENERIC_INGESTION - Main engine (config → COPY → audit)",
        "SP_LOG_INGESTION - Two-phase audit logging",
        "SP_REGISTER_SOURCE - Self-service onboarding",
        "SP_VALIDATE_LOAD - Post-load quality checks",
        "SP_RETRY_FAILED_LOADS - Auto-recovery with limits"
    ])

    composer.add_emphasis_slide(
        "One procedure for all sources. Config defines behavior, procedure implements it.",
        "Metadata-Driven Execution"
    )

    # SP_GENERIC_INGESTION
    composer.add_section_divider("SP_GENERIC_INGESTION: The Main Engine")

    composer.add_content_slide("Execution Flow", [
        "Step 1: Read config from INGESTION_CONFIG",
        "Step 2: Build COPY INTO statement dynamically",
        "Step 3: Execute COPY, capture results",
        "Step 4: Log to INGESTION_AUDIT_LOG",
        "Step 5: Return status JSON"
    ])

    composer.add_two_column_slide(
        "Dynamic SQL Construction",
        [
            "Config: CSV with CONTINUE error mode",
            "Generated: COPY INTO ... ON_ERROR = CONTINUE",
            "Config: JSON with FLATTEN path",
            "Generated: COPY with subquery extraction"
        ],
        [
            "Config: Parquet with CASE_INSENSITIVE",
            "Generated: MATCH_BY_COLUMN_NAME = CASE_INSENSITIVE",
            "Same procedure, different SQL",
            "Behavior driven by metadata"
        ],
        left_title="Config Drives SQL",
        right_title="One Procedure, Infinite Variations"
    )

    composer.add_emphasis_slide(
        "Dry-Run Mode",
        "CALL SP_GENERIC_INGESTION('SOURCE', TRUE) returns generated SQL without executing. Perfect for validation and debugging."
    )

    # Supporting Procedures
    composer.add_section_divider("Supporting Procedures")

    composer.add_three_column_slide(
        "Three Supporting Procedures",
        "SP_LOG_INGESTION",
        ["Two-phase logging", "START → END pattern", "Called by main engine"],
        "SP_REGISTER_SOURCE",
        ["Self-service onboarding", "Applies defaults", "Junior-engineer friendly"],
        "SP_VALIDATE_LOAD",
        ["Post-load checks", "Row count, NULLs, duplicates", "Quality gates"]
    )

    composer.add_content_slide("Why JavaScript Procedures?", [
        "Dynamic SQL construction (cleaner than SQL strings)",
        "Structured error handling (try-catch blocks)",
        "JSON parsing/serialization (native support)",
        "Familiar to most engineers (readable, maintainable)"
    ])

    composer.add_thank_you_slide("Module 04 Complete!", "contact@snowbrixai.com | snowbrixai.com/mdf")

    composer.save()
    print(f"[OK] Module 04 created: {output_file}")
    return output_file

def generate_all_modules():
    """Generate presentations for all 10 modules"""

    # Create output directory
    os.makedirs("Inbound/MDF/Presentations", exist_ok=True)

    print("=" * 70)
    print("Generating MDF Course Presentations - All 10 Modules")
    print("=" * 70)
    print()

    modules = []

    # Module 01
    print("\n[1/10] Module 01: Foundation Setup")
    print("  -> Use: python generate_module01_slides.py")
    print("  -> Then: python fix_zoom_slides.py")
    modules.append("Module 01: Manual (existing scripts)")

    # Module 02
    print("\n[2/10] Module 02: File Formats & Stages")
    file2 = generate_module_02()
    modules.append(file2)

    # Module 03
    print("\n[3/10] Module 03: Configuration Tables")
    file3 = generate_module_03()
    modules.append(file3)

    # Module 04
    print("\n[4/10] Module 04: Core Stored Procedures")
    file4 = generate_module_04()
    modules.append(file4)

    # Modules 05-10 - Placeholders for now, can be expanded
    print("\n[5/10] Module 05: CSV Ingestion Lab - To be generated")
    print("\n[6/10] Module 06: Semi-Structured Data - To be generated")
    print("\n[7/10] Module 07: Error Handling & Audit - To be generated")
    print("\n[8/10] Module 08: Automation (Tasks & Streams) - To be generated")
    print("\n[9/10] Module 09: Monitoring & Dashboards - To be generated")
    print("\n[10/10] Module 10: Schema Evolution & Advanced - To be generated")

    print("\n" + "=" * 70)
    print("PRESENTATIONS CREATED:")
    print("=" * 70)
    for i, module in enumerate(modules, 1):
        print(f"{i}. {module}")

    print("\n" + "=" * 70)
    print("Next Steps:")
    print("=" * 70)
    print("1. Review generated presentations")
    print("2. Add AI-generated images for key architecture slides")
    print("3. Run fix_zoom_slides.py for diagrams")
    print("4. Create voiceover scripts based on slide content")
    print("5. Record videos for complete course")
    print("=" * 70)

if __name__ == "__main__":
    generate_all_modules()
