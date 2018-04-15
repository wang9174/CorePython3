import os
from time import sleep
from tkinter import *

#定义类
class DirList(object):
    #定义构造函数
    def __init__(self,initdir=None):
        #创建顶层窗口并显示版本号
        self.top = Tk()
        self.label = Label(self.top,text="Directory Lister Lister v1.0")
        self.label.pack()

        #声明cwd变量用于保存当前所在目录名并显示
        self.cwd = StringVar(self.top)
        self.dirl = Label(self.top, fg="blue", font=("Helvetica", 12, "bold"))
        self.dirl.pack()

        #创建核心部分：Frame框架、滑块、列表框
        self.dirfm = Frame(self.top)
        self.dirsb = Scrollbar(self.dirfm)
        self.dirsb.pack(side=RIGHT, fill=Y)
        self.dirs = Listbox(self.dirfm, height=15, width=50, yscrollcommand=self.dirsb.set)
        self.dirs.bind("<Double-1>", self.setDirAndGo)  #绑定会将回调函数与一个事件连接起来（此处是双击）
        self.dirsb.config(command=self.dirs.yview)  #滑块通过config方法与listbox连接起来
        self.dirs.pack(side=LEFT, fill=BOTH)
        self.dirfm.pack()

        #创建一个文本框，允许用户输入目录名
        self.dirn = Entry(self.top, width=50, textvariable=self.cwd)
        self.dirn.bind("<Return>",self.doLS)  #绑定回车
        self.dirn.pack()

        #定义一个框架并放置三个按钮（清除、前往、退出），都有自己的回调函数
        self.bfm = Frame(self.top)
        self.clr = Button(self.bfm, text="Clear", command=self.clrDir,
                          activeforeground="white",activebackground="blue")
        self.ls = Button(self.bfm, text="List Directory", command=self.doLS,
                         activeforeground="white",activebackground="green")
        self.quit = Button(self.bfm, text="Quit", command=self.top.quit,
                           activeforeground="white",activebackground="red")
        self.clr.pack(side=LEFT)
        self.ls.pack(side=LEFT)
        self.quit.pack(side=LEFT)
        self.bfm.pack()

        #初始化GUI程序并以当前目录为显示起始点
        if initdir:
            self.cwd.set(os.curdir)
            self.doLS()

    #清空cwd
    def clrDir(self,ev=None):
        self.cwd.set("")

    #设置要前往的目录并遍历目录
    def setDirAndGo(self,ev=None):
        self.last = self.cwd.get()
        self.dirs.config(selectbackground="red")  #正在工作，背景红色
        check = self.dirs.get(self.dirs.curselection())
        if not check:
            check = os.curdir
        self.cwd.set(check)
        self.doLS()
    #核心部分，检查目录是否存在并处理，获取文件列表并展示
    def doLS(self,ev=None):
        error = ""
        tdir = self.cwd.get()
        if not tdir:
            tdir = os.curdir
        if not os.path.exists(tdir):
            error = tdir + ": no such file"
        elif not os.path.isdir(tdir):
            error = tdir + ": not a directory"

        if error:
            self.cwd.set(error)
            self.top.update()
            sleep(2)
            if not (hasattr(self, "last") and self.last):
                self.last = os.curdir
            self.cwd.set(self.last)
            self.dirs.config(selectbackground="LightSkyBlue")
            self.top.update()
            return

        self.cwd.set("FETCHING DIRECTORY CONTENTS")
        self.top.update()
        dirlist = os.listdir(tdir)
        dirlist.sort()
        os.chdir(tdir)

        self.dirl.config(text=os.getcwd())
        self.dirs.delete(0, END)
        self.dirs.insert(END, os.curdir)
        self.dirs.insert(END, os.pardir)
        for eachFile in dirlist:
            self.dirs.insert(END, eachFile)
        self.cwd.set(os.curdir)
        self.dirs.config(selectbackground="LightSkyBlue")  #完成工作，背景蓝色

#只有直接调用脚本时，代码才会执行
def main():
    d = DirList(os.curdir)
    mainloop()

if __name__ == '__main__':
    main()
