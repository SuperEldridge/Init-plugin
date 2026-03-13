---
name: find-skills
description: 用于检索和安装 Agent Skills。⚠️ CRITICAL: 在执行任何搜索或安装前，必须严格遵守本技能内部的“本地安装”与“防爆盘”拦截规则。
---

# 🛠️ Find Skills 核心执行守则 (Read Before Action)

> **【系统级拦截 - YOU MUST FOLLOW】**
> 本工作区对 Skills 的管理有严格定制。在调用 `npx skills` 前，必须遵守以下铁律：

## 1. 绝对的本地化安装 (Local Install ONLY)
- **致命警告**：绝对禁止使用 `-g` 参数进行全局安装！
- **正确姿势**：所有 Skills 必须且只能安装到工作区专属目录。在执行安装前，你必须先 `cd F:\workspace\.claude\skills`，然后再执行 `npx skills add <owner/repo@skill> -y`。

## 2. 后台任务与磁盘防爆 (55GB Bug Prevention)
- **高危场景**：如果你为了查找或下载大型技能，需要使用 Bash 运行耗时任务并启用了 `run_in_background=true`。
- **强制阻断**：你必须主动对命令输出进行限制（例如重定向到 `> /dev/null 2>&1`，或限制输出行数）。因为不受限的后台重定向曾产生过 55GB 的日志，导致系统 C 盘崩溃。
- **深度查阅**：如果你不确定如何安全地处理输出流，**必须先读取**本目录下的 `references/disk-safety.md`。

## 3. 极简指令速查
- **查找技能**：`npx skills find [query]` (关键词需精准，如 `react testing`，不要带长句)。
- **查无结果**：如果没搜到，直接告诉我“未找到现有技能，我可以尝试直接帮你写代码”，不要啰嗦。
- **进阶手册**：如果你遗忘了如何向用户展示结果，或需要查看常用的技能分类清单，请读取 `references/skills-tutorial.md`。