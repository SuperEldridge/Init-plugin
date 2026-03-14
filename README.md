# Claude Code 快捷初始化工作流插件

这是一个专为 Claude Code 打造的快捷初始化工作流插件。以下是建议的工作区框架与相关配置文件。

## 建议配置的工作区框架

请参考以下目录结构搭建你的本地工作区：

```text
F:\workspace\
├── .claude/
│   ├── hooks/
│   │   ├── format_coding.py
│   │   └── ...
│   ├── skills/
│   │   └── find-skills/
│   │       ├── references/
│   │       └── SKILL.md
│   ├── rules/
│   │   ├── env-mcp.md          # 存放 Skill 和 MCP 的下载/配置规则
│   │   ├── embedded-c.md       # 存放 C/C++、HAL库、硬件防坑守则
│   │   ├── agent-flow.md       # 存放 SubAgent 唤醒和协作逻辑
│   │   └── project-init.md     # 存放新建项目时的初始化 SOP
│   └── settings.json           # 见下方详细配置
├── projects/
│   └── <你的具体项目>/
│       ├── progress.md         # (通过规则自动生成) 项目进度与待办
│       └── LESSONS.md          # (通过规则自动生成) 项目级专属错题本
├── Doc/
│   └── CLAUDE.md.bak           # (存放过时或暂时用不到的 CLAUDE.md)
├── .mcp.json
├── CLAUDE.md                   # 主控路由文件
└── Project_LESSONS.md          # 错题本，自进化用
```

> 配置说明：
> * 全局配置：以上为核心工作区搭建，你还可以在全局设置 Agent、CLAUDE.md 和 GLOBAL_LESSONS.md 等等，全局配置需结合个人情况具体分析。
> * 路径适配：如果遇到脚本跑不通的情况，请检查绝对路径。示例中使用的是 F 盘，请根据你的实际情况改成你自己的盘符和对应路径。

---

## settings.json 配置文件

请将以下内容完整复制并保存到 `.claude/settings.json` 文件中：

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "^(Edit|Write)$",
        "hooks": [
          {
            "type": "command",
            "command": "python .claude/hooks/format_coding.py"
          }
        ]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "^Bash$",
        "hooks": [
          {
            "type": "command",
            "command": "python .claude/hooks/check_dangerous_cmd.py"
          }
        ]
      }
    ],
    "SubagentStart": [
      {
        "matcher": "^chaos[-_]tester$",
        "hooks": [
          {
            "type": "command",
            "command": "python .claude/hooks/chaos_alarm.py"
          }
        ]
      }
    ]
  }
}
```