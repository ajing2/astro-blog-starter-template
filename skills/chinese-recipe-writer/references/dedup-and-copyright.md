# Google 去重与防侵权处理指南

## 为什么必须做去重和防侵权

Google 的算法（尤其是 Helpful Content Update 和 Spam Update）会严厉惩罚：
- 重复内容（Duplicate Content）：与其他网站高度相似的文本，降权或不收录
- 侵权内容：直接复制他人文章，可能收到 DMCA 投诉导致页面从搜索结果移除
- AI 生成的低质量内容：无原创价值的机器批量生产内容

## 处理流程（写作过程中执行）

### Phase 1：素材收集阶段 — 标记来源

```
1. 查看 3-5 个参考菜谱时，只记录"做法要点"，不复制原文
2. 记录参考来源 URL（备查，不发布）
3. 用自己的话重新组织步骤逻辑
4. 故事/文化素材标注来源（百度百科/维基百科/学术文章）
```

### Phase 2：写作阶段 — 原创性保障

**核心原则：每段文字必须是自己的表达，不是改写别人的句子。**

操作步骤：

1. **步骤描述原创化**
   - 不要：复制其他网站的步骤描述然后换词
   - 要：基于自己的理解重新写，加入独特的感官描述和"为什么"解释
   - 差异化方法：加入个人经验、失败教训、中文烹饪术语解释

2. **故事段落原创化**
   - 不要：从维基百科/百度百科直接翻译
   - 要：用信息综合后用自己的叙事风格重写
   - 加入独特视角：个人故事 > 文化解读 > 历史整合

3. **食材描述差异化**
   - 不要：复制 Amazon 商品描述
   - 要：写自己使用这个食材的真实体验和推荐理由

4. **FAQ 原创化**
   - 搜索 Google "People Also Ask" 找到真实问题
   - 答案用自己的知识和经验回答，不复制排名页面的答案

### Phase 3：发布前检查 — 去重验证

#### 工具检查

1. **Copyscape**（推荐，付费）
   - 网址：https://www.copyscape.com
   - 将英文版全文粘贴检查
   - 相似度 < 10% 为安全，> 20% 必须重写

2. **Grammarly Plagiarism Checker**（付费版自带）
   - 写作时实时检测重复内容

3. **Quetext**（免费额度）
   - 网址：https://www.quetext.com
   - 备选工具，有免费查重额度

4. **手动 Google 搜索验证**
   - 从文章中随机抽取 3-5 句完整句子
   - 用引号搜索（如 "your exact sentence here"）
   - 如果找到完全匹配结果 → 必须重写该句

#### 各部分去重标准

| 文章部分 | 允许相似度 | 说明 |
|----------|-----------|------|
| Hook | < 5% | 必须完全原创 |
| Story | < 10% | 事实可相同，表达必须原创 |
| Ingredients | < 30% | 食材名称不可避免重复，但描述要原创 |
| Instructions | < 15% | 步骤逻辑可参考，文字表达必须原创 |
| Pro Tips | < 5% | 体现专业性，必须原创 |
| FAQ | < 10% | 问题可相似，答案必须原创 |

### Phase 4：多语言版本的去重

**重要：5 个语言版本之间不算重复内容**（Google 通过 hreflang 识别多语言）。

但同一语言内的注意事项：
- 不同菜谱文章之间的 Story 段落不能太相似（如都用相同的四川介绍）
- FAQ 答案不能跨文章复制粘贴
- Pro Tips 不能每篇都写一样的通用建议

### Phase 5：防 DMCA 投诉

1. **图片版权**
   - 只使用：自拍照片 / AI 生成图片 / 明确 CC0/CC-BY 授权的图片
   - 绝不使用：从其他食谱网站保存的图片
   - 推荐 AI 生图工具：Midjourney, DALL-E, Stable Diffusion
   - 免费图库：Unsplash, Pexels（但食谱图建议自生成以保持独特性）

2. **文字版权**
   - 食谱的"步骤列表"在美国法律下不受版权保护（Recipes are not copyrightable）
   - 但"表达方式"受保护 — 所以必须用自己的话写步骤
   - 故事/描述/Tips 的原创表达受版权保护

3. **品牌和商标**
   - 提到品牌名（如 Lee Kum Kee）做推荐是合法的（Fair Use）
   - 不要暗示品牌合作关系（除非真的有）
   - 在 affiliate 链接处注明 "This post contains affiliate links"

## 原创性提升技巧

让内容自然与竞品拉开差距：

1. **加入个人体验**："I've made this dish over 50 times, and the mistake I see most people make is..."
2. **加入失败案例**："The first time I tried this, my tofu completely fell apart. Here's what I learned..."
3. **加入文化深度**：引用中文俗语、烹饪哲学、地方饮食习惯
4. **加入对比**："Unlike the restaurant version that uses..."
5. **加入科学解释**："The Maillard reaction at high heat creates..."
6. **中英双语术语**：其他英文食谱不会加中文注释，这是天然差异化

## 被抄袭时的应对

如果发现别人抄袭了你的内容：
1. 截图保存证据（包含发布时间）
2. 通过 Google DMCA 工具提交投诉：https://support.google.com/legal/troubleshooter/1114905
3. 联系对方网站要求删除
4. 保持原文的发布时间戳作为原创证明
