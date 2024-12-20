from ui import WinGUI
from tkinter.messagebox import showerror, showinfo, showwarning
import pyautogui
import keyboard
import tkinter
from script import run_script, run_script_line
import threading
import time
import webbrowser
import pickle
import pathlib
import util
from tkinter import filedialog

def thread_func(infos, flag, is_need_miniwin=False):
    time.sleep(5)
    run_script(infos, flag, is_need_miniwin)


def thread_func_line(infos, flag, is_need_miniwin=False):
    time.sleep(5)
    run_script_line(infos, flag, is_need_miniwin)


class TreadFlag():
    def __init__(self, stopped):
        self.stopped = stopped


# 示例下载 https://www.pytk.net/blog/1702564569.html
class Controller:
    # 导入UI类后，替换以下的 object 类型，将获得 IDE 属性提示功能
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
        if pathlib.Path(".listbak").exists():
            with open(".listbak", "rb") as f:
                list_info = pickle.load(f)
            for info in list_info:
                if util.check_script(info):
                    self.ui.tk_list_box_lzatidv1.insert(tkinter.END, info)
        self.last_select = ()
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

    def delete(self, evt):
        select = self.ui.tk_list_box_lzatidv1.curselection()
        if len(select) > 0:
            self.ui.tk_list_box_lzatidv1.delete(*select)

    def start(self, evt):
        if not self.flag.stopped:
            showinfo("运行中", "脚本正在运行，ctrl+o关闭脚本")
            return
        infos = []
        self.update_win_title_select()
        for e in self.ui.tk_list_box_lzatidv1.get(0, tkinter.END):
            bot, message_info, input_rate, work_interval, is_use, is_safe, window_title, x, y, pixel, is_need_postion_check, is_need_auto_position = util.decode_script(
                e)
            if window_title not in self.win_title_list:
                showerror("未检测到聊天框", "聊天框" + "\"" + window_title + "\"" + "未打开")
                return
            info = {
                "bot": util.bot_name[int(bot)],
                "message_info": message_info,
                "input_rate": float(input_rate),
                "work_interval": float(work_interval),
                "is_use": True if is_use == "1" else False,
                "is_safe": True if is_safe == "1" else False,
                "window_title": window_title,
                "x": int(x),
                "y": int(y),
                "pixel": pixel,
                "is_need_postion_check": True if is_need_postion_check == "1" else False,
                "is_need_auto_position": True if is_need_auto_position == "1" else False,
            }
            infos.append(info)
        if len(infos) == 0:
            showerror("", "无任务可执行")
            return
        showinfo("帮助", "将在5秒后开始并行执行任务，请不要在执行过程中关闭群聊窗口，按ctrl+o键结束脚本")
        flag = TreadFlag(stopped=False)
        thread = threading.Thread(target=thread_func, args=(infos, flag, self.ui.tk_check_button_v_m0qc8ysn.get()))
        self.flag = flag
        thread.daemon = True
        thread.start()
        self.set_script_status()

    def start_line(self, evt):
        if not self.flag.stopped:
            showinfo("运行中", "脚本正在运行，ctrl+o关闭脚本")
            return
        infos = []
        self.update_win_title_select()
        for e in self.ui.tk_list_box_lzatidv1.get(0, tkinter.END):
            bot, message_info, input_rate, work_interval, is_use, is_safe, window_title, x, y, pixel, is_need_postion_check, is_need_auto_position = util.decode_script(
                e)
            if window_title not in self.win_title_list:
                showerror("未检测到聊天框", "聊天框" + "\"" + window_title + "\"" + "未打开")
                return
            info = {
                "bot": util.bot_name[int(bot)],
                "message_info": message_info,
                "input_rate": float(input_rate),
                "work_interval": float(work_interval),
                "is_use": True if is_use == "1" else False,
                "is_safe": True if is_safe == "1" else False,
                "window_title": window_title,
                "x": int(x),
                "y": int(y),
                "pixel": pixel,
                "is_need_postion_check": True if is_need_postion_check == "1" else False,
                "is_need_auto_position": True if is_need_auto_position == "1" else False,
            }
            infos.append(info)
        if len(infos) == 0:
            showerror("", "无任务可执行")
            return
        showinfo("帮助", "将在5秒后开始顺序执行任务，请不要在执行过程中关闭群聊窗口，按ctrl+o键结束脚本")
        flag = TreadFlag(stopped=False)
        thread = threading.Thread(target=thread_func_line, args=(infos, flag, self.ui.tk_check_button_v_m0qc8ysn.get()))
        self.flag = flag
        thread.daemon = True
        thread.start()
        self.set_script_status()


    def end(self, evt):
        self.flag.stopped = True
        self.set_script_status()
        showinfo("停止成功", "已清除所有线程")

    def end_hotkey(self):
        self.end("")

    def add(self, evt):
        self.update_win_title_select()
        pixel = self.ui.tk_label_m0bt0vsq.cget("text")
        is_use = "1" if self.ui.tk_check_button_v_m0c03zwf.get() else "0"
        is_safe = "1" if self.ui.tk_check_button_v_m0c04cpe.get() else "0"
        is_need_auto_position = "1" if self.ui.tk_check_button_v_m0g8qf1q.get() else "0"
        window_title = self.win_title_list[self.ui.tk_select_box_m0g8kw6s.current()]
        input_rate = self.ui.tk_input_lzcef2go.get()
        bot = str(self.ui.tk_select_box_lzp2hkct.current())
        message_info = self.ui.tk_input_lzz2tn8b.get()
        is_need_postion_check = "1" if self.ui.tk_check_button_v_m0c59gfd.get() else "0"
        try:
            util.check_float(input_rate)
        except:
            showerror("参数非法", "输入速率必须为大于等于0的小数")
            return
        work_interval = self.ui.tk_input_m0bzrwvq.get()
        try:
            util.check_float(work_interval)
        except:
            showerror("参数非法", "执行间隔必须为大于等于0的小数")
            return
        x = self.ui.tk_input_lzcduh4k.get()
        try:
            util.check_int(x)
        except:
            showerror("参数非法", "定位x必须为大于等于0的整数")
            return
        y = self.ui.tk_input_lzcdpre7.get()
        try:
            util.check_int(y)
        except:
            showerror("参数非法", "定位y必须为大于等于0的整数")
            return
        info = util.encode_script(bot, message_info, input_rate, work_interval, is_use, is_safe, x, y, pixel,
                                  is_need_postion_check, is_need_auto_position, window_title)
        self.ui.tk_list_box_lzatidv1.insert(tkinter.END, info)

    def change(self, evt):
        self.update_win_title_select()
        select = self.ui.tk_list_box_lzatidv1.curselection()
        if len(select) > 0:
            self.ui.tk_list_box_lzatidv1.delete(*select)
            pixel = self.ui.tk_label_m0bt0vsq.cget("text")
            is_use = "1" if self.ui.tk_check_button_v_m0c03zwf.get() else "0"
            is_safe = "1" if self.ui.tk_check_button_v_m0c04cpe.get() else "0"
            is_need_auto_position = "1" if self.ui.tk_check_button_v_m0g8qf1q.get() else "0"
            window_title = self.win_title_list[self.ui.tk_select_box_m0g8kw6s.current()]
            input_rate = self.ui.tk_input_lzcef2go.get()
            bot = str(self.ui.tk_select_box_lzp2hkct.current())
            message_info = self.ui.tk_input_lzz2tn8b.get()
            is_need_postion_check = "1" if self.ui.tk_check_button_v_m0c59gfd.get() else "0"
            try:
                util.check_float(input_rate)
            except:
                showerror("参数非法", "输入速率必须为大于等于0的小数")
                return
            work_interval = self.ui.tk_input_m0bzrwvq.get()
            try:
                util.check_float(work_interval)
            except:
                showerror("参数非法", "执行间隔必须为大于等于0的小数")
                return
            x = self.ui.tk_input_lzcduh4k.get()
            try:
                util.check_int(x)
            except:
                showerror("参数非法", "定位x必须为大于等于0的整数")
                return
            y = self.ui.tk_input_lzcdpre7.get()
            try:
                util.check_int(y)
            except:
                showerror("参数非法", "定位y必须为大于等于0的整数")
                return
            info = util.encode_script(bot, message_info, input_rate, work_interval, is_use, is_safe, x, y, pixel,
                                      is_need_postion_check, is_need_auto_position, window_title)
            self.ui.tk_list_box_lzatidv1.insert(*select, info)
        else:
            showwarning("提示", "请选中元素后修改")

    def on_select_one(self, evt):
        select = self.ui.tk_list_box_lzatidv1.curselection()
        if select:
            self.last_select = select
        else:
            try:
                self.ui.tk_list_box_lzatidv1.selection_set(*self.last_select)
            except:
                pass
        if len(select) > 0:
            self.update_win_title_select()
            info = self.ui.tk_list_box_lzatidv1.get(*select)
            bot, message_info, input_rate, work_interval, is_use, is_safe, window_title, x, y, pixel, is_need_postion_check, is_need_auto_position = util.decode_script(
                info)
            self.ui.tk_label_m0bt0vsq.config(text=pixel)
            self.ui.tk_check_button_v_m0c03zwf.set(is_use)
            self.ui.tk_check_button_v_m0c04cpe.set(is_safe)
            self.ui.tk_check_button_v_m0c59gfd.set(is_need_postion_check)
            self.ui.tk_check_button_v_m0g8qf1q.set(is_need_auto_position)
            self.ui.tk_select_box_lzp2hkct.current(bot)
            if window_title in self.win_title_list:
                self.ui.tk_select_box_m0g8kw6s.current(self.win_title_list.index(window_title))
            else:
                self.ui.tk_select_box_m0g8kw6s.current(0)
                self.ui.tk_check_button_v_m0g8qf1q.set(False)
                showerror("未检测到聊天框", "聊天框" + "\"" + window_title + "\"" + "未打开")
            if self.ui.tk_check_button_v_m0g8qf1q.get():
                self.ui.tk_input_lzcduh4k.configure(state=tkinter.DISABLED)
                self.ui.tk_input_lzcdpre7.configure(state=tkinter.DISABLED)
                if self.ui.tk_check_button_v_m0c59gfd.get():
                    self.ui.tk_check_button_v_m0c59gfd.set(False)
            else:
                self.ui.tk_input_lzcduh4k.configure(state=tkinter.NORMAL)
                self.ui.tk_input_lzcdpre7.configure(state=tkinter.NORMAL)
            self.ui.tk_input_lzz2tn8b.delete(0, tkinter.END)
            self.ui.tk_input_lzz2tn8b.insert(0, message_info)
            self.ui.tk_input_lzcduh4k.delete(0, tkinter.END)
            self.ui.tk_input_lzcdpre7.delete(0, tkinter.END)
            self.ui.tk_input_lzcduh4k.insert(0, x)
            self.ui.tk_input_lzcdpre7.insert(0, y)
            self.ui.tk_input_lzcef2go.delete(0, tkinter.END)
            self.ui.tk_input_lzcef2go.insert(0, input_rate)
            self.ui.tk_input_m0bzrwvq.delete(0, tkinter.END)
            self.ui.tk_input_m0bzrwvq.insert(0, work_interval)

    def save_list(self, evt):
        list_info = self.ui.tk_list_box_lzatidv1.get(0, tkinter.END)
        with open(".listbak", "wb") as f:
            pickle.dump(list_info, f)

    def file_out(self, evt):
        list_info = self.ui.tk_list_box_lzatidv1.get(0, tkinter.END)
        file_path = filedialog.asksaveasfilename(defaultextension=".zsl", filetypes=[("修仙小助手", ".zsl")])
        if file_path:
            with open(file_path, "wb") as f:
                pickle.dump(list_info, f)

    def file_in(self, evt):
        file_path = filedialog.askopenfilename(filetypes=[("修仙小助手", ".zsl")])
        if file_path:
            with open(file_path, "rb") as f:
                list_info = pickle.load(f)
            self.ui.tk_list_box_lzatidv1.delete(0, tkinter.END)
            for info in list_info:
                if util.check_script(info):
                    self.ui.tk_list_box_lzatidv1.insert(tkinter.END, info)


    def set_script_status(self):
        if self.flag.stopped:
            self.ui.tk_label_lzrteudf.config(text="未运行", bootstyle="danger")
        else:
            self.ui.tk_label_lzrteudf.config(text="运行中", bootstyle="success")

    def text_tutorial(self, evt):
        tutorial = '''使用步骤：1、定位qq聊天输入框(请打开qq独立窗口) 2、添加任务至任务列表 3、点击执行任务脚本按钮开始执行
快速入门：简单介绍软件的使用，实现多开自动修炼
进阶教程：实现自动每日任务
定位检查：会对定位处颜色进行检查，避免广告等因素导致脚本错误，重叠的qq输入框无法使用此功能
防封：会对脚本执行进行随机延迟，模拟人的行为，会添加一定的防封策略
热键：ctrl+p：输入框定位， ctrl+o：终止脚本
并行执行：按照执行间隔并行执行任务
顺序执行：按照任务列表中的最大执行间隔顺序执行任务
智能定位：无需手动定位，软件会自动识别输入框的位置
常见问题：1、为什么消息无法发出？请查看您的qq输入框是否设置按enter发送消息。2、为什么热键没有反应？请查看该热键是否与别的软件冲突。3、为什么有时候会艾特错人？请确保bot在群内，并在群里手动艾特并回车，查看是否能艾特到bot，艾特不到可以尝试重启qq或者重开一下q群。
        '''
        showinfo("使用教程", tutorial)

    def video1(self, evt):
        showinfo("入门视频教程", "请在github软件主页的百度网盘链接查看")
        webbrowser.open('https://github.com/WwwwwyDev/asceticism-assistant-QQ')


    def video2(self, evt):
        showinfo("进阶视频教程", "请在github软件主页的百度网盘链接查看")
        webbrowser.open('https://github.com/WwwwwyDev/asceticism-assistant-QQ')

    def update_select_win(self, evt):
        self.update_win_title_select()

    def update_win_title_select(self):
        current_title = util.get_win_title_list("修仙")
        self.win_title_list = current_title
        self.ui.tk_select_box_m0g8kw6s['values'] = current_title

    def check_auto_position(self, evt):
        check_status = self.ui.tk_check_button_v_m0g8qf1q.get()
        if check_status:
            self.ui.tk_input_lzcduh4k.configure(state=tkinter.NORMAL)
            self.ui.tk_input_lzcdpre7.configure(state=tkinter.NORMAL)
        else:
            if self.ui.tk_select_box_m0g8kw6s.current() == 0:
                showerror("开启失败", "当开启智能定位时需要选择一个窗口")
                return
            self.ui.tk_input_lzcduh4k.configure(state=tkinter.DISABLED)
            self.ui.tk_input_lzcdpre7.configure(state=tkinter.DISABLED)
            if self.ui.tk_check_button_v_m0c59gfd.get():
                self.ui.tk_check_button_v_m0c59gfd.set(False)

    def check_win_title(self, evt):
        if self.ui.tk_select_box_m0g8kw6s.current() == 0 and self.ui.tk_check_button_v_m0g8qf1q.get():
            self.ui.tk_check_button_v_m0g8qf1q.set(False)
            self.ui.tk_input_lzcduh4k.configure(state=tkinter.NORMAL)
            self.ui.tk_input_lzcdpre7.configure(state=tkinter.NORMAL)

    def check_is_need_disabled(self, evt):
        auto_position_status = self.ui.tk_check_button_v_m0g8qf1q.get()
        if auto_position_status:
            self.ui.tk_check_button_v_m0c59gfd.set(True)

    def help2(self, evt):
        showinfo("选择窗口帮助",
                 "1、群聊名字需包含\"修仙\"，并打开独立聊天窗口，否则无法识别窗口\n2、当选择窗口后，软件会自动管理窗口，避免由于窗口重叠导致无法正常运行的情况\n3、只有选择了窗口才能使用智能定位功能，如果智能定位无效可以选择手动定位")