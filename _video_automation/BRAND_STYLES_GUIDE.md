# Brand Styles Guide
## Modern Color Schemes for Professional Presentations

---

## 1. GrowthSchool Modern (Recommended)
**Command:** `--brand growthschool`

### Color Palette
- **Background**: Warm Cream `#FFFBF5` - Soft, inviting, professional
- **Cards/Overlays**: White `#FFFFFF` - Clean contrast
- **Primary Green**: Forest Green `#228B22` - Bold, trustworthy
- **Accent Green**: Bright Green `#2EB85C` - Energetic, modern
- **Text Primary**: Dark Green-Grey `#2D372D` - Readable, sophisticated
- **Text Secondary**: Medium Green-Grey `#5F735F` - Subtle hierarchy
- **Accent Colors**: Gold `#DAA520`, Orange `#FF8C00`

### Best For
- Growth-focused presentations
- Modern startup vibe
- Educational content
- Warm, approachable feel
- B2B SaaS presentations

### Visual Style
```
┌────────────────────────────────────┐
│  Warm Cream Background             │
│                                    │
│  ╔══════════════════════╗          │
│  ║  Title in Dark Green ║          │
│  ╚══════════════════════╝          │
│  (with bright green accent border) │
│                                    │
│  • Key points in forest green      │
│  • Supporting text in grey-green   │
│                                    │
└────────────────────────────────────┘
```

---

## 2. Sage Elegance
**Command:** `--brand sage`

### Color Palette
- **Background**: Light Cream `#FFFAF0` - Soft, elegant
- **Primary Green**: Sage `#769A74` - Calm, sophisticated
- **Accent Green**: Light Sage `#8FBC8F` - Gentle, natural
- **Text Primary**: Charcoal `#3C4043` - Professional
- **Accent Colors**: Terracotta `#CD853F`, Coral `#FF7F50`

### Best For
- Executive presentations
- Wellness/lifestyle brands
- Elegant, refined aesthetic
- Nature-focused content
- Consulting presentations

### Mood
Sophisticated, calm, timeless elegance

---

## 3. Emerald Modern
**Command:** `--brand emerald`

### Color Palette
- **Background**: Vanilla Cream `#FEFAF0` - Ultra-soft, premium
- **Primary Green**: Emerald `#00A86B` - Bold, luxurious
- **Accent Green**: Bright Emerald `#10B981` - Vibrant, energetic
- **Text Primary**: Near Black `#1F2937` - Strong contrast
- **Accent Colors**: Amber `#FBBF24`, Rose `#F472B6`

### Best For
- Bold, modern presentations
- Tech startups
- Innovation-focused content
- High-energy pitches
- Premium products

### Mood
Bold, confident, cutting-edge, luxurious

---

## 4. Data Engineering Warm
**Command:** `--brand dataeng`

### Color Palette
- **Background**: Warm White `#FFFCF5` - Technical but warm
- **Primary Green**: Teal `#0D9488` - Tech-professional
- **Accent Green**: Bright Teal `#14B8A6` - Modern data
- **Text Primary**: Slate `#1E293B` - Corporate professional
- **Accent Colors**: Orange `#F97316`, Purple `#A855F7`

### Best For
- Data engineering presentations
- Technical but approachable
- B2B technology
- Analytics/BI content
- Cloud platform pitches

### Mood
Professional, technical, trustworthy, modern

---

## Usage Examples

### Basic Usage
```bash
# Use GrowthSchool style (default)
python slide_redesigner_v2.py presentation.pptx --create-slides

# Use Sage style
python slide_redesigner_v2.py presentation.pptx --create-slides --brand sage

# Use Emerald style
python slide_redesigner_v2.py presentation.pptx --create-slides --brand emerald

# Use Data Engineering style
python slide_redesigner_v2.py presentation.pptx --create-slides --brand dataeng
```

### Complete Workflow with Brand
```bash
# Stage 1: Generate prompts
python slide_redesigner_v2.py my_presentation.pptx --plan-only

# Stage 2: Generate images
python slide_redesigner_v2.py my_presentation.pptx --generate

# Stage 3: Create slides with brand style
python slide_redesigner_v2.py my_presentation.pptx --create-slides --brand growthschool
```

---

## Design Principles

### Typography
- **Title Size**: 52pt (larger for impact)
- **Body Text**: 24pt (readable from distance)
- **Font Weight**: Bold for titles, Regular for body
- **Line Spacing**: Generous for readability

### Spacing
- **Margins**: Generous whitespace (0.5-1 inch)
- **Card Padding**: Comfortable breathing room
- **Element Spacing**: Clear visual hierarchy

### Layout
- **Background**: Full-bleed cream color
- **Content Cards**: White cards with subtle borders
- **Images**: Full or partial bleed with overlays
- **Text Overlays**: Semi-transparent cards for readability

### Contrast
- **Text on Cream**: Dark green-grey for maximum readability
- **Accent Elements**: Bright green for calls-to-action
- **Border Accents**: Green borders for visual interest

---

## Comparison

| Style | Vibe | Energy | Use Case |
|-------|------|--------|----------|
| **GrowthSchool** | Modern, Warm | Medium-High | Growth, Education, Startup |
| **Sage** | Elegant, Calm | Low-Medium | Executive, Consulting, Wellness |
| **Emerald** | Bold, Luxury | High | Innovation, Premium, Tech |
| **DataEng** | Professional, Tech | Medium | B2B Tech, Analytics, Cloud |

---

## Customization

Want to create your own brand style? Edit `brand_colors.py`:

```python
CUSTOM_STYLE = {
    'name': 'My Brand',
    'description': 'My company colors',
    'bg_primary': RGBColor(255, 255, 255),  # Your background
    'green_primary': RGBColor(0, 128, 0),    # Your primary
    'text_primary': RGBColor(0, 0, 0),       # Your text
    # ... add more colors
}
```

---

## Tips for Best Results

### 1. Match Your Brand
- Use **GrowthSchool** for modern, approachable brands
- Use **Sage** for elegant, professional brands
- Use **Emerald** for bold, innovative brands
- Use **DataEng** for technical, B2B brands

### 2. Consistency
- Stick to one brand style per presentation
- Use across all your presentations for brand consistency

### 3. Image Selection
- Choose images that complement cream backgrounds
- Avoid very dark images (low contrast with green text)
- Prefer bright, airy images

### 4. Text Hierarchy
- Title: Dark green (maximum contrast)
- Body: Medium green-grey (readable but softer)
- Highlights: Bright green (calls attention)

---

## Preview Your Style

Run this to see all styles:
```bash
python brand_colors.py
```

Output:
```
Available Brand Color Schemes:

GROWTHSCHOOL MODERN
  Warm cream background with vibrant green accents
  Command: --brand growthschool

SAGE ELEGANCE
  Soft sage green with warm cream
  Command: --brand sage

EMERALD MODERN
  Bold emerald green with soft cream
  Command: --brand emerald

DATA ENGINEERING WARM
  Professional blue-green with warm cream
  Command: --brand dataeng
```

---

**Recommended**: Start with `--brand growthschool` for the warm, modern aesthetic you described!
