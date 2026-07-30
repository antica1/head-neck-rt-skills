# 头颈肿瘤放疗 AI 靶区规划系统 —— 安装与使用指南

> 上海交通大学医学院附属第九人民医院 · 口腔颌面头颈肿瘤科放疗中心
> **18 个放疗靶区 Skill** | GitHub 开源 | CC BY-NC-SA 4.0 | v2.2.0

---

## 快速开始

### 平台选择

本 Skill 系列同时支持 **Claude Code** 和 **Hermes Agent** 双平台：

| 平台 | 安装方式 | 适用场景 |
|------|---------|---------|
| **Claude Code** | `git clone` 聚合仓库 → 本地目录加载 | 已有 Claude 桌面版 / VS Code 的用户 |
| **Hermes Agent** | `hermes skills install <repo>` 一行安装 | 独立桌面应用，支持语音输入 |

---

## 方式 A：Claude Code 安装

```bash
# 克隆总仓库（包含全部 18 个 Skill）
git clone https://github.com/antica1/head-neck-rt-skills.git

# 在 Claude Code 中添加 skills/ 目录路径即可加载全部 Skill
```

Claude Code 通过语义匹配自动选择相关 Skill——无需手动指定触发词。

## 方式 B：Hermes Agent 安装

### 1. 下载 Hermes 桌面版
👉 https://hermes-agent.nousresearch.com（Windows / Mac 均可）

### 2. 配置 AI 模型

Hermes 打开后，点击左下角 **⚙️ 设置** → 填入：

| 设置项 | 填入内容 |
|--------|---------|
| Provider | `deepseek` |
| Model | `deepseek-v4-pro` |
| API Key | 你的 DeepSeek API key（在 https://platform.deepseek.com 注册免费获取） |

> 也支持 Kimi、GLM 等其他模型。注册 DeepSeek 只需手机号，新用户送免费额度。

### 3. 安装全部 Skill

在 Hermes 底部的输入框里，粘贴这一行 → 回车：

```
hermes skills install head-neck-acc-rt-targets HNCUP-rt-targets orbital-tumor-rt-targets npc-rt-target-delineation head-neck-dvh-review head-neck-reirradiation oral-oropharynx-postop-rt-targets laryngeal-hypopharyngeal-rt-targets salivary-gland-rt-targets sinonasal-rt-targets port-oral-postop port-oropharynx-postop oropharynx-definitive-rt neoadjuvant-deescalation larynx-hypopharynx-postop larynx-hypopharynx-definitive shared-knowledge
```

Hermes 通过 `triggers_on` 触发词自动匹配加载——每个 Skill 均配置了中英文双触发词。

---

## 17 个 Skill 一览

### 口腔口咽 — 模块化

| Skill | 覆盖内容 |
|-------|---------|
| **口腔癌术后 PORT** | 舌/口底/牙龈/颊/硬腭/RMT/唇——IX/VIII过站 + 口底铁律 + 颈清逆流 + 皮瓣 |
| **口咽癌术后 PORT** | 扁桃体/舌根/软腭/咽侧壁——TORS + RP双侧必照 + p16分层 |
| **口咽癌根治性 RT** | 非手术——GTV+SIB(70/63/56) + 诱导化疗后 + HPV+ |
| **化免降级（共享模块）** | pCR/MPR——PORT降级 + 根治性RT降级 + SBRT增强 |

### 喉/下咽 — 模块化

| Skill | 覆盖内容 |
|-------|---------|
| **喉/下咽术后 PORT** | 全喉/部分喉——Stoma全层 + 咽重建 + VI区 + RP + 软骨全层 |
| **喉/下咽根治性 RT** | 保声——SIB(70/63/56) + 内镜GTV + DAHANCA 5mm |

### 特色肿瘤

| Skill | 覆盖内容 |
|-------|---------|
| **腺样囊性癌 (ACC)** | 三叉神经V2/V3三级追踪 · 面神经垂直段分层管理 · 实体型颈管理 · 鼻咽近中线双侧V2通路 |
| **鼻咽癌 (NPC)** | GTV 0mm逐级5mm · 岩尖+卵圆孔双侧 · 3100例转移率数据 · Lancet 2025 + IG-2024 |
| **眼眶肿瘤** | 间室放疗（门+隔壁）· VIII→IX→IIa淋巴级联 · 4Gy/2fx超低剂量MALT · 眼前庭共管 |
| **原发不明转移癌 (HNCUP)** | 两阶段NPC筛查 · 选择性黏膜（4跨中线结构）· 同侧颈单照 · 颈清后逆流规则 |
| **唾液腺癌** | 腮腺/颌下腺/舌下腺/副腮腺 + 非标准 PORT + RP 规则 + 面神经→内听道 |
| **鼻腔鼻窦癌** | 上颌窦/筛窦/蝶窦 + 视路保护 + SNUC/嗅母/黑色素瘤 + ICAR 2024 颈部数据 |

### 质控与特殊场景

| Skill | 覆盖内容 |
|-------|---------|
| **DVH 计划审核** | 双轨制（物理师筛子+医生裁决）· QUANTEC四维批判 · 完整SBRT量表 |
| **再程放疗** | Quad-Shot+IO · 累积BED计算 · IO增敏SER · SBRT补量 |
| **共享知识库** | 口底铁律 · 间室放疗 · 淋巴逆流规则——跨 Skill 通用原则 |

---

## ✨ 核心亮点

- 🔴 **铁律清单**——每个 Skill 开头列出 8-14 条不容违反的硬规则，模型注意力焦点锚定
- 🔗 **技能自动联动**——眼眶 ACC 自动加载 ACC Skill，HNCUP 自动加载 NPC Skill
- 📋 **前置核查清单**——靶区生成前逐条走完 22 项检查，不可遗漏
- 🏥 **全部九院经验编码**——口底铁律、间室放疗、逆流规则、四级加量指征
- 📝 **可直接粘贴入病历**——每份报告附"靶区规划摘要"模板
- 🤖 **Claude Code + Hermes 双平台兼容**——Claude Code 按语义匹配，Hermes 按触发词匹配

---

## 开始使用

在聊天框里直接输入患者的病史、手术记录、病理报告，AI 会自动：

1. ✅ 按 AJCC 第 9 版分期（含 DOI、软骨侵犯等新标准）
2. ✅ 分析是否需要 PORT、是否可降级
3. ✅ 给出靶区勾画方案（CTV 层级 + 剂量 + 豁免 + 加量区）
4. ✅ 输出可粘贴入病程录的靶区规划摘要
5. ✅ 标记手术不易切净区（茎乳孔、颅底、翼腭窝等）
6. ✅ 附完整推理链条（供低年资医生学习）

**示例输入**：
> 中年男性，右舌鳞癌，直径 2.5 cm，浸润深度 8 mm，无淋巴结转移，已行右舌扩大切除+右颈清扫，病理切缘 3 mm，PNI（-），LVI（-），无 ENE。请分析术后放疗策略。

---

## 常见问题

**Q: 免费吗？**
A: Skill 本身完全开源免费（CC BY-NC-SA 4.0）。AI 模型按用量收费——DeepSeek 新用户送免费额度，日常使用每月约 10-30 元。

**Q: 数据安全吗？**
A: Claude Code 和 Hermes 均为本地桌面应用，数据存储在本地电脑，不上传云端。

**Q: Mac/Linux 能用吗？**
A: 完全支持。Claude Code 通过 VS Code 或桌面版，Hermes 下载 Mac 版即可。

**Q: 如何获取更新？**
A: GitHub 关注 `antica1`——每次更新自动推送。Claude Code 用户 `git pull`，Hermes 用户运行 `hermes skills update`。

**Q: 如何引用？**
A: 引用 CITATION.cff。朱国培, 上海九院放疗中心. 头颈肿瘤放疗靶区勾画 Skill 系列 [OL]. GitHub: antica1, 2026.

---

## 获取帮助

- 总入口：https://github.com/antica1/head-neck-rt-skills
- 17 个 Skill 仓库全部开源——欢迎提建议、报告问题、贡献靶区经验
- 授权：CC BY-NC-SA 4.0（署名-非商业-相同方式共享）
