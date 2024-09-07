import pyautogui
import time

# กำหนดตำแหน่งที่ต้องการให้เมาส์ไปคลิก
x, y = 269, 1013

while True:
    time.sleep(1)
    pyautogui.press('f5')

    # รอ 2 วินาทีเพื่อให้หน้ารีเฟรชเสร็จ
    time.sleep(4)

    # เลื่อนเมาส์ไปที่ตำแหน่งที่กำหนดแล้วคลิก
    pyautogui.moveTo(x, y, duration=2)
    pyautogui.click()

    # รอ 8 นาที (480 วินาที) ก่อนที่จะทำงานซ้ำ
    time.sleep(300)
