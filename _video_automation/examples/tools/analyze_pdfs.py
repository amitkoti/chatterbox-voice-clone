"""
Analyze PDF presentations to extract design patterns
"""

import PyPDF2
import sys
import json

def analyze_pdf(pdf_path):
    """Extract text and structure from PDF"""
    print(f"\n{'='*70}")
    print(f"Analyzing: {pdf_path}")
    print('='*70)

    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            num_pages = len(pdf_reader.pages)

            print(f"Total pages: {num_pages}")
            print()

            slides = []

            for page_num in range(min(num_pages, 20)):  # First 20 pages
                page = pdf_reader.pages[page_num]
                text = page.extract_text()

                # Split into lines
                lines = [line.strip() for line in text.split('\n') if line.strip()]

                if lines:
                    # First line is usually title
                    title = lines[0] if lines else ""
                    content = '\n'.join(lines[1:]) if len(lines) > 1 else ""

                    print(f"\n--- Slide {page_num + 1} ---")
                    print(f"Title: {title[:80]}")
                    print(f"Content length: {len(content)} chars")

                    # Detect patterns
                    patterns = []
                    content_lower = content.lower()

                    if any(word in content_lower for word in ['vs', 'versus', 'comparison']):
                        patterns.append('COMPARISON')
                    if any(word in content_lower for word in ['architecture', 'pipeline', 'flow']):
                        patterns.append('ARCHITECTURE')
                    if any(word in content_lower for word in ['feature', 'benefit', 'key']):
                        patterns.append('FEATURES')
                    if '•' in content or '-' in content[:100]:
                        patterns.append('BULLET_POINTS')
                    if any(word in content_lower for word in ['table', 'comparison', 'data']):
                        patterns.append('DATA_TABLE')

                    if patterns:
                        print(f"Patterns: {', '.join(patterns)}")

                    # Show first few lines of content
                    preview_lines = lines[1:4] if len(lines) > 1 else []
                    for line in preview_lines:
                        print(f"  • {line[:70]}")

                    slides.append({
                        'page': page_num + 1,
                        'title': title,
                        'content_length': len(content),
                        'patterns': patterns,
                        'lines': len(lines)
                    })

            return {
                'filename': pdf_path.split('\\')[-1],
                'total_pages': num_pages,
                'slides': slides
            }

    except Exception as e:
        print(f"ERROR: {e}")
        import traceback
        traceback.print_exc()
        return None

if __name__ == "__main__":
    pdfs = [
        r"C:\Users\user\Downloads\ETL_ELT_Strategy_Guide.pdf",
        r"C:\Users\user\Downloads\ETL_ELT_The_Strategic_Choice.pdf",
        r"C:\Users\user\Downloads\Snowflake_Virtual_Warehouse_Mastery (3).pdf",
        r"C:\Users\user\Downloads\Snowflake_Virtual_Warehouses_Architectural_Mental_Model.pdf"
    ]

    all_results = []

    for pdf_path in pdfs:
        result = analyze_pdf(pdf_path)
        if result:
            all_results.append(result)

    # Summary
    print("\n" + "="*70)
    print("SUMMARY")
    print("="*70)

    for result in all_results:
        print(f"\n{result['filename']}")
        print(f"  Pages: {result['total_pages']}")

        # Count patterns
        pattern_counts = {}
        for slide in result['slides']:
            for pattern in slide['patterns']:
                pattern_counts[pattern] = pattern_counts.get(pattern, 0) + 1

        if pattern_counts:
            print(f"  Patterns found:")
            for pattern, count in sorted(pattern_counts.items(), key=lambda x: x[1], reverse=True):
                print(f"    - {pattern}: {count} slides")
