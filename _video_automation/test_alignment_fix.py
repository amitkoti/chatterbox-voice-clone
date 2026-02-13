"""
Test script to verify alignment fixes for Agenda and Two-Column layouts
"""

from snowbrix_layouts_complete import SnowbrixLayoutsComplete
from datetime import datetime

# Create unique filename
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"alignment_fixed_{timestamp}.pptx"

# Create presentation
composer = SnowbrixLayoutsComplete(
    filename,
    include_logo=True,
    include_page_numbers=True
)

# Test 1: Agenda slide with numbered circles (like content slides)
print("Creating agenda slide with numbered circles...")
agenda_items = [
    {"number": "01", "title": "Introduction and Overview", "duration": "5 min"},
    {"number": "02", "title": "Technical Architecture", "duration": "10 min"},
    {"number": "03", "title": "Implementation Approach", "duration": "15 min"},
    {"number": "04", "title": "Results and Benefits", "duration": "10 min"},
    {"number": "05", "title": "Q&A and Next Steps", "duration": "10 min"}
]
composer.add_agenda_slide("Presentation Agenda", agenda_items)

# Test 2: Two-column slide with aligned sub-headings
print("Creating two-column slide with aligned sub-headings...")
snowflake_points = [
    "Cloud data warehouse architecture",
    "SQL-native query interface",
    "Automatic clustering and optimization",
    "Zero-copy cloning for dev/test",
    "Instant data sharing capabilities"
]

databricks_points = [
    "Lakehouse platform architecture",
    "Spark-native processing engine",
    "Notebook-driven development",
    "Delta Lake for ACID transactions",
    "Integrated ML and data science tools"
]

composer.add_two_column_slide(
    title="Snowflake vs Databricks",
    left_title="Snowflake",
    left_content=snowflake_points,
    right_title="Databricks",
    right_content=databricks_points
)

# Save
composer.save()
print(f"\nTest presentation created: {filename}")
print("\nFixes applied:")
print("1. Agenda slide: Numbers now inside sage green circles (like content slides)")
print("2. Agenda slide: Cleaner, more professional numbered layout")
print("3. Two-column slide: Sub-headings aligned with bullet text (X=1.2\" and X=8.9\")")
print("4. Two-column slide: Bullets use custom green circles, not default squares")
