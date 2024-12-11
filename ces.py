import requests
while True:
    url = "http://81.68.247.125:8080/"

    payload={}
    headers = {
    'Authorization': '{{token}}',
    'User-Agent': 'Apifox/1.0.0 (https://apifox.com)'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)
