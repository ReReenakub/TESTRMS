import tkinter as tk
import pandas as pd
import numpy as np
from tkinter import ttk
import pyautogui
import pyperclip
import keyboard

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
        'FREEFIRE': 'FREEFIRE'
    }

    Game = choice.get()
    input_text = UID.get()
    keyboard.wait('ctrl+c')

    if Game not in sheet_map:
        print(f"No sheet found for game {Game}")
        return

    df = pd.read_excel('Price.xlsx', sheet_name=sheet_map[Game])

    if Game == 'PUBG':
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
        spent_UC = []
        Total_UC = 0
        for price, UC in zip(sorted_prices, sorted_UC):
            if budget >= price:
                budget -= price
                spent_UC.append(UC)
                Total_UC += UC

        spent_UC = [int(uc) for uc in spent_UC]
        remaining_budget = int_Budget - budget

        pyautogui.click(x=1261, y=232)
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

    elif Game == 'ROV':
        if 'ROV_Bmore' in df.columns and 'ROV_Cmore' in df.columns:
            df = df.replace([np.inf, -np.inf], np.nan).dropna(subset=['ROV_Bmore', 'ROV_Cmore'])
            prices = df['ROV_Bmore'].astype(int).values
            Coupon_Price = df['ROV_Cmore'].astype(int).values
        else:
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

        pyautogui.click(x=1261, y=232)
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

    elif Game == 'VALORANT':
        df = df.replace([np.inf, -np.inf], np.nan).dropna(subset=['VALORANT_baht', 'VALORANT_currency'])
        prices = df['VALORANT_baht'].astype(int).values
        Coupon_Price = df['VALORANT_currency'].astype(int).values

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

        pyautogui.click(x=1261, y=232)
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
        pyperclip.copy(input_text)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.write(['tab'] * 2)
        pyautogui.write(str(Total_Coupon))
        pyperclip.copy(' vp')
        pyautogui.hotkey('ctrl', 'v')
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

        pyautogui.click(x=1261, y=232)
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



root = tk.Tk()
root.title('บอทเกม')

tk.Label(text='ใส่ UID & Riot', padx=10, font=30).grid(row=0, sticky=tk.W)
UID = tk.StringVar()
et1 = tk.Entry(font=30, width=30, textvariable=UID)
et1.grid(row=0, column=1)

games = ["ROV", "PUBG", "VALORANT", "FREEFIRE",]
tk.Label(text='เลือกเกม', padx=10, font=30).grid(row=1, sticky=tk.W)
choice = tk.StringVar()
combo = ttk.Combobox(root, width=28, font=30, textvariable=choice)
combo['values'] = games
combo.grid(row=1, column=1, padx=10, pady=10)
combo.bind("<KeyRelease>", autocomplete)

tk.Label(text='ราคา', padx=10, font=30).grid(row=2, sticky=tk.W)
Price = tk.StringVar()
et2 = tk.Entry(font=30, width=30, textvariable=Price)
et2.grid(row=2, column=1)

tk.Button(text='ยืนยัน', font=30, width=15, command=calculate_packages).grid(row=4, column=0, sticky=tk.W)
tk.Button(text='ลบข้อมูล', font=30, width=15, command=deletetext).grid(row=4, column=1, sticky=tk.E)

root.mainloop()
