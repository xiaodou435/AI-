import requests
import json
from jsonpath import jsonpath
from write import w_d
import time

def base(question):
    
    url = "http://172.25.63.21:8080/v1/chat"
    payload =json.dumps({
    "question": question,
    "top_k": "3",
    "tool_threshold": 0.705,
    "base_threshold": 0.85,
    "flag": "1fd27f8c55384fe48e271cc677afa8cf"
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code==200:
        # print("接口请求成功") 
        re = response.json()
        # print(response)
        code  = jsonpath(re,'$.code')[0]
        assert code ==200, "Code is 200"
        messages  = jsonpath(re,'$.messages')[0]
        # print(messages)
        assert messages =="success", " messages is success"

        if messages =='success':
            data =jsonpath(re,'$.data')[0]
            llm =jsonpath(re,'$..llm')[0]
            tool = jsonpath(re,'$..tool')[0]
            rag =jsonpath(re,'$..rag')[0]
            # print(data)
            timestamp = time.strftime('%Y%m%d%H%M%S')
            total= {'question':question,'data':data,'time':timestamp}
            # print(total)
            return total
            # w_d(data)
    else:
        print("接口返回{}".format(response.status_code))
        print(response.text)
        
    



# base("电站信息")
# base("1")