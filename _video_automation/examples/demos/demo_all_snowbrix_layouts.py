"""
Demo All Snowbrix Layouts
Showcasing professional layout variety
"""

from slide_composer_snowbrix import SnowbrixSlideComposer
from datetime import datetime

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_file = f"Snowbrix_All_Layouts_Demo_{timestamp}.pptx"
composer = SnowbrixSlideComposer(output_file, include_logo=True)

print("\nCreating Snowbrix Layout Showcase...")
print("="*70)

# Layout 1: Title Slide
print("1. Title slide...")
composer.add_title_slide(
    "Snowbrix Professional Layouts",
    "Complete Design System for Data Engineering"
)

# Layout 2: Content Slide (3 points)
print("2. Content slide (3 points)...")
composer.add_content_slide(
    "Three-Point Layout",
    key_points=[
        "First key point with concise messaging",
        "Second point highlighting important features",
        "Third point summarizing benefits"
    ]
)

# Layout 3: Content Slide (4 points)
print("3. Content slide (4 points)...")
composer.add_content_slide(
    "Four-Database Architecture",
    key_points=[
        "MDF_CONTROL_DB - Configuration and orchestration",
        "MDF_RAW_DB - Raw data landing zone",
        "MDF_STAGING_DB - Cleaned and validated data",
        "MDF_CURATED_DB - Business-ready analytics"
    ]
)

# Layout 4: Content Slide (5 points)
print("4. Content slide (5 points)...")
composer.add_content_slide(
    "Five Security Roles",
    key_points=[
        "MDF_ADMIN - Full administrative control",
        "MDF_DEVELOPER - Development and configuration",
        "MDF_LOADER - Data ingestion operations",
        "MDF_TRANSFORMER - Data transformation pipelines",
        "MDF_READER - Read-only access for analysts"
    ]
)

# Layout 5: Two-Column Layout
print("5. Two-column comparison...")
composer.add_two_column_slide(
    "Snowflake vs Databricks",
    left_title="Snowflake",
    left_content=[
        "Cloud data warehouse",
        "SQL-native interface",
        "Auto-scaling clusters",
        "Instant zero-copy cloning",
        "Built for analytics workloads"
    ],
    right_title="Databricks",
    right_content=[
        "Lakehouse platform",
        "Spark-native processing",
        "Notebook-driven development",
        "Delta Lake integration",
        "Built for ML and data science"
    ]
)

# Layout 6: Section Divider
print("6. Section divider...")
composer.add_section_divider(
    "Part 2: Advanced Concepts",
    "Deep Dive into Architecture Patterns"
)

# Layout 7: Emphasis/Quote Slide
print("7. Emphasis slide...")
composer.add_emphasis_slide(
    "Key Insight",
    quote="Metadata-driven frameworks reduce development time by 80% while improving data quality"
)

# Layout 8: Thank You Slide
print("8. Thank you slide...")
composer.add_thank_you_slide(
    "Thank You!",
    "questions@snowbrixai.com | www.snowbrixai.com"
)

# Save
composer.save()

print("\n" + "="*70)
print("SNOWBRIX LAYOUT SHOWCASE COMPLETE!")
print("="*70)
print(f"\nFile: {output_file}")
print(f"Slides: 8 (demonstrating all layout types)")
print("\nLayouts Included:")
print("  1. Title Slide - Hero introduction")
print("  2. Content (3 points) - Standard messaging")
print("  3. Content (4 points) - Architecture overview")
print("  4. Content (5 points) - Detailed features")
print("  5. Two-Column - Side-by-side comparison")
print("  6. Section Divider - Chapter break (green background)")
print("  7. Emphasis - Key insight/quote")
print("  8. Thank You - Professional closing")
print("\nAll layouts feature:")
print("  - Snowbrix colors (cream + green)")
print("  - Snowbrixai logo (bottom right)")
print("  - Professional spacing and typography")
print("  - Warm, educational aesthetic")
print("\n" + "="*70)
