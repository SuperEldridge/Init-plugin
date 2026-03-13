import sys
import json

def check_command():
    try:
        # 1. 抓取 Claude Code 准备传给 Bash 工具的底层 JSON 数据
        input_data = sys.stdin.read()
        event = json.loads(input_data)
        
        # 2. 提取 AI 刚刚构思好、但还没按回车执行的 Bash 命令
        command = event.get("tool_input", {}).get("command", "")
        if not command:
            sys.exit(0) # 如果没有抓到命令，安全放行
            
        # 3. 建立嵌入式开发中的【高危命令黑名单】
        dangerous_keywords = [
            "erase_sector",      # 局部擦除
            "mass_erase",        # 全片擦除
            "rm -rf",            # 毁灭性删除
            "mkfs",              # 格式化磁盘
            "dd if=/dev/zero"    # 覆盖式破坏
        ]
        
        # 4. 扫描命令是否命中了黑名单
        for keyword in dangerous_keywords:
            if keyword in command.lower():
                # 【核心拦截机制】
                # 打印到 stderr 的内容会被 Claude Code 捕获，并作为“工具报错信息”反馈给 AI 本人
                print(f"[系统级强制拦截] 警告：检测到高危 Bash 敏感词 '{keyword}'！", file=sys.stderr)
                print(f"你的命令 '{command}' 已触发 PreToolUse 底层安全策略，操作已被物理阻断。", file=sys.stderr)
                print("请重新评估你的烧录/操作逻辑，如果是合理的，请要求用户手动执行。", file=sys.stderr)
                
                # 【极其重要】：退出码非 0 (如 sys.exit(1))，Claude Code 会直接熔断该工具的执行！
                sys.exit(1) 
                
        # 5. 如果扫描无异常，以状态码 0 退出，AI 的命令被放行执行
        sys.exit(0)
        
    except Exception as e:
        # 如果脚本自己抛出异常，为了不阻碍正常开发，选择安全放行
        print(f"安全 Hook 运行异常: {e}", file=sys.stderr)
        sys.exit(0)

if __name__ == "__main__":
    check_command()