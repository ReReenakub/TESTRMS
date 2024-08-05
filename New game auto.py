import tkinter as tk
import pandas as pd
import numpy as np
from tkinter import ttk
import pyautogui
import pyperclip
import keyboard
import time
import threading
def deletetext():
    et1.delete(0, tk.END)
    et2.delete(0, tk.END)

def autocomplete(event):
    search_term = combo.get()
    if search_term:
        filtered_games = [game for game in games if search_term.lower() in game.lower()]
        combo['values'] = filtered_games
    else:
        combo['values'] = games

def calculate_packages():
    sheet_map = {
        'PUBG': 'PUBG',
        'ROV': 'ROV',
        'VALORANT': 'VALORANT',
        'FREEFIRE': 'FREEFIRE',
        'HOK' : 'HOK',
        'ArenaBreakout': 'ARENA',
        'OPM': 'OPM'
    }

    Game = choice.get()
    input_text = UID.get()

    if Game not in sheet_map:
        print(f"No sheet found for game {Game}")
        return

    df = pd.read_excel('Price.xlsx', sheet_name=sheet_map[Game])

    if Game == 'PUBG':
        Autopubg = """แอดมินเติม UC เสร็จเรียบร้อยแล้วนะครับ🥰

⏰รอ UC ดีเลย์ประมาณ 5 - 15 นาที ⏰
👉หากเกินเวลาดีเลย์แล้ว UC ยังไม่เข้าให้แจ้งแอดมินได้เลยนะครับ

📍พร้อมบริการ “เติมเกมผ่อนได้ นานสูงสุด10เดือน”
ตอกย้ำความคุ้ม รับเงินคืน(Richman Coins) เพื่อสะสมใช้เป็นส่วนลดครั้งถัดไป สูงสุด 25%
ที่ https://www.richmanshop.com

📍ติดตามกิจกรรมโปรโมชั่น ข่าวสาร สำคัญที่
https://www.facebook.com/richmanshoptopup

ขอขอบคุณลูกค้าที่ไว้วางใจให้เราดูแล ขอบคุณครับ/ค่ะ"""
        def split_and_clean_text(input_text):
            if '(' in input_text and ')' in input_text:
                try:
                    name, uid = input_text.split('(')
                    name = name.strip()
                    uid = uid.replace(')', '').strip()
                except ValueError:
                    pass
            else:
                name = ""
                uid = "1"
            return name, uid

        try:
            name, uid = split_and_clean_text(input_text)
        except ValueError as e:
            print(e)
            return

        df = df.replace([np.inf, -np.inf], np.nan).dropna(subset=['PUBG_baht', 'PUBG_currency'])
        prices = df['PUBG_baht'].astype(int).values
        UC_Price = df['PUBG_currency'].astype(int).values

        int_Budget = int(Price.get())

        sorted_indices = np.argsort(prices)[::-1]
        sorted_prices = prices[sorted_indices]
        sorted_UC = UC_Price[sorted_indices]

        budget = int_Budget
        UC_count = {}
        Total_UC = 0
        for price, UC in zip(sorted_prices, sorted_UC):
            if budget >= price:
                budget -= price
                Total_UC += UC
                if UC in UC_count:
                    UC_count[UC] += 1
                else:
                    UC_count[UC] = 1

        spent_UC = []
        for UC, count in UC_count.items():
            if count > 1:
                spent_UC.append(f"{UC}*{count}")
            else:
                spent_UC.append(str(UC))
        spent_UC_str = " + ".join(spent_UC)

        remaining_budget = int_Budget - budget
        keyboard.wait('ctrl+c')
        time.sleep(0.3)
        pyautogui.click(x=1795, y=182)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.write(['tab'] * 1)
        pyautogui.write(Game)
        pyautogui.press('down')
        pyautogui.write(['tab'] * 1)
        pyautogui.write(str(remaining_budget))
        pyautogui.write(['tab'] * 2)
        pyautogui.press('Enter')
        pyautogui.write(['tab'] * 1)
        pyautogui.press('down')
        pyautogui.write(['tab'] * 1)
        pyautogui.write(str(int_Budget))
        pyautogui.write(['tab'] * 17)
        pyautogui.write(spent_UC_str)
        pyautogui.write(['tab'] * 11)
        pyautogui.write(uid)
        pyautogui.write(['tab'] * 1)
        pyperclip.copy(name)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.write(['tab'] * 1)
        pyautogui.write(str(Total_UC))
        pyautogui.write(' uc')
        keyboard.wait('Enter')
        pyperclip.copy(Autopubg)

root = tk.Tk()
root.title('บอทเกม')
root.geometry('400x150')

root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(4, weight=1)

tk.Label(root, text='ใส่ UID & Riot', padx=10, font=15).grid(row=0, sticky=tk.W)
UID = tk.StringVar()
et1 = tk.Entry(root, font=15, width=10, textvariable=UID)
et1.grid(row=0, column=1, sticky=tk.EW, padx=10, pady=5)

games = ["Gameall"]
tk.Label(root, text='เลือกเกม', padx=10, font=30).grid(row=1, sticky=tk.W)
choice = tk.StringVar()
combo = ttk.Combobox(root, width=28, font=30, textvariable=choice)
combo['values'] = games
combo.grid(row=1, column=1, sticky=tk.EW, padx=10, pady=5)
combo.bind("<KeyRelease>", autocomplete)

tk.Label(root, text='ราคา', padx=10, font=15).grid(row=2, sticky=tk.W)
Price = tk.StringVar()
et2 = tk.Entry(root, font=15, width=30, textvariable=Price)
et2.grid(row=2, column=1, sticky=tk.EW, padx=10, pady=5)

tk.Button(root, text='ยืนยัน', font=15, width=10, command=calculate_packages).grid(row=4, column=0, sticky=tk.W, padx=5, pady=5)
tk.Button(root, text='ลบข้อมูล', font=15, width=10, command=deletetext).grid(row=4, column=1, sticky=tk.E, padx=5, pady=5)



root.mainloop()
