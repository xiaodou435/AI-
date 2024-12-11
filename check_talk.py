from zhushou import base
import time
import os
import json
def save_data(data,question):
    # 基础文件名
    base_file_name = 'result'

    file_name = f'{question}.log'

    # 检查文件是否存在
    if os.path.exists(file_name):
        print(f"文件 '{file_name}' 已存在。追加数据。")

        # 加载现有数据
        with open(file_name, 'r', encoding='utf-8') as file:
            try:
                existing_data = json.load(file)
            except json.JSONDecodeError:
                existing_data = []
    else:
        existing_data = []

    # 将新数据追加到现有数据中
    existing_data.append(data)

    # 将合并后的 JSON 数据写入文件
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(existing_data, file, ensure_ascii=False, indent=4)

    print(f'数据已追加到文件 {file_name}')


while True:
    questions = {"0306电站位置","0306有多少电站","0306电站投产","0306电站投产容量"," "}
    questions = {"0306电站2024年5月14日收益情况","0306电站2024年5月12日充电情况","0306电站2024年5月13日放电情况","0306电站2024年5月13日告警情况"}
    questions = {"0306的BMS信息","0306的BMS状态","0306的总电压","0306的总电流","0306的SOC是多少","0306的SOH是多少","0306的PCS信息","0306的PCS状态","0306的电表信息","0306的并网表信息","0306的关口表信息","0306的环控信息"}
    
#     questions = [
#     "厦门海辰动力站20KW107KWH电站位置",
#     "厦门海辰动力站20KW107KWH有多少电站",
#     "厦门海辰动力站20KW107KWH电站投产",
#     "厦门海辰动力站20KW107KWH电站投产容量",
#     "厦门海辰动力站20KW107KWH我有那些电站",
#     "厦门海辰动力站20KW107KWH电站2024年5月14日收益情况",
#     "厦门海辰动力站20KW107KWH电站2024年5月12日充电情况",
#     "厦门海辰动力站20KW107KWH电站2024年5月13日放电情况",
#     "厦门海辰动力站20KW107KWH电站2024年5月13日告警情况",
#     "厦门海辰动力站20KW107KWH的BMS信息",
#     "厦门海辰动力站20KW107KWH的BMS状态",
#     "厦门海辰动力站20KW107KWH的总电压",
#     "厦门海辰动力站20KW107KWH的总电流",
#     "厦门海辰动力站20KW107KWH的SOC是多少",
#     "厦门海辰动力站20KW107KWH的SOH是多少",
#     "厦门海辰动力站20KW107KWH的PCS信息",
#     "厦门海辰动力站20KW107KWH的PCS状态",
#     "厦门海辰动力站20KW107KWH的电表信息",
#     "厦门海辰动力站20KW107KWH的并网表信息",
#     "厦门海辰动力站20KW107KWH的关口表信息",
#     "厦门海辰动力站20KW107KWH的环控信息"
# ]
    
    for question in questions:

        a = base(question)
        save_data(a,question)

    


