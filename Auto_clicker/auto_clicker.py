import time

import pyautogui
import tkinter as tk
from tkinter import messagebox
content=None
target_x,target_y=None,None

def submit():
    global content
    global target_x,target_y
    content=entry.get()
    if content.strip()=="":
        messagebox.showwarning("提示", "请输入内容后再提交！")
        return None
    else:
        messagebox.showinfo("提交成功", f"你输入的内容是：{content}，请3秒内手动移动至目标位置获取坐标或点击输入框")
        target_x,target_y=pyautogui.position()
        return content
def get_current_position():
    x,y=pyautogui.position()#获取鼠标当前位置
    return x,y
def click(a):
    global target_x, target_y
    time.sleep(3)
    target_x,target_y=pyautogui.position()
    pyautogui.moveTo(target_x,target_y)
    for i in range(0,a):
        pyautogui.click()
    return
def keypress(string):
    time.sleep(3)
    for i in range(0,int(string[0])):
        pyautogui.typewrite(string[1:])
    return


root = tk.Tk()
root.geometry("400x400")
root.title("Auto Clicker")

top_frame = tk.Frame(root)
top_frame.pack(fill="x", padx=10, pady=10)  # 填充水平方向，留边距

entry = tk.Entry(top_frame, width=50)  # 宽度适配容器
entry.pack(side="left", fill="x", expand=True)  # 填充水平空间并扩展

bottom_frame = tk.Frame(root)
bottom_frame.pack(side="bottom", pady=20)

btn1 = tk.Button(bottom_frame, text="Submit", command=submit)
btn1.pack(side="left", padx=10)

btn2 = tk.Button(bottom_frame, text="Mouse", command=lambda: click(int(content)))
btn2.pack(side="left", padx=10)

btn3 = tk.Button(bottom_frame, text="Keyboard", command=lambda: keypress(content))
btn3.pack(side="left", padx=10)
root.mainloop()