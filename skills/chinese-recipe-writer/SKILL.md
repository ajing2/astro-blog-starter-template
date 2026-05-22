---
name: chinese-recipe-writer
description: "Multi-language Chinese food recipe article writer. Generates SEO-optimized recipe articles in 5 languages (EN/ZH/DE/JA/FR) with proper word counts, affiliate links, structured data, and cultural adaptation. Use when: writing a Chinese recipe blog post, creating multilingual food content, generating SEO recipe articles, writing Chinese food articles for international audiences. Triggers: write recipe, write article, new recipe post, create recipe content, Chinese food article, multilingual recipe, SEO recipe, generate recipe blog post, write mapo tofu article, create dumpling recipe, food blog content, recipe SEO."
---

# Chinese Recipe Article Writer

Generate SEO-optimized, multilingual Chinese food recipe articles targeting international audiences. Each article produces 5 language versions with proper cultural adaptation and monetization.

## Workflow Overview

Writing a recipe article involves these steps:

1. Select dish and research keywords (all 5 languages)
2. Draft Chinese master version (source material)
3. Generate English version (primary, most polished)
4. Translate to DE/JA/FR with localization
5. Add SEO metadata, structured data, and affiliate links
6. Deduplication and copyright check (per-section verification)
7. SEO ranking optimization pass
8. Final review per checklist

## Word Count Targets (SEO Sweet Spots)

| Language | Target Range | Unit |
|----------|-------------|------|
| EN | 1,500-2,500 | words |
| ZH | 2,000-4,000 | characters |
| DE | 1,200-2,000 | Woerter |
| JA | 3,000-5,000 | characters |
| FR | 1,200-2,000 | mots |

Below minimum = thin content risk. Above maximum = bounce rate increase.

## Article Structure (11 Parts)

Every article follows this structure:

1. **Hook** (~3%) - Sensory description or surprising fact, 1-2 sentences
2. **Story** (~13%) - Cultural background, history, or personal story. See [references/story-angles.md](references/story-angles.md)
3. **Quick Info** (~2%) - Prep time, cook time, servings, difficulty, spice level
4. **Ingredients** (~7%) - Grouped by purpose, with substitutes and affiliate links
5. **Instructions** (~27%) - One action per step, with sensory cues and "why" explanations
6. **Pro Tips** (~10%) - 3-5 advanced techniques
7. **Serving Suggestions** (~5%) - Pairings with internal links to other recipes
8. **Storage & Reheating** (~4%) - Practical 2-3 sentences
9. **FAQ** (~20%) - 4-6 real questions targeting "People Also Ask"
10. **Recipe Card** - JSON-LD structured data (not counted in word count)
11. **Affiliate CTA** (~5%) - 2-3 natural product recommendations

## Multilingual Production Flow

```
Step 1: Chinese master draft (source material, research)
Step 2: English version (primary site version, most effort)
Step 3: Translate EN → DE, JA, FR with cultural adaptation
Step 4: Localize each version (ingredients, measurements, shopping)
Step 5: SEO metadata per language (title, description, keywords)
```

### Key Localization Rules

- **EN**: US measurements (tbsp, cup, oz), Amazon US links, explain Chinese culture
- **ZH**: Metric (g, ml), casual tone, suitable for WeChat/Xiaohongshu redistribution
- **DE**: Metric, precise detailed steps, Amazon.de links, mention Asian-Laden stores
- **JA**: Metric (グラム, ml, 大さじ), Amazon.co.jp, highlight difference from Japanese-style versions
- **FR**: Metric (grammes, ml), Amazon.fr, compare techniques with French cooking where relevant

## SEO Requirements

For each language version, prepare:

- Title tag (EN/DE/FR: ≤60 chars, ZH: ≤30 chars, JA: ≤30 full-width chars)
- Meta description (EN/DE/FR: ≤160 chars, ZH/JA: ≤80 chars)
- URL slug (DE/FR use local language, JA keeps English)
- Target keyword + 2-3 secondary keywords
- hreflang tags linking all 5 versions
- JSON-LD Recipe structured data

For detailed SEO metadata format, see [references/seo-metadata.md](references/seo-metadata.md).

## URL Structure

```
/en/[slug]/     or /[slug]/  (English, default)
/zh/[slug]/                   (Chinese)
/de/[slug-in-german]/         (German, localized URL)
/ja/[slug]/                   (Japanese, English URL)
/fr/[slug-in-french]/         (French, localized URL)
```

## Affiliate Strategy

| Language | Platform | Links |
|----------|----------|-------|
| EN | Amazon US | affiliate-program.amazon.com |
| DE | Amazon.de | partnernet.amazon.de |
| JA | Amazon.co.jp | affiliate.amazon.co.jp |
| FR | Amazon.fr | partenaires.amazon.fr |
| ZH | JD/Taobao or AdSense only | — |

Place affiliate links in: ingredient descriptions (brand recommendations), cooking steps (tools), and end-of-article product section.

## Writing Guidelines

- Each step: one core action, specific temperature/time, sensory cues
- Include Chinese cooking terms with pinyin for authenticity (e.g., "炒出红油" chao chu hong you)
- FAQ is the word count adjuster: add questions if under target, trim Story if over
- Internal link to 2-3 other recipe articles per language version
- All images shared across languages, but alt tags localized

## Deduplication and Copyright Protection

Every article must pass deduplication checks before publishing. This prevents Google penalties for duplicate content and protects against DMCA takedown risks.

Key steps:
1. Never copy-paste from reference recipes — rewrite in your own words
2. Add unique value: personal experience, Chinese cooking terms, failure stories
3. Verify with plagiarism tools (Copyscape/Quetext): overall similarity < 15%
4. Use original or AI-generated images only — never save from other recipe sites
5. Mark affiliate links with disclosure statement

For the complete dedup workflow, tools, per-section similarity thresholds, and anti-DMCA guidelines, see [references/dedup-and-copyright.md](references/dedup-and-copyright.md).

## SEO Ranking Optimization

Beyond basic SEO metadata, apply ranking strategies to compete for Google page 1:

1. **Search Intent Coverage** — answer every question a user might have about the dish
2. **E-E-A-T Signals** — demonstrate Experience (first-person stories), Expertise (cooking science), Authority (internal linking), Trust (affiliate disclosure)
3. **Core Web Vitals** — LCP < 2.5s, INP < 200ms, CLS < 0.1 (Astro + Cloudflare CDN handles most)
4. **Internal Linking** — 3 types per article: same-ingredient, pairing suggestion, knowledge guide
5. **Content Freshness** — update published articles regularly, add "Last updated" date
6. **Avoid Penalties** — no keyword stuffing, no bulk low-quality AI content, stable publish cadence

For the full SEO ranking strategy (E-E-A-T details, technical SEO, link building, monitoring metrics, and penalty avoidance), see [references/seo-ranking.md](references/seo-ranking.md).

## Quality Checklist

For the full pre-publish checklist, see [references/checklist.md](references/checklist.md).

## Time Estimate

~4 hours per article (all 5 languages), breakdown:
- Research + keywords: 30min
- Chinese draft: 15min
- English version + polish: 55min
- DE/JA/FR translation + localization: 50min
- Images: 20min
- SEO optimization: 25min
- Final review: 20min
