import tkinter as tk

window = tk.Tk()
window.title('My Window')
window.geometry('500x300')

l = tk.Label(window, text='      ', bg='green')
l.pack()

counter = 0
def do_job():
    global counter
    l.config(text='do ' + str(counter))
    counter += 1

# 创建菜单
menubar = tk.Menu(window)

# 创建一个一级目录
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)
# 创建另一个一级目录
editmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit', menu=editmenu)

# 为File一级目录添加内容
filemenu.add_command(label='New', command=do_job)
filemenu.add_command(label='Open', command=do_job)
filemenu.add_command(label='Save', command=do_job)
filemenu.add_separator()    # 添加一条分隔线
filemenu.add_command(label='Exit', command=window.quit)  # 用tkinter里面自带的quit()函数
# 为Edit一级目录添加内容
editmenu.add_command(label='Cut', command=do_job)
editmenu.add_command(label='Copy', command=do_job)
editmenu.add_command(label='Paste', command=do_job)

# 在File一级目录中添加二级目录
submenu = tk.Menu(filemenu, tearoff=0)
filemenu.add_cascade(label='Import', menu=submenu, underline=0)
# 在刚刚添加的目录中添加内容
submenu.add_command(label='Submenu_1', command=do_job)

window.config(menu=menubar)  # 将目录放入窗口中
window.mainloop()
