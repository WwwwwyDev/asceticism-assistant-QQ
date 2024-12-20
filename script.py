import time  
import pyautogui
import pyperclip
import threading
from threading import Lock
import random
import util
import pygetwindow as gw
lock = Lock()

def send_message(positon, content, bot_name, rate = 0.3):
    time.sleep(0.1 + rate/10)
    pyautogui.click(positon[0], positon[1])
    time.sleep(0.1 + rate)
    pyperclip.copy("@" + bot_name)
    time.sleep(0.1 + rate/10)
    pyautogui.hotkey('Ctrl', 'V')
    time.sleep(0.1 + rate)
    pyautogui.press('enter')
    time.sleep(0.1 + rate)
    pyperclip.copy(content)
    time.sleep(0.1 + rate/10)
    pyautogui.hotkey('Ctrl', 'V')
    time.sleep(0.1 + rate)
    pyautogui.press(' ')
    time.sleep(0.1 + rate)
    pyautogui.press('enter')
    time.sleep(0.1 + rate)


def run_task(info, flag, is_need_miniwin = False):
    global lock
    if info['is_use'] == False:
         return
    bot = info["bot"]
    message_info = info['message_info']
    input_rate = info['input_rate']
    is_safe = info['is_safe']
    x = info['x']
    y = info['y']
    pixel = info['pixel']
    is_need_postion_check = info['is_need_postion_check']
    work_interval = info['work_interval']
    window_title = info['window_title']
    is_need_auto_position =  info['is_need_auto_position']
    safe_cnt = random.randint(5, 10)
    safe_cnt2 = random.randint(10, 20)
    safe_cnt3 = random.randint(5, 15)
    win : gw.Win32Window= info["win"]
    while not flag.stopped:
        lock.acquire()
        if win:
            win.restore()
            win.activate()
        if is_need_auto_position and win:
            x = win.bottomleft.x + 110
            y = win.bottomleft.y - 110
        if is_need_postion_check and not is_need_auto_position:
            current_pixel = util.rgb2hex(pyautogui.pixel(x, y))
            if current_pixel != pixel:
                time.sleep(work_interval)
                continue
        safe_rate = 0
        if is_safe:
             safe_rate = random.uniform(input_rate/8,input_rate/4)
        if is_safe:
            if not flag.stopped:
                if safe_cnt == 0:
                    send_message(positon=[x, y], content="我的状态", bot_name=bot, rate=input_rate+safe_rate)
                    safe_cnt = random.randint(5,10)
                else:
                    safe_cnt -= 1
                if safe_cnt2 == 0:
                    send_message(positon=[x, y], content="我的修仙信息", bot_name=bot, rate=input_rate+safe_rate)
                    safe_cnt2 = random.randint(10,20)
                else:
                    safe_cnt2 -= 1
                if safe_cnt3 == 0:
                    send_message(positon=[x, y], content="我的背包", bot_name=bot, rate=input_rate+safe_rate)
                    safe_cnt3 = random.randint(5,15)
                else:
                    safe_cnt3 -= 1
        if not flag.stopped:
            send_message(positon=[x, y], content=message_info, bot_name=bot, rate=input_rate+safe_rate)
        if win and is_need_miniwin:
            win.minimize()
        lock.release()
        time.sleep(work_interval + safe_rate)

def run_script(infos, flag, is_need_miniwin=False):
    for info in infos:
        window_title = info['window_title']
        if window_title != "未选择":
            wins= gw.getWindowsWithTitle(window_title)
            win= None
            if len(wins) >= 1:
                win: gw.Win32Window= wins[0]
                if is_need_miniwin:
                    win.minimize()
            info["win"] = win
        else:
            info["win"] = None

    for info in infos:
        thread = threading.Thread(target=run_task, args=(info,flag,is_need_miniwin))
        thread.daemon = True
        thread.start()
        time.sleep(random.uniform(0,1))

def run_script_line(infos, flag, is_need_miniwin=False):
    max_interval = 0
    for info in infos:
        interval = info["work_interval"]
        info['safe_cnt'] = random.randint(5, 10)
        info['safe_cnt2'] = random.randint(10, 20)
        info['safe_cnt3'] = random.randint(5, 15)
        window_title = info['window_title']
        if window_title != "未选择":
            wins= gw.getWindowsWithTitle(window_title)
            win= None
            if len(wins) >= 1:
                win: gw.Win32Window= wins[0]
                if is_need_miniwin:
                    win.minimize()
            info["win"] = win
        else:
            info["win"] = None
        if interval > max_interval:
            max_interval = interval

    while not flag.stopped:
        sum_rate = 0
        for info in infos:
            bot = info["bot"]
            message_info = info['message_info']
            input_rate = info['input_rate']
            is_safe = info['is_safe']
            x = info['x']
            y = info['y']
            pixel = info['pixel']
            is_need_postion_check = info['is_need_postion_check']
            window_title = info['window_title']
            is_need_auto_position =  info['is_need_auto_position']
            win : gw.Win32Window= info["win"]
            if win:
                win.restore()
                win.activate()
            if is_need_postion_check and not is_need_auto_position:
                current_pixel = util.rgb2hex(pyautogui.pixel(x, y))
                if current_pixel != pixel:
                    continue
            if is_need_auto_position and win:
                x = win.bottomleft.x + 110
                y = win.bottomleft.y - 110
            safe_rate = 0
            if is_safe:
                safe_rate = random.uniform(input_rate/8,input_rate/4)
            if is_safe:
                if not flag.stopped:
                    if info['safe_cnt'] == 0:
                        send_message(positon=[x, y], content="我的状态", bot_name=bot, rate=input_rate+safe_rate)
                        sum_rate += (input_rate+safe_rate) * 6.2
                        info['safe_cnt'] = random.randint(5,10)
                    else:
                        info['safe_cnt'] -= 1
                    if info['safe_cnt2'] == 0:
                        send_message(positon=[x, y], content="我的修仙信息", bot_name=bot, rate=input_rate+safe_rate)
                        sum_rate += (input_rate+safe_rate) * 6.2
                        info['safe_cnt2'] = random.randint(10,20)
                    else:
                        info['safe_cnt2'] -= 1
                    if info['safe_cnt3'] == 0:
                        send_message(positon=[x, y], content="我的背包", bot_name=bot, rate=input_rate+safe_rate)
                        sum_rate += (input_rate+safe_rate) * 6.2
                        info['safe_cnt3'] = random.randint(5,15)
                    else:
                        info['safe_cnt3'] -= 1
            if not flag.stopped:
                send_message(positon=[x, y], content=message_info, bot_name=bot, rate=input_rate+safe_rate)
                sum_rate += (input_rate+safe_rate) * 6.2
            if win and is_need_miniwin:
                win.minimize()
        sleep_time = max_interval-sum_rate
        if sleep_time < 0:
            sleep_time = 0
        time.sleep(sleep_time)