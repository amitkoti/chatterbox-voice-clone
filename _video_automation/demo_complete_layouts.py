"""
Demo All Snowbrix Layouts - Complete Professional System
Matches Snowflake template variety
"""

from snowbrix_layouts_complete import SnowbrixLayoutsComplete
from datetime import datetime

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_file = f"Snowbrix_Complete_Layouts_{timestamp}.pptx"
composer = SnowbrixLayoutsComplete(output_file, include_logo=True, include_page_numbers=True)

print("\n" + "="*70)
print("CREATING COMPLETE SNOWBRIX LAYOUT SYSTEM")
print("="*70)
print()

# 1. Title Slide
print("1. Title slide...")
composer.add_title_slide(
    "Snowbrix Complete Layout System",
    "Professional Presentation Design - All Layouts"
)

# 2. Agenda
print("2. Agenda slide...")
composer.add_agenda_slide(
    "Presentation Agenda",
    [
        {"number": "01", "title": "Introduction and Overview", "duration": "5 min"},
        {"number": "02", "title": "Technical Architecture", "duration": "10 min"},
        {"number": "03", "title": "Implementation Approach", "duration": "15 min"},
        {"number": "04", "title": "Results and Benefits", "duration": "10 min"},
        {"number": "05", "title": "Q&A and Next Steps", "duration": "10 min"}
    ]
)

# 3. Section Divider
print("3. Section divider...")
composer.add_section_divider(
    "Layout Gallery",
    "Professional Design Options"
)

# 4. Content with 3 points
print("4. Content (3 points)...")
composer.add_content_slide(
    "Three-Point Content Layout",
    key_points=[
        "Clear and concise messaging for simple topics",
        "Ample white space for visual breathing room",
        "Easy to digest for audience comprehension"
    ]
)

# 5. Content with 4 points
print("5. Content (4 points)...")
composer.add_content_slide(
    "Four-Database Architecture",
    key_points=[
        "Control Database - Configuration and orchestration",
        "Raw Database - Immutable source data preservation",
        "Staging Database - Cleansed and validated data",
        "Curated Database - Business-ready analytical datasets"
    ]
)

# 6. Content with 5 points
print("6. Content (5 points)...")
composer.add_content_slide(
    "Five Functional Security Roles",
    key_points=[
        "MDF_ADMIN - Full administrative control and framework ownership",
        "MDF_DEVELOPER - Development access for procedures and configuration",
        "MDF_LOADER - Data ingestion operations with write access to raw layer",
        "MDF_TRANSFORMER - Transformation pipelines with read/write to staging and curated",
        "MDF_READER - Read-only access for analysts and reporting tools"
    ]
)

# 7. Content with Subtitle
print("7. Content with subtitle...")
composer.add_content_slide(
    "Data Quality Framework",
    subtitle="Ensuring accuracy, completeness, and reliability",
    key_points=[
        "Automated validation rules at ingestion boundary",
        "Statistical anomaly detection on key metrics",
        "Business rule enforcement in transformation layer",
        "Continuous monitoring with alerting and dashboards"
    ]
)

# 8. Two-Column Comparison
print("8. Two-column comparison...")
composer.add_two_column_slide(
    "Snowflake vs Databricks",
    left_title="Snowflake",
    left_content=[
        "Cloud data warehouse architecture",
        "SQL-native query interface",
        "Automatic clustering and optimization",
        "Zero-copy cloning for dev/test",
        "Instant data sharing capabilities"
    ],
    right_title="Databricks",
    right_content=[
        "Lakehouse platform architecture",
        "Spark-native processing engine",
        "Notebook-driven development",
        "Delta Lake for ACID transactions",
        "Integrated ML and data science tools"
    ]
)

# 9. Two-Column with Paragraphs
print("9. Two-column with paragraphs...")
composer.add_two_column_paragraph_slide(
    "Project Approach",
    left_title="Discovery Phase",
    left_paragraphs=[
        "We begin with comprehensive stakeholder interviews to understand business requirements, technical constraints, and success criteria. This includes mapping existing data sources, identifying integration points, and documenting current pain points.",
        "The discovery phase typically takes 2-3 weeks and results in a detailed requirements document and architecture proposal."
    ],
    right_title="Implementation Phase",
    right_paragraphs=[
        "Development proceeds in 2-week sprints with continuous stakeholder feedback. We prioritize high-value use cases first to demonstrate quick wins while building the foundational architecture.",
        "Each sprint includes development, testing, and documentation. Production deployment happens incrementally with rollback capabilities."
    ]
)

# 10. Three-Column Layout
print("10. Three-column layout...")
composer.add_three_column_slide(
    "Cloud Platform Comparison",
    col1_title="AWS",
    col1_points=[
        "Redshift data warehouse",
        "S3 data lake storage",
        "Glue ETL service",
        "Largest cloud provider"
    ],
    col2_title="Azure",
    col2_points=[
        "Synapse Analytics",
        "Data Lake Storage Gen2",
        "Data Factory for ETL",
        "Enterprise Microsoft integration"
    ],
    col3_title="GCP",
    col3_points=[
        "BigQuery data warehouse",
        "Cloud Storage for data lake",
        "Dataflow for ETL",
        "Advanced ML/AI capabilities"
    ]
)

# 11. Image + Text Split (Image on LEFT)
print("11. Image + text split (image left)...")
composer.add_image_text_split(
    "Architecture Diagram",
    image_path=None,  # Placeholder
    content_points=[
        "Data flows from sources through ingestion layer",
        "Multiple validation checkpoints ensure quality",
        "Transformed data stored in business-ready format",
        "Monitoring provides real-time pipeline visibility",
        "Automated error handling and retry logic"
    ],
    image_on_left=True
)

# 12. Image + Text Split (Image on RIGHT)
print("12. Image + text split (image right)...")
composer.add_image_text_split(
    "ETL Pipeline Overview",
    image_path=None,
    content_points=[
        "Extract from 25+ heterogeneous data sources",
        "Transform using metadata-driven configurations",
        "Load with automatic schema detection",
        "Validate using configurable business rules",
        "Monitor with comprehensive audit logging"
    ],
    image_on_left=False
)

# 13. Paragraph Layout (Text-heavy)
print("13. Paragraph layout (text-heavy)...")
composer.add_paragraph_slide(
    "Implementation Methodology",
    subtitle="Proven approach for successful delivery",
    paragraphs=[
        "Our metadata-driven framework implementation follows an agile methodology with two-week sprints. Each sprint delivers working functionality that stakeholders can review and validate. This iterative approach reduces risk and ensures the solution meets business needs.",
        "The framework is built incrementally, starting with core ingestion capabilities and expanding to advanced features like data quality monitoring, automated alerting, and self-service configuration. This phased approach allows teams to realize value quickly while building toward the complete solution.",
        "Throughout the implementation, we maintain comprehensive documentation, provide hands-on training, and establish best practices for ongoing maintenance. Knowledge transfer is embedded in every phase to ensure your team can confidently operate and extend the framework."
    ]
)

# 14. Emphasis/Quote
print("14. Emphasis/quote slide...")
composer.add_emphasis_slide(
    "Key Insight",
    quote="Metadata-driven frameworks reduce development time by 80% while improving data quality and reliability"
)

# 15. Thank You
print("15. Thank you slide...")
composer.add_thank_you_slide(
    "Thank You!",
    "hello@snowbrixai.com | www.snowbrixai.com"
)

composer.save()

print("\n" + "="*70)
print("COMPLETE LAYOUT SYSTEM CREATED!")
print("="*70)
print(f"\nFile: {output_file}")
print(f"Total Slides: 15")
print("\nAll Layouts Demonstrated:")
print("  1. Title Slide - Hero cover")
print("  2. Agenda - Table of contents with timing")
print("  3. Section Divider - Green chapter break")
print("  4. Content (3 points) - Simple messaging")
print("  5. Content (4 points) - Architecture")
print("  6. Content (5 points) - Detailed features")
print("  7. Content with Subtitle - Contextual framing")
print("  8. Two-Column Bullets - Side-by-side comparison")
print("  9. Two-Column Paragraphs - Detailed text comparison")
print("  10. Three-Column - Feature/platform grid")
print("  11. Image + Text Split (Image Left) - Visual + bullets")
print("  12. Image + Text Split (Image Right) - Bullets + visual")
print("  13. Paragraph Layout - Text-heavy content")
print("  14. Emphasis/Quote - Key insights")
print("  15. Thank You - Professional closing")
print("\nFeatures:")
print("  - Page numbers on all slides")
print("  - Snowbrixai logo on all slides")
print("  - Consistent spacing and alignment")
print("  - Professional Snowbrix color scheme")
print("\n" + "="*70)
print("Now you have a complete professional layout system!")
print("="*70)
