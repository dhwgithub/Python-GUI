import tkinter as tk
from PIL import ImageTk

window = tk.Tk()
window.title('My Window')
window.geometry('1500x800')

canvas = tk.Canvas(window, bg='green', height=1500, width=800)

image_file = ImageTk.PhotoImage(file=r'./img/one.jpg')
image = canvas.create_image(280, 0, anchor='n', image=image_file)  # n表示北，还有w,nw,s...，前面坐标表示以窗口左上角为基准

x0, y0, x1, y1 = 100, 100, 150, 150
line = canvas.create_line(280, 10, 500, 100)                   # 画直线
oval = canvas.create_oval(10, 10, 50, 50, fill='yellow')  # 画圆 用黄色填充 两坐标表示圆外矩阵左上和右下角坐标
arc = canvas.create_arc(50, 50, 100, 100, start=0, extent=270)      # 画扇形 从0度打开收到180度结束 两坐标同理
rect = canvas.create_rectangle(200, 200, 400, 400)                  # 画矩形正方形


def moveit():
    canvas.move(rect, 2, 2)  # 移动正方形rect（也可以改成其他图形名字用以移动一起图形、元素），按每次（x=2, y=2）步长进行移动

b = tk.Button(window, text='move item',command=moveit).pack()

canvas.pack()
window.mainloop()
