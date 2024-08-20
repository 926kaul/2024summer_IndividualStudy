import json


pairs = {}
with open('7week/fixed_data.json','r') as json_file:
    gpts = json.load(json_file)

cnt = 0
while True:
    ID = input()

    for gpt_lst in gpts.values():
        for gpt in gpt_lst:
            if "ID" in gpt and gpt["ID"] == ID:
                with open(f'7week/similar/{cnt}.inst.txt','w',encoding='utf-8') as f:
                    if "instructions" in gpt:
                        tmp = gpt["instructions"]
                        tmp.replace('.','\n')
                        f.write(tmp)
    cnt +=1