"""开发记事本软件的菜单"""
from tkinter.colorchooser import askcolor
from tkinter.filedialog import askopenfile
from tkinter.filedialog import asksaveasfilename
from tkinter import *
from tkinter import messagebox
import random
class Application(Frame):


    def __init__(self, master = None):
        super(). __init__(master)
        self.master = master
        self.textpad = None         # textpad是表示文本框对象
        self.pack()
        self.crateWidget()
        self.filename = None

    def crateWidget(self):
        menubar = Menu(root)        # 1.创建菜单栏

        menuFile = Menu(menubar, tearoff=0)        # 2.创建子菜单
        menuEdit = Menu(menubar, tearoff=0)
        menuHelp = Menu(menubar, tearoff=0)

        menubar.add_cascade(label="文件（F）", menu=menuFile)       # 3.将子菜单加入到主菜单
        menubar.add_cascade(label="编辑（E）", menu=menuEdit)
        menubar.add_cascade(label="文件（H）", menu=menuHelp)

        menuFile.add_command(label="新建", accelerator="ctrl+n", command=self.newfile)     # 4.添加菜单项
        menuFile.add_command(label="打开", accelerator="ctrl+o", command=self.openfile)
        menuFile.add_command(label="保存", accelerator="ctrl+s", command=self.savefile)
        menuFile.add_separator()
        menuFile.add_command(label="退出", accelerator="ctrl+q", command=self.exit)

        root["menu"]=menubar        # 5.root.config(menu=menubar)，配置顶层窗口使用菜单栏


        self.textpad = Text(root, width=85, height=30)
        self.textpad.pack()                 # 文本编辑区

        self.contextMeun= Menu(root,tearoff=0)
        self.contextMeun.add_command(label="背景颜色", command=self.openAskColor)       # 创建上下菜单

        root.bind("<Button-3>", self.creatcontextMeun)
        # 创建绑定快捷键
        root.bind("<Control-N>", lambda event:self.newfile)
        root.bind("<Control-O>", lambda event:self.openfile)
        root.bind("<Control-S>", lambda event:self.savefile)
        root.bind("<Control-Q>", lambda event:self.exit)

    def test (self):
        pass

    def openfile(self, event=None):
        # 使用 'r' 模式打开，这是默认的，但明确总是好的。同时确保返回的是一个文件对象。
        f = askopenfile(title="打开文本文件", filetypes=[("文本文件", "*.txt"), ("所有文件", "*.*")], mode='r')

        self.filename = f.name

        if f is not None:  # 确保用户选择了文件
            try:
                content = f.read()  # 读取文件内容
                self.textpad.delete(1.0, END)  # 可选：如果您想先清空文本框
                self.textpad.insert(INSERT, content)  # 插入到文本框
            except Exception as e:
                messagebox.showerror("打开文件", f"打开文件时出错：{e}")
            finally:
                f.close()  # 确保文件被关闭
        else:
            # 可选：如果用户取消文件打开操作，您可能想给出提示
            messagebox.showinfo("提示", "未选择任何文件")

    def newfile(self, event=None):
        print("New file is called")
        self.filename=asksaveasfilename(title="另存为", initialfile="未命名.txt", filetypes=
                            [("文本文档","*.txt")], defaultextension=".txt")

        self.savefile()




    def savefile(self, event=None):
        if not self.filename:
            self.filename = asksaveasfilename(title="保存文件", filetypes=[("文本文件", "*.txt"), ("所有文件", "*.*")],
                                              defaultextension=".txt", )
            if not self.filename:
                return
        try:
            with open(self.filename, "w")as f:
                c = self.textpad.get(1.0, END)
                f.write(c)
        except Exception as e:
            messagebox.showerror("保存文件", f"保存文件时出错：{e}")

    def exit(self, event=None):
        self.master.quit()

    def openAskColor(self):
        s1 = askcolor(title="变化背景颜色", color="red")

        self.textpad.config(bg=s1[1])


    def creatcontextMeun(self, event):
        self.contextMeun.post(event.x_root, event.y_root)



if __name__ == '__main__':
    root = Tk()
    root.title("刘博的简易记事本")
    root.geometry("600x300+250+250")
    app = Application(master=root)
    root.mainloop()
