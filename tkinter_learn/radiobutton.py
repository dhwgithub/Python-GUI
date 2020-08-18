import tkinter as tk

window = tk.Tk()
window.title('My Window')
window.geometry('500x300')

# 在图形界面上创建一个标签label用以显示并放置
l = tk.Label(window, bg='yellow', width=20, text='you have selected A')
l.pack()

def print_selection():
    l.config(text='you have selected ' + var.get())

var = tk.StringVar()  # 定义一个var用来将radiobutton的值和Label的值联系在一起.
var.set('A')
r1 = tk.Radiobutton(window, text='Option A', variable=var, value='A', command=print_selection)
r1.pack()
r2 = tk.Radiobutton(window, text='Option B', variable=var, value='B', command=print_selection)
r2.pack()
r3 = tk.Radiobutton(window, text='Option C', variable=var, value='C', command=print_selection)
r3.pack()

window.mainloop()
