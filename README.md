# 头颈肿瘤放疗 AI 靶区规划系统——安装指南

> 上海交通大学医学院附属第九人民医院 · 口腔颌面头颈肿瘤科放疗组
> **12 个放疗靶区勾画 Skill** | GitHub 开源 | 一行命令安装

---

## 快速开始

### 1. 下载 Hermes 桌面版
👉 https://hermes-agent.nousresearch.com（Windows / Mac 均可）

### 2. 配置 AI 模型
注册 DeepSeek（platform.deepseek.com）→ 填入 Hermes 设置

### 3. 安装全部 12 个 Skill
```
hermes skills install head-neck-acc-rt-targets hncup-rt-targets orbital-tumor-rt-targets npc-rt-target-delineation head-neck-dvh-review reirradiation-plan-recommend oral-oropharynx-postop-rt-targets laryngeal-hypopharyngeal-rt-targets port-oral-postop port-oropharynx-postop oropharynx-definitive-rt neoadjuvant-deescalation larynx-hypopharynx-postop larynx-hypopharynx-definitive
```

---

## 12 个 Skill 一览

### 🆕 v3.0 全新模块化（口腔口咽）

| Skill | 内容 |
|-------|------|
| **口腔癌术后 PORT** | 舌/口底/牙龈/颊/硬腭/RMT/唇 — IX/VIII + 口底铁律 |
| **口咽癌术后 PORT** | 扁桃体/舌根/软腭/咽侧壁 — TORS + RP |
| **口咽癌根治性 RT** | 非手术 — GTV+SIB(70/63/56) + 诱导化疗后 + HPV+ |
| **化免降级（共享）** | pCR/MPR — PORT降级 + 根治性RT降级 + SBRT增强 |

### 🆕 v2.0 全新模块化（喉/下咽）

| Skill | 内容 |
|-------|------|
| **喉/下咽术后 PORT** | 全喉/部分喉 — Stoma + 咽重建 + VI区 + RP + 软骨全层 |
| **喉/下咽根治性 RT** | 保声 — SIB(70/63/56) + 内镜GTV + DAHANCA 5mm |

### 其余 6 个 Skill

| Skill | 内容 |
|-------|------|
| 腺样囊性癌 (ACC) | 面神经径路、颅底孔道追踪 |
| 原发不明转移癌 | 选择性黏膜、EBV/HPV分层、颈清后逆流 |
| 眼眶肿瘤 | 间室放疗、眼前庭共管 |
| 鼻咽癌 (NPC) | GTV 0mm逐级5mm、岩尖+卵圆孔双侧 |
| 再程放疗 | Quad-Shot+IO、累积BED、SER增敏 |
| DVH 计划审核 | 双轨制——物理师筛子+医生裁决 |

---

## 获取帮助

- GitHub: https://github.com/antica1
- 全部开源，欢迎提建议、报告问题
