import requests

user_id = "802239915"

url = f"https://enka.network/hsr/{user_id}/__data.json?x-sveltekit-invalidated=01"

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
    uid = user_id
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
    print("Honkai Star Rail")
    print(f"UID : {uid}")
    print(f"ชื่อตัวละคร : {nickname}")
    print(f"เซิฟเวอร์ : {server}")

except KeyError as e:
    print(f"KeyError: {e}")
    print("Check JSON the correct keys.")
except IndexError as e:
    print(f"IndexError: {e}")
    print("Check list the JSON response.")