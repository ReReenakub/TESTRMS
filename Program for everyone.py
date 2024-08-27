import tkinter as tk
import pandas as pd
import numpy as np
from tkinter import ttk
import pyautogui
import pyperclip
import keyboard
import time
import mouse
import requests
from requests.exceptions import ConnectionError


mouse.wait(button='left', target_types=('down',))
Q = pyautogui.position()

def deletetext():
    et1.delete(0, tk.END)
    et2.delete(0, tk.END)

def determine_game(input_text):
    if '#' in input_text:
        return 'VALORANT'
    elif '(' in input_text and ')' in input_text:
        try:
            name, uid = input_text.split('(')
            name = name.strip()
            uid = uid.replace(')', '').strip()

            if uid.isdigit():
                return 'PUBG'
        except ValueError:
            pass
    elif input_text.isdigit():
        return 'ROV'
    elif any(char.isdigit() for char in input_text) and ' ' in input_text:
        return 'FREEFIRE'
    elif '_' in input_text:
        return 'OPM'
    else:
        return 'Unknown Game'
def autocomplete(event):
    search_term = combo.get()
    if search_term:
        filtered_games = [game for game in games if search_term.lower() in game.lower()]
        combo['values'] = filtered_games
    else:
        combo['values'] = games

def check_game():
    if choice.get() == "GENSHIN":
        pass
    else:
        print("Button + pressed, but the game is not Genshin")

def calculate_packages():
    sheet_map = {
        'PUBG': 'PUBG',
        'ROV': 'ROV',
        'VALORANT': 'VALORANT',
        'FREEFIRE': 'FREEFIRE',
        'HOK' : 'HOK',
        'ArenaBreakout': 'ARENA',
        'OPM': 'OPM',
        'LOL PC': 'LOL PC',
        'LOL WR': 'LOL WR',
        'GENSHIN': 'GENSHIN'
    }

    input_text = UID.get()  # รับค่าจาก UID
    game_choice = choice.get()  # รับค่าจากตัวเลือกเกม

    if game_choice == "PRVFO":
        Game = determine_game(input_text)
    else:
        Game = game_choice

    if Game not in sheet_map:
        print(f"No sheet found for game {Game}")
        return

    df = pd.read_excel('Price.xlsx', sheet_name=sheet_map[Game])

    if Game == 'PUBG':
        keyboard.wait('ctrl+c')
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

        df['PUBG_baht'] = df['PUBG_baht'].astype(str)

        remaining_budget = et2.get().strip()

        matching_row = df[df['PUBG_baht'] == remaining_budget]

        if not matching_row.empty:
            Total_UC = matching_row['PUBG_currency'].values[0]
            spent_UC_str = matching_row['PUBG_spend'].values[0]
            pyautogui.click(Q)
            time.sleep(0.3)
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
            pyautogui.write(str(remaining_budget))
            pyautogui.write(['tab'] * 17)
            pyautogui.write(str(spent_UC_str))
            pyautogui.write(['tab'] * 11)
            pyautogui.write(uid)
            pyautogui.write(['tab'] * 1)
            pyperclip.copy(name)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.write(['tab'] * 1)
            pyautogui.write(str(Total_UC))
            pyautogui.write(' uc')
            et1.delete(0, tk.END)
            et2.delete(0, tk.END)
            keyboard.wait('ctrl+c')
            keyboard.wait('Enter')
            pyperclip.copy(Autopubg)
        else:
            Total_UC = "ยังไม่มีราคานี้"
            spent_UC_str = "กรุณาตรวจสอบราคาอีกที"
            pyautogui.click(Q)
            time.sleep(0.3)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.write(['tab'] * 1)
            pyautogui.write(Game)
            pyautogui.press('down')
            pyautogui.write(['tab'] * 1)
            pyautogui.write(remaining_budget)
            pyautogui.write(['tab'] * 2)
            pyautogui.press('Enter')
            pyautogui.write(['tab'] * 1)
            pyautogui.press('down')
            pyautogui.write(['tab'] * 1)
            pyautogui.write(str(remaining_budget))
            pyautogui.write(['tab'] * 17)
            pyperclip.copy(spent_UC_str)
            time.sleep(0.2)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.write(['tab'] * 11)
            pyperclip.copy('1')
            time.sleep(0.2)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.write(['tab'] * 1)
            pyperclip.copy(name)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.write(['tab'] * 1)
            pyperclip.copy(Total_UC)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.write(['tab'] * 35)
            pyautogui.hotkey('ctrl', 'c')
            ROR = pyperclip.paste()
            formatted_string = f"รอตรวจสอบแพ็คเกจ---{ROR}"
            pyperclip.copy(formatted_string)
            pyautogui.hotkey('ctrl', 'v')
            et1.delete(0, tk.END)
            et2.delete(0, tk.END)

    elif Game == 'ROV':
        keyboard.wait('ctrl+c')
        input_text = et1.get().strip()

        url = "https://termgame.com/api/auth/player_id_login"
        payload = {
            "app_id": 100055,
            "login_id": input_text
        }
        headers = {
            "accept": "application/json, text/plain, */*",
            "accept-encoding": "gzip, deflate, br, zstd",
            "accept-language": "th,en;q=0.9",
            "content-type": "application/json",
            "cookie": "region=IN.TH; mspid2=4392c6b671c912e61690d782288cb90b; _ga=GA1.1.211920480.1722078655; source=pc; datadome=H_f9dNaxQbJinW0lAbmepdI24MNcODbkztLD8eR5mVvSRpR6G2gsWfhew49gyCXB42UgOhqn_Jpu_X4eLTNbOMSvXlI19dsTn8z0nQQKsh0dQNNAIk2vT4vN_NpIjmP_; session_key=321acf69ufde9ejet0dl67qr7emqtebz; _ga_VRZ5RWC6GM=GS1.1.1724644843.24.1.1724646971.0.0.0",
            "origin": "https://termgame.com",
            "referer": "https://termgame.com/?app=100055",
            "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
            "x-datadome-clientid": "H_f9dNaxQbJinW0lAbmepdI24MNcODbkztLD8eR5mVvSRpR6G2gsWfhew49gyCXB42UgOhqn_Jpu_X4eLTNbOMSvXlI19dsTn8z0nQQKsh0dQNNAIk2vT4vN_NpIjmP_"
        }

        response = requests.post(url, headers=headers, json=payload)
        response_json = response.json()

        if 'error' in response_json:
            if response_json['error'] == 'invalid_id':
                input_text = "ไอดีผิด"
            elif response_json['error'] == 'server':
                input_text = "ระบบขัดข้อง"
        else:
            input_text = et1.get().strip()

        Autorov = """แอดมินเติมคูปองเสร็จเรียบร้อยแล้วนะครับ🥰\n\n⏰รอคูปองดีเลย์ประมาณ 5 - 15 นาที ⏰\n👉หากเกินเวลาดีเลย์แล้วคูปองยังไม่เข้าให้แจ้งแอดมินได้เลยนะครับ\n\n📍พร้อมบริการ “เติมเกมผ่อนได้ นานสูงสุด10เดือน”\nตอกย้ำความคุ้ม รับเงินคืน(Richman Coins) เพื่อสะสมใช้เป็นส่วนลดครั้งถัดไป สูงสุด 25%\nที่ https://www.richmanshop.com\n\n📍ติดตามกิจกรรมโปรโมชั่น ข่าวสาร สำคัญที่\nhttps://www.facebook.com/richmanshoptopup\n\n🎉รับรู้สปอยสกินใหม่ก่อนใครได้ ได้ที่ Youtube ช่อง Richman Shop  🎉\nhttps://www.youtube.com/@Richmanshop\n💞อย่าลืมกดกด Subscribe เพื่อติดตาม Youtube Channel ช่อง Richman Shop ของเราด้วยนะครับ🙏\n\nขอขอบคุณลูกค้าที่ไว้วางใจให้เราดูแล ขอบคุณครับ/ค่ะ"""
        df['ROV_baht'] = df['ROV_baht'].astype(str)

        remaining_budget = et2.get().strip()

        matching_row = df[df['ROV_baht'] == remaining_budget]
        if not matching_row.empty:
            Total_Coupon = matching_row['ROV_currency'].values[0]
            spent_coupon = matching_row['ROV_spend'].values[0]
            pyautogui.click(Q)
            time.sleep(0.3)
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
            pyautogui.write(str(remaining_budget))
            pyautogui.write(['tab'] * 17)
            pyautogui.write(str(spent_coupon))
            pyautogui.write(['tab'] * 11)
            pyperclip.copy(input_text)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.write(['tab'] * 2)
            pyautogui.write(str(Total_Coupon))
            pyperclip.copy(' คูปอง')
            pyautogui.hotkey('ctrl', 'v')
            if 'error' in response_json:
                if response_json['error'] == 'invalid_id':
                    pyautogui.write(['tab'] * 35)
                    pyautogui.hotkey('ctrl', 'c')
                    ROR = pyperclip.paste()
                    formatted_string = f"รอไอดี-------{ROR}"
                    pyperclip.copy(formatted_string)
                    pyautogui.hotkey('ctrl', 'v')
                elif response_json['error'] == 'server':
                    pass
            else:
                keyboard.wait('ctrl+c')
                keyboard.wait('Enter')
                pyperclip.copy(Autorov)
            et1.delete(0, tk.END)
            et2.delete(0, tk.END)
        else:
            Total_Coupon = "ยังไม่มีราคานี้"
            spent_coupon = "กรุณาตรวจสอบราคาอีกที"
            pyautogui.click(Q)
            time.sleep(0.3)
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
            pyautogui.write(str(remaining_budget))
            pyautogui.write(['tab'] * 17)
            pyperclip.copy(spent_coupon)
            time.sleep(0.3)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.write(['tab'] * 11)
            pyautogui.write('1')
            pyautogui.write(['tab'] * 2)
            pyperclip.copy(Total_Coupon)
            time.sleep(0.3)
            pyautogui.hotkey('ctrl', 'v')
            et1.delete(0, tk.END)
            et2.delete(0, tk.END)
            pyautogui.write(['tab'] * 35)
            pyautogui.hotkey('ctrl', 'c')
            ROR = pyperclip.paste()
            formatted_string = f"รอตรวจสอบแพ็คเกจ---{ROR}"
            pyperclip.copy(formatted_string)
            pyautogui.hotkey('ctrl', 'v')
            et1.delete(0, tk.END)
            et2.delete(0, tk.END)

    elif Game == 'VALORANT':
        keyboard.wait('ctrl+c')
        url = "https://order-sg.codashop.com/initPayment.action"
        payload = {
            'voucherPricePoint.id': '950893',
            'voucherPricePoint.price': '279.0000',
            'voucherPricePoint.variablePrice': '0',
            'user.userId': f'{input_text}',
            'voucherTypeName': 'VALORANT',
            'voucherTypeId': '109',
            'gvtId': '139',
            'lvtId': '1325',
            'pcId': '342',
            'shopLang': 'th_TH',
            'absoluteUrl': 'https://www.codashop.com/th-th/valorant',
            'userSessionId': 'ae0c05aa-e80a-41bd-ba88-44697c29a094',
            'clevertapId': 'c12525d3cd934695a81c53bf2dcd9d1a',
            'pricingEngineToken': 'ASfeXyCPT+v87D3hzJ3dqA==#Bq3L3u5VlBc5/QHcWBwZ3HJDXjFIoUu7bM97aHfyFdvV8RlN/svtrfbKGNRC0arAH18wAAiwtFOwDLx+cnLUkuC9uuW5BppmlZP2dnenvtDOCjCF9XuyPD5wmul10Fk73TKoS/A83jBzwjvoWQaSTU2BvufQhkyuPaDXG65F7OJR7oE+Jq3oF+wmB1DqVofaMY/vJMLEZQ8/bXME9WwcJk1JKLN0f2wUcLQbrCV7mbKb7yppRVA/l34Rv0geg3bzzME761kpRo37jnwptdmGJozhqRRvCKLxd+261ayU6nEBv7N/dJxKCXktAlBWIPnSqQ5vS8Bzp+8vDP3hp3aTijTt2GCvkJ5O37gkihnQAHvOkCH2YzT75f/ZygbUleuwj4hkf0kF/Hl3Oh4DA5Ab/jxNo/Z8V9ZtvX8GcNJo3ZOmaVSkybXzYoVcwMbTrc7cSzwXWAVMvwkdLuxOZYXQirUhyCagotcsRPzRIXTUcMJkYmlj+/fkVNIopZR2F1z0HNCP8bFuKHkhVVO3HAgoQD0qJgRzGru/eTh3lnejhnwv7/Hvod/5LmSqX7dtkgmGn8LxQA6+Mqax0e1G1wrCaYX+i6D0gzCaXaKSbb2zyhwZ5/nl6HPdiH9OrSxs2UfG/vqFCR+HZHnpY7WELZmYNVn2VHZVwDOQSo6hTR8kx+GZuZfKytW1nPRKX5zrafSw73jzl/Wyvm5FTOSLqP6zATbHvRnTHjoXmAyL+UXQMol2TMBpcPNt+KItU9hH4mTw3NRiJX0AgThEpWs='
        }

        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'th-TH',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'referer': 'https://www.codashop.com/',
            'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
            'x-expt-context': '{"ns":"codashop","fullUrl":"https://www.codashop.com/th-th/valorant","libraryVersion":"0.38.1","codaCookieId":"c047d05a-dc3a-4c41-bc7e-cc76f1b2544c","domainName":"www.codashop.com","userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36","os":"Windows","mobile":false,"browser":"Not)A;Brand:99/Google Chrome:127/Chromium:127","ip":"58.8.174.145","exptToken":"eyJraWQiOiIyMDIzMTAzMSIsImFsZyI6IkVTMjU2In0.eyJpZCI6IjAxOTBlZWE4LTcyMjktNzk3YS1hMmU1LWM2YjQ5MTUyZDdkMiJ9.6baWRBa-ROitWn4I7Y_QnzhJ1FFNwG7Diz8WSbt98CNCZXrpduxSZ8nVPxqke4abMwRGapeeH8BKo0CQfHztAA","url":"https://www.codashop.com/th-th/valorant","deviceId":"854b0a67-a134-476a-a778-d002f2138127","platformId":1,"lvtId":1325,"lastUsedPcId":342,"emailSaved":false,"country":"TH","loginStatus":0,"userType":0,"whiteLabelId":null,"gvtId":139,"appVersion":"vue2","pageTypeName":"ProductDetail","checkoutId":"24b61be4-ef8f-4fb8-a998-7c133f84163a"}',
            'x-expt-token': 'eyJraWQiOiIyMDIzMTAzMSIsImFsZyI6IkVTMjU2In0.eyJpZCI6IjAxOTBlZWE4LTcyMjktNzk3YS1hMmU1LWM2YjQ5MTUyZDdkMiJ9.6baWRBa-ROitWn4I7Y_QnzhJ1FFNwG7Diz8WSbt98CNCZXrpduxSZ8nVPxqke4abMwRGapeeH8BKo0CQfHztAA',
        }

        response = requests.post(url, data=payload, headers=headers)

        response_json = response.json()
        error_code = response_json.get('errorCode', '')
        Autovalorant = """แอดมินเติม VP เสร็จเรียบร้อยแล้วนะครับ🥰\n\n⏰รอ VP ดีเลย์ประมาณ 5 - 15 นาที ⏰\n👉หากเกินเวลาดีเลย์แล้ว VP ยังไม่เข้าให้แจ้งแอดมินได้เลยนะครับ\n\n📍พร้อมบริการ “เติมเกมผ่อนได้ นานสูงสุด10เดือน”\nตอกย้ำความคุ้ม รับเงินคืน(Richman Coins) เพื่อสะสมใช้เป็นส่วนลดครั้งถัดไป สูงสุด 25%\nที่ https://www.richmanshop.com\n\n📍ติดตามกิจกรรมโปรโมชั่น ข่าวสาร สำคัญที่\nhttps://www.facebook.com/richmanshoptopup\n\nขอขอบคุณลูกค้าที่ไว้วางใจให้เราดูแล ขอบคุณครับ/ค่ะ"""
        df['VALORANT_baht'] = df['VALORANT_baht'].astype(str)

        remaining_budget = et2.get().strip()

        matching_row = df[df['VALORANT_baht'] == remaining_budget]

        if not matching_row.empty:
            Total_VP = matching_row['VALORANT_currency'].values[0]
            spent_VP = matching_row['VALORANT_spend'].values[0]
            pyautogui.click(Q)
            time.sleep(0.3)
            if error_code == '':
                riotid = input_text
                pyautogui.click(Q)
                pyautogui.hotkey('ctrl', 'v')
                pyautogui.write(['tab'] * 1)
                pyautogui.write(Game)
                pyautogui.press('down')
                pyautogui.write(['tab'] * 1)
                pyautogui.write(str(remaining_budget))
                pyautogui.write(['tab'] * 2)
                pyautogui.press('Enter')
                time.sleep(0.2)
                pyautogui.write(['tab'] * 1)
                pyautogui.press('down')
                pyautogui.write(['tab'] * 1)
                pyautogui.write(str(remaining_budget))
                pyautogui.write(['tab'] * 17)
                pyautogui.write(str(spent_VP))
                pyautogui.write(['tab'] * 11)
                pyperclip.copy(riotid)
                time.sleep(0.1)
                pyautogui.hotkey('ctrl', 'v')
                pyautogui.write(['tab'] * 2)
                pyautogui.write(str(Total_VP))
                pyautogui.write(' vp')
                et1.delete(0, tk.END)
                et2.delete(0, tk.END)
                keyboard.wait('ctrl+c')
                keyboard.wait('Enter')
                pyperclip.copy(Autovalorant)
            else:
                if error_code == -200:
                    riotid = "ไอดีต่างประเทศ"
                    error = "รอไอดีใหม่"
                elif error_code == -100:
                    riotid = "ไม่พบไอดีนี้"
                    error = "รอไอดีใหม่"
                elif error_code == -222:
                    riotid = "ใส่ไอดีไม่ครบ"
                    error = "รอไอดีใหม่"
                else:
                    riotid = "ระบบขัดข้อง"
                    error = "รอตรวจสอบไอดี"

                pyautogui.click(Q)
                pyautogui.hotkey('ctrl', 'v')
                pyautogui.write(['tab'] * 1)
                pyautogui.write(Game)
                pyautogui.press('down')
                pyautogui.write(['tab'] * 1)
                pyautogui.write(str(remaining_budget))
                pyautogui.write(['tab'] * 2)
                pyautogui.press('Enter')
                time.sleep(0.2)
                pyautogui.write(['tab'] * 1)
                pyautogui.press('down')
                pyautogui.write(['tab'] * 1)
                pyautogui.write(str(remaining_budget))
                pyautogui.write(['tab'] * 17)
                pyautogui.write(str(spent_VP))
                pyautogui.write(['tab'] * 11)
                pyperclip.copy(riotid)
                time.sleep(0.1)
                pyautogui.hotkey('ctrl', 'v')
                pyautogui.write(['tab'] * 2)
                pyautogui.write(str(Total_VP))
                pyautogui.write(' vp')
                pyautogui.write(['tab'] * 35)
                pyautogui.hotkey('ctrl', 'c')
                ROR = pyperclip.paste()
                formatted_string = f"{error}------{ROR}"
                pyperclip.copy(formatted_string)
                pyautogui.hotkey('ctrl', 'v')
                et1.delete(0, tk.END)
                et2.delete(0, tk.END)

        else:
            Total_VP = "ยังไม่มีราคานี้"
            spent_VP = "กรุณาตรวจสอบราคาอีกที"
            pyautogui.click(Q)
            time.sleep(0.3)
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
            pyautogui.write(str(remaining_budget))
            pyautogui.write(['tab'] * 17)
            pyperclip.copy(spent_VP)
            time.sleep(0.3)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.write(['tab'] * 11)
            pyautogui.write('1')
            pyautogui.write(['tab'] * 2)
            pyperclip.copy(Total_VP)
            time.sleep(0.3)
            pyautogui.hotkey('ctrl', 'v')
            et1.delete(0, tk.END)
            et2.delete(0, tk.END)
            pyautogui.write(['tab'] * 35)
            pyautogui.hotkey('ctrl', 'c')
            ROR = pyperclip.paste()
            formatted_string = f"รอตรวจสอบแพ็คเกจ---{ROR}"
            pyperclip.copy(formatted_string)
            pyautogui.hotkey('ctrl', 'v')
            et1.delete(0, tk.END)
            et2.delete(0, tk.END)

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
        pyautogui.click(Q)
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
        et1.delete(0, tk.END)
        et2.delete(0, tk.END)

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
        pyautogui.click(Q)
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
        et1.delete(0, tk.END)
        et2.delete(0, tk.END)

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
        pyautogui.click(Q)
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
        et1.delete(0, tk.END)
        et2.delete(0, tk.END)

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
        pyautogui.click(Q)
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
        keyboard.wait('ctrl+c')
        keyboard.wait('Enter')
        pyperclip.copy(OPMs)
        et1.delete(0, tk.END)
        et2.delete(0, tk.END)

    elif Game == 'LOL PC':
        Autololpc = """🍁แอดมินเติม RP เสร็จเรียบร้อยแล้วนะครับ🍁\n\n⏰รอ RP ดีเลย์ประมาณ 5 - 15 นาที ⏰\n👉หากเกินเวลาดีเลย์แล้ว RP ยังไม่เข้าให้แจ้งแอดมินได้เลยนะครับ\n\n📍พร้อมบริการ “เติมเกมผ่อนได้ นานสูงสุด10เดือน”\nตอกย้ำความคุ้ม รับเงินคืน(Richman Coins) เพื่อสะสมใช้เป็นส่วนลดครั้งถัดไป สูงสุด 25%\nที่ https://www.richmanshop.com\n\n📍ติดตามกิจกรรมโปรโมชั่น ข่าวสาร สำคัญที่\nhttps://www.facebook.com/richmanshoptopup\n\nขอขอบคุณลูกค้าที่ไว้วางใจให้เราดูแล ขอบคุณครับ/ค่ะ"""
        df = df.replace([np.inf, -np.inf], np.nan).dropna(subset=['LPC_baht', 'LPC_currency'])
        prices = df['LPC_baht'].astype(int).values
        RP_Price = df['LPC_currency'].astype(int).values

        int_Budget = int(Price.get())

        sorted_indices = np.argsort(prices)[::-1]
        sorted_prices = prices[sorted_indices]
        sorted_RP = RP_Price[sorted_indices]

        budget = int_Budget
        RP_count = {}
        Total_RP = 0
        for price, RP in zip(sorted_prices, sorted_RP):
            if budget >= price:
                budget -= price
                Total_RP += RP
                if RP in RP_count:
                    RP_count[RP] += 1
                else:
                    RP_count[RP] = 1

        spent_RP = []
        for RP, count in RP_count.items():
            if count > 1:
                spent_RP.append(f"{RP}*{count}")
            else:
                spent_RP.append(str(RP))
        spent_RP_str = " + ".join(spent_RP)

        remaining_budget = int_Budget - budget
        keyboard.wait('ctrl+c')
        time.sleep(0.3)
        pyautogui.click(Q)
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
        pyautogui.write(str(spent_RP_str))
        pyautogui.write(['tab'] * 11)
        time.sleep(0.3)
        pyperclip.copy(input_text)
        time.sleep(0.3)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.write(['tab'] * 2)
        pyautogui.write(str(Total_RP))
        pyautogui.write(' rp')
        et1.delete(0, tk.END)
        et2.delete(0, tk.END)
        keyboard.wait('ctrl+c')
        keyboard.wait('Enter')
        pyperclip.copy(Autololpc)

    elif Game == 'LOL WR':
        Autololwr = """💓 แอดมินเติม WC เสร็จเรียบร้อยแล้วนะครับ 💓\n\n⏰รอ WC ดีเลย์ประมาณ 5 - 15 นาที ⏰\n👉หากเกินเวลาดีเลย์แล้ว WC ยังไม่เข้าให้แจ้งแอดมินได้เลยนะครับ\n\n📍พร้อมบริการ “เติมเกมผ่อนได้ นานสูงสุด10เดือน”\nตอกย้ำความคุ้ม รับเงินคืน(Richman Coins) เพื่อสะสมใช้เป็นส่วนลดครั้งถัดไป สูงสุด 25%\nที่ https://www.richmanshop.com\n\n📍ติดตามกิจกรรมโปรโมชั่น ข่าวสาร สำคัญที่\nhttps://www.facebook.com/richmanshoptopup\n\nขอขอบคุณลูกค้าที่ไว้วางใจให้เราดูแล ขอบคุณครับ/ค่ะ"""

        df = df.replace([np.inf, -np.inf], np.nan).dropna(subset=['LWR_baht', 'LWR_currency'])
        prices = df['LWR_baht'].astype(int).values
        WC_Price = df['LWR_currency'].astype(int).values

        int_Budget = int(Price.get())

        sorted_indices = np.argsort(prices)[::-1]
        sorted_prices = prices[sorted_indices]
        sorted_WC = WC_Price[sorted_indices]

        budget = int_Budget
        WC_count = {}
        Total_WC = 0
        for price, WC in zip(sorted_prices, sorted_WC):
            if budget >= price:
                budget -= price
                Total_WC += WC
                if WC in WC_count:
                    WC_count[WC] += 1
                else:
                    WC_count[WC] = 1

        spent_WC = []
        for WC, count in WC_count.items():
            if count > 1:
                spent_WC.append(f"{WC}*{count}")
            else:
                spent_WC.append(str(WC))
        spent_WC_str = " + ".join(spent_WC)

        remaining_budget = int_Budget - budget
        keyboard.wait('ctrl+c')
        time.sleep(0.3)
        pyautogui.click(Q)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.write(['tab'] * 1)
        pyautogui.write("lol w")
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
        pyautogui.write(str(spent_WC_str))
        pyautogui.write(['tab'] * 11)
        time.sleep(0.3)
        pyperclip.copy(input_text)
        time.sleep(0.3)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.write(['tab'] * 2)
        pyautogui.write(str(Total_WC))
        pyautogui.write(' wc')
        et1.delete(0, tk.END)
        et2.delete(0, tk.END)
        keyboard.wait('ctrl+c')
        keyboard.wait('Enter')
        pyperclip.copy(Autololwr)

    elif Game == 'GENSHIN':
        def update_server(uid: int) -> str:
            uid_str = str(uid)
            if uid_str.startswith('8'):
                return f"Uid: {uid_str} , Genshin Server: Asia"
            elif uid_str.startswith('7'):
                return f"Uid: {uid_str} , Genshin Server: Europe"
            elif uid_str.startswith('6'):
                return f"Uid: {uid_str} , Genshin Server: America"
            elif uid_str.startswith('9'):
                return f"Uid: {uid_str} , Genshin Server: TW, HK, MO"
            elif uid_str.startswith('1'):
                return f"Uid: {uid_str} , Genshin Server: Asia"
            else:
                return f"Uid: {uid_str} , Genshin Server: Unknown"
        AutoGC = """แอดมินเติม Genesis Crytals หรือ พรดวงจันทร์ เสร็จเรียบร้อยแล้วนะครับ🥰\n\n⏰รอ Genesis Crytals หรือ พรดวงจันทร์ ดีเลย์ประมาณ 5 - 15 นาที ⏰\n👉หากเกินเวลาดีเลย์แล้ว Genesis Crytal ยังไม่เข้าให้แจ้งแอดมินได้เลยนะครับ\n\n📍พร้อมบริการ “เติมเกมผ่อนได้ นานสูงสุด10เดือน”\nตอกย้ำความคุ้ม รับเงินคืน(Richman Coins) เพื่อสะสมใช้เป็นส่วนลดครั้งถัดไป สูงสุด 25%\nที่ https://www.richmanshop.com\n\n📍ติดตามกิจกรรมโปรโมชั่น ข่าวสาร สำคัญที่\nhttps://www.facebook.com/richmanshoptopup\n\nขอขอบคุณลูกค้าที่ไว้วางใจให้เราดูแล ขอบคุณครับ/ค่ะ"""
        df['Genshin_baht'] = df['Genshin_baht'].astype(str)

        gensin_suit_input = et2.get().strip()

        matching_row = df[df['Gensin_suit'] == gensin_suit_input]

        if not matching_row.empty:
            input_price = matching_row['Genshin_baht'].values[0]
            spent_GC_str = matching_row['Genshin_currency'].values[0]
        else:
            spent_GC_str = "ราคาไม่พบในชีท"
            input_price = "ไม่พบในชีท"

        uid = int(et1.get().strip())
        server_info = update_server(uid)

        keyboard.wait('ctrl+c')
        time.sleep(0.3)
        pyautogui.click(Q)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.write(['tab'] * 1)
        pyautogui.write("gen")
        pyautogui.press('down')
        pyautogui.write(['tab'] * 1)
        pyautogui.write(str(input_price))
        pyautogui.write(['tab'] * 2)
        pyautogui.press('Enter')
        pyautogui.write(['tab'] * 1)
        pyautogui.press('down')
        pyautogui.write(['tab'] * 1)
        pyautogui.write(str(input_price))
        pyautogui.write(['tab'] * 17)
        pyperclip.copy(str(server_info))
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.write(['tab'] * 11)
        time.sleep(0.3)
        pyperclip.copy(input_text)
        time.sleep(0.3)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.write(['tab'] * 2)
        pyperclip.copy(spent_GC_str)
        pyautogui.hotkey('ctrl', 'v')
        et1.delete(0, tk.END)
        et2.delete(0, tk.END)
        keyboard.wait('ctrl+c')
        keyboard.wait('Enter')
        pyperclip.copy(AutoGC)

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

games = ["PRVFO", "ROV", "PUBG", "VALORANT", "FREEFIRE", "HOK", "ArenaBreakout", "OPM", "LOL PC", "LOL WR", "GENSHIN"]
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

plus_button = tk.Button(root, text='+', font=15, command=check_game)
plus_button.grid(row=1, column=2, padx=5, pady=5)

root.mainloop()
