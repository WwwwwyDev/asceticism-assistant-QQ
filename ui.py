import webbrowser
from tkinter import *
from ttkbootstrap import *
from ttkbootstrap.constants import *

class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.menubar = Menu(self,tearoff=False)
        self.tk_label_frame_lzcdutum = self.__tk_label_frame_lzcdutum(self)
        self.tk_input_lzcef2go = self.__tk_input_lzcef2go( self.tk_label_frame_lzcdutum)
        self.tk_label_lzceirtt = self.__tk_label_lzceirtt( self.tk_label_frame_lzcdutum)
        self.tk_label_lzcenb7o = self.__tk_label_lzcenb7o( self.tk_label_frame_lzcdutum)
        self.tk_button_lzcf1a8e = self.__tk_button_lzcf1a8e( self.tk_label_frame_lzcdutum)
        self.tk_button_lzgfuvek = self.__tk_button_lzgfuvek( self.tk_label_frame_lzcdutum)
        self.tk_select_box_lzp2hkct = self.__tk_select_box_lzp2hkct( self.tk_label_frame_lzcdutum)
        self.tk_label_lzumekad = self.__tk_label_lzumekad( self.tk_label_frame_lzcdutum)
        self.tk_label_lzumfgbg = self.__tk_label_lzumfgbg( self.tk_label_frame_lzcdutum)
        self.tk_input_lzz2tn8b = self.__tk_input_lzz2tn8b( self.tk_label_frame_lzcdutum)
        self.tk_label_m0bzr5au = self.__tk_label_m0bzr5au( self.tk_label_frame_lzcdutum)
        self.tk_input_m0bzrwvq = self.__tk_input_m0bzrwvq( self.tk_label_frame_lzcdutum)
        self.tk_label_m0bzs1ie = self.__tk_label_m0bzs1ie( self.tk_label_frame_lzcdutum)
        self.tk_check_button_m0c03zwf = self.__tk_check_button_m0c03zwf( self.tk_label_frame_lzcdutum)
        self.tk_check_button_m0c04cpe = self.__tk_check_button_m0c04cpe( self.tk_label_frame_lzcdutum)
        self.tk_label_frame_m0g8gr89 = self.__tk_label_frame_m0g8gr89( self.tk_label_frame_lzcdutum)
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
        self.tk_label_lzchquhe = self.__tk_label_lzchquhe(self)
        self.tk_button_lzatlxij = self.__tk_button_lzatlxij(self)
        self.tk_list_box_lzatidv1 = self.__tk_list_box_lzatidv1(self)
        self.tk_button_lzkl69k2 = self.__tk_button_lzkl69k2(self)
        self.tk_label_m0bu4u1a = self.__tk_label_m0bu4u1a(self)
        self.tk_label_frame_m0bzixj4 = self.__tk_label_frame_m0bzixj4(self)
        self.tk_button_m0bzktof = self.__tk_button_m0bzktof( self.tk_label_frame_m0bzixj4)
        self.tk_button_m0bzkv4f = self.__tk_button_m0bzkv4f( self.tk_label_frame_m0bzixj4)
        self.tk_button_m0c8ja0z = self.__tk_button_m0c8ja0z( self.tk_label_frame_m0bzixj4)
        self.tk_label_frame_m0bzspo0 = self.__tk_label_frame_m0bzspo0(self)
        self.tk_label_lzrteudf = self.__tk_label_lzrteudf( self.tk_label_frame_m0bzspo0)
        self.tk_button_lzatv5gr = self.__tk_button_lzatv5gr( self.tk_label_frame_m0bzspo0)
        self.tk_button_lzb1t8nh = self.__tk_button_lzb1t8nh( self.tk_label_frame_m0bzspo0)
        self.tk_label_lzrtdzsr = self.__tk_label_lzrtdzsr( self.tk_label_frame_m0bzspo0)
        self.tk_button_m0euqevt = self.__tk_button_m0euqevt( self.tk_label_frame_m0bzspo0)
        self.tk_check_button_m0qc8ysn = self.__tk_check_button_m0qc8ysn( self.tk_label_frame_m0bzspo0)
        self.tk_button_m0ew1isb = self.__tk_button_m0ew1isb(self)
        self.tk_button_m0ew1uxv = self.__tk_button_m0ew1uxv(self)
        self.tk_check_button_m0c03zwf, self.tk_check_button_v_m0c03zwf = self.__tk_check_button_m0c03zwf( self.tk_label_frame_lzcdutum)
        self.tk_check_button_m0c04cpe, self.tk_check_button_v_m0c04cpe = self.__tk_check_button_m0c04cpe( self.tk_label_frame_lzcdutum)
        self.tk_check_button_m0c59gfd, self.tk_check_button_v_m0c59gfd = self.__tk_check_button_m0c59gfd( self.tk_label_frame_m0c1cupj)
        self.tk_check_button_m0g8qf1q, self.tk_check_button_v_m0g8qf1q= self.__tk_check_button_m0g8qf1q( self.tk_label_frame_m0c1cupj)
        self.tk_check_button_m0qc8ysn, self.tk_check_button_v_m0qc8ysn = self.__tk_check_button_m0qc8ysn( self.tk_label_frame_m0bzspo0)

    def __win(self):
        self.title("修仙小助手")
        # 设置窗口大小、居中
        width = 813
        height = 515
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)

        self.resizable(width=False, height=False)

    def scrollbar_autohide(self, vbar, hbar, widget):
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

    def v_scrollbar(self, vbar, widget, x, y, w, h, pw, ph):
        widget.configure(yscrollcommand=vbar.set)
        vbar.config(command=widget.yview)
        vbar.place(relx=(w + x) / pw, rely=y / ph, relheight=h / ph, anchor='ne')

    def h_scrollbar(self, hbar, widget, x, y, w, h, pw, ph):
        widget.configure(xscrollcommand=hbar.set)
        hbar.config(command=widget.xview)
        hbar.place(relx=x / pw, rely=(y + h) / ph, relwidth=w / pw, anchor='sw')

    def create_bar(self, master, widget, is_vbar, is_hbar, x, y, w, h, pw, ph):
        vbar, hbar = None, None
        if is_vbar:
            vbar = Scrollbar(master)
            self.v_scrollbar(vbar, widget, x, y, w, h, pw, ph)
        if is_hbar:
            hbar = Scrollbar(master, orient="horizontal")
            self.h_scrollbar(hbar, widget, x, y, w, h, pw, ph)
        self.scrollbar_autohide(vbar, hbar, widget)

    def __tk_label_frame_lzcdutum(self,parent):
        frame = LabelFrame(parent,text="添加任务",)
        frame.place(x=233, y=14, width=362, height=490)
        return frame
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
    def __tk_button_lzcf1a8e(self,parent):
        btn = Button(parent, text="添加", takefocus=False,)
        btn.place(x=48, y=424, width=95, height=35)
        return btn
    def __tk_button_lzgfuvek(self,parent):
        btn = Button(parent, text="修改", takefocus=False,)
        btn.place(x=199, y=424, width=95, height=35)
        return btn
    def __tk_select_box_lzp2hkct(self,parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ("小小","汐汐酱","一念成仙","小北")
        cb.place(x=124, y=11, width=125, height=35)
        return cb
    def __tk_label_lzumekad(self,parent):
        label = Label(parent,text="机器人",anchor="center", )
        label.place(x=14, y=11, width=106, height=35)
        return label
    def __tk_label_lzumfgbg(self,parent):
        label = Label(parent,text="挂机信息",anchor="center", )
        label.place(x=14, y=55, width=106, height=35)
        return label
    def __tk_input_lzz2tn8b(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=124, y=55, width=125, height=35)
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
    def __tk_check_button_m0c03zwf(self,parent):
        cb_v = BooleanVar()
        cb_v.set(True)
        cb = Checkbutton(parent, text="启用", variable=cb_v, bootstyle="round-toggle")
        cb.place(x=262, y=23, width=92, height=44)
        return cb, cb_v
    def __tk_check_button_m0c04cpe(self,parent):
        cb_v = BooleanVar()
        cb_v.set(False)
        cb = Checkbutton(parent, text="防封", variable=cb_v, bootstyle="round-toggle")
        cb.place(x=261, y=85, width=92, height=44)
        return cb, cb_v
    def __tk_label_frame_m0g8gr89(self,parent):
        frame = LabelFrame(parent,text="窗口配置",)
        frame.place(x=5, y=191, width=351, height=215)
        return frame
    def __tk_select_box_m0g8kw6s(self,parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ("未选择")
        cb.place(x=102, y=9, width=197, height=37)
        return cb
    def __tk_label_frame_m0c1cupj(self,parent):
        frame = LabelFrame(parent,text="输入框定位（ctrl+p)",)
        frame.place(x=5, y=58, width=338, height=125)
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
        cb = Checkbutton(parent, text="定位检查", variable=cb_v, bootstyle="round-toggle")
        cb.place(x=210, y=1, width=120, height=44)
        return cb, cb_v
    def __tk_check_button_m0g8qf1q(self,parent):
        cb_v = BooleanVar()
        cb_v.set(False)
        cb = Checkbutton(parent, text="智能定位", variable=cb_v, bootstyle="round-toggle")
        cb.place(x=210, y=56, width=120, height=44)
        return cb, cb_v
    def __tk_label_m0g8lgzm(self,parent):
        label = Label(parent,text="选择窗口",anchor="center", )
        label.place(x=10, y=8, width=91, height=34)
        return label
    def __tk_button_m0g8uipe(self,parent):
        btn = Button(parent, text="?", takefocus=False,bootstyle="warning-outline")
        btn.place(x=312, y=10, width=34, height=30)
        return btn
    def __tk_label_lzchquhe(self,parent):
        label = Label(parent, text="github开源地址", foreground="blue", cursor='hand2', anchor="center")
        label.place(x=47, y=451, width=134, height=35)
        return label
    def __tk_button_lzatlxij(self,parent):
        btn = Button(parent, text="删除", takefocus=False,bootstyle="danger")
        btn.place(x=25, y=343, width=77, height=35)
        return btn
    def __tk_list_box_lzatidv1(self,parent):
        lb = Listbox(parent)

        lb.place(x=8, y=44, width=210, height=276)
        self.create_bar(parent, lb, True, True,8, 44, 210,276,813,515)
        return lb
    def __tk_button_lzkl69k2(self,parent):
        btn = Button(parent, text="保存", takefocus=False,)
        btn.place(x=134, y=343, width=77, height=35)
        return btn
    def __tk_label_m0bu4u1a(self,parent):
        label = Label(parent,text="任务列表",anchor="center", )
        label.place(x=49, y=7, width=116, height=30)
        return label
    def __tk_label_frame_m0bzixj4(self,parent):
        frame = LabelFrame(parent,text="教程",)
        frame.place(x=611, y=10, width=191, height=172)
        return frame
    def __tk_button_m0bzktof(self,parent):
        btn = Button(parent, text="快速入门", takefocus=False,)
        btn.place(x=46, y=54, width=100, height=35)
        return btn
    def __tk_button_m0bzkv4f(self,parent):
        btn = Button(parent, text="进阶教程", takefocus=False,)
        btn.place(x=46, y=103, width=100, height=36)
        return btn
    def __tk_button_m0c8ja0z(self,parent):
        btn = Button(parent, text="文字教程", takefocus=False,)
        btn.place(x=46, y=5, width=100, height=35)
        return btn
    def __tk_label_frame_m0bzspo0(self,parent):
        frame = LabelFrame(parent,text="执行任务",)
        frame.place(x=612, y=196, width=188, height=305)
        return frame
    def __tk_label_lzrteudf(self,parent):
        label = Label(parent,text="未运行",anchor="center", )
        label.place(x=33, y=243, width=118, height=35)
        return label
    def __tk_button_lzatv5gr(self,parent):
        btn = Button(parent, text="并行执行", takefocus=False, bootstyle="success")
        btn.place(x=34, y=7, width=112, height=36)
        return btn
    def __tk_button_lzb1t8nh(self,parent):
        btn = Button(parent, text="终止脚本", takefocus=False, bootstyle="danger")
        btn.place(x=34, y=157, width=112, height=36)
        return btn
    def __tk_label_lzrtdzsr(self,parent):
        label = Label(parent,text="脚本运行状态",anchor="center", )
        label.place(x=34, y=202, width=112, height=35)
        return label
    def __tk_button_m0euqevt(self,parent):
        btn = Button(parent, text="顺序执行", takefocus=False, bootstyle="success")
        btn.place(x=34, y=66, width=112, height=36)
        return btn
    def __tk_check_button_m0qc8ysn(self,parent):
        cb_v = BooleanVar()
        cb_v.set(False)
        cb = Checkbutton(parent, text="自动最小化", variable=cb_v)
        cb.place(x=40, y=113, width=141, height=37)
        return cb, cb_v
    def __tk_button_m0ew1isb(self,parent):
        btn = Button(parent, text="导出", takefocus=False,)
        btn.place(x=25, y=402, width=77, height=35)
        return btn
    def __tk_button_m0ew1uxv(self,parent):
        btn = Button(parent, text="导入", takefocus=False,)
        btn.place(x=134, y=403, width=77, height=35)
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
        self.tk_button_lzatlxij.bind('<Button>',self.ctl.delete)
        self.tk_button_lzatv5gr.bind('<Button>',self.ctl.start)
        self.tk_button_m0euqevt.bind('<Button>',self.ctl.start_line)
        self.tk_button_lzb1t8nh.bind('<Button>',self.ctl.end)
        self.tk_button_lzcf1a8e.bind('<Button>',self.ctl.add)
        self.tk_button_lzgfuvek.bind('<Button>',self.ctl.change)
        self.tk_button_lzkl69k2.bind('<Button>',self.ctl.save_list)
        self.tk_button_m0ew1isb.bind('<Button>',self.ctl.file_out)
        self.tk_button_m0ew1uxv.bind('<Button>',self.ctl.file_in)
        self.tk_button_m0c8ja0z.bind('<Button>',self.ctl.text_tutorial)
        self.tk_button_m0bzktof.bind('<Button>',self.ctl.video1)
        self.tk_button_m0bzkv4f.bind('<Button>',self.ctl.video2)
        self.tk_input_lzz2tn8b.bind("<Button-3>", lambda x: self.rightKey(x, self.tk_input_lzz2tn8b))
        self.tk_input_lzcdpre7.bind("<Button-3>", lambda x: self.rightKey(x, self.tk_input_lzcdpre7))
        self.tk_input_lzcef2go.bind("<Button-3>", lambda x: self.rightKey(x, self.tk_input_lzcef2go))
        self.tk_input_lzcduh4k.bind("<Button-3>", lambda x: self.rightKey(x, self.tk_input_lzcduh4k))
        self.tk_input_m0bzrwvq.bind("<Button-3>", lambda x: self.rightKey(x, self.tk_input_m0bzrwvq))
        self.tk_list_box_lzatidv1.bind('<<ListboxSelect>>',self.ctl.on_select_one)
        self.tk_select_box_m0g8kw6s.bind('<Button>',self.ctl.update_select_win)
        self.tk_check_button_m0g8qf1q.bind('<Button>',self.ctl.check_auto_position)
        self.tk_check_button_m0c59gfd.bind('<Button>',self.ctl.check_is_need_disabled)
        self.tk_select_box_m0g8kw6s.bind("<<ComboboxSelected>>", self.ctl.check_win_title)
        self.tk_button_m0g8uipe.bind('<Button>',self.ctl.help2)
        self.tk_label_lzchquhe.bind('<Button>',
                                     lambda _: webbrowser.open('https://github.com/WwwwwyDev/asceticism-assistant-QQ'))
        pass
    def __style_config(self):
        pass
if __name__ == "__main__":
    win = WinGUI()
    win.mainloop()