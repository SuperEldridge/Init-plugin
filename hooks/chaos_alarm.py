import sys
import os
import platform
import time

def play_piercing_alarm():
    if platform.system() != "Windows":
        return
        
    import winsound
    
    # 读取外部音频文件
    wav_path = os.path.join(os.path.dirname(__file__), "chaos-warning.wav")
    if os.path.exists(wav_path):
        # 【关键修复】：去掉了 SND_ASYNC。
        # 这样程序会“卡”在这里，直到你的 4 秒音频完全播放完毕，才会继续往下走。
        winsound.PlaySound(wav_path, winsound.SND_FILENAME)
        return

    # 保底方案：高频刺耳“嘀嘀嘀”三声（响 1 秒，停 0.3 秒）
    for _ in range(3):
        winsound.Beep(3500, 1000)
        time.sleep(0.3)

try:
    input_data = sys.stdin.read()
    
    # 1. 【时序优化】：先打印警告条，让视觉压迫感先出来！
    print("\n\033[41;97m" + "▇"*75 + "\033[0m", file=sys.stderr)
    print("\033[41;97m ☢️  [致命警告] 限制解除！硬件破坏性压测智能体 Chaos-Tester 已接管终端！ ☢️  \033[0m", file=sys.stderr)
    print("\033[41;97m" + "▇"*75 + "\033[0m\n", file=sys.stderr)
    
    # 2. 播放音频（程序阻塞，直到放完）
    play_piercing_alarm()
    
    # 3. 声音放完，进程退出，Agent 正式开始干活
    sys.exit(0)

except Exception as e:
    sys.exit(0)