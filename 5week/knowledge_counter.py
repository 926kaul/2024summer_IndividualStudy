import os
import re

# 디렉토리 경로 설정
directory_path = r'C:/MyCode/5week/knowledge_file'

# 파일 이름이 숫자로 시작하고 'FAIL'이라는 단어가 들어가지 않은 파일을 필터링하는 함수
def is_valid_file(filename):
    #return re.match(r'^\d', filename) and 'FAIL' not in filename
    return re.match(r'^\d', filename)

# 디렉토리 내의 파일을 탐색하고 조건을 만족하는 파일의 수를 센다
valid_file_count = sum(1 for filename in os.listdir(directory_path) if is_valid_file(filename))

print(f"조건을 만족하는 파일의 수: {valid_file_count}")