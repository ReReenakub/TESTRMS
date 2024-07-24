import pyautogui
import keyboard
import time
import pyperclip



def alt_Rabyod_action():
    pyautogui.click(x=2590, y=658)
    time.sleep(0.3)
    pyautogui.click(x=2552, y=337)
    time.sleep(0.2)
    pyautogui.click(x=2718, y=645)
    time.sleep(0.1)
    pyautogui.click(x=2739, y=572)
    pyautogui.press('Enter')
def alt_backspace_action():
    pyautogui.click(x=2590, y=658)

def alt_Rabyodd_action():
    pyperclip.copy('รอคิว')
    pyautogui.click(x=2590, y=658)
    time.sleep(0.3)
    pyautogui.click(x=2502, y=251)
    time.sleep(0.3)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('Enter')
    time.sleep(0.3)
    pyautogui.click(x=2552, y=337)
    time.sleep(0.1)
    pyautogui.click(x=2718, y=645)
    time.sleep(0.1)
    pyautogui.click(x=2739, y=572)
    pyautogui.press('Enter')
def alt_e_action():
    pyautogui.click(x=2590, y=658)
    time.sleep(0.2)
    pyautogui.click(x=2586, y=203)
    time.sleep(0.2)
    pyautogui.click(x=2548, y=321)
    time.sleep(0.1)
    pyautogui.click(x=2716, y=645)
    time.sleep(0.1)
    pyautogui.click(x=3241, y=354)


while True:
    if keyboard.is_pressed('alt') and keyboard.is_pressed('w'):
        alt_backspace_action()
        while keyboard.is_pressed('alt') or keyboard.is_pressed('w'):
            time.sleep(0.1)
    elif keyboard.is_pressed('alt') and keyboard.is_pressed('1'):
        alt_e_action()
        while keyboard.is_pressed('alt') or keyboard.is_pressed('1'):
            time.sleep(0.1)
    elif keyboard.is_pressed('alt') and keyboard.is_pressed('2'):
        alt_Rabyod_action()
        while keyboard.is_pressed('alt') or keyboard.is_pressed('2'):
            time.sleep(0.1)
    time.sleep(0.1)