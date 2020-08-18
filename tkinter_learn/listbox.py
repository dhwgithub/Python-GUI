import tkinter as tk

window = tk.Tk()
window.title('My Window')
window.geometry('500x300')

var1 = tk.StringVar()  # 创建变量，用var1用来接收鼠标点击具体选项的内容
l = tk.Label(window, bg='green', fg='yellow', font=('Arial', 12), width=10, textvariable=var1)
l.pack()

# 创建一个方法用于按钮的点击事件
def print_selection():
    if lb.curselection().__len__() is 0:
        return
    value = lb.get(lb.curselection())   # 获取当前选中的文本
    var1.set(value)  # 为label设置值

# 创建一个按钮并放置，点击按钮调用print_selection函数
b1 = tk.Button(window, text='print selection', width=15, height=2, command=print_selection)
b1.pack()

# 创建Listbox并为其添加内容
var2 = tk.StringVar()
var2.set((1, 2, 3, 4))  # 为变量var2设置值
lb = tk.Listbox(window, listvariable=var2)

# 创建一个list并将值循环添加到Listbox控件中
list_items = [11, 22, 33, 44]
for item in list_items:
    lb.insert('end', item)  # 从最后一个位置开始加入值

lb.insert(1, 'first')       # 在第一个位置加入'first'字符
lb.insert(2, 'second')      # 在第二个位置加入'second'字符
lb.delete(2)                # 删除第二个位置的字符
lb.pack()

window.mainloop()
