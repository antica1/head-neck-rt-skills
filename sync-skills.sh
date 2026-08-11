#!/bin/bash
# ============================================================
# 头颈放疗 Skill 批量同步脚本 — v2.1.0
# 将 head-neck-rt-skills/skills/ 中的修复版 SKILL.md
# 同步到 17 个独立 GitHub 仓库并推送
#
# 使用前提:
#   1. 当前目录为 head-neck-rt-skills 根目录
#   2. 17 个独立仓库已 git clone 到 ../<repo-name>/
#   3. npc-rt-target-delineation 空仓库需先创建初始提交:
#      cd ../npc-rt-target-delineation
#      git commit --allow-empty -m "init"
#
# 执行:
#   chmod +x sync-skills.sh
#   ./sync-skills.sh
# ============================================================

set -e

AGGREGATED_DIR="$(pwd)/skills"
BASE_DIR="$(pwd)/.."

echo "═══════════════════════════════════════════════"
echo "  头颈放疗 Skill 批量同步 — v2.1.0 修复版"
echo "═══════════════════════════════════════════════"
echo ""

SYNC_COUNT=0
SKIP_COUNT=0
FAIL_COUNT=0

sync_repo() {
    local repo=$1
    if [ -d "$BASE_DIR/$repo" ]; then
        echo "▶ $repo"
        cp "$AGGREGATED_DIR/$repo/SKILL.md" "$BASE_DIR/$repo/SKILL.md"
        cd "$BASE_DIR/$repo"
        if [ -n "$(git status --porcelain)" ]; then
            git add SKILL.md
            git commit -m "v2.1.0: 编码修复+双平台兼容 (metadata.hermes/triggers_on/代码块闭合)"
            git push origin $(git branch --show-current)
            echo "  ✅ pushed"
            return 0
        else
            echo "  ⏭️  no changes"
            return 1
        fi
    else
        echo "  ❌ $repo not found — clone first:"
        echo "     git clone https://github.com/antica1/$repo.git $BASE_DIR/$repo"
        return 2
    fi
}

for repo in \
    hncup-rt-targets \
    adenoid-cystic-carcinoma-rt-targets \
    head-neck-dvh-plan-review \
    reirradiation-plan-recommend \
    laryngeal-hypopharyngeal-rt-targets \
    larynx-hypopharynx-definitive \
    larynx-hypopharynx-postop \
    neoadjuvant-deescalation \
    npc-rt-target-delineation \
    oral-oropharynx-postop-rt-targets \
    orbital-tumor-rt-targets \
    oropharynx-definitive-rt \
    port-oral-postop \
    port-oropharynx-postop \
    salivary-gland-rt-targets \
    shared-knowledge \
    sinonasal-rt-targets; do

    sync_repo "$repo"
    case $? in
        0) SYNC_COUNT=$((SYNC_COUNT + 1)) ;;
        1) SKIP_COUNT=$((SKIP_COUNT + 1)) ;;
        2) FAIL_COUNT=$((FAIL_COUNT + 1)) ;;
    esac
done

echo ""
echo "═══════════════════════════════════════════════"
echo "  Synced: $SYNC_COUNT  Skipped: $SKIP_COUNT  Failed: $FAIL_COUNT"
echo "═══════════════════════════════════════════════"

if [ $FAIL_COUNT -gt 0 ]; then
    echo ""
    echo "⚠️  $FAIL_COUNT repo(s) missing. Clone them and re-run."
fi
