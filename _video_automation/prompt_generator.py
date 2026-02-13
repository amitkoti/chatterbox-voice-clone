"""
Intelligent Prompt Generator for Data Engineering Slides
Generates context-aware image prompts based on slide content
"""

import re
from typing import Dict, List, Tuple
from enum import Enum


class SlideType(Enum):
    """Types of slides we can detect"""
    TITLE = "title"
    COMPARISON = "comparison"
    ARCHITECTURE = "architecture"
    FEATURES = "features"
    METRICS = "metrics"
    TECHNICAL = "technical"
    SIMPLE = "simple"
    TABLE = "table"


class PromptGenerator:
    """Generates intelligent image prompts for Data Engineering slides"""

    def __init__(self):
        # Keywords for slide type detection
        self.keywords = {
            SlideType.COMPARISON: [
                'vs', 'versus', 'comparison', 'compare', 'difference',
                'contrast', 'between', 'snowflake vs', 'databricks vs'
            ],
            SlideType.ARCHITECTURE: [
                'architecture', 'pipeline', 'flow', 'design', 'infrastructure',
                'system', 'diagram', 'structure', 'data flow', 'etl', 'elt'
            ],
            SlideType.FEATURES: [
                'feature', 'benefit', 'advantage', 'capability', 'key points',
                'highlights', 'what', 'why', 'strengths'
            ],
            SlideType.METRICS: [
                'performance', 'metrics', 'benchmark', 'speed', 'cost',
                'pricing', 'statistics', 'numbers', 'results', 'data'
            ],
            SlideType.TECHNICAL: [
                'sql', 'code', 'query', 'syntax', 'command', 'script',
                'implementation', 'example', 'how to'
            ],
            SlideType.TABLE: [
                'table', 'comparison table', 'summary', 'overview',
                'matrix', 'grid'
            ]
        }

        # Prompt templates for each slide type
        self.templates = {
            SlideType.TITLE: self._generate_title_prompt,
            SlideType.COMPARISON: self._generate_comparison_prompt,
            SlideType.ARCHITECTURE: self._generate_architecture_prompt,
            SlideType.FEATURES: self._generate_features_prompt,
            SlideType.METRICS: self._generate_metrics_prompt,
            SlideType.TECHNICAL: self._generate_technical_prompt,
            SlideType.TABLE: self._generate_table_prompt,
            SlideType.SIMPLE: self._generate_simple_prompt,
        }

    def detect_slide_type(self, title: str, content: str, slide_number: int) -> SlideType:
        """Detect what type of slide this is"""
        combined = f"{title} {content}".lower()

        # First slide is always title
        if slide_number == 1:
            return SlideType.TITLE

        # Check for each type based on keywords
        for slide_type, keywords in self.keywords.items():
            if any(keyword in combined for keyword in keywords):
                return slide_type

        # Default to simple
        return SlideType.SIMPLE

    def extract_key_terms(self, text: str) -> List[str]:
        """Extract key technical terms from text"""
        terms = []

        # Data Engineering specific terms
        tech_terms = [
            'snowflake', 'databricks', 'spark', 'hadoop', 'kafka',
            'airflow', 'dbt', 'fivetran', 'airbyte', 'aws', 's3',
            'redshift', 'bigquery', 'azure', 'data lake', 'data warehouse',
            'lakehouse', 'etl', 'elt', 'pipeline', 'streaming',
            'batch', 'real-time', 'sql', 'python', 'scala'
        ]

        text_lower = text.lower()
        for term in tech_terms:
            if term in text_lower:
                terms.append(term)

        return list(set(terms))[:5]  # Max 5 terms

    def _generate_title_prompt(self, title: str, content: str, terms: List[str]) -> str:
        """Generate prompt for title slide"""
        prompt = f"""Professional title image for data engineering presentation.
Title: {title}

Style: Modern, warm, professional, educational
Background: Abstract data visualization, flowing data streams, or cloud infrastructure
Colors: Soft cream/beige (#FDF8F3) background with forest green (#2D5F3F) and sage green (#6B9080) accents
Elements: Subtle geometric patterns, data nodes, or connection lines in green tones
Mood: Professional, warm, inviting, trustworthy, educational
Text: Large, clean typography for title (if needed)

Visual elements suggesting: {', '.join(terms) if terms else 'data engineering, cloud, analytics'}

Format: 16:9 aspect ratio, light cream background with green accents
Quality: High resolution, professional corporate presentation style
Aesthetic: Warm, approachable, modern educational platform style"""

        return prompt

    def _generate_comparison_prompt(self, title: str, content: str, terms: List[str]) -> str:
        """Generate prompt for comparison slide"""
        # Detect what's being compared
        is_snowflake_databricks = 'snowflake' in content.lower() and 'databricks' in content.lower()

        if is_snowflake_databricks:
            prompt = f"""Split-screen comparison visual for: {title}

LEFT SIDE: Snowflake
- Snowflake logo or icon
- Sage green accent (#6B9080)
- Cloud data warehouse visual
- Clean, modern design

RIGHT SIDE: Databricks
- Databricks logo or icon
- Terracotta accent (#C97D60)
- Lakehouse platform visual
- Modern design matching left side

CENTER: Forest green "VS" text or versus symbol (#2D5F3F)

Style: Professional tech comparison, side-by-side layout
Background: Soft cream/beige (#FDF8F3)
Visual balance: Equal emphasis on both sides
Icons/symbols: Data, cloud, processing symbols in green tones
Modern, clean, warm educational style

Format: 16:9 aspect ratio, warm and professional"""
        else:
            prompt = f"""Comparison visual for: {title}

Show: Side-by-side comparison of {', '.join(terms[:2]) if len(terms) >= 2 else 'concepts'}
Style: Professional split-screen or dual panel design
Elements: Icons, symbols, or visual metaphors for each side
Colors: Forest green (#2D5F3F) and sage green (#6B9080) accents with terracotta highlights (#C97D60)
Background: Soft cream/beige (#FDF8F3)
Layout: Clear visual separation, balanced design
Mood: Objective, analytical, warm, professional

Format: 16:9 aspect ratio, clean warm educational style
{f'Key terms: {", ".join(terms)}' if terms else ''}"""

        return prompt

    def _generate_architecture_prompt(self, title: str, content: str, terms: List[str]) -> str:
        """Generate prompt for architecture diagram"""
        prompt = f"""Technical architecture diagram for: {title}

Diagram showing: Data engineering pipeline/architecture
Components to visualize:
- Data sources (left side): Databases, APIs, streaming data
- Ingestion layer: Data connectors, ETL/ELT tools
- Storage layer: Data warehouse, data lake (Snowflake, Databricks, cloud storage)
- Processing layer: Data transformation, compute engines
- Output layer (right side): BI tools, analytics, ML models

Style: Modern technical diagram, warm educational aesthetic
Visual elements:
- Component boxes with icons
- Arrows showing data flow (left to right)
- Clean, minimalist design
- Color-coded layers (forest green #2D5F3F for storage, sage green #6B9080 for processing, terracotta #C97D60 for output)

Colors: Forest green (#2D5F3F) and sage green (#6B9080) primary, terracotta (#C97D60) accents
Background: Soft cream/beige (#FDF8F3) for clarity
Layout: Horizontal flow chart style, organized layers
Icons: Use simple, recognizable tech/data icons in green tones

Key technologies: {', '.join(terms) if terms else 'cloud data platforms'}

Format: 16:9 aspect ratio, professional warm educational style
Clarity: Labels for each component, easy to understand"""

        return prompt

    def _generate_features_prompt(self, title: str, content: str, terms: List[str]) -> str:
        """Generate prompt for features/benefits slide"""
        prompt = f"""Feature highlights visual for: {title}

Style: Icon grid or feature showcase
Layout: 2x3 or 3x2 grid of feature cards

Each feature represented by:
- Clean icon (checkmark, star, lightning, shield, rocket, etc.) in forest green
- Short descriptive text
- Visual consistency across all features

Design: Modern, clean, warm, professional
Colors: Forest green (#2D5F3F) and sage green (#6B9080) icons with terracotta (#C97D60) highlights
Background: Soft cream/beige (#FDF8F3) warm educational style
Icons: Simple, modern, recognizable in green tones
Typography: Clean, readable fonts

Context: Data engineering platform features
{f'Related to: {", ".join(terms)}' if terms else ''}

Overall mood: Innovative, powerful, reliable, warm, approachable, professional
Format: 16:9 aspect ratio, presentation-ready quality"""

        return prompt

    def _generate_metrics_prompt(self, title: str, content: str, terms: List[str]) -> str:
        """Generate prompt for metrics/performance slide"""
        prompt = f"""Performance metrics visualization for: {title}

Visual elements:
- Bar charts or column charts showing performance comparisons
- Upward trending graphs (indicating improvement)
- Key metric cards with large numbers
- Speed/performance indicators

Style: Data visualization, dashboard-like, warm educational
Colors: Forest green (#2D5F3F) and sage green (#6B9080) for positive metrics, terracotta (#C97D60) accents
Background: Soft cream/beige (#FDF8F3)
Layout: Clean, organized, easy to read
Typography: Large numbers in forest green, clear labels

Context: Data engineering performance metrics
{f'Technologies: {", ".join(terms)}' if terms else ''}
Metrics might include: Speed, cost, scalability, efficiency

Mood: Professional, data-driven, warm, trustworthy, impressive results
Format: 16:9 aspect ratio, business presentation style with warm aesthetic"""

        return prompt

    def _generate_technical_prompt(self, title: str, content: str, terms: List[str]) -> str:
        """Generate prompt for technical/code slide"""
        prompt = f"""Technical concept visualization for: {title}

Style: Developer/technical focused, warm educational
Visual elements:
- Code editor or terminal aesthetic (subtle, not dominant) with cream background
- Technical diagrams or flowcharts
- Command-line or API visual metaphors
- Developer workspace aesthetic

Colors: Soft cream/beige (#FDF8F3) background with forest green (#2D5F3F) syntax highlighting
Mood: Technical, precise, developer-friendly, warm, approachable
Layout: Clean, organized, code-like structure

Context: {', '.join(terms) if terms else 'data engineering technical concept'}

NOT a screenshot - a professional illustration with technical aesthetic
Format: 16:9 aspect ratio, technical documentation style with warm colors"""

        return prompt

    def _generate_table_prompt(self, title: str, content: str, terms: List[str]) -> str:
        """Generate prompt for table/comparison table slide"""
        prompt = f"""Comparison table visualization for: {title}

Style: Professional data table or matrix, warm educational
Layout: Grid-based comparison chart
Visual elements:
- Clean rows and columns
- Header row with clear labels in forest green (#2D5F3F)
- Alternating row colors for readability (cream #FDF8F3 and light green #E8F3ED)
- Icons or symbols for checkmarks/features in sage green (#6B9080)

Colors: Forest green (#2D5F3F) headers, sage green (#6B9080) accents
Background: Soft cream/beige (#FDF8F3) for table readability
Typography: Clean, readable fonts
Design: Modern, minimalist, warm educational style

Context: {', '.join(terms) if terms else 'data platform comparison'}

Format: 16:9 aspect ratio, professional warm presentation style
Clarity: Easy to scan and compare information"""

        return prompt

    def _generate_simple_prompt(self, title: str, content: str, terms: List[str]) -> str:
        """Generate prompt for simple concept slide"""
        prompt = f"""Concept visualization for: {title}

Style: Clean, minimal, professional, warm educational
Visual: Abstract or conceptual representation of the main idea
Elements:
- Simple geometric shapes or flowing lines
- Data/technology aesthetic
- Minimalist design

Colors: Forest green (#2D5F3F) and sage green (#6B9080) primary, terracotta (#C97D60) accents
Background: Soft cream/beige (#FDF8F3)
Mood: Professional, modern, warm, inviting, clear
Layout: Centered, balanced, not cluttered

Context: {', '.join(terms) if terms else 'data engineering concept'}

Format: 16:9 aspect ratio, warm educational presentation style
Simple, elegant, supports the message without overwhelming"""

        return prompt

    def generate_prompt(self, title: str, content: str, slide_number: int) -> Tuple[str, SlideType]:
        """Generate image prompt for a slide"""
        # Detect slide type
        slide_type = self.detect_slide_type(title, content, slide_number)

        # Extract key terms
        terms = self.extract_key_terms(f"{title} {content}")

        # Generate prompt using appropriate template
        generator_func = self.templates.get(slide_type, self._generate_simple_prompt)
        prompt = generator_func(title, content, terms)

        return prompt, slide_type


def main():
    """Test prompt generator"""
    generator = PromptGenerator()

    # Test cases
    test_slides = [
        ("Introduction to Data Engineering", "Welcome to our presentation on modern data platforms", 1),
        ("Snowflake vs Databricks", "Comparing data warehouse and lakehouse architectures", 2),
        ("Modern Data Pipeline Architecture", "ETL pipeline with ingestion, storage, and processing layers", 3),
        ("Key Features", "Scalability, performance, security, cost optimization", 4),
    ]

    for title, content, slide_num in test_slides:
        prompt, slide_type = generator.generate_prompt(title, content, slide_num)
        print(f"\n{'='*70}")
        print(f"Slide {slide_num}: {title}")
        print(f"Type: {slide_type.value}")
        print(f"{'='*70}")
        print(prompt)


if __name__ == "__main__":
    main()
