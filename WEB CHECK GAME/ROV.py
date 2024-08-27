import requests

url = "https://termgame.com/api/auth/player_id_login"

payload = {
    "app_id": 100055,
    "login_id": "316588817581170"
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

print(response.status_code)
print(response.json())
