"""
Snowbrix Color Palette
Authentic cream + green design system
Professional, warm, educational aesthetic
"""

from pptx.dml.color import RGBColor


class SnowbrixColors:
    """Snowbrix brand color palette - cream + green aesthetic"""

    # THE SNOWBRIX PALETTE
    SNOWBRIX_AUTHENTIC = {
        'name': 'Snowbrix Professional',
        'description': 'Cream + Forest/Sage Green - Warm, educational, professional',

        # === BACKGROUNDS (Cream/Warm Beige) ===
        'bg_primary': RGBColor(253, 248, 243),      # #FDF8F3 - Main cream background
        'bg_secondary': RGBColor(250, 245, 240),    # #FAF5F0 - Light cream alternate
        'bg_card': RGBColor(254, 254, 254),         # #FEFEFE - Off-white for cards
        'bg_accent': RGBColor(232, 243, 237),       # #E8F3ED - Light green background

        # === PRIMARY COLORS (Green Spectrum) ===
        'color_primary': RGBColor(45, 95, 63),      # #2D5F3F - Forest Green (headlines, CTAs)
        'color_primary_dark': RGBColor(35, 75, 50), # Darker forest green
        'color_primary_light': RGBColor(232, 243, 237), # #E8F3ED - Mint cream

        # === SECONDARY/ACCENT GREENS ===
        'color_secondary': RGBColor(107, 144, 128), # #6B9080 - Sage Green (sub-headings)
        'color_accent': RGBColor(139, 168, 136),    # #8BA888 - Olive/Accent Green
        'color_accent_light': RGBColor(232, 243, 237), # #E8F3ED - Light green

        # === TEXT COLORS ===
        'text_primary': RGBColor(26, 26, 26),       # #1A1A1A - Dark charcoal (main text)
        'text_secondary': RGBColor(74, 74, 74),     # #4A4A4A - Warm gray (body text)
        'text_on_green': RGBColor(253, 248, 243),   # Cream text on green backgrounds

        # === SUPPORTING COLORS ===
        'accent_terracotta': RGBColor(201, 125, 96), # #C97D60 - Warm accent
        'accent_slate': RGBColor(44, 62, 80),       # #2C3E50 - Slate gray (strong emphasis)

        # === USAGE NOTES ===
        'usage': {
            'title_slides': {
                'background': '#FDF8F3',
                'title': '#2D5F3F',
                'subtitle': '#6B9080'
            },
            'content_slides': {
                'background': '#FAF5F0',
                'heading': '#2D5F3F',
                'body': '#4A4A4A',
                'bullets': '#6B9080'
            },
            'emphasis_slides': {
                'background': '#E8F3ED',
                'text': '#2D5F3F',
                'accent': '#C97D60'
            },
            'closing_slides': {
                'background': '#2D5F3F',
                'text': '#FDF8F3'
            }
        }
    }

    @classmethod
    def get_scheme(cls) -> dict:
        """Get the Snowbrix color scheme"""
        return cls.SNOWBRIX_AUTHENTIC

    @classmethod
    def get_color_combinations(cls):
        """Get recommended color combinations"""
        return [
            {
                'name': 'Snowbrix Classic',
                'bg': '#FDF8F3',
                'heading': '#2D5F3F',
                'body': '#4A4A4A',
                'accent': '#6B9080'
            },
            {
                'name': 'High Contrast',
                'bg': '#FAF5F0',
                'heading': '#1A1A1A',
                'body': '#2D5F3F',
                'accent': '#C97D60'
            },
            {
                'name': 'Soft & Modern',
                'bg': '#E8F3ED',
                'heading': '#2D5F3F',
                'body': '#2C3E50',
                'accent': '#8BA888'
            }
        ]


if __name__ == "__main__":
    print("SNOWBRIX COLOR PALETTE")
    print("="*70)
    print()

    scheme = SnowbrixColors.get_scheme()
    print(f"{scheme['name']}")
    print(f"{scheme['description']}")
    print()

    print("PRIMARY COLORS:")
    print(f"  Cream Background: #FDF8F3")
    print(f"  Forest Green:     #2D5F3F (Primary)")
    print(f"  Sage Green:       #6B9080 (Secondary)")
    print(f"  Terracotta:       #C97D60 (Accent)")
    print()

    print("RECOMMENDED COMBINATIONS:")
    for combo in SnowbrixColors.get_color_combinations():
        print(f"\n  {combo['name']}:")
        print(f"    Background: {combo['bg']}")
        print(f"    Heading:    {combo['heading']}")
        print(f"    Body:       {combo['body']}")
        print(f"    Accent:     {combo['accent']}")
