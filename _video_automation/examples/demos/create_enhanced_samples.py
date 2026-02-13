"""Create enhanced samples with strong visual contrast"""

from slide_composer_v2 import SlideComposerV2
import sys

def create_enhanced_sample(brand='warm'):
    output = f"_enhanced_{brand}_brand.pptx"
    composer = SlideComposerV2(output, brand)

    # Title slide
    composer.add_title_slide(
        "Data Engineering Excellence",
        "Transforming Data into Business Value"
    )

    # Content slide 1
    composer.add_content_slide(
        "Why Choose Snowflake?",
        key_points=[
            "Lightning-fast queries - 10x faster than traditional warehouses",
            "Zero maintenance overhead - fully managed cloud infrastructure",
            "Instant scalability - grow from GB to PB seamlessly"
        ]
    )

    # Content slide 2
    composer.add_content_slide(
        "Modern Data Architecture",
        key_points=[
            "Cloud-native design built for distributed computing",
            "Separation of storage and compute for optimal costs",
            "Multi-cloud support across AWS, Azure, and GCP"
        ]
    )

    # Content slide 3
    composer.add_content_slide(
        "Key Capabilities",
        key_points=[
            "Time Travel - query historical data up to 90 days",
            "Zero-copy cloning for instant dev/test environments",
            "Secure data sharing without moving or copying data"
        ]
    )

    composer.save()
    print(f"Created: {output}\n")

if __name__ == "__main__":
    styles = ['warm', 'bold', 'sophisticated', 'energetic', 'natural']

    for style in styles:
        create_enhanced_sample(style)
