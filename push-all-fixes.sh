#!/bin/bash
# 放疗 Skills 全部修复推送脚本
# 用法: bash push-all-fixes.sh /path/to/fixed-repos /path/to/all-repos

FIXED="$1"
REPOS="$2"

if [ -z "$FIXED" ] || [ -z "$REPOS" ]; then
    echo "用法: bash push-all-fixes.sh <fixed-repos目录> <所有仓库的父目录>"
    echo "示例: bash push-all-fixes.sh ./fixed-repos ~/repos"
    exit 1
fi

echo "=== 1. 覆盖修改过的 SKILL.md ==="
for repo in HNCUP-rt-targets head-neck-acc-rt-targets laryngeal-hypopharyngeal-rt-targets larynx-hypopharynx-definitive neoadjuvant-deescalation orbital-tumor-rt-targets oropharynx-definitive-rt port-oral-postop port-oropharynx-postop sinonasal-rt-targets; do
    if [ -d "$REPOS/$repo" ]; then
        cp "$FIXED/$repo/SKILL.md" "$REPOS/$repo/SKILL.md"
        echo "  ✓ $repo"
    else
        echo "  ✗ $repo 目录不存在于 $REPOS"
    fi
done

echo ""
echo "=== 2. 处理 npc-rt-target-delineation ==="
if [ -d "$REPOS/npc-rt-target-delineation" ]; then
    cp "$FIXED/npc-rt-target-delineation/SKILL.md" "$REPOS/npc-rt-target-delineation/SKILL.md"
    echo "  ✓ npc-rt-target-delineation"
else
    echo "  ✗ 目录不存在，需要先 clone"
fi

echo ""
echo "=== 3. 提交并推送所有仓库 ==="
for repo in HNCUP-rt-targets head-neck-acc-rt-targets laryngeal-hypopharyngeal-rt-targets larynx-hypopharynx-definitive neoadjuvant-deescalation orbital-tumor-rt-targets oropharynx-definitive-rt port-oral-postop port-oropharynx-postop sinonasal-rt-targets npc-rt-target-delineation; do
    if [ -d "$REPOS/$repo" ]; then
        cd "$REPOS/$repo"
        if [ -n "$(git status --porcelain)" ]; then
            git add SKILL.md
            git commit -m "修复: 临床逻辑和代码质量改进 (2026-07-29)" && git push && echo "  ✓ $repo 已推送"
        else
            echo "  - $repo 无变更"
        fi
    fi
done

echo ""
echo "=== 4. head-neck-rt-skills ==="
if [ -d "$REPOS/head-neck-rt-skills" ]; then
    cd "$REPOS/head-neck-rt-skills"
    if [ -n "$(git status --porcelain)" ]; then
        git add -A
        git commit -m "v2.0: 修复 nmetadata 拼写+Git 冲突+子Skill升级+临床逻辑修复" && git push && echo "  ✓ head-neck-rt-skills 已推送"
    fi
fi

echo ""
echo "全部完成。"
