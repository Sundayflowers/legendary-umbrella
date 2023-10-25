"""开发画图软件的菜单"""
from tkinter.colorchooser import askcolor
from tkinter.filedialog import askopenfile
from tkinter.filedialog import asksaveasfilename
from tkinter import *
from tkinter import messagebox
import random

win_width=900; win_height=450;

class Application(Frame):


    def __init__(self, master = None, bgcolor="#FFFFFF"):
        super(). __init__(master)
        self.drawpad = None
        self.master = master
        self.pack()
        self.x = 0
        self.y = 0
        self.fgcolor = "#FF0000"
        self.bgcolor = bgcolor
        self.crateWidget()

    def crateWidget(self):
        # 创建画板
        self.drawpad = Canvas(root, width=win_width, height=win_height*0.9, bg=self.bgcolor)
        self.drawpad.pack()

        # 创建按钮
        bnt_start = Button(root, text="开始", name="start")
        bnt_start.pack(side="left", padx=10)
        bnt_pen = Button(root, text="画笔", name="pen")
        bnt_pen.pack(side="left", padx=10)
        bnt_rect = Button(root, text="矩形", name="rect")
        bnt_rect.pack(side="left", padx=10)
        bnt_clear = Button(root, text="清屏", name="clear")
        bnt_clear.pack(side="left", padx=10)
        bnt_eraser = Button(root, text="橡皮擦", name="eraser")
        bnt_eraser.pack(side="left", padx=10)
        bnt_line = Button(root, text="直线", name="line")
        bnt_line.pack(side="left", padx=10)
        bnt_lineArrow = Button(root, text="箭头直线", name="lineArrow")
        bnt_lineArrow.pack(side="left", padx=10)
        bnt_color = Button(root, text="颜色", name="color")
        bnt_color.pack(side="left", padx=10)
        # 增加事件处理
        bnt_pen.bind_class("Button", "<1>", self.eventManger)
        # 增加画笔颜色快捷键
        root.bind("<KeyPress-r>", self.kuaijiejian)
        root.bind("<KeyPress-g>", self.kuaijiejian)
        root.bind("<KeyPress-y>", self.kuaijiejian)

    def eventManger(self, event):
        name = event.widget.winfo_name()
        print(name)
        if name == "line":
            self.drawpad.bind("<ButtonPress-1>", self.get_start)
            self.drawpad.bind("<ButtonRelease-1>", self.myline)
        elif name == "lineArrow":
            self.drawpad.bind("<ButtonPress-1>", self.get_startArrow)
            self.drawpad.bind("<ButtonRelease-1>", self.mylineArrow)
        elif name == "rect":
            self.drawpad.bind("<ButtonPress-1>", self.get_startRect)
            self.drawpad.bind("<ButtonRelease-1>", self.mylineRect)
        elif name == "pen":
            self.drawpad.bind("<ButtonPress-1>", self.get_startPen)
            self.drawpad.bind("<ButtonRelease-1>", self.mylinePen)
        elif name == "eraser":
            self.drawpad.bind("<Button-1>", self.activate_eraser)
        elif name == "clear":
            self.drawpad.delete("all")
        elif name == "color":
            c = askcolor(color=self.fgcolor, title="选择改变画笔颜色")
            self.fgcolor = c[1]

    def get_start(self, event):
        self.x = event.x
        self.y = event.y

    def myline(self, event):
        x2, y2 = event.x, event.y
        self.drawpad.create_line(self.x, self.y, x2, y2, fill=self.fgcolor)

    def get_startArrow(self, event):
        self.x = event.x
        self.y = event.y

    def mylineArrow(self, event):
        x2, y2 = event.x, event.y
        self.drawpad.create_line(self.x, self.y, x2, y2, fill=self.fgcolor, arrow="last")


    def get_startRect(self, event):
        self.x = event.x
        self.y = event.y

    def mylineRect(self, event):
        x2, y2 = event.x, event.y
        self.drawpad.create_rectangle(self.x, self.y, x2, y2, outline=self.fgcolor, )

    def get_startPen(self, event):
        self.x = event.x
        self.y = event.y

    def mylinePen(self, event):
        x2, y2 = event.x, event.y
        self.drawpad.create_line(self.x, self.y, x2, y2, fill=self.fgcolor, width=2)
        self.x = x2
        self.y = y2

    def activate_eraser(self,event):
        self.drawpad.bind("<B1-Motion>", self.use_eraser)

    def use_eraser(self, event):
        x, y = event.x, event.y
        eraser_size = 10  # 调整橡皮擦的大小
        self.drawpad.create_rectangle(
            x - eraser_size, y - eraser_size, x + eraser_size, y + eraser_size,
            outline=self.bgcolor, fill=self.bgcolor, width=0
        )

    def kuaijiejian(self, event):
        if event.char=="r":
           self.fgcolor = "#ff0000"
        elif event.char=="g":
            self.fgcolor = "#00ff00"
        elif event.char=="y":
            self.fgcolor = "#ffff00"





if __name__ == '__main__':
    root = Tk()
    root.title("刘博的画图软件")
    root.geometry("900x450+250+250")
    app = Application(master=root)
    root.mainloop()
