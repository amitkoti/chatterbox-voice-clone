"""
Generate Full Snowbrix Logo
Complete logo with snowflake + bricks icons and text
"""

from PIL import Image, ImageDraw, ImageFont
import math
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

def draw_snowflake(draw, center_x, center_y, size, color):
    """Draw a geometric snowflake icon"""
    # Draw 6 branches from center
    for angle in range(0, 360, 60):
        rad = math.radians(angle)

        # Main branch
        end_x = center_x + size * math.cos(rad)
        end_y = center_y + size * math.sin(rad)
        draw.line([(center_x, center_y), (end_x, end_y)], fill=color, width=8)

        # Side branches
        mid_x = center_x + (size * 0.6) * math.cos(rad)
        mid_y = center_y + (size * 0.6) * math.sin(rad)

        for side_angle in [-30, 30]:
            side_rad = math.radians(angle + side_angle)
            side_end_x = mid_x + (size * 0.3) * math.cos(side_rad)
            side_end_y = mid_y + (size * 0.3) * math.sin(side_rad)
            draw.line([(mid_x, mid_y), (side_end_x, side_end_y)], fill=color, width=6)

    # Center circle
    draw.ellipse([center_x-12, center_y-12, center_x+12, center_y+12], fill=color)

def draw_3d_cube(draw, x, y, size, color, shade_factor=0.7):
    """Draw a 3D isometric cube"""
    # Calculate points for isometric cube
    top_center = (x + size, y)
    left_corner = (x, y + size//2)
    right_corner = (x + size*2, y + size//2)
    bottom_center = (x + size, y + size)

    # Top face (lighter)
    top_color = tuple(int(c * 1.1) if int(c * 1.1) <= 255 else 255 for c in color)
    draw.polygon([top_center, left_corner, (x + size, y + size//2), (x + size*2, y)],
                 fill=top_color)

    # Left face (darker)
    left_color = tuple(int(c * shade_factor) for c in color)
    draw.polygon([left_corner, (x + size, y + size//2), bottom_center, (x, y + size)],
                 fill=left_color)

    # Right face (medium)
    right_color = tuple(int(c * 0.85) for c in color)
    draw.polygon([(x + size*2, y), (x + size, y + size//2), bottom_center, right_corner],
                 fill=right_color)

    # Outline
    draw.polygon([top_center, left_corner, (x, y + size), bottom_center, right_corner,
                  (x + size*2, y), top_center], outline=tuple(int(c * 0.6) for c in color), width=2)

def draw_brick_structure(draw, start_x, start_y, color):
    """Draw a structure of 3D bricks"""
    cube_size = 40

    # Back row (top)
    draw_3d_cube(draw, start_x + cube_size, start_y - cube_size//2, cube_size, color, 0.65)
    draw_3d_cube(draw, start_x + cube_size*3, start_y - cube_size//2, cube_size, color, 0.65)

    # Middle row
    draw_3d_cube(draw, start_x, start_y + cube_size//2, cube_size, color, 0.75)
    draw_3d_cube(draw, start_x + cube_size*2, start_y + cube_size//2, cube_size, color, 0.75)
    draw_3d_cube(draw, start_x + cube_size*4, start_y + cube_size//2, cube_size, color, 0.75)

    # Front row (bottom) - brightest
    draw_3d_cube(draw, start_x + cube_size, start_y + cube_size*1.5, cube_size, color, 0.85)
    draw_3d_cube(draw, start_x + cube_size*3, start_y + cube_size*1.5, cube_size, color, 0.85)

def create_full_logo(background='cream'):
    """Create the complete Snowbrix logo"""

    # Canvas size
    width, height = 1920, 600

    if background == 'cream':
        bg_color = COLORS['cream']
    elif background == 'white':
        bg_color = COLORS['white']
    else:  # transparent
        bg_color = (255, 255, 255, 0)

    img = Image.new('RGBA', (width, height), bg_color)
    draw = ImageDraw.Draw(img)

    # Load fonts
    try:
        font_logo = ImageFont.truetype("arialbd.ttf", 140)
        font_ai = ImageFont.truetype("arialbd.ttf", 100)
        font_tagline = ImageFont.truetype("arial.ttf", 36)
    except:
        font_logo = ImageFont.load_default()
        font_ai = ImageFont.load_default()
        font_tagline = ImageFont.load_default()

    # === DRAW ICONS ===
    icon_y = 180

    # Snowflake (left) - Forest Green
    snowflake_x = 280
    draw_snowflake(draw, snowflake_x, icon_y, 80, COLORS['forest_green'])

    # Bricks (right) - Terracotta
    bricks_x = 1450
    draw_brick_structure(draw, bricks_x, icon_y - 60, COLORS['terracotta'])

    # === DRAW TEXT ===
    text_y = 240

    # "SNOW" in Forest Green
    draw.text((500, text_y), "SNOW", fill=COLORS['forest_green'], font=font_logo)

    # "BRIX" in Terracotta
    draw.text((900, text_y), "BRIX", fill=COLORS['terracotta'], font=font_logo)

    # "AI" in Charcoal
    draw.text((1260, text_y + 20), "AI", fill=COLORS['charcoal'], font=font_ai)

    # Tagline
    tagline = "AI-Powered Data Engineering Solutions"
    draw.text((560, text_y + 170), tagline, fill=COLORS['sage_green'], font=font_tagline)

    return img

def create_logo_variations():
    """Create multiple logo variations"""

    print("\nGenerating Snowbrix Logo Variations...\n")

    variations = [
        ('cream', 'Full Logo - Cream Background'),
        ('white', 'Full Logo - White Background'),
        ('transparent', 'Full Logo - Transparent'),
    ]

    output_files = []

    for bg_type, description in variations:
        print(f"Creating: {description}...")
        img = create_full_logo(bg_type)

        # Save
        filename = f"Snowbrix_Logo_{bg_type.capitalize()}.png"
        output_path = Path(filename)

        if bg_type == 'transparent':
            img.save(output_path, 'PNG')
        else:
            # Convert RGBA to RGB for non-transparent versions
            rgb_img = Image.new('RGB', img.size, bg_type if bg_type == 'white' else COLORS['cream'])
            rgb_img.paste(img, mask=img.split()[3] if len(img.split()) == 4 else None)
            rgb_img.save(output_path, 'PNG')

        output_files.append(output_path)
        print(f"  [OK] Saved: {output_path}")

    return output_files

def create_logo_icon_only():
    """Create icon-only version (square)"""

    print("\nCreating icon-only version...")

    size = 800
    img = Image.new('RGBA', (size, size), COLORS['cream'])
    draw = ImageDraw.Draw(img)

    # Snowflake (left)
    snowflake_x = 220
    snowflake_y = 400
    draw_snowflake(draw, snowflake_x, snowflake_y, 100, COLORS['forest_green'])

    # Bricks (right)
    bricks_x = 420
    bricks_y = 340
    draw_brick_structure(draw, bricks_x, bricks_y, COLORS['terracotta'])

    # Save
    output_path = Path("Snowbrix_Icon_Only.png")
    rgb_img = Image.new('RGB', img.size, COLORS['cream'])
    rgb_img.paste(img, mask=img.split()[3] if len(img.split()) == 4 else None)
    rgb_img.save(output_path, 'PNG')

    print(f"  [OK] Saved: {output_path}")

    return output_path

if __name__ == "__main__":
    print("="*70)
    print("SNOWBRIX LOGO GENERATOR")
    print("="*70)

    # Create full logo variations
    logo_files = create_logo_variations()

    # Create icon-only version
    icon_file = create_logo_icon_only()

    print("\n" + "="*70)
    print("LOGO FILES CREATED")
    print("="*70)

    print("\nFull Logos:")
    for f in logo_files:
        print(f"  - {f}")

    print(f"\nIcon Only:")
    print(f"  - {icon_file}")

    print("\n" + "="*70)
    print("SNOWBRIX BRAND COLORS")
    print("="*70)
    print("\nSnowflake Icon: Forest Green (#2D5F3F)")
    print("Bricks Icon: Terracotta (#C97D60)")
    print("'SNOW' Text: Forest Green (#2D5F3F)")
    print("'BRIX' Text: Terracotta (#C97D60)")
    print("'AI' Text: Charcoal (#4A4A4A)")
    print("Tagline: Sage Green (#6B9080)")
    print("Background: Cream (#FDF8F3)")

    print("\n" + "="*70)
    print("Files ready for use!")
    print("="*70)
