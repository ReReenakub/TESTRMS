import numpy as np
import pandas as pd
import tkinter as tk
game = 'Pubg'
df = pd.read_csv('Price.csv')
prices = df[f"{game}_baht"].values
UC_Price = df['UC'].values

def calculate_packages():
    try:
        initial_budget = int(budget_entry.get())
    except ValueError:
        result_text.configure(state="normal")
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "กรุณาป้อนงบประมาณเป็นตัวเลข")
        result_text.configure(state="disabled")
        return

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

    spent_prices_int = [int(price) for price in spent_prices]
    Total_UC_int = int(Total_UC)
    initial_budget_int = int(initial_budget)
    budget_int = int(budget)

    result_message = (
        f"แพ็คที่ใช้แนะนำ: {spent_prices_int}\n"
        f"แอดแนะนำแพ็ค {initial_budget_int - budget_int} บาทได้ {Total_UC_int} UC ครับ"
    )
    result_text.configure(state="normal")
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, result_message)
    result_text.configure(state="disabled")

root = tk.Tk()
root.title("โปรแกรมคำนวณ UC")
root.geometry("400x400")
root.configure(bg="#f0f0f0")

frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=20, padx=20, fill="both", expand=True)

font = ("Niramit", 12)

budget_label = tk.Label(frame, text="ป้อนงบประมาณ (บาท):", bg="#f0f0f0", font=font)
budget_label.pack(pady=5)

budget_entry = tk.Entry(frame, width=20, font=font)
budget_entry.pack(pady=5)

calculate_button = tk.Button(frame, text="คำนวณ", command=calculate_packages, bg="#4CAF50", fg="white", font=font)
calculate_button.pack(pady=5)

canvas = tk.Canvas(frame, bg="#ffffff")
canvas.pack(pady=20, padx=10, fill="both", expand=True)

scrollbar = tk.Scrollbar(canvas, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

result_text = tk.Text(canvas, yscrollcommand=scrollbar.set, wrap="word", bg="#ffffff", font=font)
result_text.pack(side="left", fill="both", expand=True)

canvas.create_window((0, 0), window=result_text, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

result_text.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

root.mainloop()
