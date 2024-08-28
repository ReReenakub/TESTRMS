import requests

# URL of the endpoint
url = "https://www.midasbuy.com/interface/getCharac"

# Headers for the request
headers = {
    "authority": "www.midasbuy.com",
    "method": "POST",
    "path": "/interface/getCharac",
    "scheme": "https",
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "th,en;q=0.9",
    "content-type": "application/json",
    "origin": "https://www.midasbuy.com",
    "referer": "https://www.midasbuy.com/midasbuy/th/buy/pubgm",
    "sec-ch-ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "traceparent": "00-732acd3f24bfc8d0cb66ba5a1473d9af-4374b761050f6e7c-00",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
}

# Cookies for the request
cookies = {
    "midasbuyDeviceId": "048461223618699111715375275519",
    "tKeplerToken": "tid0FuoCuJXdIgi7_6ZZ7WzjxGLLrIT3wkpBkwNobHQtKPs*",
    "tencent_tdrc": "SCricc11qQjtwg6SrPgQ0wsEr9gREtGqNi",
    # Add other cookies as needed
}

# Payload for the POST request
payload = {
    "ctoken": "3050ef61de169aedd3390bb7ba0022dda86fab873204ead52059674642b560331774d983a74a45c2fb07f55e2891b801",
    "ctoken_ver": "1.0.1",
    "encrypt_msg": "ktBOlNrGBwxgN3fUHMr1Pi7h4m3gzq3ygRg5SBvAh22Aly/2Bk59roI65/MJd25oX2Ugp/k2eyQcwuNE0QO/6bRxqnCHq7QctcVG5xKYbHWbZ0E9zCmpNfYnTxZYP/0CZlPsPl89qSUre5xzAUs1rxhNmtEfbGLmIBA/HMvffG2SNcJX2nQvo12uYPTJ0u1O/zKDPAW9lFRtRtgSlTTKoLrSXKwYoaFQhQsmIsqWn658nkZy7OFKiSvOB334rNcv08ovQCle7lCVVB9OtpyajbGlVtzUuoHsZEElYRa0+tVb5FF+4DyBgAxMEUPR475fCNqs1GEXAm5E5YYBx7TwNa7Dy9bntBfNvJm8WsNCPVZLpEAgSHzawg1611jQhVKPTg1GYc/nmi1bI6AwlV1xBkmYHyRFK4gitgTiFu3TEH0hc7PAvSXtnOWvgZvyjm56wnRnzJer46qRJdVCfRm8OGqbbNMlPqbFyCKAud3OTZtbpw+KMiWSzdYyObQR4cNZkXoPBn4N3SOp9lgTwWQOIafNkVT3Ynf4tgRu8awsu3sJHbaogPyXF5cq8pHhRVEn12x8c+412A+bHSR3raRByHr66qY1/rsJNLToFXaiCo/ag/92w58EkZNV2fHTKJjEdHVH4Bp67QlEHEi2YZRej+f/i+ow1crRvRfIK8FwEiwXi7QauRK11mVsL6IIWjylZM3QobrJfLDDPhk3ZLDga/TMTk6Yqg6sMTO5wYkQ6+A79zKtmA3H0fghzEEnn2AQySUYFJPtlgCBudZlCoJ6UyHfTzvxdcm5YzlNW5td4rNQhbEVVU5/MCjGou22QfaJMkc0JjoBpIpYywRv/mdmzbjQsjf+HTWNpR/pznUPLyuJI3FwYkfiLOOeaMbjb+Gwvu0fQaLpcWY3I5zxb/zDe82sMS+4UIWEygGdo57fntQ8XIWyc3od7wNd+vTaRplz/81ZGS09lrjpko+LB2KgwPo2Q02Bo+jl8O5j/Lv4fQFr/vUv25GwRUsfD2LwlBcSmx+B0olOMdfnJ/41sSActfdV8EjJkCuIdZJUrUQ1ZH7mGS+IhNGa52UwewbNEPdCfJayrfD9N3VukiaMa11x+FVAbXq2lUnJ3f1ddFlQ9C9qDgVn9VuFCA7Oea8y1CfVBKcyI4wVtEpGGMiJV0Rnbs2XHmMtX42wBG3Pg5bIkUGQ4x343Pqytw/CuTlbtlef+cXzl1RMDFSeiYgye+yy4udwtKJmLzGewheTshoGOGKe3St1ZZVzWJPvqYSaAqwwk88KvVK77R80aKV+mk3+Pxt6tMMP8TC69MIel04ueLWdcCNxvit9ivadc6GW+4azkufV7dajqHIVrond+TfbU0EShGJVN+meBCos8ZJCpMrSYsE2Gh4rAKaJKvDkh86d6alDOYpy0R2Cmh8jIEf0bpFkJKKCPJWsRTPQtug4dHs="
}

# Send the POST request
response = requests.post(url, headers=headers, cookies=cookies, json=payload)

# Check the response status
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Request failed with status code {response.status_code}")
