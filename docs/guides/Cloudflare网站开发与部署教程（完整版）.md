# Cloudflare 网站开发与部署教程（完整版）

本教程基于你已有的 Cloudflare 账号和 Workers 项目（astro-blog-starter-template），涵盖两种部署方式：Cloudflare Pages（推荐，连接 GitHub 自动部署）和 Workers（手动 CLI 部署）。

## 一、前置准备

你需要准备以下工具和账号：

- GitHub 账号 — 代码托管，地址：https://github.com
- Cloudflare 账号 — 你已经有了，控制台地址：https://dash.cloudflare.com
- Node.js 环境 — 本地开发需要，建议 v18+
- Git — 版本管理工具

## 二、方式一：Cloudflare Pages + GitHub 自动部署（推荐）

这是最省心的方式：代码推送到 GitHub，Cloudflare 自动构建和部署。适合博客、食谱网站等内容站。

### 步骤 1：在 GitHub 创建仓库

1. 登录 https://github.com
2. 点击右上角 "+" → "New repository"
3. 仓库名建议用网站相关名称，例如 chinese-food-recipes
4. 选择 Public（公开）或 Private（私有）都可以
5. 点击 "Create repository"

### 步骤 2：本地初始化 Astro 项目

打开终端，执行以下命令：

```shell
# 创建 Astro 项目（选择 blog 模板）
npm create astro@latest -- --template blog

# 进入项目目录
cd your-project-name

# 安装依赖
npm install

# 本地预览（浏览器打开 http://localhost:4321）
npm run dev
```

### 步骤 3：推送代码到 GitHub

```shell
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/你的用户名/chinese-food-recipes.git
git push -u origin main
```

### 步骤 4：在 Cloudflare Pages 连接 GitHub

1. 登录 Cloudflare 控制台：https://dash.cloudflare.com
2. 左侧菜单点击 "Workers & Pages"
3. 点击 "Create" 按钮
4. 选择 "Pages" 标签页
5. 点击 "Connect to Git"
6. 授权 Cloudflare 访问你的 GitHub 账号
7. 选择刚才创建的仓库（chinese-food-recipes）
8. 配置构建设置：
   - Framework preset: 选择 Astro
   - Build command: npm run build
   - Build output directory: dist
9. 点击 "Save and Deploy"

等待 1-2 分钟构建完成，你就会获得一个类似 chinese-food-recipes.pages.dev 的免费域名。

### 步骤 5：后续更新（自动部署）

以后每次修改代码，只需要：

```shell
git add .
git commit -m "新增麻婆豆腐食谱"
git push
```

Cloudflare 会自动检测到 GitHub 的推送，自动重新构建和部署，全程无需手动操作。

## 三、方式二：Wrangler CLI 手动部署（适合 Workers 项目）

你现有的 astro-blog-starter-template 就是用这种方式部署的。适合需要服务端逻辑（SSR）的场景。

### 步骤 1：安装 Wrangler CLI

```shell
npm install -g wrangler
```

### 步骤 2：登录 Cloudflare

```shell
wrangler login
```

会自动打开浏览器，登录你的 Cloudflare 账号并授权。

### 步骤 3：初始化项目（如果是新项目）

```shell
# 创建新的 Workers 项目
wrangler init my-website

# 或者进入已有项目目录
cd your-existing-project
```

### 步骤 4：本地开发和预览

```shell
# 本地开发（热更新）
wrangler dev

# 使用远程资源（如 KV、D1 数据库）进行开发
wrangler dev --remote
```

浏览器打开 http://localhost:8787 即可预览。

### 步骤 5：部署到线上

```shell
# 部署到生产环境
wrangler deploy

# 部署到预览环境（测试用）
wrangler deploy --env preview
```

部署成功后，会输出你的网站地址，例如：
https://astro-blog-starter-template.lingajing2.workers.dev

### 步骤 6：查看线上日志

```shell
# 实时查看线上日志
wrangler tail
```

## 四、Astro 项目关键配置文件

### wrangler.toml（Workers 部署必需）

```toml
name = "astro-blog-starter-template"
main = "dist/_worker.js"
compatibility_date = "2024-01-01"

[site]
bucket = "./dist"
```

### astro.config.mjs（Astro 配置）

```javascript
import { defineConfig } from 'astro/config';
import cloudflare from '@astrojs/cloudflare';

export default defineConfig({
  output: 'server',  // 或 'static' 如果是纯静态站
  adapter: cloudflare(),
  site: 'https://your-domain.com',
});
```

### package.json 关键脚本

```json
{
  "scripts": {
    "dev": "astro dev",
    "build": "astro build",
    "preview": "wrangler dev",
    "deploy": "astro build && wrangler deploy"
  }
}
```

## 五、绑定自定义域名

1. 在 Cloudflare Pages/Workers 项目页面，点击 "Custom domains"
2. 点击 "Set up a domain"
3. 输入你在 spaceship.com 购买的域名
4. Cloudflare 会提示你修改 DNS 设置

如果域名不在 Cloudflare 管理：
- 去 spaceship.com 的域名管理页面
- 将 Nameservers 修改为 Cloudflare 提供的两个地址
- 等待 DNS 生效（通常几分钟到 24 小时）

如果域名已经转入 Cloudflare：
- 直接在 DNS 设置里添加 CNAME 记录指向你的 Pages 项目即可
- 基本是秒生效

## 六、日常开发工作流总结

```
编写/修改内容（Markdown 文件）
    ↓
本地预览（npm run dev）
    ↓
确认无误后提交代码（git add + commit + push）
    ↓
Cloudflare 自动构建部署（Pages 方式）
或手动执行 wrangler deploy（Workers 方式）
    ↓
网站更新上线
```

## 七、两种部署方式对比

| 对比项 | Cloudflare Pages | Cloudflare Workers |
|--------|-----------------|-------------------|
| 部署方式 | 连接 GitHub，自动部署 | 手动 wrangler deploy |
| 适用场景 | 静态站、博客、食谱网站 | 需要服务端逻辑、API |
| 构建 | Cloudflare 云端构建 | 本地构建后上传 |
| 预览环境 | 每个 PR 自动生成预览链接 | 需要手动配置 |
| 免费额度 | 每月 500 次构建 | 每天 10 万次请求 |
| 推荐程度 | ⭐⭐⭐⭐⭐ 强烈推荐 | ⭐⭐⭐ 进阶使用 |

**建议：** 做食谱网站用 Cloudflare Pages 即可，简单省心，推代码就自动上线。

## 八、常见问题

**Q: 部署失败怎么办？**
A: 去 Cloudflare Pages 项目页面查看构建日志，通常是 Node.js 版本不对或者依赖安装失败。可以在 Settings → Environment Variables 里设置 NODE_VERSION 为 18。

**Q: 网站打不开显示 522 错误？**
A: 通常是自定义域名的 DNS 还没生效，或者没有正确配置 CNAME 记录。等几分钟再试。

**Q: 免费额度够用吗？**
A: 对于个人博客/食谱网站完全够用。Pages 每月 500 次构建（每天更新一篇也才 30 次），Workers 每天 10 万次请求（日均 UV 几千完全没问题）。

**Q: 国内访问速度怎么样？**
A: Cloudflare 在全球有 300+ 节点，国内用户访问速度取决于运营商线路。如果觉得慢，可以后续配置 Cloudflare 优选 IP 来优化。

---

教程版本：v1.0 | 更新日期：2025-05
