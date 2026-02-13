"""
Create sample slides showing different brand styles
"""

from slide_composer import SlideComposer
from pathlib import Path

def create_sample(brand_style='growthschool'):
    """Create sample presentation for brand style"""
    output_path = f"_sample_{brand_style}_brand.pptx"

    composer = SlideComposer(output_path, brand_style=brand_style)

    # Title slide
    composer.add_title_slide(
        "Data Engineering Excellence",
        "Modern Presentation Design"
    )

    # Content slide with key points
    composer.add_slide_with_image(
        title="Why Choose Snowflake?",
        image_path=None,
        slide_type="features",
        notes="Snowflake is the leading cloud data platform offering unmatched performance, scalability, and ease of use.",
        key_points=[
            "Instant scalability for any workload",
            "Zero management overhead",
            "Secure data sharing across organizations"
        ]
    )

    # Another content slide
    composer.add_slide_with_image(
        title="Architecture Overview",
        image_path=None,
        slide_type="architecture",
        notes="Our modern data architecture leverages cloud-native technologies for maximum efficiency.",
        key_points=[
            "Cloud-native design",
            "Microservices architecture",
            "Real-time data processing"
        ]
    )

    composer.save()
    print(f"\nSample created: {output_path}")
    print(f"Brand style: {composer.brand_name}\n")

if __name__ == "__main__":
    import sys

    brand = sys.argv[1] if len(sys.argv) > 1 else 'growthschool'
    create_sample(brand)
