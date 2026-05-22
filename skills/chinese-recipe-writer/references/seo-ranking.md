# Google SEO 排名优化策略

## Google 排名核心算法因素（食谱站适用）

Google 对食谱类内容的排名主要看以下维度（按权重排序）：

1. **内容质量与搜索意图匹配**（最重要）
2. **E-E-A-T 信号**（Experience, Expertise, Authoritativeness, Trustworthiness）
3. **页面体验指标**（Core Web Vitals）
4. **外链与权威度**
5. **技术 SEO**

## 一、内容质量优化

### 搜索意图完整覆盖

Google 排名的本质：**谁能最完整地回答用户的问题，谁排第一。**

食谱类搜索意图分析：
```
用户搜索 "mapo tofu recipe" 时，实际想知道：
├── 怎么做（步骤）        → Instructions 部分
├── 用什么材料（食材）     → Ingredients 部分
├── 多长时间（效率）       → Quick Info 部分
├── 难不难（信心）         → Difficulty + Pro Tips
├── 哪里买食材（行动）     → Affiliate + 替代方案
├── 能不能变化（灵活性）   → Vegetarian/调整建议
├── 怎么保存（实用）       → Storage 部分
└── 好不好吃（预期）       → Hook + 图片
```

每篇文章必须覆盖以上所有意图，遗漏任何一项都可能被覆盖更全的竞品超越。

### 内容深度信号

Google 判断内容深度的信号：
- 文章涵盖主题的多个方面（不只是步骤，还有文化、技巧、FAQ）
- 信息密度高（每段都有实质内容，无水分）
- 包含其他页面没有的独特信息（个人经验、中文术语、历史故事）
- FAQ 回答了 "People Also Ask" 中的真实问题

### 内容新鲜度

- 定期更新已发布文章（修正信息、添加新 FAQ、更新 affiliate 链接）
- 在文章中标注 "Last updated: [date]"
- Google 偏好活跃更新的内容而非发布后不管的内容

## 二、E-E-A-T 优化（食谱站重点）

### Experience（经验）— 最易突破的维度

Google 2023 年新增的"经验"维度，对食谱站最友好：

1. **第一人称叙述**："I've been making this dish for 10 years..."
2. **失败经验分享**："Don't make the mistake I made the first time..."
3. **原创照片**：真实的烹饪过程照片（比 stock photo 权重高）
4. **具体细节**：只有亲自做过才知道的小细节
5. **变体经验**："I've tried 5 different brands of doubanjiang, and this one..."

### Expertise（专业性）

1. **About 页面**：建立作者档案，说明烹饪背景
2. **中文烹饪术语**：展示对中餐的深入了解
3. **营养信息**：提供准确的营养成分数据
4. **烹饪科学**：解释为什么这么做（美拉德反应、淀粉糊化等）

### Authoritativeness（权威性）

1. **内链系统**：各菜谱文章相互引用，建立主题权威
2. **外部引用**：引用可靠来源（Wikipedia、学术论文、权威媒体）
3. **一致的发布频率**：持续输出高质量内容
4. **社交信号**：在 Pinterest、YouTube 等平台获得分享

### Trustworthiness（可信度）

1. **Affiliate 披露**：每篇文章标注 "This post contains affiliate links"
2. **隐私政策和免责声明**：网站底部链接
3. **HTTPS**：Cloudflare 自动提供
4. **联系信息**：提供真实的联系方式

## 三、页面体验优化（Core Web Vitals）

### LCP（最大内容渲染）< 2.5s

- 图片使用 WebP 格式，启用懒加载
- 首屏图片优先加载（preload）
- Cloudflare CDN 自动加速

### INP（交互延迟）< 200ms

- Astro 静态站天然优秀（几乎无 JS）
- 避免阻塞主线程的脚本

### CLS（布局偏移）< 0.1

- 图片设置明确的 width/height 属性
- 字体使用 font-display: swap
- 广告位预留空间

### 移动端优先

- 响应式设计（Google 使用移动版索引）
- 食谱步骤在手机上易于逐步跟随
- 按钮和链接触摸目标 ≥ 48px

## 四、技术 SEO 优化

### 结构化数据（最关键）

食谱站必须使用 Recipe Schema：
- 能在搜索结果中显示星级、烹饪时间、卡路里
- 点击率提升 30-50%
- 实现方法见 [references/seo-metadata.md](seo-metadata.md) 中的 JSON-LD 部分

### 站点结构

```
首页
├── 按菜系分类页（川菜、粤菜、北方菜...）
│   └── 具体菜谱文章
├── 按食材分类页（豆腐、鸡肉、猪肉...）
│   └── 具体菜谱文章
├── 按难度分类页
├── 按时间分类页（15分钟快手菜、周末大菜...）
└── 知识类文章（食材指南、厨具推荐、烹饪技巧）
```

### 内链策略

每篇文章设置 3 类内链：
1. **同食材链接**："More tofu recipes: [Mapo Tofu](/mapo-tofu/), [Kung Pao Tofu](/kung-pao-tofu/)"
2. **搭配推荐链接**："Serve with [Egg Drop Soup](/egg-drop-soup/)"
3. **知识补充链接**："Learn more about Sichuan peppercorn in our [Spice Guide](/sichuan-spice-guide/)"

### URL 和 Sitemap

- URL 短且含关键词：`/mapo-tofu-recipe/` 而非 `/recipes/2024/05/authentic-sichuan-style-mapo-tofu-recipe-easy/`
- 多语言 sitemap 包含所有语言版本的 URL
- 每次发布新文章后提交 sitemap 到 Google Search Console

### Robots 和索引控制

- 允许 Google 爬取所有有价值页面
- noindex 标签页、搜索结果页等低价值页面
- 避免同一内容出现在多个 URL（canonical 标签）

## 五、外链建设策略

### 自然获取外链

1. **创建可引用资源**：如 "Complete Guide to Sichuan Spices" 长文
2. **原创研究**：如 "We tested 10 brands of soy sauce — here are the results"
3. **信息图表**：如 "Chinese Regional Cuisines Map"
4. **Pinterest 引流**：食谱图片在 Pinterest 上分享率高

### 主动建设外链

1. **Guest Post**：在其他美食博客投稿
2. **资源页面**：联系 "Best Chinese Recipe Sites" 类文章的作者
3. **HARO/Connectively**：回答记者关于中餐的问题
4. **社区参与**：Reddit r/chinesefood、r/cooking 等社区答疑

## 六、排名监测与迭代

### 工具

- **Google Search Console**（免费，必用）：查看搜索词、点击率、排名位置
- **Google Analytics**（免费，必用）：查看流量、用户行为
- **Ahrefs/SEMrush**（付费）：竞品分析、关键词追踪

### 关键指标

| 指标 | 目标值 | 含义 |
|------|--------|------|
| Average Position | < 10 | 首页排名 |
| CTR | > 5% | 标题和描述吸引人 |
| Bounce Rate | < 60% | 内容匹配搜索意图 |
| Avg. Session Duration | > 3min | 内容有深度 |
| Pages/Session | > 1.5 | 内链有效 |

### 排名提升迭代

当文章排名停滞时：
1. 检查排在前面的竞品多了什么内容 → 补充进文章
2. 增加 FAQ 覆盖新出现的 "People Also Ask"
3. 更新过时信息（价格、链接、品牌推荐）
4. 增加原创图片或视频
5. 获取更多外链指向该页面

## 七、避免 Google 惩罚

### 不要做

- 关键词堆砌（keyword stuffing）
- 隐藏文字或链接
- 购买低质量外链
- 大量生成无差异化的 AI 内容
- 使用 doorway pages 或 cloaking
- 多个页面竞争同一关键词（内部竞争）

### 注意事项

- 每篇文章只针对一个核心关键词
- 长尾关键词分散在不同文章中
- 内容更新频率保持稳定（每周 1-2 篇比突然发 50 篇更安全）
- AI 生成内容必须经过人工编辑，加入原创经验和观点
