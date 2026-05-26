---
name: chinese-recipe-writer
description: "Automated Chinese food recipe article creation for the Wok & Story Astro blog. Takes a reference article URL or recipe topic, writes SEO-optimized content with cultural storytelling, generates food photography images, translates to 5 languages (EN/ZH/DE/JA/FR), performs Google search deduplication, and publishes to the Astro blog project. Use when the user says: 写菜谱文章、create recipe、write recipe post、新建食谱、generate recipe article、菜谱创作、recipe blog post、中餐食谱、Chinese recipe、写一篇菜谱、帮我写个食谱、create a recipe article、publish recipe、发布菜谱."
---

# Chinese Recipe Writer

Automates the full workflow of creating Chinese food recipe articles for the **Wok & Story** Astro blog at `/Users/lingjing/ai/claude_code/chinese-food`.

## Workflow Overview

1. **Research** — Fetch reference article or research the dish
2. **Write English article** — Create SEO-optimized recipe content with cultural storytelling
3. **Generate images** — Create food photography for hero, ingredients, and cooking steps
4. **Translate** — Produce ZH/DE/JA/FR versions with proper localization
5. **SEO optimization** — Add JSON-LD structured data, meta descriptions, keywords
6. **Google deduplication** — Search for existing similar content and ensure uniqueness
7. **Publish** — Add files to the project, build, and push to Git

## Project Architecture

- **Content schema** (`src/content.config.ts`): Each post has `lang` (enum: en/zh/de/ja/fr), `translations` (record mapping lang to slug)
- **Blog index** (`src/pages/blog/index.astro`): Only shows posts with `lang: "en"`
- **Language switcher**: `src/components/LanguageSwitcher.astro` shows flag buttons on each post
- **Images**: `public/images/recipes/[dish-slug]/` — hero, ingredients, step images, serving
- **Build/Deploy**: `npm run build` / `npm run deploy` (Cloudflare Workers)
- **Git remote**: `github.com:ajing2/astro-blog-starter-template.git`

## Step-by-Step Instructions

### Step 1: Research the Dish

If a reference URL is provided:
- Use `web_fetch` to retrieve the article content
- Extract key information: ingredients, steps, history, tips

If only a dish name is given:
- Research the dish's history, regional variations, authentic preparation methods
- Identify what makes this recipe unique and SEO-worthy

### Step 2: Google Search Deduplication

Before writing, search Google to ensure uniqueness:

```
web_search("[dish name] recipe authentic Chinese")
web_search("[dish name] recipe site:wokandstory.com")  # check own site
```

Analyze top results:
- Identify angles NOT covered by existing articles
- Find unique cultural stories or techniques to differentiate
- Choose a title that doesn't duplicate existing high-ranking content
- If the exact same recipe exists on the blog already, inform the user and stop

### Step 3: Write the English Article

Follow the template structure in `references/article-template.md`. Key requirements:

**Frontmatter:**
```yaml
---
title: "[Dish Name] Recipe - [Hook/Benefit] ([Unique Selling Point])"
description: "[130-155 char meta description with primary keyword near start]"
pubDate: "[current date]"
heroImage: "/images/recipes/[dish-slug]/[dish-slug]-hero.jpg"
lang: "en"
translations:
  zh: "[dish-slug]-zh"
  de: "[dish-slug]-de"
  ja: "[dish-slug]-ja"
  fr: "[dish-slug]-fr"
---
```

**Article structure:**
1. Opening hook (sensory/emotional, 2-3 sentences)
2. History/cultural story section (2-3 paragraphs, with Chinese characters and pinyin)
3. Quick Info box (prep time, cook time, servings, difficulty, spice level)
4. Ingredients (grouped: main protein, sauce, aromatics)
5. Step-by-step instructions (each step has an image, technique tips with Chinese terms)
6. Pro Tips section (5+ expert tips)
7. Serving Suggestions
8. Storage & Reheating
9. FAQ section (5-6 questions, targeting People Also Ask)
10. JSON-LD Recipe structured data (`<script type="application/ld+json">`)

**Writing style:**
- Conversational, knowledgeable, like a Chinese cooking teacher
- Include Chinese characters (汉字) and pinyin for key ingredients/techniques
- Use sensory language for cooking descriptions
- Include "Critical tip" callouts for common mistakes

### Step 4: Generate Images

Create images for the recipe using the `GenerateImage` tool. Required images:

| Image | Filename | Description |
|-------|----------|-------------|
| Hero | `[slug]-hero.jpg` | Final dish, styled food photography, dark/moody background |
| Ingredients | `[slug]-ingredients.jpg` | All ingredients in small bowls on dark slate |
| Step images | `step[N]-[action].jpg` | Key cooking moments (4-6 steps) |
| Serving | `serving-complete.jpg` | Final plated dish with sides |

**Image generation prompt template:**
```
Professional food photography of [description], shot from [angle], 
[lighting style] lighting, on [surface/background], styled with 
[props], shallow depth of field, [mood] atmosphere, high resolution
```

Since GenerateImage only displays in chat (does NOT save to filesystem), after generating use the Python Pillow fallback script at `scripts/generate-placeholder-images.py` to create actual image files in the project:

```bash
python3 scripts/generate-placeholder-images.py [dish-slug] [image-list]
```

**Important**: Inform the user that the GenerateImage outputs shown in chat are the intended visuals, and placeholder files are created for the build. User should replace with real photos or use an external image generation service for production.

### Step 5: Translate to Other Languages

Create 4 additional versions (ZH, DE, JA, FR). File naming convention:
- `[dish-slug].md` — English (primary)
- `[dish-slug]-zh.md` — Chinese
- `[dish-slug]-de.md` — German
- `[dish-slug]-ja.md` — Japanese
- `[dish-slug]-fr.md` — French

**Translation rules:**
- Each file has `lang: "[code]"` and `translations:` pointing to all other versions
- Localize measurements (metric for DE/JA/FR, keep both for ZH)
- Translate cultural context appropriately (don't over-explain Chinese culture in ZH version)
- Adapt SEO title/description for each language's search patterns
- Keep the same image paths across all versions
- JSON-LD `inLanguage` field should match the article language

**ZH-specific:** Use natural Chinese food writing style, not word-for-word translation. Chinese readers know ingredients like 料酒 without explanation.

**JA-specific:** Use proper Japanese culinary terms where they exist (e.g., 紹興酒, 片栗粉)

**DE-specific:** Use formal recipe writing style common in German food blogs

**FR-specific:** Use French culinary terminology where applicable

### Step 6: SEO Optimization Checklist

Verify before publishing:
- [ ] Title under 60 characters, primary keyword near front
- [ ] Meta description 130-155 characters with keyword
- [ ] H2/H3 headings include relevant keywords naturally
- [ ] Image alt texts are descriptive and include keywords
- [ ] Internal links to related recipes (if any exist)
- [ ] JSON-LD Recipe schema is complete and valid
- [ ] FAQ section targets "People Also Ask" queries
- [ ] URL slug is clean and keyword-rich

### Step 7: Publish

```bash
cd /Users/lingjing/ai/claude_code/chinese-food

# Add all new files
git add src/content/blog/[dish-slug]*.md
git add public/images/recipes/[dish-slug]/

# Build to verify no errors
npm run build

# Commit and push
git commit -m "feat: add [Dish Name] recipe (5 languages)"
git push

# Optional: deploy to Cloudflare
npm run deploy
```

## File Locations

All files go in the Astro project at `/Users/lingjing/ai/claude_code/chinese-food`:
- Articles: `src/content/blog/`
- Images: `public/images/recipes/[dish-slug]/`

## Quick Reference

**Supported languages:** en, zh, de, ja, fr
**Image directory pattern:** `public/images/recipes/[dish-slug]/`
**Slug format:** lowercase-hyphenated (e.g., `mapo-tofu`, `kung-pao-chicken`)
**Build command:** `npm run build`
**Deploy command:** `npm run deploy`
