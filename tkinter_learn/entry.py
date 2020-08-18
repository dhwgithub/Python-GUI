import tkinter as tk

window = tk.Tk()
window.title('My Window')
window.geometry('500x300')

e1 = tk.Entry(window, show='*', font=('Arial', 14))   # 显示成密文形式
e2 = tk.Entry(window, show=None, font=('Arial', 14))  # 显示成明文形式
e1.pack()
e2.pack()

window.mainloop()
