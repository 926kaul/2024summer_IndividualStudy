import json


pairs = {}
with open('7week/similar_gpts2.json','r') as json_file:
    pairs = json.load(json_file)

for item in pairs:
    ori = pairs[item][1]['instructions']
    sim = pairs[item][2]['instructions']
    with open(f'7week/similar2/{item}.original_{pairs[item][0]}.txt','w',encoding='utf-8') as f:
        ori.replace('.','\n')
        f.write(ori)
    with open(f'7week/similar2/{item}.repilca_{pairs[item][0]}.txt','w',encoding='utf-8') as f:
        sim.replace('.','\n')
        f.write(sim)