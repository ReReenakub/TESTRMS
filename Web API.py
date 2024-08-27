import requests

url = "https://order-sg.codashop.com/initPayment.action"

#wiff main#trash ไอดีต่างประเทศ
#Evilz#9753 ไอดีไทย
#Evilz#975 ไอดีผิด
#Evilz ใส่ไอดีไม่ครบ

payload = {
    'voucherPricePoint.id': '950893',
    'voucherPricePoint.price': '279.0000',
    'voucherPricePoint.variablePrice': '0',
    'user.userId': 'Evilz#9753',
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
error_msg = response_json.get('errorMsg', '')

print("errorMsg:", error_msg)
