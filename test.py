import requests
import json

url = "http://hc-lims.hithium.com:8090/api/login"

payload = json.dumps({
  "staffNo": "HC22010001",
  "password": "ZZOLaNpl/P1znsIl2QQD/QTHBjpUBoxm1AXdX2c3MqY3qmy+dXmxy0VnBgp2Ug4AaBT+B0/X2NlyUWFbae9hVlQqIVIUB82xc42gEB7G/uVQ28mmq4Fhc0laqu8ExJp1/hdZmHeXt+YXLdjmNQ4GFU5MKJ2FcOMcwLckYaKwu9s=",
  "captcha": ""
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, json=payload)

print(response.text)


