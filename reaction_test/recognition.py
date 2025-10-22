import cv2
import mss
import numpy as np
import pyautogui,time

flag=False
def start(event):
    global flag
    flag=True
    #recognition("mizuha.jpeg")
    return
def stop(event):
    global flag
    flag=False
    return

def recognition(src1):
    sct=mss.mss()
    monitor=sct.monitors[1]
    main_image=cv2.imread(src1)
    if main_image is None:
        print(f"错误：无法读取模板图像 {src1}，请检查路径是否正确")
        return
    while True:
        if flag:
            sct_img = sct.grab(monitor)
            frame = np.array(sct_img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
            result = cv2.matchTemplate(frame, main_image, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            threshold = 0.1
            if max_val >= threshold:
                top_left = max_loc
                bottom_right = (top_left[0] + main_image.shape[1], top_left[1] + main_image.shape[0])
                target_x = (top_left[0] + bottom_right[0]) // 2
                target_y = (top_left[1] + bottom_right[1]) // 2
                pyautogui.moveTo(target_x, target_y, duration=0.3)
                print(f"匹配成功！相似度：{max_val:.2f}，已移动到 ({target_x}, {target_y})")
            else:
                print(f"error最高相似度：{max_val:.2f}（低于阈值 {threshold}")
            time.sleep(1)
        else:
            break
    sct.close()
