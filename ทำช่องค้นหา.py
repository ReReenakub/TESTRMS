import tkinter as tk
from tkinter import ttk

def autocomplete(event):
    search_term = combo.get()
    if search_term:
        filtered_games = [game for game in games if search_term.lower() in game.lower()]
        combo['values'] = filtered_games
    else:
        combo['values'] = games

root = tk.Tk()
root.title("Game Search")

# รายชื่อเกม
games = ["ROV", "PUBG", "VALORANT", "FREEFIRE", "ACE RACER"]

# สร้าง Combobox แบบ Autocomplete
choice = tk.StringVar()
combo = ttk.Combobox(root, width=30, font=('Helvetica', 10), textvariable=choice)
combo['values'] = games
combo.grid(row=1, column=1, padx=10, pady=10)


combo.bind("<KeyRelease>", autocomplete)

root.mainloop()
