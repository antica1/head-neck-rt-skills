# 头颈放疗靶区 Skill 完整索引

> 上海九院放疗中心 · 朱国培 | GitHub: antica1 | v2.1.0 | 2026-07-29
> 17 个 Skill · 7,253 行 Markdown · Claude Code & Hermes 双平台

---

## 一、目录树

```
head-neck-rt-skills/
├── README.md                        # 双平台安装指南
├── CITATION.cff                     # 引用元数据
├── index.html                       # Web 入口页
├── SKILLS_INDEX.md                  # 本文件——完整索引
└── skills/
    ├── shared-knowledge/            # 根——共享知识库（224 行）
    │
    ├── neoadjuvant-deescalation/    # 化免新辅助降级（242 行）——被 11 个 Skill 引用
    │
    ├── oral-oropharynx-postop-rt-targets/  # 口腔口咽 PORT 总集（1,089 行）——含口底铁律
    │   ├── port-oral-postop/               # 口腔 PORT 子模块（574 行）
    │   └── port-oropharynx-postop/         # 口咽 PORT 子模块（207 行）
    │
    ├── oropharynx-definitive-rt/    # 口咽根治性 RT（267 行）
    │
    ├── laryngeal-hypopharyngeal-rt-targets/  # 喉/下咽索引（50 行）——仅路由
    │   ├── larynx-hypopharynx-postop/        # 喉/下咽术后 PORT（381 行）
    │   └── larynx-hypopharynx-definitive/    # 喉/下咽根治性 RT（308 行）
    │
    ├── head-neck-acc-rt-targets/    # ACC 腺样囊性癌（437 行）
    ├── HNCUP-rt-targets/            # 原发不明转移癌（517 行）
    ├── npc-rt-target-delineation/   # NPC 鼻咽癌（78 行）
    ├── orbital-tumor-rt-targets/    # 眼眶肿瘤（1,026 行）
    ├── sinonasal-rt-targets/        # 鼻腔鼻窦癌（525 行）
    ├── salivary-gland-rt-targets/   # 唾液腺癌（806 行）
    ├── head-neck-reirradiation/     # 再程放疗（261 行）
    └── head-neck-dvh-review/        # DVH 计划审核（257 行）
```

---

## 二、依赖关系图

```
shared-knowledge
    │
    ├── neoadjuvant-deescalation ──────────────────────────────────┐
    │   (当患者有新辅助史时加载)                                      │
    │                                                                │
    ├── oral-oropharynx-postop-rt-targets ──────────────────────────┤
    │   ├── port-oral-postop            ← neoadjuvant-deescalation ─┤
    │   └── port-oropharynx-postop      ← neoadjuvant-deescalation ─┤
    │                                                                │
    ├── oropharynx-definitive-rt        ← neoadjuvant-deescalation ─┤
    │                                                                │
    ├── laryngeal-hypopharyngeal-rt-targets ────────────────────────┤
    │   ├── larynx-hypopharynx-postop   ← neoadjuvant-deescalation ─┤
    │   └── larynx-hypopharynx-definitive ──────────────────────────┤
    │                                                                │
    ├── head-neck-acc-rt-targets                                     │
    ├── HNCUP-rt-targets                ← npc-rt-target-delineation  │
    ├── npc-rt-target-delineation                                    │
    ├── orbital-tumor-rt-targets        ← head-neck-acc-rt-targets   │
    ├── sinonasal-rt-targets                                         │
    ├── salivary-gland-rt-targets       ← head-neck-acc-rt-targets   │
    ├── head-neck-reirradiation                                      │
    └── head-neck-dvh-review                                         │
```

---

## 三、YAML Name ↔ 仓库名对照表

| 仓库名（目录） | YAML `name` | 行数 | 版本 |
|:---|---:|---:|:---:|
| shared-knowledge | shared-knowledge | 228 | 1.4.0 |
| neoadjuvant-deescalation | neoadjuvant-deescalation | 242 | — |
| oral-oropharynx-postop-rt-targets | oral-oropharynx-postop-rt-targets | 1,089 | 1.2.0 |
| port-oral-postop | port-oral-postop | 574 | 1.0.0 |
| port-oropharynx-postop | port-oropharynx-postop | 207 | — |
| oropharynx-definitive-rt | oropharynx-definitive-rt | 267 | — |
| laryngeal-hypopharyngeal-rt-targets | laryngeal-hypopharyngeal-rt-targets | 50 | 2.0.0 |
| larynx-hypopharynx-postop | larynx-hypopharynx-postop | 381 | — |
| larynx-hypopharynx-definitive | larynx-hypopharynx-definitive | 308 | — |
| head-neck-acc-rt-targets | adenoid-cystic-carcinoma-rt-targets | 437 | 1.5.1 |
| HNCUP-rt-targets | cervical-cup-rt-targets | 517 | 1.0.0 |
| npc-rt-target-delineation | npc-rt-target-delineation | 78 | 1.0.0 |
| orbital-tumor-rt-targets | orbital-tumor-rt-targets | 1,026 | 1.0.0 |
| sinonasal-rt-targets | sinonasal-rt-targets | 525 | 1.3.2 |
| salivary-gland-rt-targets | salivary-gland-rt-targets | 806 | 1.2.0 |
| head-neck-reirradiation | reirradiation-plan-recommend | 261 | — |
| head-neck-dvh-review | head-neck-dvh-plan-review | 257 | — |

> **注意**：YAML `name` 是 `related_skills` 引用的标识符。3 个仓库的目录名与 YAML name 不一致：`head-neck-acc-rt-targets` → `adenoid-cystic-carcinoma-rt-targets`、`HNCUP-rt-targets` → `cervical-cup-rt-targets`、`head-neck-reirradiation` → `reirradiation-plan-recommend`、`head-neck-dvh-review` → `head-neck-dvh-plan-review`。这是有意为之——目录名用于 GitHub 仓库 URL（短名），YAML name 用于 Hermes 内部索引（语义名）。

---

## 四、跨 Skill 自动联动

| 触发场景 | 自动加载链 |
|----------|-----------|
| "眼眶 ACC" / "泪腺 ACC" | orbital-tumor-rt-targets → head-neck-acc-rt-targets |
| "腮腺 ACC" / "颌下腺 ACC" | salivary-gland-rt-targets → head-neck-acc-rt-targets |
| "鼻咽部 ACC" | npc-rt-target-delineation → head-neck-acc-rt-targets |
| "口腔癌术后 + 化免 pCR" | port-oral-postop → neoadjuvant-deescalation |
| "口咽癌术后 + 化免 MPR" | port-oropharynx-postop → neoadjuvant-deescalation |
| "下咽癌术后 + 化免 pCR" | larynx-hypopharynx-postop → neoadjuvant-deescalation |
| "喉癌根治 + 化免 pCR" | larynx-hypopharynx-definitive → neoadjuvant-deescalation |
| "口咽根治 SIB + 化免 pCR" | oropharynx-definitive-rt → neoadjuvant-deescalation |
| "CUP 颈部转移 + 怀疑 NPC" | HNCUP-rt-targets → npc-rt-target-delineation |
| "再程放疗 + 需 DVH 审核" | head-neck-reirradiation → head-neck-dvh-review |
| "任何靶区生成 + 需 DVH 审核" | any-skill → head-neck-dvh-review |

---

## 五、铁律清单覆盖

| Skill | 铁律条数 | 状态 |
|------|:---:|:---:|
| shared-knowledge | ✅ | 共享知识库——含口底铁律、间室放疗、淋巴逆流规则 |
| neoadjuvant-deescalation | ✅ | 化免降级梯度规则 |
| oral-oropharynx-postop-rt-targets | ✅ | PORT 总集铁律 |
| port-oral-postop | ✅ 12 条 | 口腔 PORT 铁律 |
| port-oropharynx-postop | ✅ | 口咽 PORT 铁律 |
| oropharynx-definitive-rt | ✅ 14 条 | 口咽根治铁律 |
| laryngeal-hypopharyngeal-rt-targets | ❌ | 仅索引路由——无需铁律（合理） |
| larynx-hypopharynx-postop | ✅ | 喉 PORT 铁律 |
| larynx-hypopharynx-definitive | ⚠️ | 308 行完整临床 Skill——待补 |
| head-neck-acc-rt-targets | ✅ | ACC 三级追踪铁律 |
| HNCUP-rt-targets | ✅ | CUP 铁律 |
| npc-rt-target-delineation | ❌ | 78 行纯解剖参考——无需铁律（合理） |
| orbital-tumor-rt-targets | ✅ | 眼眶铁律 |
| sinonasal-rt-targets | ⚠️ | 525 行完整临床 Skill——待补 |
| salivary-gland-rt-targets | ✅ | 唾液腺铁律 |
| head-neck-reirradiation | ✅ | 再程放疗铁律 |
| head-neck-dvh-review | ✅ | DVH 审核铁律 |

**铁律覆盖率**：13/17（含 2 个不应有铁律的纯索引/参考文件） = 实际覆盖率 13/15 = 87%

---

## 六、双平台兼容性

| 平台 | 机制 | 状态 |
|------|------|:---:|
| Claude Code | 语义匹配 → 自动选择相关 Skill | 17/17 ✅ |
| Hermes Agent | `triggers_on` 触发词匹配 | 17/17 ✅ |
| 前端物质完整性 | `name` `description` `version` `author` `license` | 17/17 ✅ |
| `metadata.hermes` 完整性 | `tags` `triggers_on` `related_skills` | 17/17 ✅ |
| 代码块闭合 | Markdown ``` 配对 | 17/17 ✅ |

---

## 七、安装命令

**Hermes（一行全装）：**
```
hermes skills install head-neck-acc-rt-targets HNCUP-rt-targets orbital-tumor-rt-targets npc-rt-target-delineation head-neck-dvh-review head-neck-reirradiation oral-oropharynx-postop-rt-targets laryngeal-hypopharyngeal-rt-targets salivary-gland-rt-targets sinonasal-rt-targets port-oral-postop port-oropharynx-postop oropharynx-definitive-rt neoadjuvant-deescalation larynx-hypopharynx-postop larynx-hypopharynx-definitive shared-knowledge
```

**Claude Code（一行克隆）：**
```bash
git clone https://github.com/antica1/head-neck-rt-skills.git
```

---

> 朱国培 · 上海交通大学医学院附属第九人民医院口腔颌面-头颈肿瘤科放疗中心
> 授权：CC BY-NC-SA 4.0 | GitHub: antica1
