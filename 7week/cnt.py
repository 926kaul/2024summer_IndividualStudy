import json

file_path = '6week/original_data0~500.json'
file_path2 = '6week/merged_data.json'
with open(file_path, 'r', encoding='utf-8') as file:
    top500 = json.load(file)
with open(file_path2, 'r', encoding='utf-8') as file:
    merged = json.load(file)

maxl = 0
maxli = 0
for i in range(500):
    try:
        if maxl < max(maxl,  len(top500[str(i)]['developer_urls'])):
            maxli = i
        maxl = max(maxl,  len(top500[str(i)]['developer_urls']))
    except:
        pass
    try:
        for item in merged[str(i)]:
            if maxl < max(maxl, len(item['developer_urls'])):
                maxli = i + 1000
            maxl = max(maxl, len(item['developer_urls']))
    except:
        pass


print(maxl)
print(maxli)