from tkinter import *
import webbrowser
from ttkbootstrap import *
from ttkbootstrap.constants import *
from util import bot_name

class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.menubar = Menu(self,tearoff=False)
        self.tk_input_lzcef2go = self.__tk_input_lzcef2go(self)
        self.tk_label_lzceirtt = self.__tk_label_lzceirtt(self)
        self.tk_label_lzcenb7o = self.__tk_label_lzcenb7o(self)
        self.tk_select_box_lzp2hkct = self.__tk_select_box_lzp2hkct(self)
        self.tk_label_lzumekad = self.__tk_label_lzumekad(self)
        self.tk_label_lzumfgbg = self.__tk_label_lzumfgbg(self)
        self.tk_input_lzz2tn8b = self.__tk_input_lzz2tn8b(self)
        self.tk_label_m0bzr5au = self.__tk_label_m0bzr5au(self)
        self.tk_input_m0bzrwvq = self.__tk_input_m0bzrwvq(self)
        self.tk_label_m0bzs1ie = self.__tk_label_m0bzs1ie(self)
        self.tk_check_button_m0c04cpe = self.__tk_check_button_m0c04cpe(self)
        self.tk_label_frame_m0g8gr89 = self.__tk_label_frame_m0g8gr89(self)
        self.tk_select_box_m0g8kw6s = self.__tk_select_box_m0g8kw6s( self.tk_label_frame_m0g8gr89) 
        self.tk_label_frame_m0c1cupj = self.__tk_label_frame_m0c1cupj( self.tk_label_frame_m0g8gr89) 
        self.tk_label_m0bt0vsq = self.__tk_label_m0bt0vsq( self.tk_label_frame_m0c1cupj) 
        self.tk_input_lzcdpre7 = self.__tk_input_lzcdpre7( self.tk_label_frame_m0c1cupj) 
        self.tk_label_lzcdqs5e = self.__tk_label_lzcdqs5e( self.tk_label_frame_m0c1cupj) 
        self.tk_label_lzcdpzvp = self.__tk_label_lzcdpzvp( self.tk_label_frame_m0c1cupj) 
        self.tk_input_lzcduh4k = self.__tk_input_lzcduh4k( self.tk_label_frame_m0c1cupj) 
        self.tk_check_button_m0c59gfd = self.__tk_check_button_m0c59gfd( self.tk_label_frame_m0c1cupj) 
        self.tk_check_button_m0g8qf1q = self.__tk_check_button_m0g8qf1q( self.tk_label_frame_m0c1cupj) 
        self.tk_label_m0g8lgzm = self.__tk_label_m0g8lgzm( self.tk_label_frame_m0g8gr89) 
        self.tk_button_m0g8uipe = self.__tk_button_m0g8uipe( self.tk_label_frame_m0g8gr89) 
        self.tk_label_lzrteudf = self.__tk_label_lzrteudf(self)
        self.tk_button_lzatv5gr = self.__tk_button_lzatv5gr(self)
        self.tk_button_lzb1t8nh = self.__tk_button_lzb1t8nh(self)
        self.tk_label_lzrtdzsr = self.__tk_label_lzrtdzsr(self)
        self.tk_button_m21i0hq4 = self.__tk_button_m21i0hq4(self)
        self.tk_check_button_m0c04cpe, self.tk_check_button_v_m0c04cpe = self.__tk_check_button_m0c04cpe(self) 
        self.tk_check_button_m0c59gfd, self.tk_check_button_v_m0c59gfd = self.__tk_check_button_m0c59gfd(self.tk_label_frame_m0c1cupj)
        self.tk_check_button_m0g8qf1q, self.tk_check_button_v_m0g8qf1q= self.__tk_check_button_m0g8qf1q(self.tk_label_frame_m0c1cupj)  
    def __win(self):
        self.title("修仙小助手")
        # 设置窗口大小、居中
        width = 370
        height = 565
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        
        self.resizable(width=False, height=False)
        
    def scrollbar_autohide(self,vbar, hbar, widget):
        """自动隐藏滚动条"""
        def show():
            if vbar: vbar.lift(widget)
            if hbar: hbar.lift(widget)
        def hide():
            if vbar: vbar.lower(widget)
            if hbar: hbar.lower(widget)
        hide()
        widget.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Leave>", lambda e: hide())
        if hbar: hbar.bind("<Enter>", lambda e: show())
        if hbar: hbar.bind("<Leave>", lambda e: hide())
        widget.bind("<Leave>", lambda e: hide())
    
    def v_scrollbar(self,vbar, widget, x, y, w, h, pw, ph):
        widget.configure(yscrollcommand=vbar.set)
        vbar.config(command=widget.yview)
        vbar.place(relx=(w + x) / pw, rely=y / ph, relheight=h / ph, anchor='ne')
    def h_scrollbar(self,hbar, widget, x, y, w, h, pw, ph):
        widget.configure(xscrollcommand=hbar.set)
        hbar.config(command=widget.xview)
        hbar.place(relx=x / pw, rely=(y + h) / ph, relwidth=w / pw, anchor='sw')
    def create_bar(self,master, widget,is_vbar,is_hbar, x, y, w, h, pw, ph):
        vbar, hbar = None, None
        if is_vbar:
            vbar = Scrollbar(master)
            self.v_scrollbar(vbar, widget, x, y, w, h, pw, ph)
        if is_hbar:
            hbar = Scrollbar(master, orient="horizontal")
            self.h_scrollbar(hbar, widget, x, y, w, h, pw, ph)
        self.scrollbar_autohide(vbar, hbar, widget)
    def __tk_input_lzcef2go(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=128, y=101, width=78, height=35)
        return ipt
    def __tk_label_lzceirtt(self,parent):
        label = Label(parent,text="消息输入速度",anchor="center", )
        label.place(x=14, y=101, width=107, height=35)
        return label
    def __tk_label_lzcenb7o(self,parent):
        label = Label(parent,text="秒",anchor="center", )
        label.place(x=211, y=102, width=41, height=35)
        return label
    def __tk_select_box_lzp2hkct(self,parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = bot_name
        cb.place(x=126, y=11, width=125, height=35)
        return cb
    def __tk_label_lzumekad(self,parent):
        label = Label(parent,text="机器人",anchor="center", )
        label.place(x=13, y=10, width=106, height=35)
        return label
    def __tk_label_lzumfgbg(self,parent):
        label = Label(parent,text="挂机信息",anchor="center", )
        label.place(x=14, y=55, width=106, height=35)
        return label
    def __tk_input_lzz2tn8b(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=126, y=55, width=125, height=35)
        return ipt
    def __tk_label_m0bzr5au(self,parent):
        label = Label(parent,text="执行间隔",anchor="center", )
        label.place(x=14, y=146, width=107, height=35)
        return label
    def __tk_input_m0bzrwvq(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=128, y=146, width=78, height=35)
        return ipt
    def __tk_label_m0bzs1ie(self,parent):
        label = Label(parent,text="秒",anchor="center", )
        label.place(x=212, y=146, width=41, height=35)
        return label
    def __tk_check_button_m0c04cpe(self,parent):
        cb_v = BooleanVar()
        cb_v.set(False)
        cb = Checkbutton(parent,text="防封", variable=cb_v, bootstyle="round-toggle")
        cb.place(x=261, y=85, width=92, height=44)
        return cb, cb_v
    def __tk_label_frame_m0g8gr89(self,parent):
        frame = LabelFrame(parent,text="窗口配置",)
        frame.place(x=5, y=196, width=358, height=210)
        return frame
    def __tk_select_box_m0g8kw6s(self,parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ("未选择")
        cb.place(x=102, y=9, width=197, height=37)
        return cb
    def __tk_label_frame_m0c1cupj(self,parent):
        frame = LabelFrame(parent,text="输入框定位（ctrl+p)",)
        frame.place(x=11, y=57, width=338, height=125)
        return frame
    def __tk_label_m0bt0vsq(self,parent):
        label = Label(parent,text="e3ecff",anchor="center", )
        label.place(x=0, y=0, width=0, height=0)
        return label
    def __tk_input_lzcdpre7(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=150, y=31, width=51, height=35)
        return ipt
    def __tk_label_lzcdqs5e(self,parent):
        label = Label(parent,text="y",anchor="center", )
        label.place(x=107, y=31, width=38, height=35)
        return label
    def __tk_label_lzcdpzvp(self,parent):
        label = Label(parent,text="x",anchor="center", )
        label.place(x=5, y=31, width=38, height=35)
        return label
    def __tk_input_lzcduh4k(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=48, y=31, width=54, height=35)
        return ipt
    def __tk_check_button_m0c59gfd(self,parent):
        cb_v = BooleanVar()
        cb_v.set(False)
        cb = Checkbutton(parent,text="定位检查",variable=cb_v, bootstyle="round-toggle")
        cb.place(x=210, y=1, width=120, height=44)
        return cb, cb_v
    def __tk_check_button_m0g8qf1q(self,parent):
        cb_v = BooleanVar()
        cb_v.set(False)
        cb = Checkbutton(parent,text="智能定位", variable=cb_v, bootstyle="round-toggle")
        cb.place(x=210, y=56, width=120, height=44)
        return cb, cb_v
    def __tk_label_m0g8lgzm(self,parent):
        label = Label(parent,text="选择窗口",anchor="center", )
        label.place(x=10, y=8, width=91, height=34)
        return label
    def __tk_button_m0g8uipe(self,parent):
        btn = Button(parent, text="?", takefocus=False,)
        btn.place(x=312, y=10, width=34, height=30)
        return btn
    def __tk_label_lzrteudf(self,parent):
        label = Label(parent,text="未运行",anchor="w", )
        label.place(x=186, y=480, width=118, height=35)
        return label
    def __tk_button_lzatv5gr(self,parent):
        btn = Button(parent, text="开始执行", takefocus=False,bootstyle="success")
        btn.place(x=36, y=425, width=112, height=36)
        return btn
    def __tk_button_lzb1t8nh(self,parent):
        btn = Button(parent, text="终止运行", takefocus=False,bootstyle="danger")
        btn.place(x=210, y=425, width=112, height=36)
        return btn
    def __tk_label_lzrtdzsr(self,parent):
        label = Label(parent,text="脚本运行状态",anchor="center", )
        label.place(x=70, y=480, width=112, height=35)
        return label
    def __tk_button_m21i0hq4(self,parent):
        btn = Label(parent, text="github开源地址", foreground="blue", cursor='hand2')
        btn.place(x=120, y=518, width=133, height=36)
        return btn
    
class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.__style_config()
        self.ctl.init(self)
    
    @staticmethod
    def cut(editor, event=None):
        editor.event_generate("<<Cut>>")
    @staticmethod
    def copy(editor, event=None):
        editor.event_generate("<<Copy>>")
    @staticmethod
    def paste(editor, event=None):
        editor.event_generate('<<Paste>>')

    def rightKey(self, event, editor):
        self.menubar.delete(0,END)
        self.menubar.add_command(label='复制',command=lambda:Win.copy(editor))
        self.menubar.add_command(label='粘贴',command=lambda:Win.paste(editor))
        self.menubar.add_command(label='剪切',command=lambda:Win.cut(editor))
        self.menubar.post(event.x_root,event.y_root)

    def __event_bind(self):
        self.tk_button_lzatv5gr.bind('<Button>',self.ctl.start)
        self.tk_button_lzb1t8nh.bind('<Button>',self.ctl.end)        
        self.tk_button_m0g8uipe.bind('<Button>',self.ctl.help)
        self.tk_input_lzz2tn8b.bind("<Button-3>", lambda x: self.rightKey(x, self.tk_input_lzz2tn8b))
        self.tk_input_lzcdpre7.bind("<Button-3>", lambda x: self.rightKey(x, self.tk_input_lzcdpre7))
        self.tk_input_lzcef2go.bind("<Button-3>", lambda x: self.rightKey(x, self.tk_input_lzcef2go))
        self.tk_input_lzcduh4k.bind("<Button-3>", lambda x: self.rightKey(x, self.tk_input_lzcduh4k))
        self.tk_input_m0bzrwvq.bind("<Button-3>", lambda x: self.rightKey(x, self.tk_input_m0bzrwvq))
        self.tk_select_box_m0g8kw6s.bind('<Button>',self.ctl.update_select_win)
        self.tk_check_button_m0g8qf1q.bind('<Button>',self.ctl.check_auto_position)
        self.tk_check_button_m0c59gfd.bind('<Button>',self.ctl.check_is_need_disabled)
        self.tk_select_box_m0g8kw6s.bind("<<ComboboxSelected>>", self.ctl.check_win_title)
        self.tk_button_m21i0hq4.bind('<Button>', lambda _: webbrowser.open('https://github.com/WwwwwyDev/asceticism-assistant-QQ'))
    def __style_config(self):
        pass
if __name__ == "__main__":
    win = WinGUI()
    win.mainloop()