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

def generate_module_05():
    """Module 05: CSV Ingestion Lab"""
    output_file = f"Inbound/MDF/Presentations/Module_05_CSV_Ingestion_Lab_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pptx"

    composer = SnowbrixLayoutsComplete(output_file, include_logo=True, include_page_numbers=False)

    composer.add_title_slide(
        "Module 05: CSV Ingestion Lab",
        "End-to-End Hands-On Pipeline"
    )

    composer.add_agenda_slide("Lab Flow", [
        {"number": "01", "title": "Create Target Tables", "duration": "8 min"},
        {"number": "02", "title": "Upload CSV Files", "duration": "7 min"},
        {"number": "03", "title": "Run Ingestion", "duration": "5 min"},
        {"number": "04", "title": "Verify Results", "duration": "10 min"}
    ])

    composer.add_section_divider("First Pure Hands-On Lab")

    composer.add_content_slide("Lab Scenario", [
        "Three CSV sources: customers, orders, products",
        "Prove the framework works (no new objects)",
        "One procedure call loads all three",
        "Complete audit trail automatically"
    ])

    composer.add_content_slide("Sample Data Overview", [
        "customers.csv - 15 rows (master data)",
        "orders.csv - 20 rows (transactions)",
        "products.csv - 12 rows (catalog)",
        "Total: 47 rows across 3 tables"
    ])

    composer.add_section_divider("Target Tables")

    composer.add_content_slide("MDF Metadata Columns", [
        "_MDF_FILE_NAME - Source file for lineage",
        "_MDF_FILE_ROW - Row number for debugging",
        "_MDF_LOADED_AT - Load timestamp",
        "Added to every RAW table automatically"
    ])

    composer.add_section_divider("Upload & Verify")

    composer.add_two_column_slide(
        "Upload Methods",
        [
            "SnowSQL command line",
            "PUT file://path @stage",
            "Good for automation",
            "Supports wildcards"
        ],
        [
            "Snowsight web UI",
            "Data → Stages → Upload",
            "Good for ad-hoc files",
            "Visual file browser"
        ],
        left_title="Method 1: CLI",
        right_title="Method 2: UI"
    )

    composer.add_content_slide("Preview Before Loading", [
        "SELECT $1, $2, $3 FROM @stage/file LIMIT 5",
        "Catches schema mismatches early",
        "Verifies delimiter and format",
        "Always preview first in production"
    ])

    composer.add_section_divider("Run Ingestion")

    composer.add_emphasis_slide(
        "The Moment of Truth",
        "CALL SP_GENERIC_INGESTION('ALL', FALSE); -- One call, three sources loaded"
    )

    composer.add_content_slide("What Just Happened?", [
        "Procedure read 3 config rows",
        "Built 3 dynamic COPY commands",
        "Executed all 3 loads in sequence",
        "Logged 3 audit entries automatically",
        "Returned JSON status summary"
    ])

    composer.add_section_divider("Verification")

    composer.add_three_column_slide(
        "Three-Layer Verification",
        "Audit Log",
        ["Check RUN_STATUS", "Verify row counts", "Review duration"],
        "Loaded Data",
        ["COUNT(*) per table", "Sample rows", "Check metadata columns"],
        "Lineage",
        ["Trace to source file", "Find row numbers", "Timestamp verification"]
    )

    composer.add_content_slide("Lab Success Criteria", [
        "All 3 sources show RUN_STATUS = SUCCESS",
        "Row counts match: 15 + 20 + 12 = 47 total",
        "No errors in INGESTION_ERROR_LOG",
        "Metadata columns populated correctly"
    ])

    composer.add_content_slide("Challenge Exercise", [
        "Add a 4th source (shipments.csv)",
        "Use SP_REGISTER_SOURCE for self-service",
        "Upload file and run ingestion",
        "Verify in audit log (10 min exercise)"
    ])

    composer.add_thank_you_slide("Module 05 Complete!", "contact@snowbrixai.com | snowbrixai.com/mdf")

    composer.save()
    print(f"[OK] Module 05 created: {output_file}")
    return output_file

def generate_module_06():
    """Module 06: Semi-Structured Data"""
    output_file = f"Inbound/MDF/Presentations/Module_06_Semi_Structured_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pptx"

    composer = SnowbrixLayoutsComplete(output_file, include_logo=True, include_page_numbers=False)

    composer.add_title_slide(
        "Module 06: Semi-Structured Data",
        "JSON & Parquet with FLATTEN"
    )

    composer.add_agenda_slide("Module Overview", [
        {"number": "01", "title": "Schema-on-Read Concept", "duration": "5 min"},
        {"number": "02", "title": "JSON Ingestion & FLATTEN", "duration": "15 min"},
        {"number": "03", "title": "Parquet with Column Matching", "duration": "10 min"},
        {"number": "04", "title": "Lab Exercises", "duration": "10 min"}
    ])

    composer.add_section_divider("Schema-on-Read")

    composer.add_two_column_slide(
        "Schema-on-Write vs Schema-on-Read",
        [
            "CSV approach: Define columns first",
            "Data must match schema exactly",
            "New column = load breaks",
            "Type safety from the start",
            "Good for structured, stable data"
        ],
        [
            "JSON approach: Load into VARIANT first",
            "Schema extracted at query time",
            "New field = just appears in JSON",
            "Flexibility, handles schema drift",
            "Good for dynamic, evolving data"
        ],
        left_title="Schema-on-Write (CSV)",
        right_title="Schema-on-Read (JSON/Parquet)"
    )

    composer.add_section_divider("JSON Ingestion")

    composer.add_content_slide("JSON File Formats", [
        "STRIP_OUTER_ARRAY = TRUE (unwrap [{...}] into rows)",
        "STRIP_NULL_VALUES = FALSE (preserve schema)",
        "IGNORE_UTF8_ERRORS = TRUE (resilience)",
        "FLATTEN_PATH in config points to nested arrays"
    ])

    composer.add_content_slide("LATERAL FLATTEN for Nested Data", [
        "Extracts nested arrays into separate rows",
        "Preserves parent-child relationships",
        "Essential for event data with items/properties",
        "FLATTEN_OUTER = TRUE keeps rows with no matches"
    ])

    composer.add_section_divider("Parquet & Column Matching")

    composer.add_content_slide("MATCH_BY_COLUMN_NAME Options", [
        "NONE - Map by position (like CSV)",
        "CASE_SENSITIVE - Exact column name match",
        "CASE_INSENSITIVE - Flexible matching (recommended)",
        "Critical for Parquet, Avro, ORC (self-describing)"
    ])

    composer.add_emphasis_slide(
        "Parquet Best Practice",
        "Use MATCH_BY_COLUMN_NAME = CASE_INSENSITIVE for resilience when source systems change column casing."
    )

    composer.add_thank_you_slide("Module 06 Complete!", "contact@snowbrixai.com | snowbrixai.com/mdf")

    composer.save()
    print(f"[OK] Module 06 created: {output_file}")
    return output_file

def generate_module_07():
    """Module 07: Error Handling & Audit"""
    output_file = f"Inbound/MDF/Presentations/Module_07_Error_Handling_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pptx"

    composer = SnowbrixLayoutsComplete(output_file, include_logo=True, include_page_numbers=False)

    composer.add_title_slide(
        "Module 07: Error Handling & Audit",
        "Building Resilient Pipelines"
    )

    composer.add_agenda_slide("Error Resilience Topics", [
        {"number": "01", "title": "Error Philosophy", "duration": "5 min"},
        {"number": "02", "title": "ON_ERROR Strategy", "duration": "8 min"},
        {"number": "03", "title": "Validation Layers", "duration": "7 min"},
        {"number": "04", "title": "Retry Logic", "duration": "5 min"}
    ])

    composer.add_section_divider("Error Philosophy")

    composer.add_emphasis_slide(
        "Core Philosophy",
        "Errors are expected. Undetected errors are catastrophic. Design for resilience, log everything, alert intelligently."
    )

    composer.add_content_slide("Three Pillars of Resilience", [
        "Fail fast - Validation errors (config, permissions, schema strict)",
        "Fail gracefully - Recoverable errors (network, transients, partial)",
        "Partial success - Some rows better than no rows"
    ])

    composer.add_section_divider("ON_ERROR Strategy")

    composer.add_three_column_slide(
        "Three Error Modes",
        "CONTINUE",
        ["Skip bad rows", "Load good rows", "Event streams", "High volume"],
        "SKIP_FILE",
        ["Skip bad files", "Load good files", "Orders, invoices", "Balanced approach"],
        "ABORT_STATEMENT",
        ["Fail on first error", "Zero tolerance", "Payments", "Financial data"]
    )

    composer.add_content_slide("Error Classification", [
        "INFO - Expected (no files found, already loaded)",
        "WARNING - Non-critical (partial success, low failure rate)",
        "ERROR - Needs investigation (format mismatch, parse error)",
        "CRITICAL - Immediate action (permissions, quota, system failure)"
    ])

    composer.add_section_divider("Validation Layers")

    composer.add_content_slide("Three-Layer Validation", [
        "Layer 1: COPY-time (ON_ERROR, SIZE_LIMIT, pattern match)",
        "Layer 2: Post-load (SP_VALIDATE_LOAD, row count, NULL checks)",
        "Layer 3: Promotion gates (dbt tests, business rules)"
    ])

    composer.add_emphasis_slide(
        "Immutable RAW Principle",
        "RAW layer accepts partial loads. Validation failures block promotion to STAGING, not ingestion to RAW."
    )

    composer.add_section_divider("Retry Logic")

    composer.add_two_column_slide(
        "Retry Decision Matrix",
        [
            "Network timeouts",
            "Cloud storage throttling",
            "Warehouse busy/queued",
            "Temporary file locks"
        ],
        [
            "Schema mismatch (source changed)",
            "Permission denied (RBAC issue)",
            "Format mismatch (wrong delimiter)",
            "Table not found (missing DDL)"
        ],
        left_title="Retry (Transient Errors)",
        right_title="Alert (Fatal Errors)"
    )

    composer.add_content_slide("SP_RETRY_FAILED_LOADS", [
        "Retry recent failures (last 24 hours default)",
        "Max 3 attempts (prevent infinite loops)",
        "Exponential backoff (1 min, 5 min, 15 min)",
        "Only retries transient error types"
    ])

    composer.add_thank_you_slide("Module 07 Complete!", "contact@snowbrixai.com | snowbrixai.com/mdf")

    composer.save()
    print(f"[OK] Module 07 created: {output_file}")
    return output_file

def generate_module_08():
    """Module 08: Automation (Tasks & Streams)"""
    output_file = f"Inbound/MDF/Presentations/Module_08_Automation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pptx"

    composer = SnowbrixLayoutsComplete(output_file, include_logo=True, include_page_numbers=False)

    composer.add_title_slide(
        "Module 08: Automation",
        "Tasks & Streams for Self-Driving Pipelines"
    )

    composer.add_agenda_slide("Automation Topics", [
        {"number": "01", "title": "Why Automate?", "duration": "3 min"},
        {"number": "02", "title": "Snowflake Tasks", "duration": "12 min"},
        {"number": "03", "title": "Streams for CDC", "duration": "8 min"},
        {"number": "04", "title": "Event-Driven Patterns", "duration": "7 min"}
    ])

    composer.add_section_divider("Why Automate?")

    composer.add_emphasis_slide(
        "Manual Problem",
        "Right now, someone has to manually call procedures. That someone is usually you. At 3 AM. On Saturday."
    )

    composer.add_content_slide("Automation Solves Two Problems", [
        "Scheduling - Run procedures on CRON (daily, hourly, custom)",
        "Change detection - React to data changes (config, audit events)",
        "Zero human intervention after setup",
        "Audit-driven and event-driven automation"
    ])

    composer.add_section_divider("Snowflake Tasks")

    composer.add_content_slide("Task Tree Structure", [
        "MDF_TASK_ROOT - Parent task (triggers children)",
        "MDF_TASK_INGEST_CSV - Child task (runs after root)",
        "MDF_TASK_RETRY - Runs after ingestion completes",
        "Dependencies: AFTER keyword creates execution order"
    ])

    composer.add_two_column_slide(
        "CRON Expression Examples",
        [
            "0 6 * * * - Daily at 6 AM",
            "0 */2 * * * - Every 2 hours",
            "0 0 1 * * - First day of month",
            "0 6 * * 1-5 - Weekdays only"
        ],
        [
            "*/15 * * * * - Every 15 minutes",
            "0 6,18 * * * - 6 AM and 6 PM",
            "0 6 * * 0 - Sundays at 6 AM",
            "Custom schedules per source"
        ],
        left_title="Common Patterns",
        right_title="Advanced Patterns"
    )

    composer.add_content_slide("Task Management", [
        "Resume leaf tasks first (children → parent)",
        "Suspend root first (parent → children)",
        "EXECUTE TASK for manual testing",
        "Query TASK_HISTORY for monitoring"
    ])

    composer.add_section_divider("Streams for Change Detection")

    composer.add_content_slide("What Are Streams?", [
        "Track changes in tables (INSERT, UPDATE, DELETE)",
        "Enable event-driven processing",
        "MDF_CONFIG_STREAM - Detects new source registrations",
        "MDF_AUDIT_STREAM - Detects failures for auto-alert"
    ])

    composer.add_emphasis_slide(
        "Event-Driven Pattern",
        "New row in INGESTION_CONFIG → Stream captures → Task processes automatically. No manual coordination needed."
    )

    composer.add_thank_you_slide("Module 08 Complete!", "contact@snowbrixai.com | snowbrixai.com/mdf")

    composer.save()
    print(f"[OK] Module 08 created: {output_file}")
    return output_file

def generate_module_09():
    """Module 09: Monitoring & Dashboards"""
    output_file = f"Inbound/MDF/Presentations/Module_09_Monitoring_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pptx"

    composer = SnowbrixLayoutsComplete(output_file, include_logo=True, include_page_numbers=False)

    composer.add_title_slide(
        "Module 09: Monitoring & Dashboards",
        "Operational Visibility at Query Speed"
    )

    composer.add_agenda_slide("Monitoring Components", [
        {"number": "01", "title": "Seven Monitoring Views", "duration": "10 min"},
        {"number": "02", "title": "Snowsight Dashboard", "duration": "8 min"},
        {"number": "03", "title": "Alert Configuration", "duration": "7 min"}
    ])

    composer.add_section_divider("Seven Monitoring Views")

    composer.add_content_slide("The View Ecosystem", [
        "VW_SOURCE_HEALTH - Health status per source",
        "VW_DAILY_SUMMARY - Today's KPIs at a glance",
        "VW_ERROR_ANALYSIS - Error patterns and trends",
        "VW_PERFORMANCE_METRICS - Duration and throughput",
        "VW_THROUGHPUT_METRICS - Hourly bucketed volume"
    ])

    composer.add_three_column_slide(
        "Health Status Classification",
        "HEALTHY",
        ["0 failures in 7 days", "100% success rate", "Green status"],
        "WARNING",
        ["1-2 failures in 7 days", "Monitor closely", "Yellow status"],
        "CRITICAL",
        ["3+ failures in 7 days", "Immediate action", "Red status"]
    )

    composer.add_section_divider("VW_SOURCE_HEALTH Deep Dive")

    composer.add_content_slide("Key Columns", [
        "RUNS_LAST_7D - Total execution count",
        "SUCCESS_RATE_7D_PCT - Success percentage",
        "LAST_RUN_AT - Most recent execution",
        "HEALTH_STATUS - HEALTHY/WARNING/CRITICAL",
        "AVG_DURATION_7D - Performance trend"
    ])

    composer.add_emphasis_slide(
        "Morning Standup Query",
        "SELECT * FROM VW_SOURCE_HEALTH WHERE HEALTH_STATUS IN ('WARNING', 'CRITICAL');"
    )

    composer.add_section_divider("Snowsight Dashboard")

    composer.add_content_slide("Dashboard Components", [
        "KPI tiles (success rate, rows loaded, avg duration)",
        "Health heat map (source status color-coded)",
        "Trend line (7-day load volume)",
        "Error frequency chart (top 10 errors)"
    ])

    composer.add_content_slide("Alert Integration", [
        "Snowflake Alerts on audit log INSERT",
        "Webhook to Slack/Teams on failure",
        "Email for CRITICAL severity",
        "Configurable thresholds per source"
    ])

    composer.add_thank_you_slide("Module 09 Complete!", "contact@snowbrixai.com | snowbrixai.com/mdf")

    composer.save()
    print(f"[OK] Module 09 created: {output_file}")
    return output_file

def generate_module_10():
    """Module 10: Schema Evolution & Advanced"""
    output_file = f"Inbound/MDF/Presentations/Module_10_Schema_Evolution_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pptx"

    composer = SnowbrixLayoutsComplete(output_file, include_logo=True, include_page_numbers=False)

    composer.add_title_slide(
        "Module 10: Schema Evolution & Advanced",
        "Handling Schema Drift Automatically"
    )

    composer.add_agenda_slide("Advanced Topics", [
        {"number": "01", "title": "Schema Evolution Concept", "duration": "5 min"},
        {"number": "02", "title": "Detection & Application", "duration": "12 min"},
        {"number": "03", "title": "Multi-Client Onboarding", "duration": "8 min"},
        {"number": "04", "title": "Advanced Patterns", "duration": "5 min"}
    ])

    composer.add_section_divider("Schema Evolution")

    composer.add_content_slide("The Schema Drift Problem", [
        "Source systems add columns without warning",
        "Traditional approach: Load breaks, manual ALTER TABLE",
        "MDF approach: Detect changes, apply with safety limits",
        "Automatic or manual review mode"
    ])

    composer.add_two_column_slide(
        "Two-Step Process",
        [
            "SP_DETECT_SCHEMA_CHANGES",
            "Compares file schema vs table schema",
            "Returns: new_columns, type_changes",
            "Read-only, safe to run anytime"
        ],
        [
            "SP_APPLY_SCHEMA_EVOLUTION",
            "Applies detected changes",
            "Dry-run mode available",
            "MAX_NEW_COLUMNS safety limit (default: 10)"
        ],
        left_title="Step 1: Detect",
        right_title="Step 2: Apply"
    )

    composer.add_content_slide("Safety Limits", [
        "MAX_NEW_COLUMNS prevents runaway drift (default: 10)",
        "Only ADDs columns, never drops or modifies",
        "Manual review mode by default (auto-apply disabled)",
        "Alerts sent when drift detected"
    ])

    composer.add_section_divider("Multi-Client Onboarding")

    composer.add_content_slide("Onboarding Pattern", [
        "One procedure call registers entire client",
        "Automatically creates schemas and config rows",
        "Applies naming conventions (CLIENT_SYSTEM_TABLE)",
        "3 sources registered in under a second"
    ])

    composer.add_emphasis_slide(
        "Production Scale",
        "Schema evolution + multi-client onboarding = framework that handles hundreds of sources with minimal maintenance."
    )

    composer.add_content_slide("Course Complete: What You Built", [
        "Production-grade metadata-driven framework",
        "10 modules from foundation to advanced",
        "Complete audit trail and observability",
        "Automated scheduling and error recovery",
        "Ready to scale to 1,000+ data sources"
    ])

    composer.add_thank_you_slide("MDF Course Complete!", "contact@snowbrixai.com | snowbrixai.com/mdf")

    composer.save()
    print(f"[OK] Module 10 created: {output_file}")
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

    # Module 05
    print("\n[5/10] Module 05: CSV Ingestion Lab")
    file5 = generate_module_05()
    modules.append(file5)

    # Module 06
    print("\n[6/10] Module 06: Semi-Structured Data")
    file6 = generate_module_06()
    modules.append(file6)

    # Module 07
    print("\n[7/10] Module 07: Error Handling & Audit")
    file7 = generate_module_07()
    modules.append(file7)

    # Module 08
    print("\n[8/10] Module 08: Automation (Tasks & Streams)")
    file8 = generate_module_08()
    modules.append(file8)

    # Module 09
    print("\n[9/10] Module 09: Monitoring & Dashboards")
    file9 = generate_module_09()
    modules.append(file9)

    # Module 10
    print("\n[10/10] Module 10: Schema Evolution & Advanced")
    file10 = generate_module_10()
    modules.append(file10)

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
