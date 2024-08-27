import requests
import pycountry

url = "https://termgame.com/api/auth/player_id_login"
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "th,en;q=0.9",
    "content-type": "application/json",
    "cookie": "mspid2=b7e8317a2475947e3c328b599c94ef04; _fbp=fb.1.1708628069101.490407097; _ga_67W3SZP2HC=GS1.1.1718265334.5.1.1718265346.0.0.0; region=IN.TH; _ga=GA1.1.137757638.1708628069; source=pc; datadome=WQ7QKeT40MfCTqylyNBeuYyfxFLsfDSkUDg9SGN~0cmBW5Pdkv3zsT2HBI6XBqMGuRRPnrKUny9BtvvnaDNYBbWn5KAujdOq1bhVYjAHNjVNnyz9WXPurwkgkq9BRPa8; session_key=yn0iosktrmuuzbif48fnop74jkn950k1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "origin": "https://termgame.com",
    "referer": "https://termgame.com/?app=100067",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "sec-ch-ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    "sec-ch-ua-platform": '"Windows"',
    "x-datadome-clientid": "WQ7QKeT40MfCTqylyNBeuYyfxFLsfDSkUDg9SGN~0cmBW5Pdkv3zsT2HBI6XBqMGuRRPnrKUny9BtvvnaDNYBbWn5KAujdOq1bhVYjAHNjVNnyz9WXPurwkgkq9BRPa8"
}




uid = "6488619130"
payload = {
    "app_id": 100067,
    "login_id": f"{uid}"
}
response = requests.post(url, headers=headers, json=payload)
try:
    data = response.json()
    region_code = data.get('region', '').upper()
    country = pycountry.countries.get(alpha_2=region_code)
    country_name = country.name if country else f"{region_code}"
    print(f"UID: {uid}\nName: {data['nickname']}\nRegion: {country_name}")
except KeyError:
    print(data)

