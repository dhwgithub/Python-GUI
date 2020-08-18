import tkinter as tk

window = tk.Tk()
window.title('My Window')
window.geometry('500x300')

l = tk.Label(window, bg='green', fg='white', width=20, text='empty')
l.pack()

def print_selection(v):
    l.config(text='you have selected ' + v)

s = tk.Scale(window, label='try me', from_=0, to=10, orient=tk.HORIZONTAL,
             length=200, showvalue=0, tickinterval=2, resolution=0.1, command=print_selection)
s.pack()

window.mainloop()
