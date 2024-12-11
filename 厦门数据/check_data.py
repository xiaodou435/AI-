import json
import glob

log_files = [
    '0306的环控信息.log', '0306的BMS信息.log', '0306的BMS状态.log',
    '0306的PCS信息.log', '0306的PCS状态.log', '0306的SOC是多少.log',
    '0306的SOH是多少.log', '0306的关口表信息.log', '0306的并网表信息.log',
    '0306的总电压.log', '0306的总电流.log', '0306的环控信息.log', '0306的电表信息.log'
]

log_files2 = [
    "厦门海辰动力站20KW107KWH的环控信息.log",
    "厦门海辰动力站20KW107KWH的BMS信息.log",
    "厦门海辰动力站20KW107KWH的BMS状态.log",
    "厦门海辰动力站20KW107KWH的PCS信息.log",
    "厦门海辰动力站20KW107KWH的PCS状态.log",
    "厦门海辰动力站20KW107KWH的SOC是多少.log",
    "厦门海辰动力站20KW107KWH的SOH是多少.log",
    "厦门海辰动力站20KW107KWH的关口表信息.log",
    "厦门海辰动力站20KW107KWH的并网表信息.log",
    "厦门海辰动力站20KW107KWH的总电压.log",
    "厦门海辰动力站20KW107KWH的总电流.log",
    "厦门海辰动力站20KW107KWH的环控信息.log",
    "厦门海辰动力站20KW107KWH的电表信息.log"
]

for log_file in log_files:
    with open(log_file, 'r', encoding='utf-8') as file:
        try:
            data_list = json.load(file)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from {log_file}: {str(e)}")
            continue
        
    matching_items = []
    question_count = 0
    station_count = 0

    for item in data_list:
        if "question" in item and "data" in item and "tool" in item["data"] and "arguments" in item["data"]["tool"]:
            question = item["question"]
            question_count += 1

            arguments = item["data"]["tool"]["arguments"]
            
            if "station" in arguments:
                station_name = arguments["station"]
                if question == station_name:
                    print(f"Question: {question}")
                    print(f"Station Name: {station_name}")
                    
                    station_count += 1
                    matching_items.append(item)

    print(f"Total Questions: {question_count}")
    print(f"Total Repeat Stations: {station_count}")
