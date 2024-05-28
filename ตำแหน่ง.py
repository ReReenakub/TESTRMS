import pyautogui
import time

print("ขยับไปที่ ชื่อลูกค้าในไลน์")
time.sleep(5)
position1 = pyautogui.position()

print("ขยับเมาส์ไปที่ ชื่อลูกค้าในโปรแกรมคิว")
time.sleep(5)
position2 = pyautogui.position()
#แสดงทั้งสองตำแหน่ง
print(f"ตำแหน่งชื่อลูกค้า: {position1}")
print(f"ตำแหน่งชื่อลูกค้าในโปรแกรมคิว: {position2}")
