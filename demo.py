import requests
import json

url = 'http://172.25.63.21:8080/v1/chat'

payload = json.dumps({
  "question": "军营村电站2024年4月24日收益",
  "top_k": "3",
  "tool_threshold": 0.705,
  "base_threshold": 0.85,
  "flag": "1fd27f8c55384fe48e271cc677afa8cf"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
