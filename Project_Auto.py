import tkinter as tk
import pandas as pd
import numpy as np
from tkinter import ttk
import pyautogui
import pyperclip
import keyboard
import time
def deletetext():
    et1.delete(0, tk.END)
    et2.delete(0, tk.END)


def determine_game(input_text):
    if '(' in input_text and ')' in input_text:
        try:
            name, uid = input_text.split('(')
            name = name.strip()
            uid = uid.replace(')', '').strip()

            # ตรวจสอบ UID ว่ามีตัวเลขหรือไม่
            if uid.isdigit():
                return 'PUBG'
        except ValueError:
            pass

    # ตรวจสอบว่ามีแค่ตัวเลข
    elif input_text.isdigit():
        return 'ROV'

    # ตรวจสอบว่ามีตัวเลขและตัวอักษร
    elif any(char.isdigit() for char in input_text) and ' ' in input_text:
        return 'FREEFIRE'

    return 'Unknown Game'

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
    UID_value = UID.get()
    Game = determine_game(UID_value)
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
        pyautogui.click(x=1419, y=71)
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




    elif Game == 'ROV':
        Autorov = """แอดมินเติมคูปองเสร็จเรียบร้อยแล้วนะครับ🥰\n\n⏰รอคูปองดีเลย์ประมาณ 5 - 15 นาที ⏰\n👉หากเกินเวลาดีเลย์แล้วคูปองยังไม่เข้าให้แจ้งแอดมินได้เลยนะครับ\n\n📍พร้อมบริการ “เติมเกมผ่อนได้ นานสูงสุด10เดือน”\nตอกย้ำความคุ้ม รับเงินคืน(Richman Coins) เพื่อสะสมใช้เป็นส่วนลดครั้งถัดไป สูงสุด 25%\nที่ https://www.richmanshop.com\n\n📍ติดตามกิจกรรมโปรโมชั่น ข่าวสาร สำคัญที่\nhttps://www.facebook.com/richmanshoptopup\n\n🎉รับรู้สปอยสกินใหม่ก่อนใครได้ ได้ที่ Youtube ช่อง Richman Shop  🎉\nhttps://www.youtube.com/@Richmanshop\n💞อย่าลืมกดกด Subscribe เพื่อติดตาม Youtube Channel ช่อง Richman Shop ของเราด้วยนะครับ🙏\n\nขอขอบคุณลูกค้าที่ไว้วางใจให้เราดูแล ขอบคุณครับ/ค่ะ"""
        df = df.replace([np.inf, -np.inf], np.nan).dropna(subset=['ROV_baht', 'ROV_currency'])
        prices = df['ROV_baht'].astype(int).values
        Coupon_Price = df['ROV_currency'].astype(int).values

        int_Budget = int(Price.get())

        sorted_indices = np.argsort(prices)[::-1]
        sorted_prices = prices[sorted_indices]
        sorted_Coupon = Coupon_Price[sorted_indices]

        budget = int_Budget
        spent_Coupon = []
        Total_Coupon = 0
        for price, Coupon in zip(sorted_prices, sorted_Coupon):
            if budget >= price:
                budget -= price
                spent_Coupon.append(Coupon)
                Total_Coupon += Coupon

        spent_Coupon = [int(uc) for uc in spent_Coupon]
        remaining_budget = int_Budget - budget
        keyboard.wait('ctrl+c')
        time.sleep(0.3)
        pyautogui.click(x=1419, y=71)
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
        pyautogui.write(str(spent_Coupon))
        pyautogui.write(['tab'] * 11)
        pyautogui.write(input_text)
        pyautogui.write(['tab'] * 2)
        pyautogui.write(str(Total_Coupon))
        pyperclip.copy(' คูปอง')
        pyautogui.hotkey('ctrl', 'v')
        keyboard.wait('Enter')
        pyperclip.copy(Autorov)

    elif Game == 'VALORANT':
        Autovalorant = """แอดมินเติม VP เสร็จเรียบร้อยแล้วนะครับ🥰\n\n⏰รอ VP ดีเลย์ประมาณ 5 - 15 นาที ⏰\n👉หากเกินเวลาดีเลย์แล้ว VP ยังไม่เข้าให้แจ้งแอดมินได้เลยนะครับ\n\n📍พร้อมบริการ “เติมเกมผ่อนได้ นานสูงสุด10เดือน”\nตอกย้ำความคุ้ม รับเงินคืน(Richman Coins) เพื่อสะสมใช้เป็นส่วนลดครั้งถัดไป สูงสุด 25%\nที่ https://www.richmanshop.com\n\n📍ติดตามกิจกรรมโปรโมชั่น ข่าวสาร สำคัญที่\nhttps://www.facebook.com/richmanshoptopup\n\nขอขอบคุณลูกค้าที่ไว้วางใจให้เราดูแล ขอบคุณครับ/ค่ะ"""
        df = df.replace([np.inf, -np.inf], np.nan).dropna(subset=['VALORANT_baht', 'VALORANT_currency'])
        prices = df['VALORANT_baht'].astype(int).values
        VP_Price = df['VALORANT_currency'].astype(int).values

        int_Budget = int(Price.get())

        sorted_indices = np.argsort(prices)[::-1]
        sorted_prices = prices[sorted_indices]
        sorted_VP = VP_Price[sorted_indices]

        budget = int_Budget
        spent_VP = []
        Total_VP = 0
        for price, VP in zip(sorted_prices, sorted_VP):
            if budget >= price:
                budget -= price
                spent_VP.append(VP)
                Total_VP += VP

        remaining_budget = int_Budget - budget
        keyboard.wait('ctrl+c')
        time.sleep(0.3)
        pyautogui.click(x=1419, y=71)
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
        pyautogui.write(['tab'] * 28)
        time.sleep(0.3)
        pyperclip.copy(input_text)
        time.sleep(0.3)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.write(['tab'] * 2)
        pyautogui.write(str(Total_VP))
        pyautogui.write(' vp')
        keyboard.wait('Enter')
        pyperclip.copy(Autovalorant)



    elif Game == 'FREEFIRE':
        def split_uid_and_name(input_text):
            parts = input_text.split()
            uid = parts[0]
            name = " ".join(parts[1:])
            return uid, name

        try:
            uid, name = split_uid_and_name(input_text)
        except ValueError as e:
            print(e)
            return

        df = df.replace([np.inf, -np.inf], np.nan).dropna(subset=['FREEFIRE_baht', 'FREEFIRE_currency'])
        prices = df['FREEFIRE_baht'].astype(int).values
        Diamond_Price = df['FREEFIRE_currency'].astype(int).values

        int_Budget = int(Price.get())

        sorted_indices = np.argsort(prices)[::-1]
        sorted_prices = prices[sorted_indices]
        sorted_Diamond = Diamond_Price[sorted_indices]

        budget = int_Budget
        spent_Diamond = []
        Total_Diamond = 0
        for price, Diamond in zip(sorted_prices, sorted_Diamond):
            if budget >= price:
                budget -= price
                spent_Diamond.append(Diamond)
                Total_Diamond += Diamond

        spent_Diamond = [int(d) for d in spent_Diamond]
        remaining_budget = int_Budget - budget
        keyboard.wait('ctrl+c')
        time.sleep(0.3)
        pyautogui.click(x=1419, y=71)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.write(['tab'] * 1)
        pyautogui.write('free')
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
        pyautogui.write(str(spent_Diamond))
        pyautogui.write(['tab'] * 11)
        pyautogui.write(uid)
        pyautogui.write(['tab'] * 1)
        pyperclip.copy(name)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.write(['tab'] * 1)
        pyautogui.write(str(Total_Diamond))
        pyperclip.copy(' เพชร')
        pyautogui.hotkey('ctrl', 'v')

    elif Game == 'HOK':
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

        df = df.replace([np.inf, -np.inf], np.nan).dropna(subset=['HOK_baht', 'HOK_currency'])
        prices = df['HOK_baht'].astype(int).values
        Token_Price = df['HOK_currency'].astype(int).values

        int_Budget = int(Price.get())

        sorted_indices = np.argsort(prices)[::-1]
        sorted_prices = prices[sorted_indices]
        sorted_Token = Token_Price[sorted_indices]

        budget = int_Budget
        spent_Token = []
        Total_Token = 0
        for price, UC in zip(sorted_prices, sorted_Token):
            if budget >= price:
                budget -= price
                spent_Token.append(UC)
                Total_Token += UC

        spent_Token = [int(uc) for uc in spent_Token]
        remaining_budget = int_Budget - budget
        keyboard.wait('ctrl+c')
        time.sleep(0.3)
        pyautogui.click(x=1419, y=71)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.write(['tab'] * 1)
        pyautogui.write('glo')
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
        pyautogui.write(str(spent_Token))
        pyautogui.write(['tab'] * 11)
        pyautogui.write(uid)
        pyautogui.write(['tab'] * 1)
        pyperclip.copy(name)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.write(['tab'] * 1)
        pyautogui.write(str(Total_Token))
        pyautogui.write(' TOKEN')

    elif Game == 'ArenaBreakout':
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

        df = df.replace([np.inf, -np.inf], np.nan).dropna(subset=['ARENABREAKOUT_baht', 'ARENABREAKOUT_currency'])
        prices = df['ARENABREAKOUT_baht'].astype(int).values
        Bond_Price = df['ARENABREAKOUT_currency'].astype(int).values

        int_Budget = int(Price.get())

        sorted_indices = np.argsort(prices)[::-1]
        sorted_prices = prices[sorted_indices]
        sorted_Bond = Bond_Price[sorted_indices]

        budget = int_Budget
        spent_Bond = []
        Total_Bond = 0
        for price, UC in zip(sorted_prices, sorted_Bond):
            if budget >= price:
                budget -= price
                spent_Bond.append(UC)
                Total_Bond += UC

        spent_Bond = [int(uc) for uc in spent_Bond]
        remaining_budget = int_Budget - budget
        keyboard.wait('ctrl+c')
        time.sleep(0.3)
        pyautogui.click(x=1419, y=71)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.write(['tab'] * 1)
        pyautogui.write('are')
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
        pyautogui.write(str(spent_Bond))
        pyautogui.write(['tab'] * 11)
        pyautogui.write(uid)
        pyautogui.write(['tab'] * 1)
        pyperclip.copy(name)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.write(['tab'] * 1)
        pyautogui.write(str(Total_Bond))
        pyautogui.write(' Bond')

    elif Game == 'OPM':
        OPMs = """แอดมินเติม คูปองส้ม เสร็จเรียบร้อยแล้วนะครับ🥰

⏰รอ คูปองส้ม  ดีเลย์ประมาณ 5 - 15 นาที ⏰
👉หากเกินเวลาดีเลย์แล้ว คูปองส้ม  ยังไม่เข้าให้แจ้งแอดมินได้เลยนะครับ

📍พร้อมบริการ “เติมเกมผ่อนได้ นานสูงสุด10เดือน”
ตอกย้ำความคุ้ม รับเงินคืน(Richman Coins) เพื่อสะสมใช้เป็นส่วนลดครั้งถัดไป สูงสุด 25%
ที่ https://www.richmanshop.com

📍ติดตามกิจกรรมโปรโมชั่น ข่าวสาร สำคัญที่
https://www.facebook.com/richmanshoptopup

ขอขอบคุณลูกค้าที่ไว้วางใจให้เราดูแล ขอบคุณครับ/ค่ะ"""
        def split_uid_and_name(input_text):
            parts = input_text.split()
            uid = parts[0]
            name = " ".join(parts[1:])
            return uid, name

        try:
            uid, name = split_uid_and_name(input_text)
        except ValueError as e:
            print(e)
            return

        df = df.replace([np.inf, -np.inf], np.nan).dropna(subset=['OPM_baht', 'OPM_currency'])
        prices = df['OPM_baht'].astype(int).values
        Pongsom_Price = df['OPM_currency'].astype(int).values

        int_Budget = int(Price.get())

        sorted_indices = np.argsort(prices)[::-1]
        sorted_prices = prices[sorted_indices]
        sorted_OPM = Pongsom_Price[sorted_indices]

        budget = int_Budget
        spent_OPM = []
        Total_pongsom = 0
        for price, Diamond in zip(sorted_prices, sorted_OPM):
            if budget >= price:
                budget -= price
                spent_OPM.append(Diamond)
                Total_pongsom += Diamond

        spent_OPM = [int(d) for d in spent_OPM]
        remaining_budget = int_Budget - budget
        keyboard.wait('ctrl+c')
        time.sleep(0.3)
        pyautogui.click(x=1419, y=71)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.write(['tab'] * 1)
        pyautogui.write('opm')
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
        pyautogui.write(str(spent_OPM))
        pyautogui.write(['tab'] * 11)
        pyautogui.write(uid)
        pyautogui.write(['tab'] * 1)
        pyperclip.copy(name)
        time.sleep(0.3)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.write(['tab'] * 1)
        pyautogui.write(str(Total_pongsom))
        pyperclip.copy(' คูปอง')
        pyautogui.hotkey('ctrl', 'v')
        keyboard.wait('Enter')
        pyperclip.copy(OPMs)



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

games = ["ROV", "PUBG", "VALORANT", "FREEFIRE", "HOK", "ArenaBreakout", "OPM","Gameall"]
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
