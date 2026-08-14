# 头颈肿瘤放疗 AI 靶区规划系统——安装指南

> 上海交通大学医学院附属第九人民医院 · 口腔颌面头颈肿瘤科放疗中心
> **16 个放疗靶区 Skill** | GitHub 开源 | 一行命令安装 | CC BY-NC-SA 4.0

---

## 快速开始（三步）

### 第一步：下载 Hermes 桌面版（一次性）

👉 **https://hermes-agent.nousresearch.com**（Windows / Mac 均可）

1. 浏览器打开上方链接
2. 点击 **Download for Windows**（或 Mac）
3. 双击安装包 → 一路"下一步"→ 完成
4. 桌面出现 Hermes 图标 → 双击打开

---

### 第二步：配置 AI 模型（一次性）

Hermes 打开后，点击左下角 **⚙️ 设置** → 填入：

| 设置项 | 填入内容 |
|--------|---------|
| Provider | `deepseek` |
| Model | `deepseek-v4-pro` |
| API Key | 你的 DeepSeek API key（在 https://platform.deepseek.com 注册免费获取） |

> 也支持 Kimi、GLM 等其他模型。注册 DeepSeek 只需手机号，新用户送免费额度。

---

### 第三步：安装全部 Skill（一行命令）

在 Hermes 底部的输入框里，粘贴这一行 → 回车：

```
hermes skills install head-neck-rt-skills
```

或手动逐个安装（16 个独立仓库）：

```
hermes skills install adenoid-cystic-carcinoma-rt-targets
hermes skills install head-neck-dvh-plan-review
hermes skills install head-neck-lymphoma-rt-targets
hermes skills install head-neck-sarcoma-rt-targets
hermes skills install hncup-rt-targets
hermes skills install hypopharynx-rt-targets
hermes skills install larynx-rt-targets
hermes skills install neoadjuvant-deescalation
hermes skills install npc-rt-target-delineation
hermes skills install orbital-tumor-rt-targets
hermes skills install oropharynx-definitive-rt
hermes skills install port-oral-postop
hermes skills install port-oropharynx-postop
hermes skills install reirradiation-plan-recommend
hermes skills install salivary-gland-rt-targets
hermes skills install sinonasal-rt-targets
```

> 如遇个别 Skill 安装失败，可单独重试：`hermes skills install <skill名>`

---

## Skill 一览

### 特色肿瘤

| Skill | 版本 | 覆盖内容 |
|-------|:--:|---------|
| **腺样囊性癌 (ACC)** | v1.6.0 | V2/V3 三级神经追踪 + 面神经垂直段 + 实体型颈管理 + 鼻腔鼻窦 ACC + CAP 化疗 + 骨寡转移 SBRT |
| **鼻咽癌 (NPC)** | v1.3.0 | GTV 0mm 逐级 5mm + 岩尖卵圆孔双侧（九院）+ Lancet 2025 |
| **眼眶肿瘤** | v1.1.0 | 间室放疗（门+隔壁）+ VIII→IX→IIa 淋巴级联 + 眼前庭共管 |
| **原发不明转移癌 (HNCUP)** | v1.0.0 | 选择性黏膜（4 跨中线结构）+ EBV/HPV 分层 + 颈清后逆流 |
| **唾液腺癌** | v1.2.0 | 腮腺/颌下腺/舌下腺/副腮腺 + 非标准 PORT + RP 规则 + 面神经→内听道 |
| **鼻腔鼻窦癌** | v1.4.1 | 上颌窦/筛窦/蝶窦 + 视路保护 + SNUC/嗅母/黑色素瘤 + SMARCA4/INI1 + ICAR 2024 颈部数据 |
| **头颈淋巴瘤 (RT)** | v1.1.0 | ISRT/INRT 框架 + 亚型剂量 + 颈部解剖 + OAR（含原发骨淋巴瘤） |
| **头颈肉瘤（软组织+骨）🆕** | v1.1.0 | 软组织肉瘤+骨肉瘤（颌骨重点）+ HYPORT 术前大分割 + NCT03539172 艾坦同步放疗 + SBRT 转移灶 |

### 质控与特殊场景

| Skill | 版本 | 覆盖内容 |
|-------|:--:|---------|
| **DVH 计划审核** | v1.3.0 | 双轨制 + QUANTEC 四维批判 + 唾液腺剂量-效应数据 |
| **再程放疗** | v1.2.0 | Quad-Shot(JAMA 2026)+IO + 累积 BED + SBRT 补量 + 骨寡转移 SBRT |

### 🆕 口腔口咽 — 模块化

| Skill | 覆盖内容 |
|-------|---------|
| **口腔癌术后 PORT** | 舌/口底/牙龈/颊/硬腭/RMT/唇——IX/VIII过站 + 口底铁律 + 颈清逆流 + 皮瓣 |
| **口咽癌术后 PORT** | 扁桃体/舌根/软腭/咽侧壁——TORS + RP双侧必照 + p16分层 |
| **口咽癌根治性 RT** | 非手术——GTV+SIB(70/63/56) + 诱导化疗后 + HPV+ |
| **化免降级（共享模块）** | pCR/MPR——PORT降级 + 根治性RT降级 + SBRT增强（替雷利珠+白紫+顺铂） |

### 🆕 喉/下咽 — 按部位模块化（2026-08 重构）

| Skill | 覆盖内容 |
|-------|---------|
| **喉癌全流程 (larynx-rt-targets)** | 根治+PORT 自包含——声门保声 SIB + Stoma 全层 + VI区 + 软骨全层 + 降级（降范围优先） |
| **下咽癌全流程 (hypopharynx-rt-targets)** | 根治+PORT 自包含——梨状窝/环后/咽后壁 + RP上界C1 + VI触发 + 咽重建 + 降级（降剂量优先） |

---

## ✨ 核心亮点

- 🔴 **铁律清单**——每个 Skill 开头列出 8-14 条不容违反的硬规则，模型注意力焦点锚定
- 🔗 **技能自动联动**——眼眶 ACC 自动加载 ACC Skill，HNCUP 自动加载 NPC Skill
- 📋 **前置核查清单**——靶区生成前逐条走完 22 项检查，不可遗漏
- 🏥 **全部九院经验编码**——口底铁律、间室放疗、逆流规则、四级加量指征……手术不易切净区自动标记
- 📝 **可直接粘贴入病历**——每份报告附"靶区规划摘要"模板
- 💻 **双平台兼容**——Claude Code 和 Hermes 均可加载

---

## 开始使用

在 Hermes 聊天框里，直接输入患者的病史、手术记录、病理报告，AI 会自动：

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
A: Hermes 是桌面应用，数据存储在本地电脑，不上传云端。

**Q: 我是 Mac 用户？**
A: 同样支持。下载 Mac 版 Hermes，其余步骤完全相同。

**Q: 不会打字，能语音输入吗？**
A: 能。Hermes 右上角麦克风按钮——按下说话，自动用 Whisper 转成文字。

**Q: 在哪里看更新？**
A: GitHub 关注 `antica1`——每次更新自动推送。Hermes 内运行 `hermes skills update` 即可更新。

---

## 获取帮助

- 总入口：https://github.com/antica1/head-neck-rt-skills
- 16 个 Skill 仓库全部开源——欢迎提建议、报告问题、贡献靶区经验（shared-knowledge 为私有仓库，不公开）
- 授权：CC BY-NC-SA 4.0（署名-非商业-相同方式共享）

**Q: 如何引用？**
A: 引用 CITATION.cff。朱国培, 上海九院放疗中心. 头颈肿瘤放疗靶区勾画 Skill 系列 [OL]. GitHub: antica1, 2026.
