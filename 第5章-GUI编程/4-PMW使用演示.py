#使用Python MegaWidgets创建GUI程序
#找不到官方文档，气的要死系列
from tkinter import Button, END, Label, W
from Pmw import initialise, ComboBox, Counter

#创建顶层窗口
top = initialise()

lb = Label(top, text="Animals (in pairs ;min: pair, max: dozen)")
lb.pack()

#counter控件
ct = Counter(top, labelpos=W, label_text="Number:", datatype="integer",
             entryfield_value=2, increment=2, entryfield_validate={"validator": "integer",
                                                                   "min": 2, "max": 12})
ct.pack()

#combobox控件
cb = ComboBox(top,labelpos=W, label_text="Type:")
for animal in ("dog", "cat", "hamster", "python"):
    cb.insert(END, animal)
cb.pack()

qb = Button(top, text="QUIT", command=top.quit, bg="red", fg="white")
qb.pack()

top.mainloop()
