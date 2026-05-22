# Cloudflare 网站开发与部署教程（完整版）

## 一、概述

Cloudflare 提供两种主要的网站托管方式：Cloudflare Pages（适合静态网站和前端框架）和 Cloudflare Workers（适合需要服务端逻辑的应用）。本教程以我们的中餐食谱项目为例，介绍如何在 Cloudflare 上开发和部署代码。

## 二、前置准备

1. 注册 Cloudflare 账号：https://dash.cloudflare.com/sign-up
2. 安装 Node.js（建议 v18+）
3. 安装 Wrangler CLI（Cloudflare 官方命令行工具）：

```bash
npm install -g wrangler
```

4. 登录 Wrangler：

```bash
wrangler login
```

## 三、方式一：Cloudflare Pages（推荐静态站点）

### 适用场景

- 博客、文档站、营销页面
- Astro / Next.js / Nuxt 等框架的静态导出
- 不需要复杂后端逻辑的网站

### 步骤 1：连接 GitHub 仓库

1. 登录 https://dash.cloudflare.com
2. 左侧菜单选择 "Workers & Pages"
3. 点击 "Create" → "Pages" → "Connect to Git"
4. 授权 GitHub，选择你的仓库（如 `ajing2/astro-blog-starter-template`）
5. 配置构建设置：
   - 框架预设：选择 "Astro"
   - 构建命令：`npm run build`
   - 构建输出目录：`dist`
6. 点击 "Save and Deploy"

### 步骤 2：自动部署

连接后，每次 push 到 main 分支会自动触发部署。Preview 部署会在 PR 创建时自动生成。

### 步骤 3：自定义域名

1. 在 Pages 项目设置中选择 "Custom domains"
2. 添加你购买的域名
3. 按提示配置 DNS 记录（如果域名在 Cloudflare 管理，会自动配置）

## 四、方式二：Cloudflare Workers（需要服务端逻辑）

### 适用场景

- 需要 SSR（服务端渲染）
- 需要 API 路由
- 需要边缘计算逻辑

### 步骤 1：项目初始化

```bash
# 如果是新项目
npm create cloudflare@latest my-app

# 如果是已有项目（如我们的 Astro 项目）
# 确保 wrangler.json 配置正确
```

### 步骤 2：配置 wrangler.json

```json
{
  "name": "chinese-food-recipes",
  "main": "./dist/_worker.js",
  "compatibility_date": "2025-01-01",
  "assets": {
    "directory": "./dist",
    "binding": "ASSETS"
  }
}
```

### 步骤 3：本地开发

```bash
# 启动本地开发服务器
npm run dev

# 使用 Wrangler 模拟 Workers 环境
wrangler dev
```

### 步骤 4：部署

```bash
# 构建项目
npm run build

# 部署到 Cloudflare Workers
wrangler deploy
```

### 步骤 5：查看日志

```bash
# 实时查看 Worker 日志
wrangler tail
```

## 五、我们项目的部署方式

我们的中餐食谱站使用 **Astro + Cloudflare Workers** 方式部署：

1. 代码仓库：https://github.com/ajing2/astro-blog-starter-template
2. 部署地址：astro-blog-starter-template.lingajing2.workers.dev
3. 部署命令：`npm run build && wrangler deploy`

### 日常开发流程

```bash
# 1. 拉取最新代码
git pull origin main

# 2. 安装依赖
npm install

# 3. 本地开发
npm run dev

# 4. 写完代码后构建测试
npm run build
npm run preview

# 5. 提交代码
git add .
git commit -m "feat: add new recipe - mapo tofu"
git push origin main

# 6. 部署到线上
npm run build && npm run deploy
```

## 六、常用命令速查

| 命令 | 作用 |
|------|------|
| `wrangler login` | 登录 Cloudflare 账号 |
| `wrangler dev` | 本地开发模式 |
| `wrangler deploy` | 部署到生产环境 |
| `wrangler tail` | 查看实时日志 |
| `wrangler pages deploy ./dist` | Pages 方式部署 |
| `wrangler secret put KEY` | 设置环境变量/密钥 |

## 七、注意事项

1. Workers 免费版每天有 10 万次请求限制，对于新站完全够用
2. Pages 免费版每月 500 次构建，自动部署很方便
3. 建议先用 Workers 方式部署（我们当前方案），等流量大了再考虑优化
4. 自定义域名需要先在 Cloudflare 管理 DNS，或者添加 CNAME 记录
