建议配置的工作区框架如下：
F:\workspace\
├── .claude/
│   ├── hooks/
│       ├──format_coding.py
│       ├── ...
│   ├── skills/
│       ├──find-skills
│           ├── references
│           ├── SKILL.md
│   ├── rules/
│   │   ├── env-mcp.md        # 存放 Skill 和 MCP 的下载/配置规则
│   │   ├── embedded-c.md     # 存放 C/C++、HAL库、硬件防坑守则
│   │   ├── agent-flow.md     # 存放 SubAgent 唤醒和协作逻辑
│   │   └── project-init.md   # 存放新建项目时的初始化 SOP
│   ├── settings.json
├── projects/
│   └── <你的具体项目>/
│       ├── progress.md       # (通过规则自动生成) 项目进度与待办
│       └── LESSONS.md        # (通过规则自动生成) 项目级专属错题本
├── Doc/
        ├──CLAUDE.md.bak      #（存放过时或暂时用不到的CLAUDE.md）
├── .mcp.json
└── CLAUDE.md                 # 主控路由文件
└── Project_LESSONS.md        # 错题本，自进化用

以上为工作区搭建，还可在全局设置agent、CLAUDE.md和GLOBAL_LESSONS.md等等，全局的就个人情况个人分析
如果遇到有跑不通的，盘可能和我不一样，我是F盘，可以改成自己的盘和路径


















settings.json内容：
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
