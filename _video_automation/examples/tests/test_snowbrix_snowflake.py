"""
Test Snowbrix design with Snowflake content
"""

from slide_composer_snowbrix import SnowbrixSlideComposer
from datetime import datetime

# Create presentation
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_file = f"_Snowflake_Snowbrix_{timestamp}.pptx"
composer = SnowbrixSlideComposer(output_file)

# Title slide
composer.add_title_slide(
    "Snowflake Data Cloud",
    "Modern Data Platform for the Enterprise"
)

# Slide 1: Why Snowflake
composer.add_content_slide(
    "Why Snowflake?",
    key_points=[
        "10x faster queries than traditional data warehouses",
        "Zero infrastructure management - fully automated scaling",
        "Instant data sharing across teams and organizations"
    ],
    notes="Snowflake provides unmatched performance and ease of use for modern data teams."
)

# Slide 2: Architecture
composer.add_content_slide(
    "Cloud-Native Architecture",
    key_points=[
        "Separation of storage and compute for cost optimization",
        "Multi-cluster warehouses for workload isolation",
        "Cross-cloud and cross-region data replication"
    ],
    notes="Snowflake's unique architecture enables elastic scaling and cost efficiency."
)

# Slide 3: Key Capabilities
composer.add_content_slide(
    "Enterprise Features",
    key_points=[
        "Time Travel - query historical data up to 90 days",
        "Zero-copy cloning for instant dev/test environments",
        "Secure data sharing without moving or copying data"
    ],
    notes="Advanced features that differentiate Snowflake from competitors."
)

# Slide 4: Performance
composer.add_content_slide(
    "Unmatched Performance",
    key_points=[
        "Automatic query optimization and caching",
        "Massively parallel processing architecture",
        "Support for structured and semi-structured data"
    ],
    notes="Snowflake handles complex analytical workloads with ease."
)

# Slide 5: Integration
composer.add_content_slide(
    "Seamless Integration",
    key_points=[
        "Native connectors for BI tools (Tableau, PowerBI, Looker)",
        "Python, Spark, and SQL interface support",
        "Pre-built integrations with 200+ data sources"
    ],
    notes="Connect Snowflake to your entire data ecosystem."
)

# Emphasis slide
composer.add_emphasis_slide(
    "Key Insight",
    quote="The future of data is cloud-native, elastic, and collaborative"
)

# Save
composer.save()

print(f"\n{'='*70}")
print(f"TEST COMPLETE!")
print(f"{'='*70}")
print(f"\nSnowflake presentation created with Snowbrix design:")
print(f"  File: {output_file}")
print(f"  Slides: 7 (1 title + 5 content + 1 emphasis)")
print(f"  Design: Snowbrix Professional (cream + green)")
print(f"\nOpen the file to review the design!")
