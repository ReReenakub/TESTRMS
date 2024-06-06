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

def calculate_packages():
    Game = choice.get()
    if Game == 'PUBG':
        df = pd.read_csv('Price.csv')
        prices = df['PUBG_baht'].values
        UC_Price = df['PUBG_currency'].values
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

        print([int(uc) for uc in spent_UC])
        print(int(int_Budget - budget))
        print(int(Total_UC))



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
