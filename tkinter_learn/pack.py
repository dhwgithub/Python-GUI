import tkinter as tk

window = tk.Tk()
window.title('My Window')
window.geometry('500x300')

tk.Label(window, text='P', fg='red').pack(side='top')  # 上
tk.Label(window, text='P', fg='red').pack(side='bottom')  # 下
tk.Label(window, text='P', fg='red').pack(side='left')  # 左
tk.Label(window, text='P', fg='red').pack(side='right')  # 右

window.mainloop()
