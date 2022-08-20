import json
import pandas as pd

data_path = './data/law/original_data/'

with open(data_path + '은행법.json', 'r') as f:
    data = json.load(f)

law_dict = {'은행법' : {}}
df = pd.DataFrame(data['은행법'])
print(df)

# a = {1:'가', 2:'나', 3:'다', 4: {5:'바', 6: {7:'아', 8: {9: '카'}}}}

# for i in iter(a):
#     print(i)