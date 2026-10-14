# 放疗文献与自媒体检索方法论

> 补充于 2026-07-13 DVH v1.2.0 会话。记录 PubMed/YouTube/国内医学媒体检索的可行性与技术路线。

---

## 一、PubMed 文献检索（主力）

### 可用性
✅ 完全可用。NCBI E-utilities API 免费、无需 key、速率限制 3 次/秒。

### 最佳实践
- 使用 `urllib.request`（非终端 curl）——URL 过长时 curl 在 Windows git-bash 中易超时
- 三路并行检索：头颈核心 / 新技术-头颈 / 特别关注
- 每路 `retmax=10-15`，控制总量在 15-20 篇
- 请求之间必须 `sleep(0.5)` 遵守限速

### 搜索词设计原则
- 全部三路需加头颈限定（`head and neck`/`nasopharyngeal`/`oral`/`oropharyngeal`/`laryngeal`）
- 不加头颈限定 → 大量噪声（如 "adaptive" 匹配到神经科学、妇科等）
- "新技术" 路需 AND 头颈限定词，否则命中 300+ 篇但几乎全不相关
- 瘤种覆盖：鳞癌 + 唾液腺癌 + ACC + 肉瘤 + 甲状腺癌

### 数据结构
- esearch → JSON (`retmode=json`)，取 `esearchresult.idlist`
- efetch → XML (`retmode=xml`)，解析 `PubmedArticle > ArticleTitle, Author, Abstract, Journal, PubDate, ArticleId[@IdType="doi"]`

---

## 二、YouTube 放疗内容检索（高价值补充）

### 可用性
✅ 可检索。返回 20 条/搜索，不需要 API key。翻墙后可用。

### 检索参数
- `&sp=CAISAhAB` 筛选"本周上传"
- 正则提取：`videoId` 从 `/watch?v=` 模式，`title` 从 JSON 内嵌

### 2026-07-13 已验证的直链视频

| 视频 | 链接 | 来源 |
|------|------|------|
| AHNS Virtual Tumor Board - Salivary Cancer | https://youtube.com/watch?v=iPdtRokL5Lo | AHNS |
| ASCO 2026 HNC & Sarcoma Highlights | https://youtube.com/watch?v=52K5bMbriZk | ASCO |
| ASCO Guidelines: Deintensification in p16+ OPC | https://youtube.com/watch?v=e7PZCUNkRo0 | ASCO |
| ACC - Perineural Spread, Histology, Treatment | https://youtube.com/watch?v=ZSB0_DCJ4GE | — |
| Advances in RadOnc: Proton & Photon 2026 | https://youtube.com/watch?v=_uq32GZfnIk | — |
| ESTRO Webinars: Plan Exploration | https://youtube.com/watch?v=GufQbvjvjx4 | ESTRO |
| Best of ASTRO Gulf 2026: Head & Neck | https://youtube.com/watch?v=g9lU_pK7WmE | ASTRO |
| Deintensification for HPV+ HNC | https://youtube.com/watch?v=_VQ9pfWb9fM | RadOnc Podcast |
| Proton As De-Intensification for HPV+ HNC | https://youtube.com/watch?v=Sz29qE9lJDw | — |
| Proton Therapy in Skull Base Malignancies | https://youtube.com/watch?v=xVnIcq9jrRk | — |

### 关键频道
- **ASTRO** / **ESTRO** 官方 — 年会回放、Webinar
- **AHNS** — Virtual Tumor Board
- **ACCRF** — ACC 患者教育
- **Red Journal Podcast** — NPC QA、降级讨论
- **UCSF Head and Neck** — ACC 诊疗经历

---

## 三、欧美放疗门户/博客 —— 基本不可用

| 平台 | 状态 | 原因 |
|------|------|------|
| Twitter/X (#RadOnc, #HNCsm) | ❌ JS 渲染 → curl 空白 | 需要浏览器自动化 |
| MDLinx / Healio / OncLive 等 | ❌ 403 Cloudflare | 反爬 |
| Medscape / theMednet | ❌ 登录墙 | — |
| Podcast (音频) | ⚠️ 不可检索文字 | 多数有 YouTube 回放 |

---

## 四、国内医学媒体 —— 基本不可检索

| 平台 | 状态 | 原因 |
|------|------|------|
| 微信公众号（肿瘤时讯等） | ❌ 完全不可检索 | 微信生态封闭 |
| 肿瘤瞭望 (ioncol.com) | ⚠️ 首页可达，JS 渲染 | 需浏览器自动化 |
| 丁香园 / 医脉通 | ⚠️ 部分可达 | 同上 |
| Google/Bing 中文搜索 | ⚠️ 极少结果 | 国内内容未被索引 |

### 唯一可行方案
用户手动分享文章链接 → 代理读取公开网页版。

---

## 五、每周简报 cron 配置

- **Job ID**: `607d352b2b2f`
- **调度**: `0 20 * * 1`（周一晚 8 点）
- **三路 PubMed**: 头颈核心(10篇/14天) / 新技术(10篇/14天) / 特别关注(10篇/30天)
- **四路 YouTube**: ASTRO/ESTRO + AHNS + ACCRF + NPC/降级
- **输出**: ⭐⭐⭐必读 / ⭐⭐浏览 / ⭐知道即可 三档
- **翻译**: 150-300 字中文摘要，禁用 AI 套话
- **总量**: ≤20 篇/次

### 已知问题
- `action='run'` 手动触发后 deliver="origin" 不回传 → 需在主对话重跑
- 定时调度回传待 7/20 首次验证
- curl 长 URL 超时 → 用 Python urllib.request

---

## 六、推荐理由撰写关联方向

1. 间室放疗（颅底/眶/术后瘤床）
2. 淋巴逆流（颈清后 VIII/IX/X 过站）
3. ACC 术后放疗（面神经茎乳孔）
4. NPC 靶区（岩尖+卵圆孔、咽后内侧组）
5. HNCUP（真性 CUP、EBV+LN、选择性黏膜）
6. 再程放疗（Quad-Shot+IO、累积 BED）
7. 术后 PORT 降级（化免后 pCR/MPR 分层）
8. DVH 审核（QUANTEC 四维批判）
