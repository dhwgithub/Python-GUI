import tkinter as tk

window = tk.Tk()
window.title('My Window')
window.geometry('500x300')

tk.Label(window, text='on the window', bg='red', font=('Arial', 16)).pack()   # 和前面部件分开创建和放置不同，其实可以创建和放置一步完成

frame = tk.Frame(window).pack()

frame_l = tk.Frame(frame)
frame_r = tk.Frame(frame)
frame_l.pack(side="left")  # 注意立即放置和最后放置存在区别
frame_r.pack(side='right')

tk.Label(frame_l, text='on the frame_l1', bg='green').pack()
tk.Label(frame_l, text='on the frame_l2', bg='green').pack()
tk.Label(frame_l, text='on the frame_l3', bg='green').pack()
tk.Label(frame_r, text='on the frame_r1', bg='yellow').pack()
tk.Label(frame_r, text='on the frame_r2', bg='yellow').pack()
tk.Label(frame_r, text='on the frame_r3', bg='yellow').pack()

window.mainloop()
