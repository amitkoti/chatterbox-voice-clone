"""
Generate Snowbrix Text-Only Logo
Clean wordmark without icons, proper spacing
"""

from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

# Snowbrix Brand Colors
COLORS = {
    'cream': (253, 248, 243),           # #FDF8F3
    'forest_green': (45, 95, 63),       # #2D5F3F
    'sage_green': (107, 144, 128),      # #6B9080
    'terracotta': (201, 125, 96),       # #C97D60
    'charcoal': (74, 74, 74),           # #4A4A4A
    'white': (255, 255, 255),
}

def create_text_only_logo(background='cream', include_tagline=True):
    """Create clean text-only Snowbrix logo"""

    # Canvas size
    if include_tagline:
        width, height = 1920, 500
    else:
        width, height = 1920, 300

    if background == 'cream':
        bg_color = COLORS['cream']
    elif background == 'white':
        bg_color = COLORS['white']
    else:
        bg_color = (255, 255, 255, 0)

    img = Image.new('RGBA', (width, height), bg_color)
    draw = ImageDraw.Draw(img)

    # Load fonts - all same size for continuous look
    try:
        font_logo = ImageFont.truetype("arialbd.ttf", 160)  # Same size for all
        font_tagline = ImageFont.truetype("arial.ttf", 40)
    except:
        font_logo = ImageFont.load_default()
        font_tagline = ImageFont.load_default()

    # Calculate text positioning for centering
    text_y = 100

    # Get text widths for proper spacing
    snow_bbox = draw.textbbox((0, 0), "SNOW", font=font_logo)
    snow_width = snow_bbox[2] - snow_bbox[0]

    brix_bbox = draw.textbbox((0, 0), "BRIX", font=font_logo)
    brix_width = brix_bbox[2] - brix_bbox[0]

    ai_bbox = draw.textbbox((0, 0), "AI", font=font_logo)
    ai_width = ai_bbox[2] - ai_bbox[0]

    # Calculate total width and starting position
    spacing = 20  # Space between BRIX and AI
    total_width = snow_width + brix_width + spacing + ai_width
    start_x = (width - total_width) // 2

    # Draw text with proper spacing
    current_x = start_x

    # "SNOW" in Forest Green
    draw.text((current_x, text_y), "SNOW", fill=COLORS['forest_green'], font=font_logo)
    current_x += snow_width

    # "BRIX" in Terracotta (immediately after SNOW)
    draw.text((current_x, text_y), "BRIX", fill=COLORS['terracotta'], font=font_logo)
    current_x += brix_width + spacing

    # "AI" in Charcoal (same size, small gap after BRIX)
    draw.text((current_x, text_y), "AI", fill=COLORS['charcoal'], font=font_logo)

    # Tagline (optional)
    if include_tagline:
        tagline = "AI-Powered Data Engineering Solutions"
        tagline_bbox = draw.textbbox((0, 0), tagline, font=font_tagline)
        tagline_width = tagline_bbox[2] - tagline_bbox[0]
        tagline_x = (width - tagline_width) // 2
        draw.text((tagline_x, text_y + 200), tagline, fill=COLORS['sage_green'], font=font_tagline)

    return img

def create_compact_logo(background='cream'):
    """Create compact version with no spacing"""

    width, height = 1400, 300

    if background == 'cream':
        bg_color = COLORS['cream']
    elif background == 'white':
        bg_color = COLORS['white']
    else:
        bg_color = (255, 255, 255, 0)

    img = Image.new('RGBA', (width, height), bg_color)
    draw = ImageDraw.Draw(img)

    try:
        font_logo = ImageFont.truetype("arialbd.ttf", 140)
    except:
        font_logo = ImageFont.load_default()

    text_y = 80

    # Get text widths
    snow_bbox = draw.textbbox((0, 0), "SNOW", font=font_logo)
    snow_width = snow_bbox[2] - snow_bbox[0]

    brix_bbox = draw.textbbox((0, 0), "BRIX", font=font_logo)
    brix_width = brix_bbox[2] - brix_bbox[0]

    ai_bbox = draw.textbbox((0, 0), "AI", font=font_logo)
    ai_width = ai_bbox[2] - ai_bbox[0]

    # Tighter spacing
    total_width = snow_width + brix_width + ai_width + 15  # Minimal gap before AI
    start_x = (width - total_width) // 2

    current_x = start_x

    # Draw continuous text
    draw.text((current_x, text_y), "SNOW", fill=COLORS['forest_green'], font=font_logo)
    current_x += snow_width

    draw.text((current_x, text_y), "BRIX", fill=COLORS['terracotta'], font=font_logo)
    current_x += brix_width + 15

    draw.text((current_x, text_y), "AI", fill=COLORS['charcoal'], font=font_logo)

    return img

def create_all_variations():
    """Create all logo variations"""

    print("\n" + "="*70)
    print("SNOWBRIX TEXT-ONLY LOGO GENERATOR")
    print("="*70)
    print("\nGenerating clean text-only logos...\n")

    variations = [
        ('full_cream', 'Full Logo - Cream Background', True, 'cream'),
        ('full_white', 'Full Logo - White Background', True, 'white'),
        ('full_transparent', 'Full Logo - Transparent', True, 'transparent'),
        ('compact_cream', 'Compact - Cream Background', False, 'cream'),
        ('compact_white', 'Compact - White Background', False, 'white'),
    ]

    output_files = []

    for file_suffix, description, include_tagline, bg_type in variations:
        print(f"Creating: {description}...")

        if 'compact' in file_suffix:
            img = create_compact_logo(bg_type)
        else:
            img = create_text_only_logo(bg_type, include_tagline)

        # Save
        filename = f"Snowbrix_TextOnly_{file_suffix.title()}.png"
        output_path = Path(filename)

        if bg_type == 'transparent':
            img.save(output_path, 'PNG')
        else:
            # Convert RGBA to RGB
            rgb_img = Image.new('RGB', img.size, bg_type if bg_type == 'white' else COLORS['cream'])
            rgb_img.paste(img, mask=img.split()[3] if len(img.split()) == 4 else None)
            rgb_img.save(output_path, 'PNG')

        output_files.append(output_path)
        print(f"  [OK] Saved: {output_path}")

    return output_files

if __name__ == "__main__":
    # Generate all variations
    logo_files = create_all_variations()

    print("\n" + "="*70)
    print("LOGO FILES CREATED")
    print("="*70)

    for f in logo_files:
        print(f"  - {f}")

    print("\n" + "="*70)
    print("SNOWBRIX TEXT LOGO - CLEAN & SIMPLE")
    print("="*70)
    print("\nFeatures:")
    print("  ✓ No icons - text only")
    print("  ✓ Proper letter spacing (no overlap)")
    print("  ✓ AI same size as other letters")
    print("  ✓ Continuous wordmark")
    print("\nColors:")
    print("  SNOW: Forest Green (#2D5F3F)")
    print("  BRIX: Terracotta (#C97D60)")
    print("  AI: Charcoal (#4A4A4A)")
    print("  Tagline: Sage Green (#6B9080)")
    print("\n" + "="*70)
