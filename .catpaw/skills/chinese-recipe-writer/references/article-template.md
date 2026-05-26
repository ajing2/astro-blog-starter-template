# Article Template

This is the standard structure for a Wok & Story recipe article. Every article follows this format.

## Frontmatter

```yaml
---
title: "[Dish Name] Recipe - [Benefit/Hook] ([Unique Selling Point])"
description: "[130-155 chars, primary keyword near start, compelling action phrase]"
pubDate: "[Mon DD YYYY format, e.g. Jun 20 2025]"
heroImage: "/images/recipes/[dish-slug]/[dish-slug]-hero.jpg"
lang: "en"
translations:
  zh: "[dish-slug]-zh"
  de: "[dish-slug]-de"
  ja: "[dish-slug]-ja"
  fr: "[dish-slug]-fr"
---
```

## Body Structure

### 1. Opening Hook (no heading)

2-3 sentences using sensory language. Evoke the cooking experience — sounds, smells, textures. End with a bridge to the cultural story.

Example:
> The sizzle of chicken hitting hot oil, the sweet-spicy aroma of caramelized sauce coating each golden piece — General Tso's Chicken is the dish that made Chinese food famous across America, yet its true origins tell an even more fascinating story.

### 2. History/Cultural Section

Heading: `## The [Adjective] History Behind [Dish Name]`

- 2-3 paragraphs telling the dish's origin story
- Include Chinese characters (汉字) and pinyin for the dish name
- Reference specific people, places, and dates
- Connect history to why the recipe matters today

### 3. Quick Info Box

```markdown
## Quick Info

- **Prep Time:** X minutes
- **Cook Time:** X minutes
- **Total Time:** X minutes
- **Servings:** X people
- **Difficulty:** Easy / Easy-Medium / Medium / Medium-Hard / Hard
- **Spice Level:** None / Mild / Mild-Medium / Medium / Hot / Very Hot
```

### 4. Ingredients Image

```markdown
![All the ingredients for [Dish] arranged in small bowls on a dark slate surface](/images/recipes/[slug]/[slug]-ingredients.jpg)
```

### 5. Ingredients Section

Group into subsections:
```markdown
## Ingredients

### For the [Main Protein/Component]
- [quantity] [ingredient] ([Chinese name], [pinyin]) — [substitute if any]

### For the Sauce
- [quantity] [ingredient] ([Chinese name], [pinyin])

### Aromatics
- [quantity] [ingredient]
```

### 6. Instructions

Each major step gets:
- An H3 heading: `### Step N: [Action Verb + Object]`
- A step image (not every sub-step, only key moments)
- 1-2 paragraphs of instruction with technique explanation
- Chinese cooking terms where relevant

```markdown
## Instructions

### Step 1: [Verb] the [Subject]

![Alt text describing the action](/images/recipes/[slug]/step1-[action].jpg)

[Instructions paragraph with technique explanation...]

### Step 2: [Verb] the [Subject]

![Alt text](/images/recipes/[slug]/step2-[action].jpg)

[Instructions...]
```

**Step image naming:** `step[N]-[brief-action].jpg` (e.g., `step1-cutting-chicken.jpg`)

### 7. Pro Tips

```markdown
## Pro Tips for Perfect [Dish Name]

**[Tip title]:** [1-2 sentence explanation with Chinese technique terms where applicable]
```

Include 4-6 tips covering: technique, ingredient selection, temperature control, common mistakes, variations.

### 8. Serving Suggestions

```markdown
## Serving Suggestions

[2 paragraphs: primary pairing, alternative serving option]
```

### 9. Storage & Reheating

```markdown
## Storage & Reheating

[1 paragraph covering: storage duration, container type, reheating method, what to avoid]
```

### 10. FAQ Section

```markdown
## Frequently Asked Questions

### [Question targeting "People Also Ask"]?

[2-4 sentence answer, authoritative and specific]
```

Include 5-6 questions covering: authenticity, substitutions, technique troubleshooting, variations, dietary modifications.

### 11. JSON-LD Structured Data

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Recipe",
  "name": "[Dish Name]",
  "description": "[1-2 sentence description]",
  "prepTime": "PT[X]M",
  "cookTime": "PT[X]M",
  "totalTime": "PT[X]M",
  "recipeYield": "[N] servings",
  "recipeCategory": "Main Course",
  "recipeCuisine": "Chinese, [Regional style]",
  "keywords": "[keyword1], [keyword2], [keyword3]",
  "recipeIngredient": [
    "[quantity] [ingredient]"
  ],
  "recipeInstructions": [
    {"@type": "HowToStep", "text": "[Step description]"}
  ],
  "nutrition": {
    "@type": "NutritionInformation",
    "calories": "[X] calories",
    "fatContent": "[X]g",
    "proteinContent": "[X]g",
    "carbohydrateContent": "[X]g"
  }
}
</script>
```

## Image Requirements

| Type | Filename Pattern | Photography Style |
|------|-----------------|-------------------|
| Hero | `[slug]-hero.jpg` | Overhead or 45°, dark moody background, final dish |
| Ingredients | `[slug]-ingredients.jpg` | Overhead, dark slate, ingredients in small bowls |
| Step N | `stepN-[action].jpg` | Action shot, hands or wok visible, steam/motion |
| Serving | `serving-complete.jpg` | Styled plating with accompaniments |

## Translation File Naming

- English: `[slug].md`
- Chinese: `[slug]-zh.md`
- German: `[slug]-de.md`
- Japanese: `[slug]-ja.md`
- French: `[slug]-fr.md`

Each translation has the same frontmatter structure but with appropriate `lang` value and all `translations` cross-referencing each other.
