import json


file1_path = '6week/data1.json'
file2_path = '6week/data2.json'
with open(file1_path, 'r', encoding='utf-8') as file:
    data1 = json.load(file)
with open(file2_path, 'r', encoding='utf-8') as file:
    data2 = json.load(file)

merged_data = {}
for i in range(500):
    tmp = []
    if len(data1[str(i)]) == len(data2[str(i)]):
        for j in range(len(data1[str(i)])):
            if data1[str(i)][j].keys() == data2[str(i)][j].keys():
                tmp.append(data1[str(i)][j])
                try:
                    tmp[-1]["urls"] = list(set(data1[str(i)][j]["urls"] +  data2[str(i)][j]["urls"]))
                except:
                    pass
            elif len(data1[str(i)][j].keys()) > len(data2[str(i)][j].keys()):
                tmp.append(data1[str(i)][j])
            else:
                tmp.append(data1[str(i)][j])
    elif len(data1[str(i)]) > len(data2[str(i)]):
        tmp.append(data1[str(i)])
    else:
        tmp.append(data2[str(i)])
    merged_data[i] = tmp
    with open('6week/merged_data.json','w') as json_file:
        json.dump(merged_data,json_file,indent=4)