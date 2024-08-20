import matplotlib.pyplot as plt
import pandas as pd
import json

file_path = '7week/sim_lst.csv'
df = pd.read_csv(file_path, header=None, na_values='')
df = df.where(pd.notna(df), None)
sim_lst = df.values.tolist()

file_path = '7week/original_data0~500.json'
file_path2 = '7week/fixed_data.json'


with open(file_path, 'r', encoding='utf-8') as file:
    original = json.load(file)
    
with open(file_path2, 'r', encoding='utf-8') as file:
    merged = json.load(file)


cases ={}
cnt = 0
for i in range(3000):
    for j in range(3000):
        try:
            if sim_lst[i][j] is not None and i<j<i+6 and 0.5 < sim_lst[i][j] <= 0.6 and i%6==0:
                if original[str(i//6)]['ID'] != merged[str(i//6)][j-i-1]['ID']:
                    cases[cnt] = [sim_lst[i][j],original[str(i//6)],merged[str(i//6)][j-i-1]]
                    with open('7week/similar_gpts2.json','w') as json_file:
                        json.dump(cases,json_file,indent=4)
                    print((sim_lst[i][j],original[str(i//6)]['name'],merged[str(i//6)][j-i-1]['name']))
                    cnt+=1
        except:
            print(i,j)
            continue


