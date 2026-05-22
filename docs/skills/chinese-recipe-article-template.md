# 中餐食谱多语言站 —— 文章写作模板

> 每篇文章按以下结构组织，**同时产出 5 种语言版本**。
> 括号内为写作指导说明，实际写作时删除。

---

## 〇-A、各语言最佳字数（SEO 指导）

> 核心原则：不是凑字数，而是**完整回答用户所有可能的问题**。Google 算法看的不是字数本身，而是内容是否覆盖了用户的搜索意图。把"怎么做、用什么食材、哪里买、能不能替换、怎么保存、配什么吃"这些问题都回答清楚，字数自然到位。

| 语言 | 最佳字数范围 | 计量单位 | 说明 |
|------|-------------|---------|------|
| 🇺🇸 英文 | **1,500 - 2,500 词** | words | 食谱类 SEO 甜蜜区。Google 首页食谱文章平均 1,500-2,000 词。低于 1,000 词易被判定为 thin content，超过 3,000 词跳出率上升 |
| 🇨🇳 中文 | **2,000 - 4,000 字** | 汉字 | 中文信息密度高于英语。2,000 字以下在百度 SEO 中内容不够充实，4,000 字以上偏长 |
| 🇩🇪 德语 | **1,200 - 2,000 词** | Wörter | 德语单词比英语长，同等信息量词数更少但字符数更多。德国用户偏好精确详实，不必刻意缩减 |
| 🇯🇵 日语 | **3,000 - 5,000 字符** | 文字数 | 日语用汉字+假名混合书写，信息密度远高于英语。3,000-5,000 字符约等于英语 1,500-2,500 词的信息量 |
| 🇫🇷 法语 | **1,200 - 2,000 词** | mots | 法语表达相对紧凑，同等信息量词数比英语略少 |

### 各部分的字数分配参考（以英文版为例）

```
食谱正文结构                        英文词数      占比
------------------------------------------------------
Hook 开头                          50-80        ~3%
Story 故事/文化背景                 200-300      ~13%
Quick Info 速览                    30-50        ~2%
Ingredients 食材清单               100-150      ~7%
Steps 做法步骤                     400-600      ~27%
Pro Tips 大厨贴士                  150-250      ~10%
Serving Suggestions 搭配建议        80-120       ~5%
Storage and Reheating 保存加热      60-100       ~4%
FAQ 常见问题（4-6 个）              300-500      ~20%
Affiliate CTA 推荐产品              80-120       ~5%
Recipe Card JSON-LD                （不计入正文字数）
------------------------------------------------------
合计                               1,500-2,500   100%
```

### 字数红线

```
⚠️ 低于下限 → Google 可能判定为 thin content，排名受损
⚠️ 超过上限 → 用户跳出率上升，影响停留时间指标
✅ 在范围内 → 信息完整 + 用户体验好 = SEO 最优
```

> 💡 **FAQ 是字数调节器：** 如果正文写完发现字数不够，增加 1-2 个高质量 FAQ 是最自然的补充方式，同时还能抢占 Google "People Also Ask" 位置。如果字数超了，优先精简 Story 部分。

---

## 〇-B、多语言策略（核心规则）

### 目标语言（按优先级排列）

| 序号 | 语言 | 目标市场 | 预估广告 RPM | URL 前缀 | 备注 |
|------|------|----------|-------------|----------|------|
| 1 | 🇨🇳 中文 | 国内华人、海外华人 | ¥5-15 | `/zh/` | 原始内容语言，用于素材沉淀和国内平台分发 |
| 2 | 🇺🇸 英文 | 美/英/加/澳/新 | $15-30 | `/en/` (或根目录) | 主力变现语言，投入最多精力打磨 |
| 3 | 🇩🇪 德语 | 德国/奥地利/瑞士 | €10-20 | `/de/` | 竞争小、RPM 高，性价比最优的第二语言 |
| 4 | 🇯🇵 日语 | 日本 | ¥800-1500 | `/ja/` | 日本人对中华料理接受度高，市场天然匹配 |
| 5 | 🇫🇷 法语 | 法国/比利时/加拿大魁北克 | €8-15 | `/fr/` | 法国是美食大国，对各国美食开放度高 |

### 多语言生产流程

```
第 1 步：用中文整理菜品做法、故事素材、食材信息（作为"母版"）
第 2 步：基于中文母版，用 AI 生成英文版（重点打磨，作为"主站版本"）
第 3 步：基于英文版，用 AI 翻译生成德语、日语、法语版本
第 4 步：人工检查每个语言版本（重点检查食材本地化和文化适配）
第 5 步：为每个语言版本分别优化 SEO 元信息（标题、描述、关键词）
```

### 各语言版本的差异化要点

**中文版：**
- 面向海外华人或国内读者，风格亲切口语化
- 可在微信公众号、小红书等国内平台同步分发
- 食材用中式计量（克、毫升、勺）

**英文版（主力版本）：**
- 食材用美式计量（tablespoon, cup, oz）
- 食材购买建议指向 Amazon US，联盟链接用美国亚马逊
- 替代方案基于美国超市能买到的食材
- 故事部分需要更多文化背景解释（老外不了解中国文化）

**德语版：**
- 食材计量用公制（克、毫升），德国人习惯公制
- 食材购买建议指向 Amazon.de 或本地亚洲超市
- 替代方案基于德国超市（如 Edeka、REWE、Asian-Laden）能买到的食材
- 德国人做菜习惯严谨精确，步骤描述要更详细
- 亚马逊联盟链接用 Amazon.de

**日语版：**
- 食材计量用公制（グラム、ml、大さじ、小さじ）
- 很多中餐调料在日本超市可以直接买到（豆板醤、花椒など）
- 日本人对中华料理有自己的理解（如日式麻婆豆腐偏甜），需要强调"正宗中国做法"的差异
- 联盟链接用 Amazon.co.jp
- 可以加入"和日本版的区别"作为话题点

**法语版：**
- 食材计量用公制（grammes, ml, cuillère à soupe）
- 法国人重视烹饪技法，步骤中的"为什么这么做"解释可以更详细
- 替代方案基于法国超市（如 Carrefour、Monoprix）和巴黎亚洲超市（如 Tang Frères）
- 联盟链接用 Amazon.fr
- 法国人喜欢把中餐和法餐技法做对比，可以适当加入

### 网站目录结构

```
yoursite.com/                    ← 英文版（默认/主站）
yoursite.com/zh/                 ← 中文版
yoursite.com/de/                 ← 德语版
yoursite.com/ja/                 ← 日语版
yoursite.com/fr/                 ← 法语版

示例：
yoursite.com/mapo-tofu-recipe/           ← 英文
yoursite.com/zh/mapo-tofu-recipe/        ← 中文
yoursite.com/de/mapo-tofu-rezept/        ← 德语（注意 URL 用德语）
yoursite.com/ja/mapo-tofu-recipe/        ← 日语（URL 保持英文拼写）
yoursite.com/fr/recette-mapo-tofu/       ← 法语（注意 URL 用法语）
```

### SEO 多语言标记（hreflang）

> 每个页面的 `<head>` 中必须添加 hreflang 标签，告诉 Google 这些是同一内容的不同语言版本。

```html
<link rel="alternate" hreflang="en" href="https://yoursite.com/mapo-tofu-recipe/" />
<link rel="alternate" hreflang="zh" href="https://yoursite.com/zh/mapo-tofu-recipe/" />
<link rel="alternate" hreflang="de" href="https://yoursite.com/de/mapo-tofu-rezept/" />
<link rel="alternate" hreflang="ja" href="https://yoursite.com/ja/mapo-tofu-recipe/" />
<link rel="alternate" hreflang="fr" href="https://yoursite.com/fr/recette-mapo-tofu/" />
<link rel="alternate" hreflang="x-default" href="https://yoursite.com/mapo-tofu-recipe/" />
```

### 联盟链接对照表

| 语言 | 亚马逊联盟 | 申请地址 | 备注 |
|------|-----------|---------|------|
| 英文 | Amazon US Associates | affiliate-program.amazon.com | 主力收入来源 |
| 德语 | Amazon.de PartnerNet | partnernet.amazon.de | 德国站佣金率和美国接近 |
| 日语 | Amazon.co.jp Associates | affiliate.amazon.co.jp | 日本站商品丰富 |
| 法语 | Amazon.fr Partenaires | partenaires.amazon.fr | 法国站 |
| 中文 | 无亚马逊联盟 | — | 可用国内电商联盟（京东联盟、淘宝客）或 AdSense |

---

## 一、文章元信息（SEO 必填项 × 5 种语言）

> 每篇文章需要为 5 种语言分别准备 SEO 元信息，不能简单翻译，要针对每种语言做关键词研究。

### 英文版 (EN)
```
Title Tag:       [菜名英文] Recipe - [核心卖点] （≤60 字符）
                 示例：Easy Mapo Tofu Recipe - Authentic Sichuan Style (20 Min)
Meta Description: ≤160 字符，包含英文关键词
                 示例：Learn how to make authentic Mapo Tofu at home with this easy step-by-step recipe. Spicy, numbing, and ready in just 20 minutes!
URL Slug:        /mapo-tofu-recipe/
Target Keyword:  mapo tofu recipe
Secondary KW:    easy mapo tofu, sichuan tofu recipe, spicy tofu with ground pork
```

### 中文版 (ZH)
```
Title Tag:       [菜名] 的做法 - [核心卖点]（≤30 中文字符）
                 示例：正宗麻婆豆腐的做法 - 川菜经典，20分钟搞定
Meta Description: ≤80 中文字符
                 示例：手把手教你做正宗川味麻婆豆腐，麻辣鲜香，配米饭绝了！详细步骤+食材替代方案。
URL Slug:        /zh/mapo-tofu-recipe/
Target Keyword:  麻婆豆腐的做法
Secondary KW:    麻婆豆腐怎么做, 正宗麻婆豆腐, 川菜食谱
```

### 德语版 (DE)
```
Title Tag:       [菜名德文] Rezept - [核心卖点]（≤60 字符）
                 示例：Mapo Tofu Rezept - Authentisch aus Sichuan (20 Min)
Meta Description: ≤160 字符
                 示例：Lernen Sie, wie Sie authentischen Mapo Tofu zu Hause zubereiten. Scharf, würzig und in nur 20 Minuten fertig!
URL Slug:        /de/mapo-tofu-rezept/
Target Keyword:  Mapo Tofu Rezept
Secondary KW:    Sichuan Tofu Rezept, scharfer Tofu mit Hackfleisch, chinesisches Tofu Rezept
```

### 日语版 (JA)
```
Title Tag:       [菜名日文] レシピ - [核心卖点]（≤30 全角字符）
                 示例：本格麻婆豆腐のレシピ - 四川風の本場の味（20分で完成）
Meta Description: ≤80 全角字符
                 示例：本場四川の麻婆豆腐を自宅で再現！花椒の痺れる辛さがたまらない、本格レシピをご紹介します。
URL Slug:        /ja/mapo-tofu-recipe/
Target Keyword:  麻婆豆腐 レシピ 本格
Secondary KW:    四川風麻婆豆腐, 本格中華レシピ, 麻婆豆腐 作り方
```

### 法语版 (FR)
```
Title Tag:       Recette de [菜名法文] - [核心卖点]（≤60 字符）
                 示例：Recette du Mapo Tofu - Authentique Cuisine du Sichuan (20 Min)
Meta Description: ≤160 字符
                 示例：Découvrez comment préparer un authentique Mapo Tofu fait maison. Épicé, savoureux et prêt en seulement 20 minutes !
URL Slug:        /fr/recette-mapo-tofu/
Target Keyword:  recette mapo tofu
Secondary KW:    tofu sichuan recette, cuisine chinoise recette, tofu épicé porc haché
```

---

## 二、文章正文结构

### Part 1: Hook 开头（1-2 句话，抓住注意力）

> 用一个感官描述、一个有趣事实或一个问题开头。
> 要让读者立刻想往下看。

写法示例：
```
There's a reason why Mapo Tofu has been the #1 comfort food in Sichuan province
for over 150 years — one bite of that silky tofu in fiery, numbing sauce and
you'll understand why.
```

---

### Part 2: Story 故事段落（200-300 词）

> 这是你和竞争对手拉开差距的关键部分。
> 一个好故事能让读者停留更久（提升 dwell time），这是 SEO 的重要信号。

可以选择以下 5 个角度之一：

**角度 1：历史起源**
```
Mapo Tofu was invented around 1862 in Chengdu by a woman named Chen Mapo (陈麻婆).
She ran a small restaurant near the Wanfu Bridge, serving workers and oil merchants.
Her face was marked with pockmarks (麻 má), which is how she got her nickname.
The dish she created — soft tofu in a spicy, numbing sauce — became so famous
that people traveled from across the province just to taste it...
```

**角度 2：个人/家庭故事**
```
My grandmother made Mapo Tofu every Friday night. She said it was the dish that
reminded her of home — she grew up in a small village outside Chengdu...
（用第一人称讲述与这道菜的个人联系）
```

**角度 3：文化意义**
```
In Sichuan, Mapo Tofu isn't just a dish — it's a philosophy. The local saying goes:
"麻辣鲜香" (má là xiān xiāng) — numbing, spicy, fresh, fragrant — these four
flavors must be in perfect balance...
（解释这道菜在中国文化中的地位）
```

**角度 4：趣闻轶事**
```
Here's something most people don't know: Mapo Tofu was almost lost to history.
During the Cultural Revolution...
（讲一个和这道菜相关的有趣冷知识）
```

**角度 5：挑战/对比**
```
If you've only had Mapo Tofu from your local Chinese takeout, I need to tell you
something: that's not real Mapo Tofu. The authentic version from Sichuan is an
entirely different experience...
（和读者已有的认知形成反差）
```

---

### Part 3: Quick Info 速览（放在故事之后、食材之前）

> 这是一个快速参考区域，让着急的读者一眼看到关键信息。

```
⏱ Prep Time: 15 minutes
🔥 Cook Time: 10 minutes
🍽 Servings: 2-3
📊 Difficulty: Easy
🌶 Spice Level: Medium-Hot (adjustable)
```

---

### Part 4: Ingredients 食材清单

> 分组列出，不要一堆食材混在一起。
> 每个食材后面加括号说明作用或替代品，这是 affiliate 链接的好位置。

写法示例：
```
**For the sauce:**
- 2 tablespoons doubanjiang (豆瓣酱, Pixian brand recommended [联盟链接])
- 1 tablespoon fermented black beans (豆豉, adds depth of flavor)
- 1 cup chicken broth (or vegetable broth for vegetarian version)

**For the tofu:**
- 14 oz (400g) soft/silken tofu, cut into 1/2-inch cubes
- A pinch of salt (for blanching)

**Aromatics:**
- 2 cloves garlic, minced
- 1 tablespoon fresh ginger, minced
- 2 scallions, chopped (white and green parts separated)

**For finishing:**
- 1 teaspoon Sichuan peppercorn powder (花椒粉 [联盟链接])
  → Can't find it? [See my guide to Sichuan peppercorn substitutes](/sichuan-peppercorn-guide/)
```

#### 🔑 食材部分的要点：
1. 关键调料要注明中文名（增加专业感和搜索相关性）
2. 难买到的食材要给替代方案
3. 推荐品牌时嵌入联盟链接（自然，不硬推）
4. 可以内链到其他食材指南文章

---

### Part 5: Instructions 做法步骤

> 每步一个核心动作，配合感官提示。
> 用动词开头，语气直接。
> 关键操作要解释"为什么"，不只是说"怎么做"。

写法示例：
```
**Step 1: Prepare the tofu**
Cut the tofu into 1/2-inch cubes. Bring a pot of water to a gentle boil, add a pinch
of salt, and blanch the tofu for 2 minutes. This step removes the raw soybean taste
and firms up the tofu so it won't fall apart during cooking.

**Step 2: Cook the aromatics**
Heat 2 tablespoons of oil in a wok over medium heat. Add the ground pork and stir-fry
until browned, about 3 minutes. Push the meat to the side and add the doubanjiang.
Stir-fry the paste for about 30 seconds until the oil turns red — this is called
"炒出红油" (chao chu hong you), meaning to "fry out the red oil," and it's the key
to unlocking the paste's full flavor.

**Step 3: ...**
（以此类推，一般 5-8 个步骤）
```

#### 🔑 写步骤的原则：
1. 每步一个核心动作，不要把三个操作挤在一步里
2. 温度和时间要具体："medium-high heat for 2 minutes" 而不是 "cook until done"
3. 感官提示很重要："until the garlic is fragrant" "until the sauce thickens and coats the back of a spoon"
4. 中文烹饪术语加注释能增加专业感和趣味性（如上面 "炒出红油" 的例子）

---

### Part 6: Pro Tips 大厨小贴士（3-5 条）

> 分享一些进阶技巧，体现你的专业性。

写法示例：
```
💡 **Pro Tips:**

- **Silken tofu vs. firm tofu:** Traditional Mapo Tofu uses soft (silken) tofu for that
  melt-in-your-mouth texture. If you prefer a firmer bite, medium-firm tofu works too.

- **Make it vegetarian:** Skip the ground pork and use crumbled mushrooms instead.
  Shiitake mushrooms work particularly well and add a savory umami depth.

- **Control the heat:** Doubanjiang is already quite spicy. If you're sensitive to heat,
  start with 1 tablespoon and adjust to your taste.

- **The secret to silky tofu:** Blanching tofu in salted water before cooking is a trick
  Chinese grandmas have used for generations. Don't skip this step!
```

---

### Part 7: Serving Suggestions 搭配建议

> 告诉读者这道菜配什么吃，顺便可以内链到其他食谱文章。

写法示例：
```
Mapo Tofu is traditionally served over a bowl of steamed white rice — the rice soaks
up all that spicy, savory sauce and it's absolutely heavenly.

For a complete Chinese meal, pair it with:
- [Stir-Fried Bok Choy with Garlic](/bok-choy-recipe/) (内链)
- [Egg Drop Soup](/egg-drop-soup-recipe/) (内链)
- A simple cucumber salad to balance the heat
```

---

### Part 8: Storage and Reheating 保存与加热

> 简短实用，2-3 句话。

写法示例：
```
**Storage:** Leftovers can be stored in an airtight container in the refrigerator for
up to 3 days.

**Reheating:** Reheat gently in a saucepan over medium-low heat. Add a splash of water
or broth if the sauce has thickened too much.

**Freezing:** Not recommended — tofu changes texture when frozen and becomes spongy.
```

---

### Part 9: FAQ 常见问题（4-6 个）

> 用真实的问题，这些 FAQ 能帮你抢占 Google 的 "People Also Ask" 位置。

写法示例（用 Q&A 格式）：
```
**Q: What does Mapo Tofu taste like?**
A: It's a beautiful combination of spicy, numbing (from Sichuan peppercorn), savory,
and slightly sweet. The texture is soft and silky with bits of savory ground pork.

**Q: Is Mapo Tofu healthy?**
A: Yes! Tofu is an excellent source of plant-based protein and calcium. This dish is
relatively low in calories compared to many Chinese dishes.

**Q: Can I make Mapo Tofu without meat?**
A: Absolutely! Just skip the ground pork or substitute with crumbled shiitake mushrooms
for a delicious vegetarian version.

**Q: What is doubanjiang and where can I buy it?**
A: Doubanjiang is a fermented chili bean paste essential to Sichuan cooking. You can
find it at Asian grocery stores or order it on Amazon (联盟链接).
```

---

### Part 10: Recipe Card 食谱卡片

> 放在文章最底部，这是一个结构化的食谱摘要。
> 如果用 WordPress，可以用 WP Recipe Maker 插件自动生成。
> 如果用 Astro，可以用 JSON-LD 结构化数据实现。
> Google 会抓取这个结构化数据，在搜索结果里显示星级评分和烹饪时间，大幅提升点击率。

```json
{
  "@type": "Recipe",
  "name": "Mapo Tofu",
  "description": "Authentic Sichuan Mapo Tofu...",
  "prepTime": "PT15M",
  "cookTime": "PT10M",
  "totalTime": "PT25M",
  "recipeYield": "3 servings",
  "recipeCategory": "Main Course",
  "recipeCuisine": "Chinese, Sichuan",
  "recipeIngredient": ["14 oz soft tofu", "4 oz ground pork", "..."],
  "recipeInstructions": ["..."]
}
```

---

### Part 11: Affiliate CTA 变现入口（自然嵌入，不要硬推）

> 在文章中 2-3 个位置自然地推荐产品，附联盟链接。

推荐位置和方式：
```
位置1 - 食材说明部分：
"I always use this brand of doubanjiang [联盟链接] — it's the most authentic one
I've found outside of China."

位置2 - 步骤中提到工具时：
"A well-seasoned carbon steel wok [联盟链接] makes a huge difference for this dish.
The high heat distribution gives you that restaurant-quality sear."

位置3 - 文末推荐区：
"🛒 Tools and Ingredients I Used:
- Carbon Steel Wok [联盟链接]
- Pixian Doubanjiang [联盟链接]
- Sichuan Peppercorn [联盟链接]"
```

---

## 三、文章写作 Checklist

### 单语言版本检查（每个语言都要过一遍）

- [ ] Title Tag 包含主关键词，长度合规（EN/DE/FR ≤60字符，ZH ≤30字符，JA ≤30全角）
- [ ] Meta Description 长度合规，包含该语言关键词
- [ ] URL 简短干净，包含菜名（德语/法语 URL 用本地语言）
- [ ] H1 只有一个（文章标题）
- [ ] H2/H3 结构清晰
- [ ] 故事部分有趣且真实，有文化背景解释（英文版特别需要）
- [ ] 食材计量单位符合目标市场习惯（EN 用美式，其他用公制）
- [ ] 关键调料有本地化购买建议和替代方案
- [ ] 步骤清晰，每步 2-3 句话
- [ ] 至少 3 张配图（成品图、关键步骤图、食材图）
- [ ] 图片都有对应语言的 alt 标签
- [ ] 内链到 2-3 篇同语言的其他食谱文章
- [ ] FAQ 4-6 个真实问题（各语言用户关注点可能不同）
- [ ] 联盟链接 2-3 个，指向对应国家的亚马逊站点
- [ ] Recipe JSON-LD 结构化数据已添加（每个语言版本都要有）
- [ ] 通读确认语言自然，无机翻痕迹

### 多语言整体检查

- [ ] 5 个语言版本全部产出（ZH / EN / DE / JA / FR）
- [ ] 每个页面都添加了 hreflang 标签
- [ ] 各语言联盟链接指向正确的亚马逊站点
- [ ] 食材计量单位已按语言本地化
- [ ] 食材购买建议已按当地超市本地化
- [ ] 德语版步骤描述更加详细精确
- [ ] 日语版包含"与日式做法的区别"话题点
- [ ] 法语版适当加入中法烹饪技法对比
- [ ] 中文版可直接用于微信/小红书分发

---

## 四、一篇文章的生产流程（5 语言版本，参考用时）

| 步骤 | 内容 | 用时 |
|------|------|------|
| 1 | 选菜 + 5 种语言关键词研究 | 30 分钟 |
| 2 | 去下厨房/美食天下看 3-5 个版本，理解做法 | 20 分钟 |
| 3 | 查故事素材（百度百科/知乎/AI） | 15 分钟 |
| 4 | 用 AI 生成中文母版初稿 | 15 分钟 |
| 5 | 基于中文母版，用 AI 生成英文版（重点打磨） | 25 分钟 |
| 6 | 人工润色英文版，加入个人体验和本地化说明 | 30 分钟 |
| 7 | 用 AI 将英文版翻译为德语、日语、法语 | 20 分钟 |
| 8 | 逐个检查德/日/法版本（食材本地化、文化适配） | 30 分钟 |
| 9 | 准备配图（AI 生成或自拍，图片各语言共用） | 20 分钟 |
| 10 | 各语言 SEO 优化（标题、描述、hreflang、结构化数据、内链） | 25 分钟 |
| 11 | 最终检查 5 个版本、发布 | 20 分钟 |
| **合计** | | **约 4 小时/篇（含 5 语言）** |

> 💡 **效率提示：** 虽然 5 语言版本看起来工作量翻倍，但实际只增加约 60%——因为素材调研、配图、做法整理是一次性的，增加的主要是翻译和本地化的时间。而收入潜力可能增加 3-4 倍。

---

*模板版本：v2.0 | 更新日期：2025-05*
*更新内容：新增多语言策略（中/英/德/日/法 5 语言同步产出）*
