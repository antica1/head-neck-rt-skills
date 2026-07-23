# 头颈肿瘤放疗 AI 靶区规划系统——安装指南

> 上海交通大学医学院附属第九人民医院 · 口腔颌面头颈肿瘤科放疗组
> **12 个独立放疗靶区 Skill** | GitHub 开源 | 一行命令安装 | v1.4.0

---

## 快速开始

### 1. 下载 Hermes 桌面版
👉 https://hermes-agent.nousresearch.com（Windows / Mac 均可）

### 2. 配置 AI 模型
注册 DeepSeek（platform.deepseek.com）→ 填入 Hermes 设置

### 3. 安装全部 Skill
```
hermes skills install head-neck-acc-rt-targets hncup-rt-targets orbital-tumor-rt-targets npc-rt-target-delineation head-neck-dvh-review reirradiation-plan-recommend port-oral-postop port-oropharynx-postop oropharynx-definitive-rt neoadjuvant-deescalation larynx-hypopharynx-postop larynx-hypopharynx-definitive
```

---

## 12 个 Skill 一览

### 🆕 口腔口咽 — 全新模块化

| Skill | 覆盖内容 |
|-------|---------|
| **口腔癌术后 PORT** | 舌/口底/牙龈/颊/硬腭/RMT/唇——IX/VIII过站 + 口底铁律 + 颈清逆流 + 皮瓣 |
| **口咽癌术后 PORT** | 扁桃体/舌根/软腭/咽侧壁——TORS + RP双侧必照 + p16分层 |
| **口咽癌根治性 RT** | 非手术——GTV+SIB(70/63/56) + 诱导化疗后 + HPV+ |
| **化免降级（共享模块）** | pCR/MPR——PORT降级 + 根治性RT降级 + SBRT增强（替雷利珠+白紫+顺铂） |

### 🆕 喉/下咽 — 全新模块化

| Skill | 覆盖内容 |
|-------|---------|
| **喉/下咽术后 PORT** | 全喉/部分喉——Stoma全层 + 咽重建 + VI区 + RP + 软骨全层 |
| **喉/下咽根治性 RT** | 保声——SIB(70/63/56) + 内镜GTV + DAHANCA 5mm |

### 特色肿瘤

| Skill | 覆盖内容 |
|-------|---------|
| **腺样囊性癌 (ACC) v1.4.0** | 🆕 三叉神经V2/V3三级追踪（命名→全海绵窦 / 小PNI→海绵窦下界 / 无PNI→颅底）· 面神经垂直段分层管理 · 实体型颈管理（不受口裂限制）· 鼻咽近中线双侧V2通路 |
| **鼻咽癌 (NPC)** | GTV 0mm逐级5mm · 岩尖+卵圆孔双侧（九院）· III区前界=胸锁乳突肌后缘 · 3100例转移率数据 · Lancet 2025 + IG-2024 |
| **眼眶肿瘤** | 间室放疗（门+隔壁）· VIII→IX→IIa淋巴级联 · 骨侵犯→66Gy · 4Gy/2fx超低剂量MALT · 眼前庭共管 |
| **原发不明转移癌 (HNCUP)** | 两阶段NPC筛查 · 选择性黏膜（4跨中线结构）· 同侧颈单照 · 颈清后逆流规则 |

### 质控与特殊场景

| Skill | 覆盖内容 |
|-------|---------|
| **DVH 计划审核** | 双轨制（物理师筛子+医生裁决）· QUANTEC四维批判 · 完整SBRT量表(Timmerman 2022) |
| **再程放疗** | Quad-Shot(JAMA 2026)+IO · 累积BED计算 · IO增敏SER · SBRT补量 |

---

## ✨ 核心亮点

- 🔴 **铁律清单**——每个 Skill 开头列出 8-14 条不容违反的硬规则，模型注意力焦点锚定
- 🔗 **技能自动联动**——眼眶 ACC 自动加载 ACC Skill，HNCUP 自动加载 NPC Skill
- 📋 **前置核查清单**——靶区生成前逐条走完 22 项检查，不可遗漏
- 🏥 **全部九院经验编码**——口底铁律、间室放疗、逆流规则、四级加量指征……手术不易切净区自动标记
- 📝 **可直接粘贴入病历**——每份报告附"靶区规划摘要"模板

---

## 获取帮助

- GitHub: https://github.com/antica1
- 全部开源，欢迎提建议、报告问题
