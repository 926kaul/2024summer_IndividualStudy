import json

file_path = '6week/original_data0~500.json'
file_path2 = '6week/merged_data.json'
file_path3 = '6week/fixed_data.json'

ans = {}

with open(file_path2, 'r', encoding='utf-8') as file:
    merged = json.load(file)

for i in range(500):
    if len(merged[str(i)]) != 0 and type(merged[str(i)][0]) == list:
        ans[str(i)] = merged[str(i)][0]
    else:
        ans[str(i)] = merged[str(i)]

with open(file_path3, 'w') as f:
    json.dump(ans, f, indent=4)
