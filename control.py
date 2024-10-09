from ui import WinGUI
from tkinter.messagebox import showerror, showinfo
import pyautogui
import keyboard
import tkinter
from script import run_script
import threading
import time
import util

def thread_func(info, flag):
    time.sleep(5)
    run_script(info, flag)


class TreadFlag():
    def __init__(self, stopped):
        self.stopped = stopped

class Controller:

    ui: WinGUI
    def __init__(self):
        pass
    def init(self, ui):
        """
        得到UI实例，对组件进行初始化配置
        """
        self.ui = ui
        # TODO 组件初始化 赋值操作
        self.ui.tk_input_lzcef2go.insert(0, "0.3") 
        self.ui.tk_input_lzz2tn8b.insert(0, "修炼")
        self.ui.tk_input_lzcduh4k.insert(0, "0")
        self.ui.tk_input_lzcdpre7.insert(0, "0")
        self.ui.tk_input_m0bzrwvq.insert(0, "61")
        self.ui.tk_select_box_lzp2hkct.current(0)
        self.ui.tk_select_box_m0g8kw6s.current(0)
        self.update_win_title_select()
        self.flag = TreadFlag(stopped=True)
        self.set_script_status()
        keyboard.add_hotkey("ctrl+p", self.get_position)
        keyboard.add_hotkey("ctrl+o", self.end_hotkey)

    def get_position(self):
        self.ui.tk_input_lzcduh4k.delete(0, tkinter.END)
        self.ui.tk_input_lzcdpre7.delete(0, tkinter.END)
        current_position = pyautogui.position()
        self.ui.tk_label_m0bt0vsq.config(text=util.rgb2hex(pyautogui.pixel(current_position.x, current_position.y)))
        self.ui.tk_input_lzcduh4k.insert(0, str(current_position.x))
        self.ui.tk_input_lzcdpre7.insert(0, str(current_position.y))
    
        
    def start(self,evt):
        if not self.flag.stopped:
            showinfo("运行中", "脚本正在运行，ctrl+o关闭脚本")
            return
        self.update_win_title_select()
        pixel = self.ui.tk_label_m0bt0vsq.cget("text")
        is_use = "1" if self.ui.tk_check_button_v_m0c03zwf.get() else "0"
        is_safe = "1" if self.ui.tk_check_button_v_m0c04cpe.get() else "0"
        is_need_auto_position = "1" if self.ui.tk_check_button_v_m0g8qf1q.get()  else "0"
        window_title = self.win_title_list[self.ui.tk_select_box_m0g8kw6s.current()]
        input_rate = self.ui.tk_input_lzcef2go.get()
        bot = str(self.ui.tk_select_box_lzp2hkct.current())
        message_info = self.ui.tk_input_lzz2tn8b.get()
        is_need_postion_check = "1" if self.ui.tk_check_button_v_m0c59gfd.get() else "0"
        try:
            util.check_float(input_rate)
        except:
            showerror("参数非法","输入速率必须为大于等于0的小数")
            return
        work_interval = self.ui.tk_input_m0bzrwvq.get()
        try:
            util.check_float(work_interval)
        except:
            showerror("参数非法","执行间隔必须为大于等于0的小数")
            return
        x = self.ui.tk_input_lzcduh4k.get()
        try:
            util.check_int(x)
        except:
            showerror("参数非法","定位x必须为大于等于0的整数")
            return
        y = self.ui.tk_input_lzcdpre7.get()
        try:
            util.check_int(y)
        except:
            showerror("参数非法","定位y必须为大于等于0的整数")
            return
        if window_title not in self.win_title_list:
            showerror("未检测到聊天框", "聊天框" + "\"" + window_title + "\"" +"未打开")
            return
        info = {
            "bot": util.bot_name[int(bot)],
            "message_info": message_info,
            "input_rate": float(input_rate),
            "work_interval": float(work_interval),
            "is_use": True if is_use  == "1" else False,
            "is_safe": True if is_safe  == "1" else False,
            "window_title": window_title,
            "x": int(x),
            "y": int(y),
            "pixel": pixel,
            "is_need_postion_check":  True if is_need_postion_check  == "1" else False,
            "is_need_auto_position":  True if is_need_auto_position  == "1" else False,
        }
        showinfo("帮助", "将在5秒后开始执行，请不要在执行过程中关闭群聊窗口，按ctrl+o键结束脚本")
        flag = TreadFlag(stopped=False)
        thread = threading.Thread(target=thread_func, args=(info,flag))
        self.flag = flag
        thread.daemon = True
        thread.start()
        self.set_script_status()


    def end(self,evt):
        self.flag.stopped = True
        self.set_script_status()
        showinfo("停止成功","已清除所有线程")
    
    def end_hotkey(self):
        self.end("")


    def set_script_status(self):
        if self.flag.stopped:
            self.ui.tk_label_lzrteudf.config(text="未运行", bootstyle="danger")
        else:
            self.ui.tk_label_lzrteudf.config(text="运行中", bootstyle="success")


    
    def update_select_win(self,evt):
        self.update_win_title_select()

    def update_win_title_select(self):
        current_title = util.get_win_title_list("修仙")
        self.win_title_list = current_title
        self.ui.tk_select_box_m0g8kw6s['values'] = current_title

    def check_auto_position(self,evt):
        check_status = self.ui.tk_check_button_v_m0g8qf1q.get()
        if check_status:
            self.ui.tk_input_lzcduh4k.configure(state=tkinter.NORMAL)
            self.ui.tk_input_lzcdpre7.configure(state=tkinter.NORMAL)
        else:
            if self.ui.tk_select_box_m0g8kw6s.current() == 0:
                showerror("开启失败","当开启智能定位时需要选择一个窗口")
                return 
            self.ui.tk_input_lzcduh4k.configure(state=tkinter.DISABLED)
            self.ui.tk_input_lzcdpre7.configure(state=tkinter.DISABLED)
            if self.ui.tk_check_button_v_m0c59gfd.get():
                self.ui.tk_check_button_v_m0c59gfd.set(False)

    def check_win_title(self,evt):
        if self.ui.tk_select_box_m0g8kw6s.current() == 0 and self.ui.tk_check_button_v_m0g8qf1q.get():
            self.ui.tk_check_button_v_m0g8qf1q.set(False)
            self.ui.tk_input_lzcduh4k.configure(state=tkinter.NORMAL)
            self.ui.tk_input_lzcdpre7.configure(state=tkinter.NORMAL)

    def check_is_need_disabled(self,evt):
        auto_position_status = self.ui.tk_check_button_v_m0g8qf1q.get()
        if auto_position_status:
            self.ui.tk_check_button_v_m0c59gfd.set(True)

    def help(self,evt):
        showinfo("选择窗口帮助", "1、群聊名字需包含\"修仙\"，并打开独立聊天窗口，否则无法识别窗口\n2、当选择窗口后，软件会自动管理窗口，避免由于窗口重叠导致无法正常运行的情况\n3、只有选择了窗口才能使用智能定位功能，否则需要手动定位")