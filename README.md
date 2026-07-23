# 头颈肿瘤放疗 AI 靶区规划系统——安装指南

> 上海交通大学医学院附属第九人民医院 · 口腔颌面头颈肿瘤科放疗组
> **10 个放疗靶区勾画 Skill** | GitHub 开源 | 一行命令安装

---

## 一、你需要什么？

一台能上网的电脑（Windows / Mac 均可）。**不需要懂编程**——全程复制粘贴，5 分钟完成。

---

## 二、第一步：安装 Hermes 桌面版（一次性）

1. 浏览器打开：https://hermes-agent.nousresearch.com
2. 点击 **Download for Windows**（或 Mac）
3. 双击安装包 → 一路"下一步"→ 完成
4. 桌面出现 Hermes 图标 → 双击打开

---

## 三、第二步：配置 AI 模型（一次性）

Hermes 打开后，点击左下角 **⚙️ 设置** → 填入：

| 设置项 | 填入内容 |
|--------|---------|
| Provider | `deepseek` |
| Model | `deepseek-v4-pro` |
| API Key | 你的 DeepSeek API key（在 https://platform.deepseek.com 注册免费获取） |

> 也支持 Kimi、GLM 等其他模型。注册 DeepSeek 只需手机号，新用户送免费额度。

---

## 四、第三步：安装十大放疗 Skill（一行命令）

在 Hermes 底部的输入框里，粘贴这一行 → 回车：

```
hermes skills install head-neck-acc-rt-targets hncup-rt-targets orbital-tumor-rt-targets npc-rt-target-delineation head-neck-dvh-review reirradiation-plan-recommend oral-oropharynx-postop-rt-targets laryngeal-hypopharyngeal-rt-targets port-oral-postop port-oropharynx-postop oropharynx-definitive-rt neoadjuvant-deescalation
```

看到 ✅ 即安装成功。

---

## 五、开始使用

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

## 10 个 Skill 涵盖范围

### v3.0.0 新增：口腔口咽癌拆分为三大模块

> ⚠️ 原"口腔口咽癌术后靶区"（v1.2.0，1100行）已拆分为 3 个自包含模块——每个病例只需加载对应的一个。

| Skill | 内容 | v3.0 状态 |
|-------|------|:--:|
| **口腔癌术后 PORT** | 舌/口底/牙龈/颊/硬腭/RMT/唇——亚部位 CTV + IX/VIII + 口底铁律 + 皮瓣 + PNI | 🆕 |
| **口咽癌术后 PORT** | 扁桃体/舌根/软腭/咽侧壁——TORS + RP + 双侧颈 | 🆕 |
| **口咽癌根治性 RT** | 非手术口咽癌——GTV 勾画 + SIB + 诱导化疗后处理 + HPV+ 分层 | 🆕 |
| **化免降级（共享）** | pCR/MPR/non-MPR 分层——术后 PORT 降级 + 根治性 RT 降级 + SBRT 增强 | 🆕 |

### 其余 6 个 Skill

| Skill | 内容 |
|-------|------|
| 腺样囊性癌 (ACC) | 面神经径路——垂直段/水平段、颅底孔道追踪 |
| 原发不明颈部转移癌 (HNCUP) | 选择性黏膜照射、EBV/HPV 分层、颈清后逆流 |
| 眼眶肿瘤 | 间室放疗（门和隔壁比喻）、眼前庭共管、VIII/IX 过站 |
| 鼻咽癌 (NPC) | GTV 0mm 逐级 5mm、岩尖+卵圆孔双侧 |
| 喉癌/下咽癌 | 软骨侵犯、Stoma、RP/Ⅵ区、失败模式对照 |
| 再程放疗 | Quad-Shot+IO、累积 BED 计算、SBRT+SER 增敏 |
| DVH 计划审核 | 双轨制——物理师筛子+医生裁决、降级 PORT 专属 OAR |

---

## 常见问题

**Q: 免费吗？**
A: Skill 本身完全开源免费。AI 模型按用量收费——DeepSeek 新用户送免费额度，日常使用每月约 10-30 元。

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

- GitHub Issues: https://github.com/antica1
- 十个 Skill 仓库全部开源，欢迎提建议、报告问题、贡献靶区经验
