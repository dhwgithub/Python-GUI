import tkinter as tk

window = tk.Tk()
window.title('My Window')
window.geometry('500x300')

for i in range(3):
    for j in range(3):
        tk.Label(window, text=1).grid(row=i, column=j, padx=10, pady=10, ipadx=30, ipady=30)  # 后面4项是方格内位置和占地大小

window.mainloop()
