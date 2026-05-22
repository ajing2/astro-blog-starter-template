# SEO Metadata Format

## Per-Language Metadata Template

### English (EN)
```
Title Tag:       [Dish Name] Recipe - [Core Benefit] (≤60 chars)
                 Example: Easy Mapo Tofu Recipe - Authentic Sichuan Style (20 Min)
Meta Description: ≤160 chars, include primary keyword
                 Example: Learn how to make authentic Mapo Tofu at home with this easy step-by-step recipe. Spicy, numbing, and ready in just 20 minutes!
URL Slug:        /mapo-tofu-recipe/
Target Keyword:  mapo tofu recipe
Secondary KW:    easy mapo tofu, sichuan tofu recipe, spicy tofu with ground pork
```

### Chinese (ZH)
```
Title Tag:       [菜名] 的做法 - [核心卖点]（≤30 中文字符）
                 Example: 正宗麻婆豆腐的做法 - 川菜经典，20分钟搞定
Meta Description: ≤80 中文字符
                 Example: 手把手教你做正宗川味麻婆豆腐，麻辣鲜香，配米饭绝了！详细步骤+食材替代方案。
URL Slug:        /zh/mapo-tofu-recipe/
Target Keyword:  麻婆豆腐的做法
Secondary KW:    麻婆豆腐怎么做, 正宗麻婆豆腐, 川菜食谱
```

### German (DE)
```
Title Tag:       [Dish Name DE] Rezept - [Core Benefit] (≤60 chars)
                 Example: Mapo Tofu Rezept - Authentisch aus Sichuan (20 Min)
Meta Description: ≤160 chars
                 Example: Lernen Sie, wie Sie authentischen Mapo Tofu zu Hause zubereiten. Scharf, würzig und in nur 20 Minuten fertig!
URL Slug:        /de/mapo-tofu-rezept/
Target Keyword:  Mapo Tofu Rezept
Secondary KW:    Sichuan Tofu Rezept, scharfer Tofu mit Hackfleisch, chinesisches Tofu Rezept
```

### Japanese (JA)
```
Title Tag:       [菜名JA] レシピ - [核心卖点]（≤30 全角字符）
                 Example: 本格麻婆豆腐のレシピ - 四川風の本場の味（20分で完成）
Meta Description: ≤80 全角字符
                 Example: 本場四川の麻婆豆腐を自宅で再現！花椒の痺れる辛さがたまらない、本格レシピをご紹介します。
URL Slug:        /ja/mapo-tofu-recipe/
Target Keyword:  麻婆豆腐 レシピ 本格
Secondary KW:    四川風麻婆豆腐, 本格中華レシピ, 麻婆豆腐 作り方
```

### French (FR)
```
Title Tag:       Recette de [Dish Name FR] - [Core Benefit] (≤60 chars)
                 Example: Recette du Mapo Tofu - Authentique Cuisine du Sichuan (20 Min)
Meta Description: ≤160 chars
                 Example: Découvrez comment préparer un authentique Mapo Tofu fait maison. Épicé, savoureux et prêt en seulement 20 minutes !
URL Slug:        /fr/recette-mapo-tofu/
Target Keyword:  recette mapo tofu
Secondary KW:    tofu sichuan recette, cuisine chinoise recette, tofu épicé porc haché
```

## hreflang Tags (Required on Every Page)

```html
<link rel="alternate" hreflang="en" href="https://yoursite.com/[en-slug]/" />
<link rel="alternate" hreflang="zh" href="https://yoursite.com/zh/[slug]/" />
<link rel="alternate" hreflang="de" href="https://yoursite.com/de/[de-slug]/" />
<link rel="alternate" hreflang="ja" href="https://yoursite.com/ja/[slug]/" />
<link rel="alternate" hreflang="fr" href="https://yoursite.com/fr/[fr-slug]/" />
<link rel="alternate" hreflang="x-default" href="https://yoursite.com/[en-slug]/" />
```

## JSON-LD Recipe Structured Data

Include in every article for rich search results (stars, cook time in SERP):

```json
{
  "@context": "https://schema.org",
  "@type": "Recipe",
  "name": "[Dish Name]",
  "description": "[Brief description]",
  "prepTime": "PT[X]M",
  "cookTime": "PT[X]M",
  "totalTime": "PT[X]M",
  "recipeYield": "[X] servings",
  "recipeCategory": "Main Course",
  "recipeCuisine": "Chinese, [Region]",
  "keywords": "[target keyword], [secondary keywords]",
  "recipeIngredient": [
    "[quantity] [ingredient]",
    "..."
  ],
  "recipeInstructions": [
    {
      "@type": "HowToStep",
      "text": "[Step description]"
    }
  ],
  "nutrition": {
    "@type": "NutritionInformation",
    "calories": "[X] calories"
  }
}
```

Each language version needs its own JSON-LD with localized content.
