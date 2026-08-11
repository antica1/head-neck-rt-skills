# ============================================================
#  头颈放疗 Skill 一键同步脚本 (PowerShell)
#  双击运行或: powershell -ExecutionPolicy Bypass -File sync-all.ps1
#
#  功能:
#  1. 克隆 17 个独立仓库到当前目录的上一级
#  2. 将 head-neck-rt-skills/skills/ 下的修复版覆盖到各仓库
#  3. git commit + git push 到 GitHub
# ============================================================

$ErrorActionPreference = "Stop"

# 获取脚本所在目录（即 head-neck-rt-skills）
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$BaseDir = Split-Path -Parent $ScriptDir

Write-Host ""
Write-Host "═══════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host "  头颈放疗 Skill 一键同步 — v2.1.0" -ForegroundColor Cyan
Write-Host "═══════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host ""

$Repos = @(
    "hncup-rt-targets",
    "adenoid-cystic-carcinoma-rt-targets",
    "head-neck-dvh-plan-review",
    "reirradiation-plan-recommend",
    "laryngeal-hypopharyngeal-rt-targets",
    "larynx-hypopharynx-definitive",
    "larynx-hypopharynx-postop",
    "neoadjuvant-deescalation",
    "npc-rt-target-delineation",
    "oral-oropharynx-postop-rt-targets",
    "orbital-tumor-rt-targets",
    "oropharynx-definitive-rt",
    "port-oral-postop",
    "port-oropharynx-postop",
    "salivary-gland-rt-targets",
    "shared-knowledge",
    "sinonasal-rt-targets"
)

# ============================================================
#  第一步：克隆所有仓库
# ============================================================
Write-Host "━━━ 第一步：克隆 17 个独立仓库 ━━━" -ForegroundColor Yellow
Write-Host ""

$Cloned = 0
$Skipped = 0

foreach ($Repo in $Repos) {
    $RepoPath = Join-Path $BaseDir $Repo
    if (Test-Path $RepoPath) {
        Write-Host "  ⏭️  $Repo (already exists)" -ForegroundColor Gray
        $Skipped++
    } else {
        Write-Host "  ⬇ $Repo" -ForegroundColor White
        git clone "https://github.com/antica1/$Repo.git" $RepoPath 2>&1 | Out-Null
        # 空仓库也可以克隆成功
        $Cloned++
    }
}

Write-Host ""
Write-Host "  ✅ Cloned: $Cloned, Already present: $Skipped" -ForegroundColor Green
Write-Host ""

# ============================================================
#  第二步 & 第三步：复制修复版 SKILL.md + commit + push
# ============================================================
Write-Host "━━━ 第二步 & 第三步：同步 + 推送 ━━━" -ForegroundColor Yellow
Write-Host ""

$Synced = 0
$SkippedSync = 0
$Failed = 0

foreach ($Repo in $Repos) {
    $SourceFile = Join-Path $ScriptDir "skills\$Repo\SKILL.md"
    $DestFile = Join-Path $BaseDir "$Repo\SKILL.md"

    if (-not (Test-Path $SourceFile)) {
        Write-Host "  ❌ $Repo — SKILL.md missing in aggregated repo" -ForegroundColor Red
        $Failed++
        continue
    }

    if (-not (Test-Path (Join-Path $BaseDir $Repo))) {
        Write-Host "  ❌ $Repo — directory not found" -ForegroundColor Red
        $Failed++
        continue
    }

    # 复制文件
    Copy-Item $SourceFile $DestFile -Force

    Push-Location (Join-Path $BaseDir $Repo)

    # 检查 git 状态
    $Status = git status --porcelain 2>&1
    if ($Status) {
        Write-Host "  ▶ $Repo" -ForegroundColor White
        git add SKILL.md
        git commit -m "v2.1.0: 编码修复+双平台兼容 (metadata.hermes/triggers_on/代码块闭合/重复metadata清理)"
        try {
            $Branch = git branch --show-current
            git push origin $Branch 2>&1 | Out-Null
            Write-Host "    ✅ pushed" -ForegroundColor Green
            $Synced++
        } catch {
            Write-Host "    ⚠️ push failed — checking if git can pull first..." -ForegroundColor Yellow
            # 可能是远程有更新的提交，先 pull 再 push
            try {
                git pull origin $Branch --rebase 2>&1 | Out-Null
                git push origin $Branch 2>&1 | Out-Null
                Write-Host "    ✅ pushed (after rebase)" -ForegroundColor Green
                $Synced++
            } catch {
                Write-Host "    ❌ push failed even after rebase" -ForegroundColor Red
                Write-Host "    You may need to authenticate: try 'git push' manually in $Repo" -ForegroundColor Yellow
                $Failed++
            }
        }
    } else {
        Write-Host "  ⏭️  $Repo (no changes)" -ForegroundColor Gray
        $SkippedSync++
    }

    Pop-Location
}

Write-Host ""
Write-Host "═══════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host "  Synced: $Synced  |  No changes: $SkippedSync  |  Failed: $Failed" -ForegroundColor Cyan
Write-Host "═══════════════════════════════════════════════" -ForegroundColor Cyan

if ($Failed -gt 0) {
    Write-Host ""
    Write-Host "⚠️  $Failed repo(s) had issues. Check the output above." -ForegroundColor Yellow
} else {
    Write-Host ""
    Write-Host "✅ All 17 standalone repos up to date with v2.1.0" -ForegroundColor Green
}

Write-Host ""
Write-Host "Press any key to exit..." -ForegroundColor Gray
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
