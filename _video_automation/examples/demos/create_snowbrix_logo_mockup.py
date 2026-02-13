"""
Create Snowbrix Logo Color Mockup
Shows current vs. recommended Snowbrix brand colors
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

# Current logo colors (for comparison)
CURRENT_COLORS = {
    'blue': (41, 128, 185),             # Snowflake blue
    'orange': (255, 107, 53),           # Databricks orange
    'gray': (100, 100, 100),
}

def create_color_palette_guide():
    """Create a visual guide showing color transformation"""

    width, height = 1600, 1200
    img = Image.new('RGB', (width, height), COLORS['white'])
    draw = ImageDraw.Draw(img)

    try:
        font_title = ImageFont.truetype("arial.ttf", 60)
        font_large = ImageFont.truetype("arialbd.ttf", 48)
        font_medium = ImageFont.truetype("arial.ttf", 36)
        font_small = ImageFont.truetype("arial.ttf", 28)
    except:
        font_title = ImageFont.load_default()
        font_large = ImageFont.load_default()
        font_medium = ImageFont.load_default()
        font_small = ImageFont.load_default()

    # Title
    draw.text((50, 40), "SNOWBRIX LOGO - COLOR TRANSFORMATION",
              fill=COLORS['forest_green'], font=font_title)

    # Divider line
    draw.rectangle([50, 120, 1550, 125], fill=COLORS['sage_green'])

    # === CURRENT DESIGN (Left) ===
    draw.text((100, 160), "CURRENT DESIGN", fill=CURRENT_COLORS['blue'], font=font_large)
    draw.text((100, 220), "(Blue + Orange)", fill=COLORS['charcoal'], font=font_small)

    # Current colors
    y = 280
    # Snowflake (Blue)
    draw.rectangle([100, y, 300, y+100], fill=CURRENT_COLORS['blue'])
    draw.text((320, y+30), "Snowflake: Blue", fill=COLORS['charcoal'], font=font_medium)

    # Bricks (Orange)
    y += 120
    draw.rectangle([100, y, 300, y+100], fill=CURRENT_COLORS['orange'])
    draw.text((320, y+30), "Bricks: Orange", fill=COLORS['charcoal'], font=font_medium)

    # Text
    y += 120
    draw.rectangle([100, y, 300, y+50], fill=CURRENT_COLORS['blue'])
    draw.text((320, y+10), '"SNOW" text: Blue', fill=COLORS['charcoal'], font=font_medium)

    y += 60
    draw.rectangle([100, y, 300, y+50], fill=CURRENT_COLORS['orange'])
    draw.text((320, y+10), '"BRIX" text: Orange', fill=COLORS['charcoal'], font=font_medium)

    y += 60
    draw.rectangle([100, y, 300, y+50], fill=CURRENT_COLORS['gray'])
    draw.text((320, y+10), '"AI" text: Gray', fill=COLORS['charcoal'], font=font_medium)

    # === RECOMMENDED DESIGN (Right) ===
    draw.text((900, 160), "SNOWBRIX BRAND", fill=COLORS['forest_green'], font=font_large)
    draw.text((900, 220), "(Cream + Green)", fill=COLORS['charcoal'], font=font_small)

    # Snowbrix colors
    y = 280
    # Snowflake (Forest Green)
    draw.rectangle([900, y, 1100, y+100], fill=COLORS['forest_green'])
    draw.text((1120, y+30), "Snowflake: Forest Green (#2D5F3F)",
              fill=COLORS['charcoal'], font=font_medium)

    # Bricks (Terracotta)
    y += 120
    draw.rectangle([900, y, 1100, y+100], fill=COLORS['terracotta'])
    draw.text((1120, y+30), "Bricks: Terracotta (#C97D60)",
              fill=COLORS['charcoal'], font=font_medium)

    # Text
    y += 120
    draw.rectangle([900, y, 1100, y+50], fill=COLORS['forest_green'])
    draw.text((1120, y+10), '"SNOW" text: Forest Green',
              fill=COLORS['charcoal'], font=font_medium)

    y += 60
    draw.rectangle([900, y, 1100, y+50], fill=COLORS['terracotta'])
    draw.text((1120, y+10), '"BRIX" text: Terracotta (#C97D60)',
              fill=COLORS['charcoal'], font=font_medium)

    y += 60
    draw.rectangle([900, y, 1100, y+50], fill=COLORS['charcoal'])
    draw.text((1120, y+10), '"AI" text: Charcoal (keep as-is)',
              fill=COLORS['charcoal'], font=font_medium)

    # Background option
    y += 80
    draw.rectangle([900, y, 1100, y+100], fill=COLORS['cream'])
    draw.text((1120, y+30), "Background: Soft Cream (#FDF8F3)",
              fill=COLORS['charcoal'], font=font_medium)
    draw.text((1120, y+60), "or transparent",
              fill=COLORS['charcoal'], font=font_small)

    # === VISUAL COMPARISON ===
    y = 880
    draw.rectangle([50, y-20, 1550, y-15], fill=COLORS['sage_green'])
    draw.text((550, y), "VISUAL COMPARISON", fill=COLORS['forest_green'], font=font_large)

    # Current logo simulation (simplified)
    y += 80
    # "SNOWBRIX AI" in current colors
    draw.text((80, y), "SNOW", fill=CURRENT_COLORS['blue'], font=font_large)
    draw.text((280, y), "BRIX", fill=CURRENT_COLORS['orange'], font=font_large)
    draw.text((480, y), "AI", fill=CURRENT_COLORS['gray'], font=font_large)
    draw.text((100, y+60), "Current", fill=COLORS['charcoal'], font=font_small)

    # Recommended logo simulation
    draw.text((880, y), "SNOW", fill=COLORS['forest_green'], font=font_large)
    draw.text((1080, y), "BRIX", fill=COLORS['terracotta'], font=font_large)
    draw.text((1280, y), "AI", fill=COLORS['charcoal'], font=font_large)
    draw.text((900, y+60), "Recommended (Snowbrix Brand)", fill=COLORS['charcoal'], font=font_small)

    # Save
    output_path = Path("_Snowbrix_Logo_Color_Guide.png")
    img.save(output_path)
    print(f"[OK] Created: {output_path}")

    return output_path


def create_detailed_mockup():
    """Create detailed logo mockup on cream background"""

    width, height = 1920, 1080
    img = Image.new('RGB', (width, height), COLORS['cream'])
    draw = ImageDraw.Draw(img)

    try:
        font_logo = ImageFont.truetype("arialbd.ttf", 120)
        font_subtitle = ImageFont.truetype("arial.ttf", 40)
        font_note = ImageFont.truetype("arial.ttf", 32)
    except:
        font_logo = ImageFont.load_default()
        font_subtitle = ImageFont.load_default()
        font_note = ImageFont.load_default()

    # Title
    draw.text((760, 100), "SNOWBRIX", fill=COLORS['forest_green'], font=font_logo)

    # Subtitle
    draw.text((720, 240), "AI-Powered Data Engineering",
              fill=COLORS['sage_green'], font=font_subtitle)

    # Logo text with Snowbrix colors
    y = 400
    draw.text((400, y), "SNOW", fill=COLORS['forest_green'], font=font_logo)
    draw.text((780, y), "BRIX", fill=COLORS['terracotta'], font=font_logo)
    draw.text((1180, y), "AI", fill=COLORS['charcoal'], font=font_logo)

    # Color legend
    y = 600
    draw.text((600, y), "Forest Green (#2D5F3F) - SNOW text & Snowflake icon", fill=COLORS['forest_green'], font=font_note)
    y += 50
    draw.text((600, y), "Terracotta (#C97D60) - BRIX text & Bricks icon", fill=COLORS['terracotta'], font=font_note)
    y += 50
    draw.text((600, y), "Sage Green (#6B9080) - Accents", fill=COLORS['sage_green'], font=font_note)
    y += 50
    draw.text((600, y), "Cream Background (#FDF8F3)", fill=COLORS['charcoal'], font=font_note)

    # Note
    y = 850
    draw.text((400, y), "Warm • Professional • Educational • Modern",
              fill=COLORS['sage_green'], font=font_subtitle)

    # Save
    output_path = Path("_Snowbrix_Logo_Mockup.png")
    img.save(output_path)
    print(f"[OK] Created: {output_path}")

    return output_path


if __name__ == "__main__":
    print("\nCreating Snowbrix Logo Color Guides...\n")

    # Create comparison guide
    guide_path = create_color_palette_guide()

    # Create mockup
    mockup_path = create_detailed_mockup()

    print(f"\n{'='*70}")
    print("SNOWBRIX LOGO COLOR TRANSFORMATION")
    print(f"{'='*70}")
    print(f"\nFiles created:")
    print(f"  1. Color Guide: {guide_path}")
    print(f"  2. Logo Mockup: {mockup_path}")
    print(f"\nRecommendations:")
    print(f"  - Snowflake icon: Forest Green (#2D5F3F)")
    print(f"  - Bricks icon: Terracotta (#C97D60)")
    print(f"  - 'SNOW' text: Forest Green (#2D5F3F)")
    print(f"  - 'BRIX' text: Terracotta (#C97D60) [UPDATED]")
    print(f"  - 'AI' text: Charcoal (#4A4A4A)")
    print(f"  - Background: Cream (#FDF8F3) or transparent")
    print(f"\nVisual Pairing:")
    print(f"  SNOW (green) -> Snowflake (green)")
    print(f"  BRIX (terracotta) -> Bricks (terracotta)")
    print(f"\nThis creates perfect visual consistency!")
