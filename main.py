import keyboard  
import time  
import pyautogui
import pyperclip
import random
# 定义一个变量来追踪是否应该执行代码  
should_run = False  


def toggle_execution(e  ):  
    global should_run  
    # 切换should_run变量的状态  
    should_run = not should_run  
    print("执行状态已切换:", "开始执行" if should_run else "停止执行")  

def send_message():  
    # 输入消息  
    pyperclip.copy("@xiaoxiao")
    pyautogui.hotkey('Ctrl', 'V')
    time.sleep(0.3)
    pyautogui.press('enter')
    time.sleep(0.3)
    pyperclip.copy("修炼")
    pyautogui.hotkey('Ctrl', 'V')
    time.sleep(0.3)
    pyautogui.press(' ')
    time.sleep(0.3)
    pyautogui.press('enter')
    time.sleep(0.3)

# 监听空格键  
keyboard.on_press_key("space", toggle_execution)  
  
print("程序已启动，按空格键开始/停止执行代码。")  
  
# 保持程序运行  
while True:  
    time.sleep(1)
    if should_run:  
        # 要执行的代码  
        send_message()
        time.sleep(random.randint(61, 64)) 