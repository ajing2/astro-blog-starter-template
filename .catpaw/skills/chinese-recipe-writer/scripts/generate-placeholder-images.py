#!/usr/bin/env python3
"""
Generate placeholder recipe images for the Wok & Story blog.
Creates colored gradient images with text labels as placeholders
until real food photography is available.

Usage:
    python3 generate-placeholder-images.py <dish-slug> [--steps N]

Example:
    python3 generate-placeholder-images.py mapo-tofu --steps 5
    python3 generate-placeholder-images.py kung-pao-chicken --steps 6

This creates the directory structure:
    public/images/recipes/<dish-slug>/
        <dish-slug>-hero.jpg
        <dish-slug>-ingredients.jpg
        step1-prep.jpg
        step2-cook.jpg
        ...
        serving-complete.jpg
"""

import argparse
import os
import sys

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("Error: Pillow is required. Install with: pip3 install Pillow")
    sys.exit(1)


# Warm food-photography color palettes
COLORS = {
    "hero": [(139, 69, 19), (205, 133, 63)],        # Dark brown -> tan
    "ingredients": [(47, 79, 79), (85, 107, 47)],    # Dark slate -> olive
    "step": [(128, 0, 0), (205, 92, 92)],            # Maroon -> indian red
    "serving": [(85, 26, 26), (210, 105, 30)],       # Dark red -> chocolate
}


def create_gradient_image(width, height, color1, color2):
    """Create a vertical gradient image."""
    img = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(img)
    for y in range(height):
        r = int(color1[0] + (color2[0] - color1[0]) * y / height)
        g = int(color1[1] + (color2[1] - color1[1]) * y / height)
        b = int(color1[2] + (color2[2] - color1[2]) * y / height)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    return img


def add_label(img, text):
    """Add centered text label to image."""
    draw = ImageDraw.Draw(img)
    # Try to use a decent font, fall back to default
    font = None
    font_size = 36
    font_paths = [
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/SFNSMono.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for fp in font_paths:
        if os.path.exists(fp):
            try:
                font = ImageFont.truetype(fp, font_size)
                break
            except Exception:
                continue
    if font is None:
        font = ImageFont.load_default()

    # Get text bounding box
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    x = (img.width - text_width) // 2
    y = (img.height - text_height) // 2

    # Draw shadow then text
    draw.text((x + 2, y + 2), text, fill=(0, 0, 0), font=font)
    draw.text((x, y), text, fill=(255, 255, 255), font=font)
    return img


def generate_images(dish_slug, num_steps=6, project_root=None):
    """Generate all placeholder images for a recipe."""
    if project_root is None:
        project_root = "/Users/lingjing/ai/claude_code/chinese-food"

    output_dir = os.path.join(project_root, "public", "images", "recipes", dish_slug)
    os.makedirs(output_dir, exist_ok=True)

    width, height = 1200, 800
    generated = []

    # Hero image
    img = create_gradient_image(width, height, *COLORS["hero"])
    img = add_label(img, f"{dish_slug.replace('-', ' ').title()} - Hero")
    path = os.path.join(output_dir, f"{dish_slug}-hero.jpg")
    img.save(path, "JPEG", quality=85)
    generated.append(path)

    # Ingredients image
    img = create_gradient_image(width, height, *COLORS["ingredients"])
    img = add_label(img, f"{dish_slug.replace('-', ' ').title()} - Ingredients")
    path = os.path.join(output_dir, f"{dish_slug}-ingredients.jpg")
    img.save(path, "JPEG", quality=85)
    generated.append(path)

    # Step images
    step_names = [
        "prep", "marinate", "sauce", "fry", "stir-fry", "combine",
        "simmer", "garnish", "plate", "finish"
    ]
    for i in range(1, num_steps + 1):
        step_name = step_names[i - 1] if i <= len(step_names) else f"step{i}"
        img = create_gradient_image(width, height, *COLORS["step"])
        img = add_label(img, f"Step {i}: {step_name.replace('-', ' ').title()}")
        path = os.path.join(output_dir, f"step{i}-{step_name}.jpg")
        img.save(path, "JPEG", quality=85)
        generated.append(path)

    # Serving complete image
    img = create_gradient_image(width, height, *COLORS["serving"])
    img = add_label(img, f"{dish_slug.replace('-', ' ').title()} - Serving")
    path = os.path.join(output_dir, "serving-complete.jpg")
    img.save(path, "JPEG", quality=85)
    generated.append(path)

    return generated


def main():
    parser = argparse.ArgumentParser(
        description="Generate placeholder recipe images for Wok & Story blog"
    )
    parser.add_argument("dish_slug", help="Dish slug (e.g., mapo-tofu)")
    parser.add_argument(
        "--steps", type=int, default=6, help="Number of step images (default: 6)"
    )
    parser.add_argument(
        "--project-root",
        default="/Users/lingjing/ai/claude_code/chinese-food",
        help="Path to the Astro project root",
    )
    args = parser.parse_args()

    print(f"Generating placeholder images for: {args.dish_slug}")
    generated = generate_images(args.dish_slug, args.steps, args.project_root)

    print(f"\nCreated {len(generated)} images:")
    for path in generated:
        print(f"  ✓ {path}")
    print(f"\nDirectory: {os.path.dirname(generated[0])}")


if __name__ == "__main__":
    main()
