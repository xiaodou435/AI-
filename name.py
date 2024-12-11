import json
from collections import defaultdict

# 提供的数据列表
data_list = [
    {
        "question": "厦门海辰动力站20KW107KWH的BMS信息",
        "data": {
            "llm": "",
            "tool": {
                "name": "device_bms",
                "arguments": "{\"device\": \"厦门海辰动力站20KW107KWH\"}"
            },
            "rag": "",
            "recommend": [],
            "flag": "1fd27f8c55384fe48e271cc677afa8cf"
        },
        "time": "20240621202104"
    },
    {
        "question": "厦门海辰动力站20KW107KWH电站2024年5月13日告警情况",
        "data": {
            "llm": "",
            "tool": {
                "name": "station_warning",
                "arguments": "{\"station\": \"厦门海辰动力站20KW107KWH\", \"start\": \"2024-05-13\", \"end\": \"2024-05-13\"}"
            },
            "rag": "",
            "recommend": [],
            "flag": "1fd27f8c55384fe48e271cc677afa8cf"
        },
        "time": "20240622004007"
    },
    {
        "question": "厦门海辰动力站20KW107KWH电站2024年5月13日告警情况",
        "data": {
            "llm": "",
            "tool": {
                "name": "station_warning",
                "arguments": "{\"station\": \"厦门海辰动力站20KW107KWH电站\", \"start\": \"2024-05-13\", \"end\": \"2024-05-13\"}"
            },
            "rag": "",
            "recommend": [],
            "flag": "1fd27f8c55384fe48e271cc677afa8cf"
        },
        "time": "20240622004252"
    },
    {
        "question": "厦门海辰动力站20KW107KWH电站2024年5月13日告警情况",
        "data": {
            "llm": "",
            "tool": {
                "name": "station_warning",
                "arguments": "{\"station\": \"厦门海辰动力站20KW107KWH电站\", \"start\": \"2024-05-13\", \"end\": \"2024-05-13\"}"
            },
            "rag": "",
            "recommend": [],
            "flag": "1fd27f8c55384fe48e271cc677afa8cf"
        },
        "time": "20240622004548"
    },
    {
        "question": "厦门海辰动力站20KW107KWH电站2024年5月13日告警情况",
        "data": {
            "llm": "",
            "tool": {
                "name": "station_warning",
                "arguments": "{\"station\": \"厦门海辰动力站20KW107KWH电站\", \"start\": \"2024-05-13\", \"end\": \"2024-05-13\"}"
            },
            "rag": "",
            "recommend": [],
            "flag": "1fd27f8c55384fe48e271cc677afa8cf"
        },
        "time": "20240622004851"
    }
]

# 使用 defaultdict 来统计每个 question 下的 tool.name 的出现次数
question_tool_count = defaultdict(lambda: defaultdict(int))

for item in data_list:
    question = item["question"]
    tool_name = item["data"]["tool"]["name"]
    question_tool_count[question][tool_name] += 1

# 输出统计结果
for question, tools in question_tool_count.items():
    print(f"Question: {question}")
    for tool_name, count in tools.items():
        print(f"    {tool_name}: {count}次")
