import time
import pyautogui as pgi
import cv2

pixelRatio = pgi.screenshot().size[0]/pgi.size().width

while True: # launch game
    try:
        movement = pgi.position()
        pgi.moveTo(movement[0], 1800)
        point = pgi.locateCenterOnScreen('/Users/glenn/AutoClicker/Image/launch.png', confidence=0.6)
        if point is not None:
            pgi.moveTo(point[0]/pixelRatio,point[1]/pixelRatio)
            pgi.click()
            time.sleep(5)
            break
        else:
            time.sleep(1)  # Adding a small delay to prevent the loop from running too quickly
    except pgi.ImageNotFoundException:
        print("League has not been launched...")
        time.sleep(1) 

while True: # select TFT not done
    try:
        point = pgi.locateCenterOnScreen('/Users/glenn/AutoClicker/Image/launch.png', confidence=0.6)
        if point is not None:
            pgi.moveTo(point[0]/pixelRatio,point[1]/pixelRatio)
            pgi.click()
            break
        else:
            time.sleep(1)  # Adding a small delay to prevent the loop from running too quickly
    except pgi.ImageNotFoundException:
        print("League has not been switched to tft...")
        time.sleep(1) 

while True: # select ranked
    try:
        point = pgi.locateCenterOnScreen('/Users/glenn/AutoClicker/Image/launch.png', confidence=0.6)
        if point is not None:
            pgi.moveTo(point[0]/pixelRatio,point[1]/pixelRatio)
            pgi.click()
            break
        else:
            time.sleep(1)  # Adding a small delay to prevent the loop from running too quickly
    except pgi.ImageNotFoundException:
        print("League has not been launched...")
        time.sleep(1) 

while True: # start ranked
    try:
        movement = pgi.position()
        pgi.moveTo(movement[0], 1800)
        point = pgi.locateCenterOnScreen('/Users/glenn/AutoClicker/Image/launch.png', confidence=0.6)
        if point is not None:
            pgi.moveTo(point[0]/pixelRatio,point[1]/pixelRatio)
            pgi.click()
            break
        else:
            time.sleep(1)  # Adding a small delay to prevent the loop from running too quickly
    except pgi.ImageNotFoundException:
        print("League has not been launched...")
        time.sleep(1) 

while True: # queue acceptance
    try:
        point = pgi.locateCenterOnScreen('/Users/glenn/AutoClicker/Image/accept.png', confidence=0.7)
        if point is not None:
            pgi.moveTo(point[0]/pixelRatio,point[1]/pixelRatio)
            pgi.click()
            break
        else:
            time.sleep(3)  # Adding a small delay to prevent the loop from running too quickly
    except pgi.ImageNotFoundException:
        print("Queue not found yet...")
        time.sleep(1) 

print("end")