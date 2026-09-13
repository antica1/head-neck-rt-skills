# 头颈放疗靶区 Skill 完整索引

> 上海九院放疗中心 · 朱国培 | GitHub: antica1 | v2.5.0 | 2026-09-13
> 16 个公开 Skill · Claude Code & Hermes 双平台（shared-knowledge 已移至私有仓库，2026-08-11）

---

## 一、目录树

```
head-neck-rt-skills/
├── README.md                        # 双平台安装指南
├── CITATION.cff                     # 引用元数据
├── index.html                       # Web 入口页
├── SKILLS_INDEX.md                  # 本文件——完整索引
└── skills/
    │
    ├── neoadjuvant-deescalation/    # 化免新辅助降级（244 行）——被 11 个 Skill 引用
    │
    ├── oral-oropharynx-postop-rt-targets/  # ❌ 已删除（2026-08-14）——拆分为下方两个独立模块
    ├── port-oral-postop/                   # 口腔 PORT 自包含模块（890 行）——含口底铁律
    ├── port-oropharynx-postop/             # 口咽 PORT 自包含模块（209 行）
    │
    ├── oropharynx-definitive-rt/    # 口咽根治性 RT（303 行）
    │
    ├── larynx-rt-targets/          # 喉癌全流程（根治+PORT，415 行）——声门/声门上/声门下/跨声门、Stoma、VI区
    ├── hypopharynx-rt-targets/     # 下咽癌全流程（根治+PORT，406 行）——梨状窝/环后/咽后壁、RP上界C1、VI触发
    │   （2026-08-16 重构：原 laryngeal-hypopharyngeal-rt-targets + larynx-hypopharynx-postop + larynx-hypopharynx-definitive 三合一 → 精简为 2 个按部位模块）
    │
    ├── adenoid-cystic-carcinoma-rt-targets/    # ACC 腺样囊性癌（473 行）
    ├── hncup-rt-targets/            # 原发不明转移癌（541 行）
    ├── npc-rt-target-delineation/   # NPC 鼻咽癌（497 行）
    ├── orbital-tumor-rt-targets/    # 眼眶肿瘤-实体瘤（1001 行；淋巴瘤见 head-neck-lymphoma-rt-targets §九）
    ├── sinonasal-rt-targets/        # 鼻腔鼻窦癌（575 行）
    ├── salivary-gland-rt-targets/   # 唾液腺癌（831 行）
    ├── reirradiation-plan-recommend/     # 再程放疗（284 行）
    ├── head-neck-lymphoma-rt-targets/  # 头颈部淋巴瘤放疗（920 行）🆕
    ├── head-neck-sarcoma-rt-targets/   # 头颈肉瘤全流程（656 行）🆕——软组织肉瘤+骨肉瘤（颌骨）、HYPORT术前大分割、NCT03539172艾坦、SBRT转移灶
│
└── head-neck-dvh-plan-review/        # DVH 计划审核（257 行）
```

---

## 二、依赖关系图

```
    │
    ├── neoadjuvant-deescalation ──────────────────────────────────┐
    │   (当患者有新辅助史时加载)                                      │
    │                                                                │
    ├── oral-oropharynx-postop-rt-targets ──────────────────────────┤
    │   (❌ 已删除——拆分如下)                                          │
    ├── port-oral-postop               ← neoadjuvant-deescalation ──┤
    ├── port-oropharynx-postop         ← neoadjuvant-deescalation ──┤
    │                                                                │
    ├── oropharynx-definitive-rt        ← neoadjuvant-deescalation ─┤
    │                                                                │
    ├── larynx-rt-targets            ← neoadjuvant-deescalation ──┤
    ├── hypopharynx-rt-targets       ← neoadjuvant-deescalation ──┤
    │                                                                │
    ├── adenoid-cystic-carcinoma-rt-targets                                     │
    ├── hncup-rt-targets                ← npc-rt-target-delineation  │
    ├── npc-rt-target-delineation                                    │
    ├── orbital-tumor-rt-targets        ← adenoid-cystic-carcinoma-rt-targets   │
    ├── sinonasal-rt-targets                                         │
    ├── salivary-gland-rt-targets       ← adenoid-cystic-carcinoma-rt-targets   │
    ├── reirradiation-plan-recommend                                      │
    └── head-neck-dvh-plan-review                                         │
```

---

## 三、YAML Name ↔ 仓库名对照表

| 仓库名（目录） | YAML `name` | 行数 | 版本 |
|:---|---:|---:|:---:|
| neoadjuvant-deescalation | neoadjuvant-deescalation | 244 | 2.0.0 |
| ~~oral-oropharynx-postop-rt-targets~~ | ~~已删除~~ | — | — |
| port-oral-postop | port-oral-postop | 890 | 1.6.0 |
| port-oropharynx-postop | port-oropharynx-postop | 209 | 1.0.0 |
| oropharynx-definitive-rt | oropharynx-definitive-rt | 303 | 1.1.0 |
| larynx-rt-targets | larynx-rt-targets | 415 | 1.0.0 |
| hypopharynx-rt-targets | hypopharynx-rt-targets | 406 | 1.0.0 |
| adenoid-cystic-carcinoma-rt-targets | adenoid-cystic-carcinoma-rt-targets | 473 | 1.7.0 |
| hncup-rt-targets | hncup-rt-targets | 541 | 1.1.0 |
| npc-rt-target-delineation | npc-rt-target-delineation | 497 | 1.3.0 |
| orbital-tumor-rt-targets | orbital-tumor-rt-targets | 1001 | 1.1.1 |
| sinonasal-rt-targets | sinonasal-rt-targets | 575 | 1.5.0 |
| salivary-gland-rt-targets | salivary-gland-rt-targets | 831 | 1.3.0 |
| head-neck-lymphoma-rt-targets | head-neck-lymphoma-rt-targets | 920 | 1.2.0 |
| head-neck-sarcoma-rt-targets | head-neck-sarcoma-rt-targets | 656 | 1.1.0 |
| reirradiation-plan-recommend | reirradiation-plan-recommend | 284 | 1.3.0 |
| head-neck-dvh-plan-review | head-neck-dvh-plan-review | 257 | 1.3.0 |

> **注意**：2026-08 已完成目录名统一——全部 Skill 的主仓库目录名与 YAML `name` 一致（`hncup-rt-targets`、`adenoid-cystic-carcinoma-rt-targets`、`head-neck-dvh-plan-review`、`reirradiation-plan-recommend`）。旧目录名（`HNCUP-rt-targets`、`head-neck-acc-rt-targets`、`head-neck-dvh-review`、`head-neck-reirradiation`）与旧 YAML name（`cervical-cup-rt-targets`）均已废弃；GitHub 独立仓库若仍用旧名，靠 301 重定向兼容。

---

## 四、跨 Skill 自动联动

| 触发场景 | 自动加载链 |
|----------|-----------|
| "眼眶 ACC" / "泪腺 ACC" | orbital-tumor-rt-targets → adenoid-cystic-carcinoma-rt-targets |
| "腮腺 ACC" / "颌下腺 ACC" | salivary-gland-rt-targets → adenoid-cystic-carcinoma-rt-targets |
| "鼻咽部 ACC" | npc-rt-target-delineation → adenoid-cystic-carcinoma-rt-targets |
| "口腔癌术后 + 化免 pCR" | port-oral-postop → neoadjuvant-deescalation |
| "口咽癌术后 + 化免 MPR" | port-oropharynx-postop → neoadjuvant-deescalation |
| "下咽癌术后 + 化免 pCR" | hypopharynx-rt-targets → neoadjuvant-deescalation |
| "喉癌根治 + 化免 pCR" | larynx-rt-targets → neoadjuvant-deescalation |
| "口咽根治 SIB + 化免 pCR" | oropharynx-definitive-rt → neoadjuvant-deescalation |
| "CUP 颈部转移 + 怀疑 NPC" | hncup-rt-targets → npc-rt-target-delineation |
| "再程放疗 + 需 DVH 审核" | reirradiation-plan-recommend → head-neck-dvh-plan-review |
| "任何靶区生成 + 需 DVH 审核" | any-skill → head-neck-dvh-plan-review |

---

## 五、铁律清单覆盖

| Skill | 铁律条数 | 状态 |
|------|:---:|:---:|
| neoadjuvant-deescalation | ✅ 8 条 | 化免降级梯度规则 |
| port-oral-postop | ✅ 17 条 | 口腔 PORT 铁律（含下颌骨侵犯 pT4a 决策、下颌管径路） |
| port-oropharynx-postop | ✅ 8 条 | 口咽 PORT 铁律 |
| oropharynx-definitive-rt | ✅ 8 条 | 口咽根治铁律 |
| larynx-rt-targets | ✅ 12 条 | 喉全流程铁律（根治+PORT） |
| hypopharynx-rt-targets | ✅ 10 条 | 下咽全流程铁律（根治+PORT） |
| npc-rt-target-delineation | ✅ 11 条 | NPC 铁律 |
| orbital-tumor-rt-targets | ✅ 12 条 | 眼眶铁律 |
| head-neck-dvh-plan-review | ✅ 8 条 | DVH 审核铁律 |
| head-neck-sarcoma-rt-targets | ✅ 12 条 | 头颈肉瘤铁律（软组织+骨） |
| adenoid-cystic-carcinoma-rt-targets | ✅ 15 条 | ACC 三级神经径路铁律（2026-09-13 补） |
| hncup-rt-targets | ✅ 13 条 | HNCUP 诊断门槛/选择性黏膜/逆流铁律（2026-09-13 补） |
| sinonasal-rt-targets | ✅ 15 条 | 鼻腔鼻窦铁律（2026-09-13 补） |
| salivary-gland-rt-targets | ✅ 15 条 | 唾液腺铁律（2026-09-13 补） |
| reirradiation-plan-recommend | ✅ 14 条 | 再程放疗铁律（2026-09-13 补） |
| head-neck-lymphoma-rt-targets | ✅ 12 条 | 淋巴瘤 ISRT/剂量铁律（2026-09-13 补） |

**铁律清单覆盖**：**16/16 全部已有编号铁律表**（条数为 2026-09-13 实测：8–17 条/skill，含 2026-09-13 新补的 ACC / hncup / 鼻腔鼻窦 / 唾液腺 / 再程 / 淋巴瘤 6 个）。

---

## 六、双平台兼容性

| 平台 | 机制 | 状态 |
|------|------|:---:|
| Claude Code | 语义匹配 → 自动选择相关 Skill | 16/16 ✅ |
| Hermes Agent | `triggers_on` 触发词匹配 | 16/16 ✅ |
| 前端物质完整性 | `name` `description` `version` `author` `license` | 16/16 ✅ |
| `metadata.hermes` 完整性 | `tags` `triggers_on` `related_skills` | 16/16 ✅ |
| 代码块闭合 | Markdown ``` 配对 | 16/16 ✅ |

---

## 七、安装命令

**Hermes（一行全装）：**
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

**Claude Code（一行克隆）：**
```bash
git clone https://github.com/antica1/head-neck-rt-skills.git
```

---

> 朱国培 · 上海交通大学医学院附属第九人民医院口腔颌面-头颈肿瘤科放疗中心
> 授权：CC BY-NC-SA 4.0 | GitHub: antica1
