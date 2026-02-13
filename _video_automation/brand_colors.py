"""
Modern Brand Color Schemes for Slide Templates
Professional, warm, and engaging design
"""

from pptx.dml.color import RGBColor


class BrandColors:
    """Brand color schemes for presentations"""

    # GrowthSchool-inspired: Cream + Green (Modern & Professional)
    GROWTHSCHOOL_STYLE = {
        'name': 'GrowthSchool Modern',
        'description': 'Warm cream background with vibrant green accents',

        # Backgrounds
        'bg_primary': RGBColor(255, 251, 245),      # Warm cream #FFFBF5
        'bg_secondary': RGBColor(250, 245, 235),    # Darker cream #FAF5EB
        'bg_card': RGBColor(255, 255, 255),         # White cards

        # Green palette (vibrant but professional)
        'green_primary': RGBColor(34, 139, 34),     # Forest green #228B22
        'green_accent': RGBColor(46, 184, 92),      # Bright green #2EB85C
        'green_dark': RGBColor(21, 87, 36),         # Deep green #155724
        'green_light': RGBColor(200, 230, 201),     # Light green #C8E6C9

        # Text colors
        'text_primary': RGBColor(45, 55, 45),       # Dark green-grey #2D372D
        'text_secondary': RGBColor(95, 115, 95),    # Medium green-grey #5F735F
        'text_accent': RGBColor(34, 139, 34),       # Green for highlights

        # Accent colors
        'accent_gold': RGBColor(218, 165, 32),      # Gold accent #DAA520
        'accent_orange': RGBColor(255, 140, 0),     # Orange accent #FF8C00
    }

    # Alternative: Sage Green + Cream (Softer, More Elegant)
    SAGE_STYLE = {
        'name': 'Sage Elegance',
        'description': 'Soft sage green with warm cream',

        # Backgrounds
        'bg_primary': RGBColor(255, 250, 240),      # Cream #FFFAF0
        'bg_secondary': RGBColor(245, 245, 238),    # Light beige #F5F5EE
        'bg_card': RGBColor(255, 255, 255),         # White

        # Sage green palette
        'green_primary': RGBColor(118, 154, 116),   # Sage #769A74
        'green_accent': RGBColor(143, 188, 143),    # Light sage #8FBC8F
        'green_dark': RGBColor(85, 107, 47),        # Olive green #556B2F
        'green_light': RGBColor(220, 237, 219),     # Very light sage #DCEDDB

        # Text colors
        'text_primary': RGBColor(60, 64, 67),       # Charcoal #3C4043
        'text_secondary': RGBColor(95, 99, 104),    # Grey #5F6368
        'text_accent': RGBColor(118, 154, 116),     # Sage for highlights

        # Accent colors
        'accent_terracotta': RGBColor(205, 133, 63), # Terracotta #CD853F
        'accent_coral': RGBColor(255, 127, 80),      # Coral #FF7F50
    }

    # Bold & Modern: Emerald + Cream
    EMERALD_STYLE = {
        'name': 'Emerald Modern',
        'description': 'Bold emerald green with soft cream',

        # Backgrounds
        'bg_primary': RGBColor(254, 250, 240),      # Vanilla cream #FEFAF0
        'bg_secondary': RGBColor(250, 243, 224),    # Light cream #FAF3E0
        'bg_card': RGBColor(255, 255, 255),         # White

        # Emerald palette
        'green_primary': RGBColor(0, 168, 107),     # Emerald #00A86B
        'green_accent': RGBColor(16, 185, 129),     # Bright emerald #10B981
        'green_dark': RGBColor(6, 95, 70),          # Deep emerald #065F46
        'green_light': RGBColor(209, 250, 229),     # Mint #D1FAE5

        # Text colors
        'text_primary': RGBColor(31, 41, 55),       # Near black #1F2937
        'text_secondary': RGBColor(75, 85, 99),     # Dark grey #4B5563
        'text_accent': RGBColor(0, 168, 107),       # Emerald

        # Accent colors
        'accent_amber': RGBColor(251, 191, 36),     # Amber #FBBF24
        'accent_rose': RGBColor(244, 114, 182),     # Rose #F472B6
    }

    # Data Engineering Professional (keeps blue but adds warmth)
    DATAENG_WARM = {
        'name': 'Data Engineering Warm',
        'description': 'Professional blue-green with warm cream',

        # Backgrounds
        'bg_primary': RGBColor(255, 252, 245),      # Warm white #FFFCF5
        'bg_secondary': RGBColor(248, 246, 242),    # Warm grey #F8F6F2
        'bg_card': RGBColor(255, 255, 255),         # White

        # Teal/Blue-green palette (tech + warm)
        'green_primary': RGBColor(13, 148, 136),    # Teal #0D9488
        'green_accent': RGBColor(20, 184, 166),     # Bright teal #14B8A6
        'green_dark': RGBColor(19, 78, 74),         # Deep teal #134E4A
        'green_light': RGBColor(204, 251, 241),     # Light teal #CCFBF1

        # Text colors
        'text_primary': RGBColor(30, 41, 59),       # Slate #1E293B
        'text_secondary': RGBColor(71, 85, 105),    # Medium slate #475569
        'text_accent': RGBColor(13, 148, 136),      # Teal

        # Accent colors
        'accent_orange': RGBColor(249, 115, 22),    # Orange #F97316
        'accent_purple': RGBColor(168, 85, 247),    # Purple #A855F7
    }

    @classmethod
    def get_scheme(cls, scheme_name: str = 'growthschool') -> dict:
        """Get color scheme by name"""
        schemes = {
            'growthschool': cls.GROWTHSCHOOL_STYLE,
            'sage': cls.SAGE_STYLE,
            'emerald': cls.EMERALD_STYLE,
            'dataeng': cls.DATAENG_WARM,
        }
        return schemes.get(scheme_name.lower(), cls.GROWTHSCHOOL_STYLE)

    @classmethod
    def list_schemes(cls):
        """List all available schemes"""
        return [
            ('growthschool', cls.GROWTHSCHOOL_STYLE),
            ('sage', cls.SAGE_STYLE),
            ('emerald', cls.EMERALD_STYLE),
            ('dataeng', cls.DATAENG_WARM),
        ]


# Preview/Demo
if __name__ == "__main__":
    print("Available Brand Color Schemes:\n")

    for name, scheme in BrandColors.list_schemes():
        print(f"{scheme['name'].upper()}")
        print(f"  {scheme['description']}")
        print(f"  Command: --brand {name}")
        print()
