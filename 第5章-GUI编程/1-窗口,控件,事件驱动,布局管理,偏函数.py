from functools import partial as pto
from tkinter import Tk,Button,X
from tkinter.messagebox import showinfo,showerror,showwarning

WARN = "warn"
CRIT = "crit"
REGU = "regu"

#定义字典用于查询
SIGNS = {
    "do not enter": CRIT,
    "railroad crossing": WARN,
    "55\nspeed limit": REGU,
    "wrong way":  CRIT,
    "merging traffic": WARN,
    "one way": REGU,
}

#创建回调函数，在按动按钮时调用
critCB = lambda : showerror("Error","Error Button Pressed!")
warnCB = lambda : showwarning("Warning","Warning Button Pressed!")
infoCB = lambda : showinfo("Info","Info Button Pressed!")

#创建顶层窗口并创建一个quit按钮
top = Tk()
top.title("Road Signs")
Button(top, text="QUIT", command=top.quit, bg="red", fg="white").pack()

#使用二阶偏函数进行模板化
MyButton = pto(Button, top)  #一阶模板化Button类和根窗口
CritButton = pto(MyButton, command=critCB, bg="white", fg="red")
WarnButton = pto(MyButton, command=warnCB, bg="goldenrod1")
ReguButton = pto(MyButton, command=infoCB, bg="white")

#格式化创建命令字符串并通过eval函数实例化
for eachSign in SIGNS:
    signType = SIGNS[eachSign]
    cmd = "%sButton(text=%r%s).pack(fill=X, expand=True)" % (signType.title(), eachSign,
                                                             ".upper()" if signType == CRIT else ".title()")
    eval(cmd)

#启动主事件循环
top.mainloop()
