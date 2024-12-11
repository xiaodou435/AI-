import json
import glob

log_files = [
    '0306的环控信息.log', '0306的BMS信息.log', '0306的BMS状态.log',
    '0306的PCS信息.log', '0306的PCS状态.log', '0306的SOC是多少.log',
    '0306的SOH是多少.log', '0306的关口表信息.log', '0306的并网表信息.log',
    '0306的总电压.log', '0306的总电流.log', '0306的环控信息.log', '0306的电表信息.log'
]
log_files1 = [
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



for file  in log_files:
    
    print(file)
    with open(file, 'r', encoding='utf-8') as file:
        data_list = json.load(file)

        matching_items = []
        repeat_device_count = 0
        repeat_station_count = 0
        question_count =0
        tool_null_count=0
        question_tool_count=0


    for item in data_list:
        try:
            question = item["question"]
            
            tool = item["data"]["tool"] 
            # print(tool)
            if "arguments" in tool:
                arguments = item["data"]["tool"]["arguments"]
                arguments = json.loads(item["data"]["tool"]["arguments"])
                question_count +=1
                if "device" in arguments:
                    
                    device_name = arguments["device"]
                    
                    if question == device_name:
                        # print(arguments)
                        repeat_device_count+=1
                        matching_items.append(item)

                        
                    
                
                elif "station" in arguments:
                    station_name = arguments["station"]
                    if question == station_name:
                        repeat_station_count+=1
                        matching_items.append(item)
                
            else:
                tool_null_count+=1
                # print(item)
                print(f'打印 {question} {tool}空的')
        
        except(json.JSONDecodeError, ValueError) as e:
                print(f"解析 {file} 的数据时出错：{e}")
                print(item)
                continue
    
    print(f'{question}  :标题重复{repeat_device_count}---------------------------概率{repeat_device_count/question_count*100}%')
    print(f'{question:}  :标题重复{repeat_station_count}----------------------------概率{repeat_station_count/question_count*100}%')
    print(f'{question:}   :执行次----------------------------------{question_count}')
    print(f'{question}     :null次数{tool_null_count},,,是空的概率----------------------{tool_null_count/question_count*100}%')
        
# print(f'{file:}{repeat_device_count}')
# print(f'{file:}{repeat_station_count}')
# print(f'{file:}{question_count}')