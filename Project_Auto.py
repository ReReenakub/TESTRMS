import tkinter as tk
import pandas as pd
import numpy as np
from tkinter import ttk
import pyautogui
import pyperclip


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


# Load the data
df = pd.read_csv('Price.csv')

# Clean the data by filling non-finite values
df['PUBG_baht'] = df['PUBG_baht'].replace([np.inf, -np.inf, np.nan], 0)
df['PUBG_currency'] = df['PUBG_currency'].replace([np.inf, -np.inf, np.nan], 0)

# Convert columns to integers
prices = df['PUBG_baht'].astype(int).values
coupons_per_price = df['PUBG_currency'].astype(int).values


def calculate_packages():
    try:
        initial_budget = int(Price.get())

        budget = initial_budget
        spent_price = 0
        total_coupons = 0

        sorted_indices = np.argsort(prices)[::-1]
        sorted_prices = prices[sorted_indices]
        sorted_UC = UC_Price[sorted_indices]

        budget = initial_budget
        spent_prices = []
        Total_UC = 0
        for price, UC in zip(sorted_prices, sorted_UC):
            if budget >= price:
                budget -= price
                spent_prices.append(price)
                Total_UC += UC

        Game = choice.get()
        currency2 = Price.get()
        amount = UID.get()

        if Game == 'PUBG':
            pyautogui.click(x=3559, y=181)
            pyperclip.copy('A')
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.write(['tab'] * 1)
            pyautogui.write(Game)
            pyautogui.press('down')
            pyautogui.write(['tab'] * 1)
            pyautogui.write(currency2)
            pyautogui.write(['tab'] * 2)
            pyautogui.press('Enter')
            pyautogui.write(['tab'] * 1)
            pyautogui.press('down')
            pyautogui.write(['tab'] * 1)
            pyautogui.write(currency2)
            pyautogui.write(['tab'] * 17)
            pyautogui.write(str(spent_price))
            pyautogui.write(['tab'] * 11)
            pyautogui.write(amount)
            pyautogui.write(['tab'] * 1)
            pyautogui.write('Ree')
            pyautogui.write(['tab'] * 1)
            pyautogui.write(str(total_coupons))
    except ValueError:
        print("Please enter a valid number for the price.")


root = tk.Tk()
root.title('บอทเกม')

tk.Label(text='ใส่ UID & Riot', padx=10, font=30).grid(row=0, sticky=tk.W)
UID = tk.StringVar()
et1 = tk.Entry(font=30, width=30, textvariable=UID)
et1.grid(row=0, column=1)

games = ["ROV", "PUBG", "VALORANT", "FREEFIRE", "ACE RACER"]
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
