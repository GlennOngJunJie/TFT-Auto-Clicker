import time
import pyautogui as pgi

while True:
    try:
        point = pgi.locateCenterOnScreen('/Users/glenn/AutoClicker/Image/accept.png', confidence=0.7)
        print(point)
        pixelRatio = pgi.screenshot().size[0]/pgi.size().width
        if point is not None:
            pgi.moveTo(point[0]/pixelRatio,point[1]/pixelRatio)
            pgi.click()
            break
        else:
            time.sleep(3)  # Adding a small delay to prevent the loop from running too quickly
    except pgi.ImageNotFoundException:
        print("Image not found on screen. Retrying...")
        time.sleep(1) 

print("end")
