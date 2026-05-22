---
name: recipe-image-generator
description: "AI-powered recipe image generator with copyright-safe workflow. Generates original food photography from reference images using text-to-image AI, with built-in SEO optimization and Google compliance. Use when: creating recipe images, generating food photos, making dish pictures for blog, producing copyright-free food imagery, AI food photography. Triggers: generate recipe image, create food photo, make dish picture, AI food image, recipe photography, generate cooking image, food blog image, copyright-free recipe photo, 生成菜谱图, 生成菜品图, AI生成食物图片, 菜谱配图, 做菜图片, 食物摄影, 不侵权图片生成, 参考图片生成新图."
version: "1.0.0"
---

# Recipe Image Generator (Copyright-Safe)

Generate original, copyright-safe food photography for Chinese recipe articles using AI image generation. This skill provides a complete workflow from reference image analysis to final SEO-optimized output, ensuring zero infringement risk while maintaining professional quality.

## Why This Skill Exists

Food photography is heavily copyrighted. Using or even heavily modifying someone else's food photo can lead to DMCA takedowns, Google penalties, and legal issues. This workflow ensures every image on the site is a 100% AI-original creation inspired by the concept of a dish, not by the pixels of someone else's photo.

## Core Principle

Never feed a reference image directly into an AI tool as img2img input. Instead, extract the **concept** (dish appearance, plating style, color palette, lighting mood) as text, then generate entirely new images from that text description. This creates a complete legal firewall between the reference and the output.

## Workflow

### Step 1: Analyze the Reference Image

Look at the reference photo and extract these attributes as text:

- **Subject**: What dish is shown, its key visual characteristics (color, texture, shape)
- **Plating**: How the food is arranged (centered, scattered, stacked, layered)
- **Vessel**: What container holds the food (white ceramic bowl, cast iron pan, bamboo steamer, etc.)
- **Garnish**: Decorative elements (scallion curls, sesame seeds, chili oil drizzle, cilantro leaves)
- **Background**: Table surface and surroundings (dark wood, marble, rustic tablecloth, chopsticks beside)
- **Lighting**: Direction and quality (side lighting, overhead, warm/cool, dramatic shadows vs. bright and airy)
- **Style**: Overall photography style (moody dark, bright and clean, rustic, minimalist, overhead flat-lay)

Write these as a structured description. This text description is your creative brief — the reference image is no longer needed.

### Step 2: Craft the AI Prompt

Combine the extracted attributes into a generation prompt. Follow this template:

```
A [style] food photograph of [subject description], [plating details], 
in a [vessel description], garnished with [garnish details], 
on a [background description], [lighting description], 
professional food photography, 8k resolution, shallow depth of field
```

**Example:**
```
A moody food photograph of braised pork belly cubes with glossy dark 
caramel-soy glaze, arranged in a neat pile, in a white ceramic bowl 
with blue rim, garnished with fresh scallion rings and a star anise, 
on a dark walnut table with chopsticks beside, warm side lighting 
with soft shadows, professional food photography, 8k resolution, 
shallow depth of field
```

**Prompt Enhancement Tips:**
- Add `--ar 4:3` or `--ar 16:9` for web-optimized aspect ratios
- Include "food photography" and "editorial" to bias toward realistic output
- Specify "no text, no watermark, no logo" to avoid unwanted overlays
- For Chinese dishes specifically, mention authentic elements: "Chinese ceramic", "lacquerware chopsticks", "bamboo mat"

### Step 3: Generate Multiple Candidates

Generate 3-5 images per dish using your chosen AI tool. Each batch should vary in:
- Angle (overhead flat-lay, 45-degree, eye-level)
- Lighting mood (bright/airy vs. moody/dramatic)
- Background styling

Recommended tools (in order of food photo quality):
1. **Midjourney** v6+ with `--style raw` — most photorealistic food results
2. **DALL·E 3** via ChatGPT — good Chinese food understanding, supports Chinese prompts
3. **Stable Diffusion** with food photography LoRA — fully local, no usage restrictions
4. **Adobe Firefly** — commercially safe training data, weaker on Asian food

### Step 4: Select and Validate

Choose the best image, then verify copyright safety:

1. **Google Reverse Image Search**: Upload generated image to images.google.com, confirm no visually similar results link to copyrighted sources
2. **TinEye Search**: Secondary check at tineye.com for pixel-match detection
3. **Visual Similarity Check**: Ensure the output doesn't closely resemble any single source photo in composition + color + plating simultaneously

If any check raises concern, regenerate with modified prompt (change vessel, angle, or background).

### Step 5: Post-Processing

Optimize the selected image for web publication:

1. **Upscale** to at least 1200px width (Google recommended minimum for recipe rich results)
2. **Color correction**: Boost warmth slightly (+5-10 warm), increase saturation on food (+10-15) while keeping background muted
3. **Crop** to target aspect ratio:
   - Hero image: 16:9 (1200×675)
   - Recipe card: 4:3 (1200×900)
   - Square (social): 1:1 (1200×1200)
4. **Export formats**:
   - WebP (primary, <100KB for hero, <80KB for inline)
   - JPEG fallback (quality 82)
   - AVIF if site supports it (best compression)
5. **Strip EXIF metadata**: Remove all metadata with `exiftool -all= image.webp`

### Step 6: SEO Optimization for Google

Prepare image metadata for each language version:

| Element | Format | Example |
|---------|--------|---------|
| Filename | `[dish-name]-[descriptor].webp` | `mapo-tofu-spicy-sichuan.webp` |
| Alt text (EN) | Descriptive, include dish name | `Mapo tofu with ground pork in a white bowl, garnished with Sichuan peppercorns` |
| Alt text (ZH) | 描述性文字 | `白瓷碗中的麻婆豆腐，撒有花椒和葱花` |
| Title attr | Short, keyword-rich | `Authentic Mapo Tofu Recipe Photo` |
| Caption | Optional, adds context | `Homemade mapo tofu with the perfect balance of 麻 and 辣` |

**Structured Data (JSON-LD):**
```json
{
  "@type": "ImageObject",
  "url": "https://yoursite.com/images/mapo-tofu-spicy-sichuan.webp",
  "width": 1200,
  "height": 900,
  "caption": "Authentic Sichuan mapo tofu"
}
```

### Step 7: Upload and Index

1. Place images in `/public/images/recipes/[dish-slug]/` directory
2. Generate responsive srcset variants (400w, 800w, 1200w)
3. Add to sitemap via image sitemap extension:
```xml
<url>
  <loc>https://yoursite.com/en/mapo-tofu/</loc>
  <image:image>
    <image:loc>https://yoursite.com/images/recipes/mapo-tofu/hero.webp</image:loc>
    <image:title>Mapo Tofu Recipe</image:title>
    <image:caption>Authentic Sichuan mapo tofu with ground pork</image:caption>
  </image:image>
</url>
```
4. Submit updated sitemap to Google Search Console

## Copyright Safety Checklist

Before publishing any AI-generated recipe image, verify ALL of the following:

- [ ] Image was generated from TEXT PROMPT ONLY (no img2img from copyrighted source)
- [ ] Prompt was derived from conceptual description, not pixel-level copying
- [ ] Google reverse image search shows no matching copyrighted images
- [ ] TinEye returns zero matches
- [ ] No distinctive copyrighted plating design was replicated (unique restaurant creations)
- [ ] EXIF metadata is completely stripped
- [ ] Image does not contain any text, logos, or watermarks
- [ ] No recognizable brand-name tableware or products visible

## Batch Production Template

For efficient production of multiple recipe images:

```
Dish: [Name]
Reference concept: [2-3 sentence description of what this dish looks like]
Hero prompt: [Full generation prompt for main image]
Card prompt: [Variant prompt for recipe card - overhead angle]
Social prompt: [Variant for social media - close-up, square]
Output files:
  - /public/images/recipes/[slug]/hero.webp (1200×675)
  - /public/images/recipes/[slug]/card.webp (1200×900)
  - /public/images/recipes/[slug]/social.webp (1200×1200)
```

## Common Chinese Dish Visual Vocabulary

Use these terms in prompts for authentic-looking results:

| Chinese Term | Description for AI Prompt |
|---|---|
| 红烧 | Dark mahogany-brown sauce, glossy caramelized glaze |
| 清蒸 | Pale/natural colors, delicate, clear sauce, ginger-scallion garnish |
| 爆炒 | Slightly charred edges, vibrant vegetable colors, wok hei visible steam |
| 凉拌 | Bright colors, shredded/julienned, sesame oil sheen, chili flakes |
| 炖汤 | Clear or milky broth, in clay pot or deep bowl, steam rising |
| 火锅 | Bubbling red oil, floating spices, thinly sliced ingredients around pot |
| 点心 | Small delicate portions, bamboo steamer, translucent wrappers |

## Integration with Recipe Writer Skill

This skill pairs with `chinese-recipe-writer`. After generating article content:

1. Use the dish name and description from the recipe to generate the hero image
2. Generate a step-by-step cooking process image if needed (wok with ingredients)
3. Generate a serving suggestion image (dish on table with sides)
4. Insert image references into the article markdown with proper alt tags in all 5 languages
