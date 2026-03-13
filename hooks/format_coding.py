import sys
import json
import subprocess

# 1. 抓取 Claude Code 在后台偷偷传入的 JSON 行为数据
try:
    input_data = sys.stdin.read()
    event = json.loads(input_data)
    
    # 2. 提取 AI 刚刚修改或创建的文件路径
    file_path = event.get("tool_input", {}).get("file_path", "")
    if not file_path:
        file_path = event.get("tool_input", {}).get("path", "")

    # 3. 仅拦截对 C/C++ 头文件和源文件的操作
    if file_path.endswith('.c') or file_path.endswith('.h'):
        # 4. 执行底层硬拦截：强制应用嵌入式排版规范
        # 这里预设了 4 空格缩进，且强制指针靠右对齐等严格规范
        format_cmd = [
            "clang-format", 
            "-style={BasedOnStyle: LLVM, IndentWidth: 4, PointerAlignment: Right, BreakBeforeBraces: Attach}", 
            "-i", 
            file_path
        ]
        subprocess.run(format_cmd, check=True)
        print(f"[Hook 拦截] 已强行重构 {file_path} 的底层代码排版。")
        
except Exception as e:
    # 保持退出码为0，即使格式化失败也不要中断大模型的思路
    print(f"Hook 静默失败: {e}", file=sys.stderr)
    sys.exit(0)