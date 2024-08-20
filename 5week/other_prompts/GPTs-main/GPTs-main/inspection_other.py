import os
import glob
import shutil


keywords = ["account","malicious","ID","password","send","request",".com","http","ignore","post","token","action","API","regardless","server"] 

folder_path = "C:/MyCode/5week/other_prompts/GPTs-main/GPTs-main/prompts"
file_paths =  glob.glob(os.path.join(folder_path, '*'))

result = {key: [] for key in keywords}
cntsum = set()

for file_path in file_paths:
    if os.path.isfile(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                for keyword in keywords:
                    if keyword in content:
                        cntsum.add(content)
                        result[keyword].append(file_path)
                        dst_dir = "C:/MyCode/5week/other_prompts/GPTs-main/GPTs-main/inspections/"+keyword
                        if not os.path.exists(dst_dir):
                            os.makedirs(dst_dir)
                        shutil.copy(file_path, dst_dir)
        except Exception as e:
            print(f"파일 {file_path}을(를) 읽는 중 오류 발생: {e}")

for key in result:
    print(key, len(result[key]))
print(len(cntsum))