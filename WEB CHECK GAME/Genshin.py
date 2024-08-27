import time

import requests

user_id = "1803035438"

url = f"https://enka.network/u/{user_id}/__data.json?x-sveltekit-invalidated=01"

headers = {
    'Accept': '*/*',
    'Accept-Language': 'th,en;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': 'globalToggles=eyJ1aWQiOnRydWUsIm5pY2tuYW1lIjp0cnVlLCJkYXJrIjpmYWxzZSwic2F2ZUltYWdlVG9TZXJ2ZXIiOmZhbHNlLCJzdWJzdGF0cyI6ZmFsc2UsInN1YnNCcmVha2Rvd24iOmZhbHNlLCJ1c2VyQ29udGVudCI6ZmFsc2UsImFkYXB0aXZlQ29sb3IiOmZhbHNlLCJwcm9maWxlQ2F0ZWdvcnkiOjAsImhpZGVOYW1lcyI6ZmFsc2UsImhveW9fdHlwZSI6MH0; locale=th',
    'Referer': f'https://enka.network/u/{user_id}/',
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
player_info = data['nodes'][1]['data']

uid = user_id
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

print("Genshin Impact")
print(f"UID คือ : {uid}")
print(f"ชื่อตัวละคร : {nickname}")
print(f"Level AR : {level}")
print(f"เซิฟเวอร์ : {server}")
