"""
Create Complete Snowbrix Template 2025
Professional presentation template with all layouts and guides
"""

from slide_composer_snowbrix import SnowbrixSlideComposer
from datetime import datetime

output_file = "Snowbrix_Template_2025.pptx"
composer = SnowbrixSlideComposer(output_file, include_logo=True)

print("\n" + "="*70)
print("CREATING SNOWBRIX TEMPLATE 2025")
print("="*70)
print("\nGenerating comprehensive template with examples and guides...")
print()

# ============================================================================
# SECTION 1: TEMPLATE INTRO & GUIDE
# ============================================================================

print("Section 1: Template Introduction...")

# Slide 1: Cover
composer.add_title_slide(
    "SNOWBRIX TEMPLATE 2025",
    "Professional Presentation Design System"
)

# Slide 2: Table of Contents
composer.add_content_slide(
    "Template Contents",
    key_points=[
        "Section 1: Using This Template (Slides 1-5)",
        "Section 2: Color Palette & Typography (Slides 6-8)",
        "Section 3: Layout Examples (Slides 9-20)",
        "Section 4: Best Practices (Slides 21-25)",
        "Section 5: Sample Slides (Slides 26+)"
    ],
    notes="Navigate through this template to understand all available layouts and design standards."
)

# Slide 3: How to Use
composer.add_content_slide(
    "Using This Template",
    key_points=[
        "Duplicate the slide layout you need from the examples section",
        "Replace placeholder text with your content",
        "Maintain the spacing and color scheme for consistency",
        "Use Snowbrixai logo on all slides (already included)",
        "Export as PDF for sharing or present directly"
    ],
    notes="This template provides 8 professional layouts optimized for data engineering content."
)

# Slide 4: Design Philosophy
composer.add_two_column_slide(
    "Snowbrix Design Philosophy",
    left_title="Visual Identity",
    left_content=[
        "Warm cream backgrounds (#FDF8F3)",
        "Forest green primary (#2D5F3F)",
        "Sage green accents (#6B9080)",
        "Terracotta highlights (#C97D60)",
        "Professional yet approachable"
    ],
    right_title="Content Principles",
    right_content=[
        "Maximum 5 bullet points per slide",
        "Large, readable fonts (30pt body)",
        "Generous white space (40% minimum)",
        "Icons and visuals on 30% of slides",
        "Clear visual hierarchy"
    ],
    notes="Snowbrix balances professionalism with warmth - educational without being boring."
)

# ============================================================================
# SECTION 2: COLOR & TYPOGRAPHY GUIDE
# ============================================================================

print("Section 2: Brand Guidelines...")

# Slide 5: Section Divider
composer.add_section_divider(
    "Brand Guidelines",
    "Colors, Typography & Standards"
)

# Slide 6: Color Palette
composer.add_content_slide(
    "Snowbrix Color Palette",
    key_points=[
        "Cream Background: #FDF8F3 (soft, warm, inviting)",
        "Forest Green: #2D5F3F (primary - titles, headings, emphasis)",
        "Sage Green: #6B9080 (secondary - accents, numbered circles)",
        "Terracotta: #C97D60 (highlights - warmth and energy)",
        "Charcoal: #4A4A4A (body text - professional, readable)"
    ],
    notes="Use forest green 80%+ of the time for consistency. Terracotta sparingly for impact."
)

# Slide 7: Typography Standards
composer.add_content_slide(
    "Typography Hierarchy",
    key_points=[
        "Hero Titles: 72pt Bold - Major slide titles and covers",
        "Section Headers: 56pt Bold - Content slide titles",
        "Subtitles: 36pt Regular - Supporting headlines",
        "Body Text: 30pt Bold - Bullet points and key content",
        "Notes: 22pt Regular - Logo and supplementary text"
    ],
    notes="All typography uses Arial family. Larger sizes than typical (30pt vs 10pt) for better visibility."
)

# Slide 8: Do's and Don'ts
composer.add_two_column_slide(
    "Design Do's and Don'ts",
    left_title="DO ✓",
    left_content=[
        "Use cream backgrounds consistently",
        "Limit to 5 bullets per slide",
        "Include logo on every slide",
        "Use forest green for emphasis",
        "Maintain 0.4 inch margins"
    ],
    right_title="DON'T ✗",
    right_content=[
        "Mix multiple color schemes",
        "Cram more than 5 points per slide",
        "Use fonts other than Arial",
        "Reduce margins below 0.4 inches",
        "Remove the Snowbrixai logo"
    ],
    notes="Consistency is key. Follow these guidelines for professional results."
)

# ============================================================================
# SECTION 3: LAYOUT EXAMPLES
# ============================================================================

print("Section 3: Layout Examples...")

# Slide 9: Section Divider
composer.add_section_divider(
    "Layout Gallery",
    "8 Professional Slide Templates"
)

# Slide 10: Layout 1 - Title Slide Example
composer.add_title_slide(
    "Example: Title Slide Layout",
    "Use for presentation covers and major section openers"
)

# Slide 11: Layout 2 - Content with 3 Points
composer.add_content_slide(
    "Example: Three-Point Content Layout",
    key_points=[
        "First key point - clear and concise messaging",
        "Second key point - supporting information or benefit",
        "Third key point - call to action or summary"
    ],
    notes="Best for: Simple messaging, key takeaways, high-level overviews"
)

# Slide 12: Layout 3 - Content with 4 Points
composer.add_content_slide(
    "Example: Four-Point Content Layout",
    key_points=[
        "Point one - introduce the concept or framework component",
        "Point two - add detail or explain functionality",
        "Point three - provide context or business value",
        "Point four - conclude with impact or next steps"
    ],
    notes="Best for: Architecture layers, process steps, feature categories"
)

# Slide 13: Layout 4 - Content with 5 Points
composer.add_content_slide(
    "Example: Five-Point Content Layout",
    key_points=[
        "First item - comprehensive coverage of detailed topics",
        "Second item - technical specifications or requirements",
        "Third item - implementation considerations and approach",
        "Fourth item - benefits and business value proposition",
        "Fifth item - next steps or recommendations for action"
    ],
    notes="Best for: Detailed features, role definitions, comprehensive lists"
)

# Slide 14: Layout 5 - Two Column Comparison
composer.add_two_column_slide(
    "Example: Two-Column Comparison Layout",
    left_title="Option A",
    left_content=[
        "Feature or characteristic one",
        "Feature or characteristic two",
        "Feature or characteristic three",
        "Feature or characteristic four",
        "Feature or characteristic five"
    ],
    right_title="Option B",
    right_content=[
        "Contrasting feature one",
        "Contrasting feature two",
        "Contrasting feature three",
        "Contrasting feature four",
        "Contrasting feature five"
    ],
    notes="Best for: Tool comparisons, before/after, pros/cons, option evaluation"
)

# Slide 15: Layout 6 - Emphasis/Quote
composer.add_emphasis_slide(
    "Example: Emphasis Layout",
    quote="Use this layout for powerful quotes, key insights, or memorable takeaways that deserve full-slide focus"
)

# Slide 16: Layout 7 - Section Divider
composer.add_section_divider(
    "Example: Section Divider",
    "Use for major topic transitions"
)

# Slide 17: Layout 8 - Thank You
composer.add_thank_you_slide(
    "Example: Thank You Layout",
    "your.email@company.com | www.yourwebsite.com"
)

# ============================================================================
# SECTION 4: BEST PRACTICES
# ============================================================================

print("Section 4: Best Practices & Guidelines...")

# Slide 18: Section Divider
composer.add_section_divider(
    "Best Practices",
    "Professional Design Standards"
)

# Slide 19: Content Best Practices
composer.add_content_slide(
    "Content Best Practices",
    key_points=[
        "One main idea per slide - avoid information overload",
        "5-7 words per bullet point maximum for scannability",
        "Use visuals to support 30% of slides minimum",
        "Tell a story - each slide builds on the previous",
        "End with clear call to action or next steps"
    ],
    notes="Effective presentations educate and inspire. Keep content focused and actionable."
)

# Slide 20: Visual Hierarchy
composer.add_content_slide(
    "Visual Hierarchy Principles",
    key_points=[
        "Titles in forest green (#2D5F3F) - establish topic immediately",
        "Numbered circles in sage green (#6B9080) - guide eye flow",
        "Body text in warm gray (#4A4A4A) - readable without harshness",
        "Terracotta for highlights (#C97D60) - draw attention sparingly",
        "Logo in bottom right - consistent branding without distraction"
    ],
    notes="Color directs attention. Use the hierarchy intentionally to guide your audience."
)

# Slide 21: Spacing & Alignment
composer.add_content_slide(
    "Spacing Standards",
    key_points=[
        "Maintain 0.4 inch margins on all sides minimum",
        "Use 1.3-1.6 inch vertical spacing between bullet points",
        "Allow 40% white space for visual breathing room",
        "Align all text and elements to consistent grid",
        "Keep logo and page elements in consistent positions"
    ],
    notes="Professional design is 90% spacing. Never compromise on margins."
)

# Slide 22: Typography Guidelines
composer.add_content_slide(
    "Typography Guidelines",
    key_points=[
        "Use only Arial family fonts for cross-platform compatibility",
        "Maintain size hierarchy: 72pt > 56pt > 36pt > 30pt > 22pt",
        "Body text at 30pt for excellent visibility in presentations",
        "Bold for emphasis, never underline or italic in titles",
        "Limit to 3 font sizes maximum per slide"
    ],
    notes="Larger fonts (30pt body) work better for presentations than print (10pt)."
)

# Slide 23: Accessibility Standards
composer.add_content_slide(
    "Accessibility & Readability",
    key_points=[
        "High contrast: Dark text on cream background (minimum 7:1 ratio)",
        "Never use color as the only information indicator",
        "Font size minimum 22pt for all visible text",
        "Alt text for all images and icons (when applicable)",
        "Clear visual hierarchy for screen readers"
    ],
    notes="Accessible design is good design. Benefits everyone, not just those with disabilities."
)

# ============================================================================
# SECTION 5: SAMPLE SLIDES FOR COMMON SCENARIOS
# ============================================================================

print("Section 5: Sample Slides...")

# Slide 24: Section Divider
composer.add_section_divider(
    "Sample Slides",
    "Real-World Examples"
)

# Slide 25: Data Architecture Sample
composer.add_content_slide(
    "Sample: Data Architecture Overview",
    key_points=[
        "Bronze Layer - Raw data ingestion from multiple sources",
        "Silver Layer - Cleaned, validated, and conformed data",
        "Gold Layer - Business-ready aggregated data marts",
        "Monitoring Layer - Data quality and pipeline observability"
    ],
    notes="Architecture slides should clearly show data flow and layer responsibilities."
)

# Slide 26: Security Framework Sample
composer.add_content_slide(
    "Sample: Security Framework",
    key_points=[
        "Role-Based Access Control (RBAC) with least privilege",
        "Encryption at rest and in transit for all data layers",
        "Audit logging for all data access and modifications",
        "Network isolation using private endpoints",
        "Automated compliance reporting and monitoring"
    ],
    notes="Security slides demonstrate comprehensive protection across all layers."
)

# Slide 27: Performance Metrics Sample
composer.add_content_slide(
    "Sample: Performance Improvements",
    key_points=[
        "Query response time reduced by 85% (12s to 1.8s)",
        "Daily data processing cost decreased 60% ($800 to $320)",
        "Pipeline reliability improved to 99.9% uptime",
        "Data freshness: Near real-time (5-minute latency)"
    ],
    notes="Quantify improvements with specific metrics. Numbers tell the story."
)

# Slide 28: Technology Comparison Sample
composer.add_two_column_slide(
    "Sample: Technology Evaluation",
    left_title="Current State",
    left_content=[
        "Legacy on-premise data warehouse",
        "Manual ETL processes (12 hours daily)",
        "Limited scalability (3TB maximum)",
        "High maintenance overhead (2 FTE)",
        "Expensive licensing ($240K annually)"
    ],
    right_title="Snowflake Solution",
    right_content=[
        "Cloud-native data platform",
        "Automated ELT pipelines (2 hours)",
        "Elastic scaling (petabyte-ready)",
        "Zero maintenance required",
        "Consumption-based pricing ($60K annually)"
    ],
    notes="Comparison slides should show clear before/after or option A vs option B contrasts."
)

# Slide 29: Customer Success Sample
composer.add_emphasis_slide(
    "Sample: Customer Quote",
    quote="Snowbrix reduced our data engineering development time by 80% while improving data quality and reliability"
)

# Slide 30: Team Introduction Sample
composer.add_content_slide(
    "Sample: Meet the Team",
    key_points=[
        "Data Engineering Lead - 15 years building data platforms",
        "Solutions Architect - Cloud-native architecture specialist",
        "Analytics Engineer - Business intelligence expert",
        "DevOps Engineer - Infrastructure automation and CI/CD"
    ],
    notes="Team slides build credibility. Include relevant experience and expertise."
)

# ============================================================================
# SECTION 6: INSTRUCTIONS & GUIDELINES
# ============================================================================

print("Section 6: Usage Instructions...")

# Slide 31: Section Divider
composer.add_section_divider(
    "How to Use",
    "Step-by-Step Guide"
)

# Slide 32: Getting Started
composer.add_content_slide(
    "Getting Started with Snowbrix Template",
    key_points=[
        "Step 1: Duplicate this template file (don't edit the original)",
        "Step 2: Delete instruction slides (slides 1-32)",
        "Step 3: Keep example slides as reference or starting points",
        "Step 4: Add your content slide by slide",
        "Step 5: Export as PDF or present directly from PowerPoint"
    ],
    notes="Treat this template as your starting point for all Snowbrix presentations."
)

# Slide 33: Choosing the Right Layout
composer.add_content_slide(
    "Choosing the Right Layout",
    key_points=[
        "Title Slide - Presentation cover or major section opener",
        "Content (3-5 points) - Key messages, features, benefits",
        "Two-Column - Comparisons, before/after, options evaluation",
        "Emphasis/Quote - Memorable statements, customer testimonials",
        "Section Divider - Chapter breaks, major topic transitions"
    ],
    notes="Match layout to content purpose. Don't force content into wrong layout."
)

# Slide 34: Creating New Slides
composer.add_two_column_slide(
    "Creating New Slides",
    left_title="From Template",
    left_content=[
        "Navigate to the example section",
        "Find the layout you need",
        "Right-click and duplicate slide",
        "Move to your presentation section",
        "Replace placeholder content"
    ],
    right_title="From Scratch",
    right_content=[
        "Use slide_composer_snowbrix.py",
        "Generate slides programmatically",
        "Automated batch creation",
        "Consistent styling guaranteed",
        "Ideal for large presentations"
    ],
    notes="Manual for small decks, programmatic for bulk generation."
)

# ============================================================================
# SECTION 7: LAYOUT REFERENCE EXAMPLES
# ============================================================================

print("Section 7: Layout Reference Library...")

# Slide 35: Section Divider
composer.add_section_divider(
    "Layout Reference",
    "Ready-to-Use Examples"
)

# Example slides for each scenario
examples = [
    # Technical slides
    ("Cloud Data Platform Benefits", [
        "Elastic compute scaling - pay only for what you use",
        "Zero infrastructure management - fully managed service",
        "Automatic query optimization and performance tuning",
        "Built-in data sharing across teams and organizations"
    ]),

    # Process slides
    ("Data Pipeline Orchestration", [
        "Ingestion - Automated file detection and loading",
        "Validation - Data quality checks and error handling",
        "Transformation - Business logic and enrichment",
        "Publishing - Curated datasets for analytics consumption"
    ]),

    # Architecture slides
    ("Metadata-Driven Framework Architecture", [
        "Control Database - Configuration and orchestration metadata",
        "Raw Layer - Immutable source data preservation",
        "Staging Layer - Cleansed and validated transformations",
        "Curated Layer - Business-ready analytical datasets",
        "Monitoring Layer - Pipeline health and data quality metrics"
    ]),

    # Security slides
    ("Data Governance Framework", [
        "Classification - Automatic PII and sensitive data tagging",
        "Access Control - Role-based permissions and row-level security",
        "Audit Trail - Complete lineage and access logging",
        "Compliance - Automated GDPR and regulatory reporting"
    ]),

    # Results slides
    ("Project Outcomes", [
        "Delivered 40% faster than legacy approach (6 weeks vs 10 weeks)",
        "Reduced operational costs by $180K annually (automation savings)",
        "Improved data freshness from daily to 15-minute latency",
        "Increased data quality from 87% to 99.5% accuracy"
    ])
]

slide_num = 36
for title, points in examples:
    print(f"  Creating example slide {slide_num}: {title[:40]}...")
    composer.add_content_slide(title, key_points=points)
    slide_num += 1

# ============================================================================
# SECTION 8: CLOSING
# ============================================================================

print("Section 8: Closing slides...")

# Slide 41: Template Summary
composer.add_content_slide(
    "Snowbrix Template Summary",
    key_points=[
        "8 professional layouts covering all presentation needs",
        "Consistent cream + green color scheme for brand identity",
        "Professional spacing and typography standards",
        "Ready-to-use examples for common scenarios",
        "Programmatic generation available via Python SDK"
    ],
    notes="This template represents professional-grade presentation design for data engineering."
)

# Slide 42: Next Steps
composer.add_emphasis_slide(
    "Ready to Create?",
    quote="Duplicate this template and start building your professional Snowbrix presentations today"
)

# Slide 43: Thank You
composer.add_thank_you_slide(
    "Thank You!",
    "For questions or support: hello@snowbrixai.com"
)

# Save
composer.save()

print("\n" + "="*70)
print("SNOWBRIX TEMPLATE 2025 CREATED!")
print("="*70)
print(f"\nFile: {output_file}")
print(f"Total Slides: 43")
print("\nTemplate Structure:")
print("  Section 1: Introduction & Guide (Slides 1-4)")
print("  Section 2: Brand Guidelines (Slides 5-8)")
print("  Section 3: Layout Gallery (Slides 9-17)")
print("  Section 4: Best Practices (Slides 18-23)")
print("  Section 5: Layout Examples (Slides 24-35)")
print("  Section 6: Sample Scenarios (Slides 36-40)")
print("  Section 7: Summary & Closing (Slides 41-43)")
print("\nHow to Use:")
print("  1. Open Snowbrix_Template_2025.pptx")
print("  2. Duplicate the slide layout you need")
print("  3. Replace placeholder text with your content")
print("  4. Maintain colors and spacing for consistency")
print("  5. Export or present!")
print("\nFeatures:")
print("  - 8 professional layouts")
print("  - Color palette guide")
print("  - Typography standards")
print("  - Do's and Don'ts")
print("  - Ready-to-use examples")
print("  - Snowbrixai logo on every slide")
print("\n" + "="*70)
print("\nYour own professional template - ready to compete with Snowflake!")
print("="*70)
