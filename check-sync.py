#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
head-neck-rt-skills 三位置一致性检查器
======================================
检查三个位置的 Skill 版本与内容一致性：
  ① 主仓库聚合目录  D:\\头颈肿瘤放疗靶区\\主仓库\\skills\\
  ② Hermes 运行目录 C:\\Users\\antic\\AppData\\Local\\hermes\\skills\\research\\
  ③ GitHub 远程     origin/master (通过 git)

用法:
  python check-sync.py            # 完整检查三位置
  python check-sync.py --quick    # 仅检查主仓库 vs 运行目录
  python check-sync.py --push-check  # 推送前快速检查（含未提交变更）

每次修改 Skill 后、推送前必须运行。任一 ❌ 都说明有分叉——先解决再推送。
"""
import os
import sys
import subprocess
import difflib

MAIN = r"D:\头颈肿瘤放疗靶区\主仓库\skills"
RUN  = r"C:\Users\antic\AppData\Local\hermes\skills\research"
REPO = r"D:\头颈肿瘤放疗靶区\主仓库"

def read(p):
    try:
        with open(p, encoding="utf-8") as f:
            return f.read()
    except Exception:
        return None

def version(text):
    if not text:
        return "?"
    for line in text.splitlines():
        if line.startswith("version:"):
            return line.split(":", 1)[1].strip()
    return "?"

def list_skills(d):
    if not os.path.isdir(d):
        return []
    return sorted(x for x in os.listdir(d) if os.path.isdir(os.path.join(d, x)))

def remote_skill_text(name):
    """从 origin/master 取该 skill 的 SKILL.md 文本"""
    try:
        r = subprocess.run(
            ["git", "show", f"origin/master:skills/{name}/SKILL.md"],
            cwd=REPO, capture_output=True, text=True, encoding="utf-8", errors="replace",
            timeout=30,
        )
        if r.returncode == 0:
            return r.stdout
        return None
    except Exception:
        return None

def yaml_name(text):
    """从 SKILL.md frontmatter 提取 name 字段"""
    if not text:
        return None
    for line in text.splitlines()[:15]:
        if line.startswith("name:"):
            return line.split(":", 1)[1].strip().strip('"\'')
    return None

def main():
    quick = "--quick" in sys.argv
    push_check = "--push-check" in sys.argv

    main_skills = list_skills(MAIN)
    run_skills = list_skills(RUN)

    print("=" * 72)
    print("  三位置一致性检查：主仓库 / 运行目录 / GitHub远程")
    print("=" * 72)

    errors = 0
    warnings = 0

    # 检查主仓库中的每个 skill（这是发布源）
    for name in main_skills:
        m_path = os.path.join(MAIN, name, "SKILL.md")
        tm = read(m_path)
        # 2026-08 起目录名已统一 = YAML name = 运行目录名，直接匹配
        r_path = os.path.join(RUN, name, "SKILL.md")
        tr = read(r_path)

        # 主仓库 vs 运行目录
        if tr is None:
            print(f"  ❌ {name}: 运行目录缺失 SKILL.md（主仓库有，yaml name={yn}）")
            errors += 1
        elif tm != tr:
            vm, vr = version(tm), version(tr)
            d = list(difflib.unified_diff(tm.splitlines(), tr.splitlines(), lineterm=""))
            chg = [x for x in d if x.startswith(("+", "-")) and not x.startswith(("+++", "---"))]
            print(f"  ❌ {name}: 主仓库v{vm} ≠ 运行目录v{vr}（差异 {len(chg)} 行）")
            errors += 1

        # 主仓库 vs 远程（除非是 --quick）
        if not quick and not push_check:
            trm = remote_skill_text(name)
            if trm is None:
                # 远程没有这个文件（可能是新 skill 未推送）
                status = subprocess.run(["git", "status", "--porcelain", f"skills/{name}/SKILL.md"],
                                        cwd=REPO, capture_output=True, text=True, encoding="utf-8").stdout
                if status.strip():
                    print(f"  ⚠ {name}: 远程无此文件且本地有未提交修改（新 skill 待推送？）")
                    warnings += 1
                else:
                    print(f"  ⚠ {name}: 远程无此文件（新 skill？已提交但未推送？）")
                    warnings += 1
            elif tm != trm:
                vm, vrm = version(tm), version(trm)
                d = list(difflib.unified_diff(tm.splitlines(), trm.splitlines(), lineterm=""))
                chg = [x for x in d if x.startswith(("+", "-")) and not x.startswith(("+++", "---"))]
                print(f"  ❌ {name}: 主仓库v{vm} ≠ 远程v{vrm}（差异 {len(chg)} 行）—— 未推送或远程更新未拉取")
                errors += 1

    # 检查运行目录独有的（主仓库完全没对应的，才警告）
    if not quick:
        # 收集主仓库所有 skill 的 YAML name + 目录名
        main_names = set()
        for name in main_skills:
            m_path = os.path.join(MAIN, name, "SKILL.md")
            tm = read(m_path)
            main_names.add(name)
            yn = yaml_name(tm)
            if yn:
                main_names.add(yn)
        skip_prefixes = ("nature-", "mr-", "ars-", "academic-", "nsfc-", "grant-", "clinical-",
                         "hospital-", "institutional-", "journal-", "conference-", "medical-",
                         "rt-academic", "rt-department", "competitor-", "blogwatcher", "arxiv",
                         "agnes-", "pdf-figure")
        for name in run_skills:
            if name in main_names:
                continue  # 已有对应（目录名或 YAML name 匹配）
            if name.startswith(skip_prefixes):
                continue
            print(f"  ⚠ {name}: 仅运行目录有（主仓库无）—— 是否需纳入发布？")
            warnings += 1

    print("-" * 72)
    if errors == 0 and warnings == 0:
        print("  ✅ 全部一致——可以安全推送。")
    elif errors == 0:
        print(f"  ⚠ 无错误，但有 {warnings} 个警告（见上）。")
    else:
        print(f"  ❌ 发现 {errors} 个错误、{warnings} 个警告——先解决再推送！")
    print("=" * 72)
    sys.exit(1 if errors else 0)

if __name__ == "__main__":
    main()
