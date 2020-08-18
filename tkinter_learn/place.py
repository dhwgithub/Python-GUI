import tkinter as tk

window = tk.Tk()
window.title('My Window')
window.geometry('500x300')

tk.Label(window, text='Pl', font=('Arial', 20)).place(x=10, y=10, anchor='nw')

window.mainloop()
