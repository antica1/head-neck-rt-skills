---
name: larynx-hypopharynx-postop
description: "Self-contained laryngeal/hypopharyngeal postoperative RT skill. Total/partial laryngectomy scenarios, stoma management, pharyngeal reconstruction, tracheostomy site, level VI, retropharyngeal nodes, cartilage full-thickness inclusion, and PORT dose strategy."
version: 1.1.0
author: Zhu Guopei / Shanghai Ninth People's Hospital
license: MIT
metadata:
  hermes:
    tags: [head-neck, radiotherapy, postoperative, PORT, larynx, hypopharynx]
    related_skills: [larynx-hypopharynx-definitive, neoadjuvant-deescalation]
    triggers_on: [喉癌术后, 下咽癌术后, 喉PORT, 喉术后放疗, 全喉切除, 部分喉切除, 喉癌PORT, 下咽PORT, 喉术后, larynx PORT, laryngectomy, pharyngectomy, 咽重建, stoma, 气管造口, 喉手术, larynx postop]
---

# 喉癌与下咽癌术后放疗（PORT）靶区勾画

> **自包含模块** —— 喉/下咽癌术后行 PORT 时加载。
> 若为根治性 RT（非手术），改用 `larynx-hypopharynx-definitive`。
> 若患者有化免新辅助史，额外加载 `neoadjuvant-deescalation`。
>
> 朱国培 · 上海交通大学医学院附属第九人民医院口腔颌面-头颈肿瘤科

---

## 🔑 铁律清单

| # | 铁律 | 触发条件 |
|---|------|---------|
| 1 | **Stoma 必照——全层（皮肤→气管黏膜）** | 全喉切除 PORT |
| 2 | **咽吻合口 CTV = 吻合线 + 头尾各 2cm** | 全喉+咽部分切除 |
| 3 | **气管造口旁 LN（Delphian 淋巴结区）必照** | 声门下侵犯或 T4 |
| 4 | **VI 区必照** | 声门下侵犯 ≥1cm 或 T4 或甲状腺侵犯 |
| 5 | **RP 区照** | 下咽癌（尤其梨状窝/咽后壁）、≥3 LN+ |
| 6 | **部分喉→残余喉结构照全量** | 声门上/环上部分喉切除 |
| 7 | **软骨受侵→全层软骨纳入 CTV** | 影像或病理提示软骨侵犯 |
| 8 | **术后不用 SIB——序贯为主** | 所有喉/下咽 PORT |
| 9 | **咽重建皮瓣→皮瓣体部降量(50-54Gy)，皮瓣下组织床照 60Gy** | 游离皮瓣/带蒂皮瓣重建 |
| 10 | **化免 pCR→降范围优先于降剂量** | 新辅助后 pCR |

---

## ⚠️ 影像+手术记录依赖声明

> **PORT 靶区定义依赖手术记录（术式+范围+重建方式）和病理报告。AI 无法读片——报告中边界须以"建议+依据+请确认"格式输出。** 若手术记录未提供具体切除范围→按标准术式默认处理，标注为推断。

---

## 一、术前评估——不可跳过的三件事

### 1.1 手术记录
- 术式类型：全喉 / 部分喉（声门上水平半喉 / 环上喉次全切除 / 垂直半喉）
- 切除范围：是否含舌骨、会厌谷、梨状窝壁、气管环
- 重建方式：直接缝合 / 游离空肠 / 前臂桡侧皮瓣 / 胸大肌肌皮瓣
- 颈部手术：单侧/双侧颈清、I-V 区清扫范围

### 1.2 病理报告
- 原发灶：切缘状态（声门上/声门下/环周/前连合）
- 颈部淋巴结：阳性数/总清扫数、ENE、最大径、受累站区
- 高危特征：PNI、LVI、软骨侵犯、甲状腺侵犯

### 1.3 影像
- 术前 MRI/CT 确认肿瘤原始范围
- 术后 CT 定位：术腔 + 皮瓣/重建物辨识

---

## 二、按术式确定靶区

### 2.1 全喉切除 ± 咽部分切除

| 靶区结构 | CTV 边界 | 剂量 |
|----------|---------|------|
| **Stoma** | 全层（皮肤→气管黏膜），气管造口周围 1-2cm，包括气管旁软组织 | 60 Gy |
| **咽吻合口** | 吻合线 + 头尾各 2cm，全层（黏膜→咽缩肌→椎前筋膜） | 60 Gy |
| **气管旁淋巴结区 (VI)** | 舌骨→胸骨上切迹，双侧气管食管沟 | 54 Gy（预防）/ 60 Gy（pT+ or ENE+）|
| **术腔** | 原发灶部位术床 + 1-2cm（按切缘状态调整） | 60 Gy |
| **舌根/会厌谷** | 若为声门上型或侵犯会厌→舌骨上会厌谷 | 54-60 Gy（按风险） |
| **气管造口旁 LN（Delphian）** | 环甲膜/第1-2气管环前方软组织 | 60 Gy |

### 2.2 部分喉切除

- **声门上水平半喉**：残余声门 CTV 包括整个声带水平（前连合→杓状软骨）；会厌谷→舌根交界区；同侧 II-III 区
- **环上喉次全切除（CHP/CHEP）**：环状软骨区→残余杓状软骨区；环甲膜+Delphian 区；同侧 II-III + VI
- **垂直半喉**：残余声带全层；前连合→对侧声带前部（近中线者→双侧前部）

### 2.3 咽重建的特殊处理

| 重建方式 | CTV 要点 |
|----------|---------|
| **直接缝合** | 吻合线头尾各 2cm |
| **游离空肠** | 整段空肠瓣纳入 CTV（再发风险沿系膜蔓延） |
| **前臂/股前外侧皮瓣** | 皮瓣-咽黏膜交界线 + 头尾各 2cm；皮瓣体部降量至 50-54 Gy |
| **胸大肌肌皮瓣** | 皮瓣-咽交界全层 + 血管蒂起始部（胸肩峰动脉周围） |

---

## 三、颈部淋巴结管理

### 3.1 颈部预防指征

| 临床场景 | 预防范围 |
|----------|---------|
| **声门型 T1-T2N0** | 不需颈部预防（除非病理升级） |
| **声门上型** | 双侧 II-III（T3-4→加 IV） |
| **声门下型** | 双侧 VI + 同侧 IV |
| **下咽癌（所有亚部位）** | 双侧 II-IV + 双侧 RP |
| **全喉+单侧颈清** | 对侧 II-III 50-54 Gy（原发中线者→对侧 II-IV） |
| **≥3 LN+ / ENE+** | 颈鞘至颅底 50-54 Gy |

### 3.2 RP 照射指征

| 指征 | 范围 |
|------|------|
| 下咽癌——咽后壁 / 梨状窝外侧壁 | 同侧 RP 必照（上界 C1） |
| 下咽癌——环后区 | MRI 阴性时可考虑豁免同侧 RP |
| ≥3 LN+ 或 ENE+ | 同侧 RP 外侧组 |
| 咽后壁原发（环后区外） | 双侧 RP |

---

## 四、切缘状态与 CTV 调整

| 切缘状态 | CTV 外放 | 剂量 |
|----------|---------|------|
| **阴性 ≥5mm** | 0mm（手术床本身范围） | 60 Gy（标准术床剂量） |
| **近切缘 1-4mm** | +3-5mm | 60-63 Gy（缩野补量） |
| **R1** | +5-10mm | 66 Gy |
| **R2** | +10-15mm | 66-70 Gy |
| **软骨侵犯** | 全层软骨 + 5mm | 60-66 Gy |
| **PNI（神经周围侵犯）** | 沿神经通路 + 5-8mm | 60-63 Gy |

---

## 五、剂量策略——术后不用 SIB

> **核心规则**：喉/下咽 PORT 一律序贯——不用 SIB。

| PTV 层级 | 剂量 | 分次 | 说明 |
|----------|------|------|------|
| **PTV-60（高危术床）** | 60 Gy | 30 fx | 术床+Stoma+吻合口+R1 补量区 |
| **PTV-54（预防区）** | 54 Gy | 30 fx | 未受累淋巴结站区 |
| **PTV-63（缩野补量）** | 63 Gy | 35 fx | R1 切缘缩野（序贯推量） |
| **PTV-66（加量）** | 66 Gy | 33-35 fx | R2 或 ENE+ 缩野 |

> **照射顺序**：先照 PTV-54 大野 → 30fx 后缩野至 PTV-60/63/66。

---

## 六、OAR 关键约束

| OAR | 约束值 | 优先级 |
|-----|--------|:------:|
| **脊髓 Dmax** | ≤ 45 Gy | 🔴 一票否决 |
| **脑干 Dmax** | ≤ 54 Gy | 🔴 一票否决 |
| **对侧腮腺 Dmean** | ≤ 26 Gy | 🟠 优先 |
| **患侧腮腺 Dmean** | ≤ 30 Gy | 🟡 |
| **下颌骨 Dmax** | ≤ 70 Gy | 🟡 |
| **咽缩肌 Dmean** | ≤ 50 Gy | 🟡 |
| **颈段食管 Dmax** | < 60 Gy（D1cc < 60 Gy，环周 360° 长度 <3cm）| 🟡 |
| **气管 V50** | < 50%（经验性约束，非 QUANTEC 级） | 🟡 |

---

## 七、化免新辅助后 PORT 降级

> 详见 `neoadjuvant-deescalation` Skill。
> 喉/下咽特有差异：
> - **喉癌 pCR** → 降范围优先（对侧颈/VI 可缩）
> - **下咽癌 pCR** → 降剂量优先（RP+VI 基线风险太高，不能缩野）

---

## 八、六步法（贴在 TPS 旁）

```
1. 读手术记录→确定术式+重建
2. 读病理→确定切缘+LN+高危特征
3. 定位 CT 辨识：Stoma / 吻合口 / 术腔 / 皮瓣 / 残余喉
4. Stoma 勾画：全层（皮肤→气管黏膜）→ PTV-60
5. 咽吻合口 + 头尾 2cm → PTV-60
6. 颈部：按手术 LN 结果确定预防范围 → PTV-54
```

---

## 九、失败模式对照

| 失败模式 | 原因 | 预防 |
|----------|------|------|
| **Stoma 复发** | Stoma 遗漏 / 未全层纳入 | ✅ Stoma 全层必照 |
| **咽吻合口复发** | CTV 外放不足 | ✅ 头尾各 2cm |
| **气管旁 LN 复发** | VI 区遗漏 | ✅ VI 区+Delphian 必照 |
| **RP 复发** | 下咽癌未照 RP | ✅ 下咽癌→RP |
| **皮瓣-咽交界复发** | 交界线遗漏 | ✅ 交界线全层+2cm |
| **对侧颈复发** | 中线原发未照对侧 | ✅ 中线→对侧 II-III |

---

## 参考文献

- NCCN Guidelines Version 2.2026 — Head and Neck Cancers
- CSCO 头颈部肿瘤诊疗指南 2026
- ICRU Report 83: Prescribing, Recording, and Reporting IMRT
- QUANTEC: Quantitative Analysis of Normal Tissue Effects in the Clinic (2010)
- DAHANCA guidelines for H&N target delineation
- Trotti A, et al. Radiother Oncol. 2003; 66(2): 219-226

---

> 朱国培 · 上海交通大学医学院附属第九人民医院口腔颌面-头颈肿瘤科放疗组
