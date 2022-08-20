import json
import pandas as pd
import os

data_path = './data/law/str_data/'

file_name = os.listdir(data_path)

total_dict = {}
for file in file_name:
    name = file.replace('.json','')
    print(name)
    with open(data_path + file, 'r') as f:
        data = json.load(f)
    total_dict[name] = data[name]
# print(total_dict)

with open('./master/' + 'law.json', 'w') as outfile:
    json.dump(total_dict, outfile, indent="\t", ensure_ascii=False)