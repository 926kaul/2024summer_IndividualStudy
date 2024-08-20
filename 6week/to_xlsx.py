import pandas as pd
import json
import re
import glob
import os

file_path = '6week/original_data0~500.json'
file_path2 = '6week/fixed_data.json'
csv_file_path = '6week/data'

with open(file_path, 'r', encoding='utf-8') as file:
    data1 = json.load(file)

with open(file_path2, 'r', encoding='utf-8') as file:
    data2 = json.load(file)

attributes = ['name', 'ID', 'developer', 'conversations', 'developer_urls', 'urls']
pattern = r'g-([^-\s]+)-'

for i in range(500):
    rows = []
    ii = str(i)
    new_csv = csv_file_path + ii +'.csv'
    if 'error' in data1[ii]:
        continue

    row = {attr: data1[ii].get(attr, None)  for attr in attributes}
    tmp_developer_urls = data1[ii].get('developer_urls', None)
    tmp_urls = data1[ii].get('urls', None)
    row['developer_urls'] = tmp_developer_urls[0] if len(tmp_developer_urls) > 0 else None
    row['urls'] = tmp_urls[0] if len(tmp_urls) > 0 else None
    row['ID'] = re.findall(pattern, row['ID'])[0]
    rows.append(row)
    if len(tmp_developer_urls) > 1 or len(tmp_urls)> 1:
        for j in range(1, max(len(tmp_developer_urls),len(tmp_urls))):
            row = {attr: None  for attr in attributes}
            row['developer_urls'] = tmp_developer_urls[j] if len(tmp_developer_urls) > j else None
            row['urls'] = tmp_urls[j] if len(tmp_urls) > j else None
        rows.append(row)

    for item in data2[ii]:
        if 'error' in item:
            continue
        try:
            if data1[ii]['ID'] == item['ID']:
                continue
            row = {attr: item.get(attr, None) for attr in attributes}
            tmp_developer_urls = item.get('developer_urls', None)
            tmp_urls = item.get('urls', None)
            row['developer_urls'] = tmp_developer_urls[0] if len(tmp_developer_urls) > 0 else None
            row['urls'] = tmp_urls[0] if len(tmp_urls) > 0 else None
            row['ID'] = re.findall(pattern, row['ID'])[0]
            rows.append(row)
            if len(tmp_developer_urls) > 1 or len(tmp_urls)> 1:
                for j in range(1, max(len(tmp_developer_urls),len(tmp_urls))):
                    row = {attr: None  for attr in attributes}
                    row['developer_urls'] = tmp_developer_urls[j] if len(tmp_developer_urls) > j else None
                    row['urls'] = tmp_urls[j] if len(tmp_urls) > j else None
                rows.append(row)
        except Exception as e:
            print(ii)
            print(f'{e}')

    df = pd.DataFrame(rows, columns=attributes)
    df.to_csv(new_csv, index = False)



def clean_sheet_name(sheet_name):
    # 유효하지 않은 문자 목록
    invalid_chars = ['\\', '/', '*', '[', ']', ':', '?']
    for char in invalid_chars:
        sheet_name = sheet_name.replace(char, '')
    return sheet_name

csv_files = glob.glob('6week/*.csv')
with pd.ExcelWriter('6week/data.xlsx', engine='openpyxl') as writer:
    for csv_file in csv_files:
        # CSV 파일명에서 시트 이름 생성 (확장자 제거)
        sheet_name = os.path.basename(csv_file).replace('.csv', '')
        
        # 시트 이름에서 유효하지 않은 문자 제거
        sheet_name = clean_sheet_name(sheet_name)
        
        # CSV 파일을 pandas 데이터프레임으로 읽기
        df = pd.read_csv(csv_file)
        
        # 데이터프레임을 Excel 파일의 시트로 저장
        df.to_excel(writer, sheet_name=sheet_name, index=False)