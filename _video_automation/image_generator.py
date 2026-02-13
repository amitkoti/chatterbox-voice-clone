"""
Image Generator using Google Gemini (Imagen) API
Generates images with multi-account failover and smart caching
"""

import os
import time
from pathlib import Path
from typing import Optional, Tuple
import base64


class ImageGenerator:
    """Generates images using Google Gemini API"""

    def __init__(self, api_manager, output_dir: str):
        self.api_manager = api_manager
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Try to import Google AI
        try:
            import google.generativeai as genai
            self.genai = genai
            self.api_available = True
        except ImportError:
            print("⚠️  google-generativeai not installed")
            print("   Install with: pip install google-generativeai")
            self.api_available = False

    def check_existing_image(self, slide_number: int) -> Optional[Path]:
        """Check if image already exists (manual or previously generated)"""
        # Check for various formats
        formats = ['png', 'jpg', 'jpeg']
        for fmt in formats:
            image_path = self.output_dir / f"slide_{slide_number:02d}.{fmt}"
            if image_path.exists():
                return image_path

        return None

    def generate_image(
        self,
        prompt: str,
        slide_number: int,
        slide_title: str,
        retry_count: int = 3
    ) -> Tuple[bool, Optional[Path], str]:
        """
        Generate image using Gemini API

        Returns: (success, image_path, message)
        """
        # Check if image already exists
        existing = self.check_existing_image(slide_number)
        if existing:
            return True, existing, f"Using existing image: {existing.name}"

        # Check if API is available
        if not self.api_available:
            return False, None, "Google AI library not installed"

        # Check if we have API capacity
        if not self.api_manager.has_capacity():
            return False, None, "All API accounts exhausted"

        # Get API key
        api_key = self.api_manager.get_api_key()
        if not api_key:
            return False, None, "No API key available"

        # Try to generate with retries
        for attempt in range(retry_count):
            try:
                # Configure API
                self.genai.configure(api_key=api_key)

                # Try new Gemini 2.0 approach with image generation
                try:
                    model = self.genai.GenerativeModel('gemini-2.0-flash-exp')

                    # Generate content with image output
                    response = model.generate_content(
                        f"Generate a professional 16:9 image for a presentation slide. {prompt}",
                        generation_config=self.genai.GenerationConfig(
                            response_mime_type="image/png",
                            temperature=0.4
                        )
                    )

                    # The response should contain image data
                    if hasattr(response, '_result') and response._result:
                        # Extract image data and save
                        import base64
                        from PIL import Image
                        import io

                        # Try to get image from response
                        # This is experimental and may not work with all API keys
                        output_path = self.output_dir / f"slide_{slide_number:02d}.png"

                        # For now, create placeholder as this API is experimental
                        raise Exception("Gemini image generation not fully supported with AI Studio keys")

                except Exception as gemini_error:
                    # Gemini approach failed, provide helpful message
                    return False, None, f"Image generation requires Vertex AI setup. Use manual prompts or alternative APIs. Details: {str(gemini_error)[:100]}"

            except Exception as e:
                error_msg = str(e).lower()

                # Check if quota exceeded
                if 'quota' in error_msg or '429' in error_msg or 'resource_exhausted' in error_msg:
                    self.api_manager.mark_request_failed(str(e), quota_exceeded=True)

                    # Try next account
                    api_key = self.api_manager.get_api_key()
                    if api_key:
                        continue  # Retry with new account
                    else:
                        return False, None, "All API accounts exhausted"

                # Other errors
                elif attempt < retry_count - 1:
                    print(f"   Attempt {attempt + 1} failed, retrying...")
                    time.sleep(2)  # Brief pause before retry
                    continue
                else:
                    return False, None, f"API error: {str(e)}"

        return False, None, "Max retries exceeded"

    def generate_placeholder(
        self,
        slide_number: int,
        slide_title: str,
        slide_type: str
    ) -> Path:
        """Generate placeholder image when API fails"""
        try:
            from PIL import Image, ImageDraw, ImageFont

            # Create image
            width, height = 1920, 1080
            img = Image.new('RGB', (width, height), color=(26, 35, 46))  # Dark background
            draw = ImageDraw.Draw(img)

            # Add text
            try:
                font_large = ImageFont.truetype("arial.ttf", 60)
                font_small = ImageFont.truetype("arial.ttf", 30)
            except:
                font_large = ImageFont.load_default()
                font_small = ImageFont.load_default()

            # Title
            title_text = slide_title[:50]
            draw.text((100, 400), title_text, fill=(255, 255, 255), font=font_large)

            # Placeholder text
            placeholder_text = f"[{slide_type.upper()} IMAGE]"
            draw.text((100, 500), placeholder_text, fill=(41, 179, 209), font=font_small)

            info_text = "Generate manually or run with API"
            draw.text((100, 600), info_text, fill=(150, 150, 150), font=font_small)

            # Save
            output_path = self.output_dir / f"slide_{slide_number:02d}.png"
            img.save(output_path)

            return output_path

        except Exception as e:
            print(f"   Could not create placeholder: {e}")
            return None

    def get_generation_stats(self) -> dict:
        """Get statistics about generated images"""
        existing_images = list(self.output_dir.glob("slide_*.png"))
        existing_images += list(self.output_dir.glob("slide_*.jpg"))

        return {
            'total_images': len(existing_images),
            'output_dir': str(self.output_dir)
        }


def main():
    """Test image generator"""
    from api_manager import MultiAccountAPIManager
    from config_manager import APIConfig

    # Load config
    config = APIConfig()
    if not config.validate():
        print("Please configure API keys first")
        return

    # Create API manager
    accounts = config.get_google_accounts()
    api_manager = MultiAccountAPIManager(accounts)

    # Create image generator
    output_dir = "_projects/test/images"
    generator = ImageGenerator(api_manager, output_dir)

    print(api_manager.get_status_summary())
    print()

    # Test generation
    prompt = """Professional title image for data engineering presentation.
Modern, corporate, technology-focused with blue/teal gradient theme."""

    print("Testing image generation...")
    success, image_path, message = generator.generate_image(
        prompt=prompt,
        slide_number=1,
        slide_title="Test Slide"
    )

    print(f"Success: {success}")
    print(f"Message: {message}")
    if image_path:
        print(f"Image: {image_path}")

    print("\n" + api_manager.get_status_summary())


if __name__ == "__main__":
    main()
