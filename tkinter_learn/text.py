import tkinter as tk

window = tk.Tk()
window.title('My Window')
window.geometry('500x300')

e = tk.Entry(window, show=None)  # 显示成明文形式
e.pack()

# 定义两个触发事件时的函数insert_point和insert_end（注意：因为Python的执行顺序是从上往下，所以函数一定要放在按钮的上面）
def insert_point(): # 在鼠标焦点处插入输入内容
    var = e.get()
    t.insert('insert', var)
def insert_end():   # 在文本框内容最后接着插入输入内容
    var = e.get()
    t.insert('end', var)

# 创建并放置两个按钮分别触发两种情况
b1 = tk.Button(window, text='insert point', width=10,
               height=2, command=insert_point)
b1.pack()
b2 = tk.Button(window, text='insert end', width=10,
               height=2, command=insert_end)
b2.pack()

t = tk.Text(window, height=3)
t.pack()

window.mainloop()
