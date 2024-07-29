import tkinter as tk
import pandas as pd
import numpy as np
from tkinter import ttk
import pyautogui
import pyperclip
import keyboard
import time

def perform_actions():
    pyautogui.click(x=5555, y=209)
    pyautogui.write(['tab'] * 2)
    pyautogui.press('Enter')
    pyautogui.moveTo(x=5693, y=698, duration=0.5)
    pyautogui.click(x=5693, y=698)
    pyautogui.moveTo(x=3600, y=914, duration=0.2)
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
        'TUN_ROV': 'ROV',
        'VALORANT': 'VALORANT',
        'FREEFIRE': 'FREEFIRE',
        'Golden_ROV': 'ROV',
         'TUN_VALORANT': 'VALORANT'
    }

    Game = choice.get()
    input_text = UID.get()

    if Game not in sheet_map:
        print(f"No sheet found for game {Game}")
        return

    df = pd.read_excel('GoldenPrice.xlsx', sheet_name=sheet_map[Game])

    if Game == 'Golden_PUBG':
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

        df = df.replace([np.inf, -np.inf], np.nan).dropna(subset=['GPUBG_baht', 'GPUBG_currency'])
        prices = df['GPUBG_baht'].astype(int).values
        UC_Price = df['GPUBG_currency'].astype(int).values

        int_Budget = int(Price.get())

        sorted_indices = np.argsort(prices)[::-1]
        sorted_prices = prices[sorted_indices]
        sorted_UC = UC_Price[sorted_indices]

        budget = int_Budget
        spent_UC = []
        Total_UC = 0
        for price, UC in zip(sorted_prices, sorted_UC):
            if budget >= price:
                budget -= price
                spent_UC.append(UC)
                Total_UC += UC

        spent_UC = [int(uc) for uc in spent_UC]
        remaining_budget = int_Budget - budget
        keyboard.wait('ctrl+c')
        time.sleep(0.3)
        pyautogui.click(x=5621, y=147)
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
        pyautogui.write(str(spent_UC))
        pyautogui.write(['tab'] * 11)
        pyautogui.write(uid)
        pyautogui.write(['tab'] * 1)
        pyperclip.copy(name)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.write(['tab'] * 1)
        pyautogui.write(str(Total_UC))
        pyautogui.write(' UC')

    elif Game == 'Golden_ROV':
        Autorov = """🐶หมาน้อย🐶 เติมคูปองเสร็จเรียบร้อยแล้วนะครับ 💚

คูปองอาจดีเลย์ประมาณ 5 - 15  นาทีนะครับ หากยังไม่เข้าแจ้ง น้องหมา ได้เลยน้า 🐶🐶

ขอบคุณลูกค้าที่มาใช้บริการ Golden Termgame นะค้าบบ🙏"""
        df = df.replace([np.inf, -np.inf], np.nan).dropna(subset=['GROV_baht', 'GROV_currency'])
        prices = df['GROV_baht'].astype(int).values
        Coupon_Price = df['GROV_currency'].astype(int).values

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
        pyautogui.click(x=5555, y=209)
        pyautogui.write(['tab'] * 2)
        pyautogui.press('Enter')
        pyautogui.moveTo(x=5693, y=698, duration=0.5)
        pyautogui.click(x=5693, y=698)
        pyautogui.moveTo(x=3600, y=914, duration=0.2)
        pyautogui.click(x=5621, y=147)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.write(['tab'] * 1)
        pyautogui.write('rov')
        pyautogui.press('down')
        pyautogui.write(['tab'] * 1)
        pyautogui.write(str(remaining_budget))
        pyautogui.write(['tab'] * 2)
        pyautogui.press('Enter')
        time.sleep(0.5)
        pyautogui.write(['tab'] * 3)
        pyautogui.write('kb')
        pyautogui.press('down')
        pyautogui.write(['tab'] * 18)
        time.sleep(0.3)
        pyautogui.write(str(Total_Coupon))
        pyperclip.copy(' คูปอง')
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.write(['tab'] * 9)
        pyautogui.write(input_text)
        pyperclip.copy(Autorov)

    elif Game == 'Golden_VALORANT':
        df = df.replace([np.inf, -np.inf], np.nan).dropna(subset=['GVALORANT_baht', 'GVALORANT_currency'])
        prices = df['GVALORANT_baht'].astype(int).values
        VP_Price = df['GVALORANT_currency'].astype(int).values

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
        pyautogui.click(x=4932, y=525)
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
        pyautogui.click(x=5621, y=147)
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

    if Game == 'TUN_PUBG':
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

        df = df.replace([np.inf, -np.inf], np.nan).dropna(subset=['TPUBG_baht', 'TPUBG_currency'])
        prices = df['TPUBG_baht'].astype(int).values
        UC_Price = df['TPUBG_currency'].astype(int).values

        int_Budget = int(Price.get())

        sorted_indices = np.argsort(prices)[::-1]
        sorted_prices = prices[sorted_indices]
        sorted_UC = UC_Price[sorted_indices]

        budget = int_Budget
        spent_UC = []
        Total_UC = 0
        for price, UC in zip(sorted_prices, sorted_UC):
            if budget >= price:
                budget -= price
                spent_UC.append(UC)
                Total_UC += UC

        spent_UC = [int(uc) for uc in spent_UC]
        remaining_budget = int_Budget - budget
        keyboard.wait('ctrl+c')
        time.sleep(0.3)
        pyautogui.click(x=5621, y=147)
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
        pyautogui.write(str(spent_UC))
        pyautogui.write(['tab'] * 11)
        pyautogui.write(uid)
        pyautogui.write(['tab'] * 1)
        pyperclip.copy(name)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.write(['tab'] * 1)
        pyautogui.write(str(Total_UC))
        pyautogui.write(' UC')

    elif Game == 'TUN_ROV':
        Autorov = """แอดมินเติมคูปองเสร็จเรียบร้อยแล้วน้า ขอบคุณที่มาใช้บริการนะครับ🥰

- รอคูปองดีเลย์ประมาณ 5 - 15 นาที เกินเวลารอแจ้งแอดมินให้เช็กได้เลยนะค้าบ"""
        Autorovhp = """แอดมินเติมคูปองเสร็จเรียบร้อยแล้วน้า ขอบคุณที่มาใช้บริการนะครับ🥰
- รอคูปองดีเลย์ประมาณ 5 - 15 นาที เกินเวลารอแจ้งแอดมินให้เช็กได้เลยน้าา
ขอบคุณลูกค้าที่ไว้วางใจ มาเติมกับร้าน HP SHOP นะครับ"""
        df = df.replace([np.inf, -np.inf], np.nan).dropna(subset=['TROV_baht', 'TROV_currency'])
        prices = df['TROV_baht'].astype(int).values
        Coupon_Price = df['TROV_currency'].astype(int).values

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
        time.sleep(0.2)
        pyautogui.click(x=5555, y=209)
        pyautogui.write(['tab'] * 2)
        pyautogui.press('Enter')
        pyautogui.moveTo(x=5693, y=698, duration=0.5)
        time.sleep(0.2)
        pyautogui.click(x=5693, y=698)
        time.sleep(0.2)
        pyautogui.click(x=5621, y=147)
        if hp_var.get():
            pyautogui.write('HP*')
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.write(['tab'] * 1)
        pyautogui.write('rov')
        pyautogui.press('down')
        pyautogui.write(['tab'] * 1)
        pyautogui.write(str(remaining_budget))
        pyautogui.write(['tab'] * 2)
        pyautogui.press('Enter')
        time.sleep(0.5)
        pyautogui.write(['tab'] * 3)
        pyautogui.write('tw')
        pyautogui.press('down')
        pyautogui.write(['tab'] * 18)
        time.sleep(0.3)
        pyautogui.write(str(Total_Coupon))
        pyperclip.copy(' คูปอง')
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.write(['tab'] * 9)
        pyautogui.write(input_text)
        if hp_var.get():
            pyperclip.copy(Autorovhp)
        else:
            pyperclip.copy(Autorov)

    elif Game == 'TUN_VALORANT':
        valo = """ตุ่นเติม Points เสร็จเรียบร้อยแล้ว ขอบคุณที่มาใช้บริการนะครับ🥰

💜รอ Points ดีเลย์ประมาณ 5 - 15  นาที เกินเวลารอแจ้งน้องตุ่นให้เช็กได้เลยนะค้าบ💜"""
        valohp = """แอดมินเติม VP เสร็จเรียบร้อยแล้วน้า ขอบคุณที่มาใช้บริการนะครับ🥰
- รอVP ดีเลย์ประมาณ 5 - 15 นาที เกินเวลารอแจ้งแอดมินให้เช็กได้เลยน้าา
ขอบคุณลูกค้าที่ไว้วางใจ มาเติมกับร้าน HP SHOP นะครับ"""
        df = df.replace([np.inf, -np.inf], np.nan).dropna(subset=['TVALORANT_baht', 'TVALORANT_currency'])
        prices = df['TVALORANT_baht'].astype(int).values
        VP_Price = df['TVALORANT_currency'].astype(int).values

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
        time.sleep(0.2)
        pyautogui.click(x=5555, y=209)
        pyautogui.write(['tab'] * 2)
        pyautogui.press('Enter')
        pyautogui.moveTo(x=5693, y=698, duration=0.5)
        time.sleep(0.2)
        pyautogui.click(x=5693, y=698)
        time.sleep(0.2)
        pyautogui.click(x=5621, y=147)
        if hp_var.get():
            pyautogui.write('HP*')
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.write(['tab'] * 1)
        pyautogui.write('va')
        pyautogui.press('down')
        pyautogui.write(['tab'] * 1)
        pyautogui.write(str(remaining_budget))
        pyautogui.write(['tab'] * 2)
        pyautogui.press('Enter')
        time.sleep(0.5)
        pyautogui.write(['tab'] * 3)
        pyautogui.write('tw')
        pyautogui.press('down')
        pyautogui.write(['tab'] * 18)
        time.sleep(0.3)
        pyautogui.write(str(Total_VP))
        pyautogui.write(' vp')
        pyautogui.write(['tab'] * 9)
        pyperclip.copy(input_text)
        pyautogui.hotkey('ctrl', 'v')
        if hp_var.get():
            pyperclip.copy(valohp)
        else:
            pyperclip.copy(valo)

root = tk.Tk()
root.title('บอทเกม')
root.geometry('400x200')

root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(4, weight=1)

tk.Label(root, text='ใส่ UID & Riot', padx=10, font=15).grid(row=0, column=0, sticky=tk.W)
UID = tk.StringVar()
et1 = tk.Entry(root, font=15, textvariable=UID)
et1.grid(row=0, column=1, columnspan=2, sticky=tk.EW, padx=10, pady=5)

games = ["TUN_VALORANT","TUN_ROV"]
tk.Label(root, text='เลือกเกม', padx=10, font=15).grid(row=1, column=0, sticky=tk.W)
choice = tk.StringVar()
combo = ttk.Combobox(root, font=15, textvariable=choice)
combo['values'] = games
combo.grid(row=1, column=1, columnspan=2, sticky=tk.EW, padx=10, pady=10)
combo.bind("<KeyRelease>", autocomplete)

tk.Label(root, text='ราคา', padx=10, font=15).grid(row=2, column=0, sticky=tk.W)
Price = tk.StringVar()
et2 = tk.Entry(root, font=15, textvariable=Price)
et2.grid(row=2, column=1, columnspan=2, sticky=tk.EW, padx=10, pady=5)

# Create the buttons
tk.Button(root, text='ยืนยัน', font=15, width=10, command=calculate_packages).grid(row=4, column=0, sticky=tk.W, padx=10, pady=10)
tk.Button(root, text='ก่อนทำคิว', font=15, width=10, command=perform_actions).grid(row=4, column=1, padx=10, pady=10)
tk.Button(root, text='ลบข้อมูล', font=15, width=10, command=deletetext).grid(row=4, column=2, sticky=tk.E, padx=10, pady=10)

hp_var = tk.BooleanVar()
hp_checkbox = tk.Checkbutton(root, text="HP", variable=hp_var, bg='#d3d3d3', font=('Helvetica', 14))
hp_checkbox.grid(row=3, column=0, columnspan=3, pady=5, padx=10)

root.mainloop()

