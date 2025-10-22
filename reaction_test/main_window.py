import tkinter as tk
from PIL import Image, ImageTk
import random
flag=False
size=[100,100]
label=None
x=random.randint(0,1000)
y=random.randint(0,1000)
def change(event):
    """点击图片时移动图片（需接收event参数）"""
    global label
    if label is None:
        return
    # 限制图片在窗口内（窗口大小300x300，减去图片尺寸避免超出）
    max_x = main_window.winfo_width() - size[0]
    max_y = main_window.winfo_height() - size[1]
    # 确保最大坐标不小于0（窗口未缩放时）
    max_x = max(max_x, 0)
    max_y = max(max_y, 0)
    # 生成新位置
    x1 = random.randint(0, max_x)
    y1 = random.randint(0, max_y)
    label.place(x=x1, y=y1)
def start(event):
    """启动测试：允许图片被点击移动"""
    global flag, label
    flag = True
    # 动态绑定图片点击事件（启动后才生效）
    if label is not None:
        label.bind("<Button-1>", change)
def stop(event):
    """停止测试：禁止图片被点击移动"""
    global flag, label
    flag = False
    # 解绑图片点击事件（停止后失效）
    if label is not None:
        label.unbind("<Button-1>")
main_window = tk.Tk()
main_window.title("Reaction Test")
main_window.geometry("300x300")
btn1=tk.Button(main_window, text="Start Test")
btn2=tk.Button(main_window, text="Stop Test")
btn1.pack(side="bottom",padx=5, pady=5)
btn2.pack(side="bottom",padx=5, pady=5)
btn1.bind("<Button-1>", start)
btn2.bind("<Button-1>", stop)
try:
    image=Image.open("mizuha.jpeg")
    image=image.resize((size[0],size[1]),Image.LANCZOS)#用一种算法LANCZOS以缩放图片
    tk_image=ImageTk.PhotoImage(image)#将PIL图片转换为Tkinter可用的格式
    label=tk.Label(main_window, image=tk_image)
    label.place(x=x, y=y)
    # 保持图片引用（防止被垃圾回收）
    label.image = tk_image
except FileNotFoundError:
    print("Couldn't find image")
except Exception as e:
    print(e)
main_window.mainloop()
