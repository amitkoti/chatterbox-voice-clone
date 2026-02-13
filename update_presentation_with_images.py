"""
Update Module 01 presentation with AI-generated images.

Run this after generating images using Google Imagen.
"""
import sys
import os
from pathlib import Path

# Add video automation to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "_video_automation"))

from pptx import Presentation
from pptx.util import Inches

def update_presentation_with_images():
    """Add generated images to the presentation."""

    # Paths
    pptx_path = "Inbound/MDF/Module_01_Foundation_Setup.pptx"
    images_dir = Path("Inbound/MDF/images")
    output_path = "Inbound/MDF/Module_01_Foundation_Setup_With_Images.pptx"

    # Image mappings (slide_index: image_filename)
    image_mappings = {
        6: "slide_07_four_database_architecture.png",  # Slide 7 (0-indexed)
        11: "slide_12_four_warehouses.png",             # Slide 12
        17: "slide_18_role_hierarchy.png",              # Slide 18
        23: "slide_24_three_pillars.png",               # Slide 24
    }

    # Optional images
    optional_mappings = {
        7: "slide_08_database_benefits.png",            # Slide 8
        12: "slide_13_cost_comparison.png",             # Slide 13
    }

    # Check if presentation exists
    if not os.path.exists(pptx_path):
        print(f"Error: Presentation not found at {pptx_path}")
        print("Run: python generate_module01_slides.py first")
        return False

    # Load presentation
    print(f"Loading presentation: {pptx_path}")
    prs = Presentation(pptx_path)

    images_added = 0
    images_missing = []

    # Add required images
    for slide_idx, image_filename in image_mappings.items():
        image_path = images_dir / image_filename

        if image_path.exists():
            print(f"Adding {image_filename} to slide {slide_idx + 1}...")
            slide = prs.slides[slide_idx]

            # Add image as background or large image
            # Position: centered, large but not full-screen
            left = Inches(1.5)
            top = Inches(2.0)
            width = Inches(13.0)

            slide.shapes.add_picture(
                str(image_path),
                left, top,
                width=width
            )

            images_added += 1
        else:
            print(f"  Missing: {image_filename}")
            images_missing.append(image_filename)

    # Add optional images if available
    for slide_idx, image_filename in optional_mappings.items():
        image_path = images_dir / image_filename

        if image_path.exists():
            print(f"Adding optional {image_filename} to slide {slide_idx + 1}...")
            slide = prs.slides[slide_idx]

            left = Inches(1.5)
            top = Inches(2.0)
            width = Inches(13.0)

            slide.shapes.add_picture(
                str(image_path),
                left, top,
                width=width
            )

            images_added += 1

    # Save updated presentation
    if images_added > 0:
        prs.save(output_path)
        print(f"\nSuccess! Added {images_added} images")
        print(f"Saved to: {output_path}")

        if images_missing:
            print(f"\nMissing images ({len(images_missing)}):")
            for img in images_missing:
                print(f"  - {img}")
            print("\nGenerate these images using IMAGE_GENERATION_PROMPTS.md")

        return True
    else:
        print("\nNo images found to add!")
        print("Generate images first using Google Imagen.")
        print("See: Inbound/MDF/IMAGE_GENERATION_PROMPTS.md")
        return False

def main():
    print("=" * 60)
    print("Module 01 - Add AI-Generated Images to Presentation")
    print("=" * 60)
    print()

    # Check if images directory exists
    images_dir = Path("Inbound/MDF/images")
    if not images_dir.exists():
        print("Creating images directory...")
        images_dir.mkdir(parents=True, exist_ok=True)

    # Check for images
    image_files = list(images_dir.glob("*.png"))
    if not image_files:
        print("No images found in images directory.")
        print()
        print("Next steps:")
        print("1. Open: Inbound/MDF/IMAGE_GENERATION_PROMPTS.md")
        print("2. Go to: https://aistudio.google.com/")
        print("3. Generate images using the prompts")
        print("4. Save images to: Inbound/MDF/images/")
        print("5. Run this script again")
        return

    print(f"Found {len(image_files)} images in directory:")
    for img in image_files:
        print(f"  - {img.name}")
    print()

    # Update presentation
    success = update_presentation_with_images()

    if success:
        print()
        print("=" * 60)
        print("Next Steps:")
        print("=" * 60)
        print("1. Open the updated presentation:")
        print("   Inbound/MDF/Module_01_Foundation_Setup_With_Images.pptx")
        print("2. Review image placement and sizing")
        print("3. Adjust manually in PowerPoint if needed")
        print("4. Use for video recording!")

if __name__ == "__main__":
    main()
