"""
Refined Brand Color Palettes - Cream-based Modern Design
Based on successful educational platform designs
"""

from pptx.dml.color import RGBColor


class RefinedBrandColors:
    """Refined modern color schemes optimized for cream backgrounds"""

    # Option 1: WARM & MODERN (Inspired by Notion, Airtable)
    # Cream + Deep Teal + Coral
    WARM_MODERN = {
        'name': 'Warm Modern',
        'description': 'Cream + Deep Teal + Coral - Friendly, professional, energetic',

        # Backgrounds
        'bg_primary': RGBColor(254, 250, 242),      # Soft cream #FEFAF2
        'bg_secondary': RGBColor(249, 245, 235),    # Warmer cream #F9F5EB
        'bg_card': RGBColor(255, 255, 255),         # Pure white

        # Primary colors (Deep Teal - professional yet warm)
        'color_primary': RGBColor(31, 111, 108),    # Deep teal #1F6F6C
        'color_primary_dark': RGBColor(18, 81, 79), # Darker teal #12514F
        'color_primary_light': RGBColor(184, 231, 229), # Light teal #B8E7E5

        # Accent colors (Coral - energetic, warm)
        'color_accent': RGBColor(255, 107, 107),    # Coral #FF6B6B
        'color_accent_dark': RGBColor(238, 82, 82), # Deep coral #EE5252
        'color_accent_light': RGBColor(255, 224, 224), # Pale coral #FFE0E0

        # Text colors
        'text_primary': RGBColor(45, 55, 72),       # Charcoal #2D3748
        'text_secondary': RGBColor(113, 128, 150),  # Warm grey #718296
        'text_accent': RGBColor(31, 111, 108),      # Teal

        # Additional accents
        'accent_gold': RGBColor(255, 183, 77),      # Golden yellow #FFB74D
        'accent_purple': RGBColor(156, 136, 255),   # Soft purple #9C88FF
    }

    # Option 2: BOLD & FRIENDLY (Inspired by Canva, Figma)
    # Cream + Navy + Bright Orange
    BOLD_FRIENDLY = {
        'name': 'Bold Friendly',
        'description': 'Cream + Navy + Bright Orange - Confident, approachable',

        # Backgrounds
        'bg_primary': RGBColor(255, 251, 245),      # Vanilla cream #FFFBF5
        'bg_secondary': RGBColor(252, 246, 237),    # Warm beige #FCF6ED
        'bg_card': RGBColor(255, 255, 255),         # White

        # Primary colors (Navy - professional, trustworthy)
        'color_primary': RGBColor(37, 56, 88),      # Navy #253858
        'color_primary_dark': RGBColor(26, 43, 73), # Deep navy #1A2B49
        'color_primary_light': RGBColor(214, 225, 241), # Light navy #D6E1F1

        # Accent colors (Vibrant Orange - energetic)
        'color_accent': RGBColor(255, 120, 50),     # Bright orange #FF7832
        'color_accent_dark': RGBColor(230, 95, 25), # Deep orange #E65F19
        'color_accent_light': RGBColor(255, 230, 215), # Pale orange #FFE6D7

        # Text colors
        'text_primary': RGBColor(31, 41, 55),       # Near black #1F2937
        'text_secondary': RGBColor(107, 114, 128),  # Medium grey #6B7280
        'text_accent': RGBColor(37, 56, 88),        # Navy

        # Additional accents
        'accent_green': RGBColor(72, 187, 120),     # Fresh green #48BB78
        'accent_pink': RGBColor(255, 87, 157),      # Vibrant pink #FF579D
    }

    # Option 3: SOPHISTICATED MODERN (Inspired by Stripe, Linear)
    # Cream + Charcoal + Emerald
    SOPHISTICATED = {
        'name': 'Sophisticated Modern',
        'description': 'Cream + Charcoal + Emerald - Elegant, premium',

        # Backgrounds
        'bg_primary': RGBColor(255, 253, 248),      # Ivory cream #FFFDF8
        'bg_secondary': RGBColor(250, 248, 243),    # Soft grey-cream #FAF8F3
        'bg_card': RGBColor(255, 255, 255),         # White

        # Primary colors (Charcoal - sophisticated)
        'color_primary': RGBColor(52, 64, 84),      # Charcoal #344054
        'color_primary_dark': RGBColor(31, 41, 55), # Deep charcoal #1F2937
        'color_primary_light': RGBColor(209, 213, 219), # Light grey #D1D5DB

        # Accent colors (Emerald - fresh, premium)
        'color_accent': RGBColor(16, 185, 129),     # Emerald #10B981
        'color_accent_dark': RGBColor(5, 150, 105), # Deep emerald #059669
        'color_accent_light': RGBColor(209, 250, 229), # Pale emerald #D1FAE5

        # Text colors
        'text_primary': RGBColor(17, 24, 39),       # Almost black #111827
        'text_secondary': RGBColor(75, 85, 99),     # Dark grey #4B5563
        'text_accent': RGBColor(16, 185, 129),      # Emerald

        # Additional accents
        'accent_amber': RGBColor(251, 191, 36),     # Amber #FBBF24
        'accent_indigo': RGBColor(99, 102, 241),    # Indigo #6366F1
    }

    # Option 4: ENERGETIC GROWTH (Modern EdTech style)
    # Cream + Purple + Orange gradient
    ENERGETIC_GROWTH = {
        'name': 'Energetic Growth',
        'description': 'Cream + Purple + Orange - Dynamic, creative, growth-focused',

        # Backgrounds
        'bg_primary': RGBColor(255, 250, 245),      # Peach cream #FFFAF5
        'bg_secondary': RGBColor(253, 245, 237),    # Warm cream #FDF5ED
        'bg_card': RGBColor(255, 255, 255),         # White

        # Primary colors (Rich Purple - creative, premium)
        'color_primary': RGBColor(124, 58, 237),    # Purple #7C3AED
        'color_primary_dark': RGBColor(91, 33, 182), # Deep purple #5B21B6
        'color_primary_light': RGBColor(233, 213, 255), # Pale purple #E9D5FF

        # Accent colors (Vibrant Orange - energy)
        'color_accent': RGBColor(251, 146, 60),     # Vibrant orange #FB923C
        'color_accent_dark': RGBColor(234, 88, 12), # Deep orange #EA580C
        'color_accent_light': RGBColor(254, 237, 224), # Pale orange #FEEDE0

        # Text colors
        'text_primary': RGBColor(30, 41, 59),       # Slate #1E293B
        'text_secondary': RGBColor(100, 116, 139),  # Grey-slate #64748B
        'text_accent': RGBColor(124, 58, 237),      # Purple

        # Additional accents
        'accent_pink': RGBColor(244, 114, 182),     # Pink #F472B6
        'accent_teal': RGBColor(20, 184, 166),      # Teal #14B8A6
    }

    # Option 5: NATURAL WARMTH (Earthy, organic)
    # Cream + Forest Green + Terracotta
    NATURAL_WARMTH = {
        'name': 'Natural Warmth',
        'description': 'Cream + Forest Green + Terracotta - Warm, organic, trustworthy',

        # Backgrounds
        'bg_primary': RGBColor(255, 251, 240),      # Warm cream #FFFBF0
        'bg_secondary': RGBColor(250, 245, 230),    # Soft beige #FAF5E6
        'bg_card': RGBColor(255, 255, 255),         # White

        # Primary colors (Forest Green - natural, growth)
        'color_primary': RGBColor(34, 139, 87),     # Forest green #228B57
        'color_primary_dark': RGBColor(21, 101, 64), # Deep green #156540
        'color_primary_light': RGBColor(198, 240, 218), # Mint green #C6F0DA

        # Accent colors (Terracotta - warm, earthy)
        'color_accent': RGBColor(214, 126, 79),     # Terracotta #D67E4F
        'color_accent_dark': RGBColor(192, 96, 49), # Deep terracotta #C06031
        'color_accent_light': RGBColor(246, 224, 210), # Pale terracotta #F6E0D2

        # Text colors
        'text_primary': RGBColor(42, 54, 46),       # Dark green-grey #2A362E
        'text_secondary': RGBColor(96, 112, 102),   # Medium green-grey #607066
        'text_accent': RGBColor(34, 139, 87),       # Forest green

        # Additional accents
        'accent_gold': RGBColor(218, 165, 32),      # Gold #DAA520
        'accent_sage': RGBColor(135, 169, 152),     # Sage #87A998
    }

    @classmethod
    def get_scheme(cls, scheme_name: str = 'warm') -> dict:
        """Get color scheme by name"""
        schemes = {
            'warm': cls.WARM_MODERN,
            'bold': cls.BOLD_FRIENDLY,
            'sophisticated': cls.SOPHISTICATED,
            'energetic': cls.ENERGETIC_GROWTH,
            'natural': cls.NATURAL_WARMTH,
        }
        return schemes.get(scheme_name.lower(), cls.WARM_MODERN)

    @classmethod
    def list_schemes(cls):
        """List all available schemes with color previews"""
        return [
            ('warm', cls.WARM_MODERN),
            ('bold', cls.BOLD_FRIENDLY),
            ('sophisticated', cls.SOPHISTICATED),
            ('energetic', cls.ENERGETIC_GROWTH),
            ('natural', cls.NATURAL_WARMTH),
        ]


# Preview
if __name__ == "__main__":
    print("REFINED CREAM-BASED COLOR SCHEMES")
    print("="*70)
    print()

    for name, scheme in RefinedBrandColors.list_schemes():
        print(f"{scheme['name'].upper()}")
        print(f"  {scheme['description']}")
        print(f"  Command: --brand-refined {name}")
        print()
