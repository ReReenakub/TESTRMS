import tkinter as tk
from tkinter import ttk, messagebox
import requests
import pyperclip

def fetch_player_data(uid, game):
    if game == 'GENSHIN':
        url = f"https://enka.network/u/{uid}/__data.json?x-sveltekit-invalidated=01"
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'th,en;q=0.9',
            'Connection': 'keep-alive',
            'Cookie': 'globalToggles=eyJ1aWQiOnRydWUsIm5pY2tuYW1lIjp0cnVlLCJkYXJrIjpmYWxzZSwic2F2ZUltYWdlVG9TZXJ2ZXIiOmZhbHNlLCJzdWJzdGF0cyI6ZmFsc2UsInN1YnNCcmVha2Rvd24iOmZhbHNlLCJ1c2VyQ29udGVudCI6ZmFsc2UsImFkYXB0aXZlQ29sb3IiOmZhbHNlLCJwcm9maWxlQ2F0ZWdvcnkiOjAsImhpZGVOYW1lcyI6ZmFsc2UsImhveW9fdHlwZSI6MH0; locale=th',
            'Referer': f'https://enka.network/u/{uid}/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        response = requests.get(url, headers=headers)
        data = response.json()

        try:
            player_info = data['nodes'][1]['data']
            nickname = player_info[2]
            level = player_info[3]

            if uid.startswith('8') or uid.startswith('18'):
                server = "Asia"
            elif uid.startswith('7'):
                server = "Europe"
            elif uid.startswith('6'):
                server = "America"
            elif uid.startswith('9'):
                server = "TW, HK, MO"
            else:
                server = "Unknown"

            return f"Genshin Impact\nUID : {uid}\nชื่อตัวละคร : {nickname}\nLevel AR : {level}\nเซิฟเวอร์ : {server}"

        except KeyError:
            return None
        except IndexError:
            return "เว็บค้าง เช็คด้วยตัวเองไปก่อน"

    elif game == 'HSR':
        url = f"https://enka.network/hsr/{uid}/__data.json?x-sveltekit-invalidated=01"
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'th,en;q=0.9',
            'Connection': 'keep-alive',
            'Cookie': 'locale=th; globalToggles=eyJ1aWQiOnRydWUsIm5pY2tuYW1lIjp0cnVlLCJkYXJrIjpmYWxzZSwic2F2ZUltYWdlVG9TZXJ2ZXIiOmZhbHNlLCJzdWJzdGF0cyI6ZmFsc2UsInN1YnNCcmVha2Rvd24iOmZhbHNlLCJ1c2VyQ29udGVudCI6ZmFsc2UsImFkYXB0aXZlQ29sb3IiOmZhbHNlLCJwcm9maWxlQ2F0ZWdvcnkiOjAsImhpZGVOYW1lcyI6ZmFsc2UsImhveW9fdHlwZSI6MX0',
            'Referer': 'https://enka.network/?hsr',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        response = requests.get(url, headers=headers)
        data = response.json()

        try:
            detail_info = data['nodes'][1]['data']
            nickname = detail_info[3]
            server = "Unknown"
            if uid.startswith('8') or uid.startswith('18'):
                server = "Asia"
            elif uid.startswith('7'):
                server = "Europe"
            elif uid.startswith('6'):
                server = "America"
            elif uid.startswith('9'):
                server = "TW, HK, MO"
            return f"Honkai Star Rail\nUID : {uid}\nชื่อตัวละคร : {nickname}\nเซิฟเวอร์ : {server}"
        except KeyError:
            return None
        except IndexError:
            return "เว็บค้าง เช็คด้วยตัวเองไปก่อน"

    return "Data not available for this game."


def confirm_action():
    uid = uid_entry.get()
    game = game_var.get()
    if not uid or not game:
        messagebox.showwarning("Input Error", "Please enter UID and select a game.")
        return

    data = fetch_player_data(uid, game)

    if data is None:
        messagebox.showwarning("Input Error", "เช็คไอดี หรือ เกมให้อีกที")
        return

    def copy_to_clipboard():
        pyperclip.copy(data)

    def close_info_window():
        info_window.destroy()
        uid_entry.delete(0, tk.END)

    info_window = tk.Toplevel(root)
    info_window.title("ข้อมูลตัวละคร")

    info_label = tk.Label(info_window, text=data, padx=10, pady=10)
    info_label.pack()

    confirm_button = tk.Button(info_window, text="Confirm", command=lambda: [copy_to_clipboard(), close_info_window()])
    confirm_button.pack(pady=5)

    info_window.update_idletasks()
    window_width = info_label.winfo_reqwidth() + 20
    window_height = info_label.winfo_reqheight() + 50
    info_window.geometry(f'{window_width}x{window_height}')

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    info_window.geometry(f'{window_width}x{window_height}+{x}+{y}')


def delete_data():
    uid_entry.delete(0, tk.END)
    game_var.set('')


root = tk.Tk()
root.title("Game Information")

tk.Label(root, text="UID:").grid(row=0, column=0, padx=10, pady=5)
uid_entry = tk.Entry(root)
uid_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Select Game:").grid(row=1, column=0, padx=10, pady=5)
game_var = tk.StringVar(value='GENSHIN')
game_menu = ttk.Combobox(root, textvariable=game_var, values=['GENSHIN', 'HSR'])
game_menu.grid(row=1, column=1, padx=10, pady=5)

confirm_button = tk.Button(root, text="Confirm", command=confirm_action)
confirm_button.grid(row=2, column=0, padx=10, pady=10)

delete_button = tk.Button(root, text="Delete Data", command=delete_data)
delete_button.grid(row=2, column=1, padx=10, pady=10)

# Lock the main window size
root.resizable(False, False)

root.mainloop()
