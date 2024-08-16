import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedTk
import pyperclip
from datetime import datetime

root = ThemedTk(theme="equilux")  # ใช้ธีม equilux
root.title("โปรแกรมลูกค้า")

# ตั้งค่าขนาดหน้าต่าง
root.geometry("300x220")

# ตั้งค่าธีม equilux
style = ttk.Style()
style.configure('TLabel', background='#3D3D3D', foreground='#FFFFFF')  # สีพื้นหลังและตัวอักษรสำหรับ Label
style.configure('TEntry', fieldbackground='#4F4F4F', foreground='#FFFFFF')  # สีพื้นหลังและตัวอักษรสำหรับ Entry
style.configure('TRadiobutton', background='#3D3D3D', foreground='#FFFFFF')  # สีพื้นหลังและตัวอักษรสำหรับ Radiobutton
style.configure('TButton', background='#5A5A5A', foreground='#FFFFFF')  # สีพื้นหลังและตัวอักษรสำหรับปุ่ม
root.configure(bg='#3D3D3D')  # สีพื้นหลังของหน้าต่างหลัก

# สร้างเลเบลและช่องกรอกสำหรับ "เลข SO"
label_so = ttk.Label(root, text="เลข SO ༼ つ ◕_◕ ༽つ")
label_so.pack(pady=5)
entry_so = ttk.Entry(root)
entry_so.pack(pady=5)

# สร้างเลเบลและช่องกรอกสำหรับ "ชื่อลูกค้า"
label_customer = ttk.Label(root, text="ชื่อลูกค้า (•_•)")
label_customer.pack(pady=5)
entry_customer = ttk.Entry(root)
entry_customer.pack(pady=5)

# สร้างเฟรมสำหรับจัดการปุ่ม Radio
frame_radio = tk.Frame(root, bg='#3D3D3D')
frame_radio.pack(pady=5)

# สร้างปุ่ม Radio 2 ปุ่ม สำหรับ "Facebook" และ "LINE"
contact_method = tk.StringVar(value="Facebook")
radio_facebook = ttk.Radiobutton(frame_radio, text="Facebook", variable=contact_method, value="Facebook")
radio_facebook.pack(side="left", padx=10)

radio_line = ttk.Radiobutton(frame_radio, text="LINE", variable=contact_method, value="LINE")
radio_line.pack(side="left", padx=10)

# สร้างปุ่ม "ยืนยัน" และ "ประวัติ"
frame_buttons = tk.Frame(root, bg='#3D3D3D')
frame_buttons.pack(pady=10)

history = []

def confirm():
    so_number = entry_so.get()
    customer_name = entry_customer.get()
    contact = contact_method.get()
    confirm_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    entry_data = f"{so_number} -- ชื่อลูกค้า: {customer_name} -- ช่องทางติดต่อ: {contact} -- เวลา: {confirm_time}"
    history.append(entry_data)

    entry_so.delete(0, tk.END)
    entry_customer.delete(0, tk.END)
    contact_method.set("Facebook")
    pyperclip.copy(entry_data)

def show_history():
    if history:
        history_window = tk.Toplevel(root)
        history_window.title("ประวัติการยืนยัน")
        history_window.geometry("600x400")
        history_window.configure(bg='#3D3D3D')

        text_area = tk.Text(history_window, wrap=tk.WORD, width=80, height=20, bg='#4F4F4F', fg='#FFFFFF')
        text_area.pack(pady=20, padx=10, expand=True, fill=tk.BOTH)

        for item in history:
            text_area.insert(tk.END, item + "\n")

        total_label = tk.Label(history_window, text=f"ทำรายการไปทั้งหมด {len(history)} ครั้ง", bg='#3D3D3D', fg='#FFFFFF')
        total_label.pack(pady=10)

        text_area.config(state=tk.DISABLED)  # ทำให้ Text widget เป็นโหมดอ่านอย่างเดียว
    else:
        messagebox.showinfo("ประวัติ", "ยังไม่มีรายการในประวัติ")

button_confirm = ttk.Button(frame_buttons, text="ยืนยัน", command=confirm)
button_confirm.pack(side="left", padx=10)

button_history = ttk.Button(frame_buttons, text="ประวัติ", command=show_history)
button_history.pack(side="left", padx=10)

# เริ่มต้นโปรแกรม
root.mainloop()
