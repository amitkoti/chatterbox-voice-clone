"""
Test script to verify fixed Agenda and Two-Column layouts
"""

from snowbrix_layouts_complete import SnowbrixLayoutsComplete

# Create presentation
composer = SnowbrixLayoutsComplete(
    "test_fixed_layouts.pptx",
    include_logo=True,
    include_page_numbers=True
)

# Test 1: Agenda slide with better alignment
print("Creating agenda slide with fixed alignment...")
agenda_items = [
    {"number": "01", "title": "Introduction and Overview", "duration": "5 min"},
    {"number": "02", "title": "Technical Architecture", "duration": "10 min"},
    {"number": "03", "title": "Implementation Approach", "duration": "15 min"},
    {"number": "04", "title": "Results and Benefits", "duration": "10 min"},
    {"number": "05", "title": "Q&A and Next Steps", "duration": "10 min"}
]
composer.add_agenda_slide("Presentation Agenda", agenda_items)

# Test 2: Two-column slide with better spacing and custom bullets
print("Creating two-column slide with improved spacing...")
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
print("\n✅ Test presentation created: test_fixed_layouts.pptx")
print("\nFixes applied:")
print("1. Agenda slide: Better alignment of bullets, numbers, and text")
print("2. Agenda slide: Increased font sizes and spacing")
print("3. Two-column slide: Custom green circles instead of default bullets")
print("4. Two-column slide: Increased spacing between items (1.1\" instead of 0.9\")")
print("5. Two-column slide: Larger font size (24pt instead of 20pt)")
