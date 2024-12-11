from collections import Counter
import json
# Sample data provided
log_files1 = [
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


# Iterate over each file
for file_path in log_files2:
    print(f"Processing file: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as file:
        try:
            data_list = json.load(file)

            
        except json.JSONDecodeError as e:
            print(f"Error reading JSON from file {file_path}: {e}")
            continue
    cout=0
    count={}
    for item1 in data_list:
        try:
            question = item1["question"]
            
            tool = item1["data"]["tool"] 
            # print(tool)
            if "name" in tool:
                names = [item1["data"]["tool"]["name"]][0]
                # names = [item['data']['tool']['name'] for item in item1]
                cout+=1    
            name_counts = Counter(names)                
            
                 
        except(json.JSONDecodeError, ValueError) as e:
                print(f"解析 {file} 的数据时出错：{e}")
                continue
    print(f"Name: {names}, Count: {cout}")
    print(count)