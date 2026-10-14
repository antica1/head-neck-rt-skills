#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
head-neck-rt-skills 多位置一致性检查器 v2
==========================================
检查发布源与全部消费位置的 Skill 版本与内容一致性：
  ① 主仓库工作区   D:\\头颈肿瘤放疗靶区\\主仓库\\skills\\
  ② 全部 8 个运行目录（default + bot-academic/clinical/data/literature/management/patient/slides）
  ③ GitHub 远程    origin/master
  ④ Gitee 镜像     gitee/master

v2 修订（2026-10-14）：
  - v1 只检查 default 一个运行目录 → 7 个 bot profile 漂移数月无人发现（ACC v1.2.0 vs v1.7.1 事故）
  - v2 覆盖全部 profile；附属文件（README/references/*）一并比对
  - 比对前统一换行符（CRLF/LF 假阳性根除）
  - 远程同时查 origin 与 gitee 双镜像

用法:
  python check-sync.py            # 完整检查（工作区+8运行目录+双远程）
  python check-sync.py --quick    # 仅工作区 vs 8 运行目录
  python check-sync.py --push-check  # 推送前检查（工作区+运行目录+未提交变更）

每次修改 Skill 后、推送前必须运行。任一 ❌ 都说明有分叉——先解决再推送。
"""
import os
import sys
import subprocess
import difflib

MAIN = r"D:\头颈肿瘤放疗靶区\主仓库\skills"
REPO = r"D:\头颈肿瘤放疗靶区\主仓库"
RUN_ROOTS = [
    ("default",    r"C:\Users\antic\AppData\Local\hermes\skills"),
] + [
    (p, rf"C:\Users\antic\AppData\Local\hermes\profiles\{p}\skills")
    for p in ("bot-academic", "bot-clinical", "bot-data", "bot-literature",
              "bot-management", "bot-patient", "bot-slides")
]

def read(p):
    try:
        with open(p, encoding="utf-8", newline="") as f:
            return f.read().replace("\r\n", "\n").replace("\r", "\n")
    except Exception:
        return None

def version(text):
    if not text:
        return "?"
    for line in text.splitlines():
        if line.startswith("version:"):
            return line.split(":", 1)[1].strip()
    return "?"

def list_skill_dirs(d):
    if not os.path.isdir(d):
        return []
    return sorted(x for x in os.listdir(d)
                  if os.path.isdir(os.path.join(d, x))
                  and os.path.isfile(os.path.join(d, x, "SKILL.md")))

def find_in_run(run_root, name):
    """运行目录搜索：顶层 + 所有分类子目录"""
    for cand in [os.path.join(run_root, name, "SKILL.md")] + [
            os.path.join(run_root, cat, name, "SKILL.md")
            for cat in sorted(os.listdir(run_root))
            if os.path.isdir(os.path.join(run_root, cat))]:
        if os.path.exists(cand):
            return os.path.dirname(cand)
    return None

def remote_skill_text(ref, name):
    try:
        r = subprocess.run(["git", "show", f"{ref}:skills/{name}/SKILL.md"],
                           cwd=REPO, capture_output=True, text=True,
                           encoding="utf-8", errors="replace", timeout=30)
        return r.stdout if r.returncode == 0 else None
    except Exception:
        return None

def aux_files(skill_dir):
    """附属文件：README.md、references/*.md 等（SKILL.md/ATTRIBUTION.md/LICENSE 之外）"""
    out = {}
    if not os.path.isdir(skill_dir):
        return out
    for item in sorted(os.listdir(skill_dir)):
        if item in ("SKILL.md", "ATTRIBUTION.md", "LICENSE"):
            continue
        p = os.path.join(skill_dir, item)
        if os.path.isfile(p):
            out[item] = read(p)
        elif os.path.isdir(p):
            for f in sorted(os.listdir(p)):
                if f.endswith(".md"):
                    out[f"{item}/{f}"] = read(os.path.join(p, f))
    return out

def main():
    quick = "--quick" in sys.argv
    push_check = "--push-check" in sys.argv

    main_skills = list_skill_dirs(MAIN)
    print("=" * 76)
    print("  多位置一致性检查 v2：主仓库 / 8 个运行目录 / GitHub + Gitee 双远程")
    print("=" * 76)

    errors = warnings = 0

    for name in main_skills:
        tm = read(os.path.join(MAIN, name, "SKILL.md"))
        tmaux = aux_files(os.path.join(MAIN, name))

        # ② 逐个运行目录
        for tag, run_root in RUN_ROOTS:
            rdir = find_in_run(run_root, name)
            if rdir is None:
                print(f"  ❌ {name} @ {tag}: 运行目录缺失")
                errors += 1
                continue
            tr = read(os.path.join(rdir, "SKILL.md"))
            if tr is None:
                print(f"  ❌ {name} @ {tag}: SKILL.md 读取失败")
                errors += 1
            elif tm != tr:
                d = list(difflib.unified_diff(tr.splitlines(), tm.splitlines(), lineterm=""))
                chg = sum(1 for x in d if x.startswith(("+", "-")) and not x.startswith(("+++", "---")))
                print(f"  ❌ {name} @ {tag}: 主仓库v{version(tm)} ≠ 运行目录v{version(tr)}（差异 {chg} 行）")
                errors += 1
            # 附属文件双向比对
            raux = aux_files(rdir)
            for f, content in tmaux.items():
                if f not in raux:
                    print(f"  ⚠ {name} @ {tag}: 附属文件 {f} 运行目录缺失")
                    warnings += 1
                elif raux[f] != content:
                    print(f"  ⚠ {name} @ {tag}: 附属文件 {f} 内容不同")
                    warnings += 1
            for f in raux:
                if f not in tmaux:
                    print(f"  ⚠ {name} @ {tag}: 附属文件 {f} 仅运行目录有（主仓库无——会否丢失？）")
                    warnings += 1

        # ③④ 双远程
        if not quick and not push_check:
            for ref in ("origin/master", "gitee/master"):
                trm = remote_skill_text(ref, name)
                if trm is None:
                    print(f"  ⚠ {name}: {ref} 无此文件（新 skill 未推送？）")
                    warnings += 1
                elif trm != tm:
                    d = list(difflib.unified_diff(trm.splitlines(), tm.splitlines(), lineterm=""))
                    chg = sum(1 for x in d if x.startswith(("+", "-")) and not x.startswith(("+++", "---")))
                    print(f"  ❌ {name}: 主仓库v{version(tm)} ≠ {ref} v{version(trm)}（差异 {chg} 行）")
                    errors += 1

    if push_check:
        st = subprocess.run(["git", "status", "--porcelain", "skills/"],
                            cwd=REPO, capture_output=True, text=True,
                            encoding="utf-8", errors="replace").stdout.strip()
        if st:
            print("\n  ⚠ 主仓库有未提交变更：")
            for line in st.splitlines():
                print(f"      {line}")
            warnings += len(st.splitlines())

    print("-" * 76)
    if errors == 0 and warnings == 0:
        print("  ✅ 全部一致——可以安全推送。")
    elif errors == 0:
        print(f"  ⚠ 无错误，但有 {warnings} 个警告（见上）。")
    else:
        print(f"  ❌ 发现 {errors} 个错误、{warnings} 个警告——先解决再推送！")
    print("=" * 76)
    sys.exit(1 if errors else 0)

if __name__ == "__main__":
    main()
