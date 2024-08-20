import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from time import sleep
import undetected_chromedriver as uc
from fake_useragent import UserAgent
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import random
import re
from datetime import datetime
import json
from selenium.webdriver.common.action_chains import ActionChains

# ChromeDriver 경로 명시
chrome_service = Service('C:/MyCode/5week/chromedriver.exe')

# Chrome 옵션 설정
op = uc.ChromeOptions()
op.add_argument(r"user-data-dir=C:\Users\jhk\AppData\Local\Google\Chrome\User Data")
op.add_argument('--no-sandbox')  # 옵션 추가
op.add_argument('--disable-dev-shm-usage')  # 옵션 추가
op.add_argument('--remote-debugging-port=9222')  # 디버깅 포트 설정

# 드라이버 시작
driver = uc.Chrome(service=chrome_service, options=op)

url = "https://gptstore.ai/gpts/actions?page="

# 웹페이지 순회 및 작업 수행
json_object = dict()

for rank in range(1,198):
    driver.get(url+str(rank))
    print(rank)
    sleep(5)
    try:
        inputElements = driver.find_elements(By.XPATH, '//td[@class="whitespace-nowrap px-3 py-5 text-sm "]')
        if not inputElements:
            continue
        lst = [i for i in range(len(inputElements)) if "chat-prompt" in inputElements[i].text]
        ans = []
            
        inputTitles = driver.find_elements(By.XPATH, '//a[@class="text-indigo-600 hover:text-indigo-900"]')
        ans = [inputTitles[2*idx].get_attribute('href') for idx in lst]
        for j in range(len(ans)):
            json_object[24*(rank-1)+lst[j]] = ans[j]

        if ans:
            with open('9week/chat_prompts_GPTs.json','w') as json_file:
                json.dump(json_object,json_file,indent=4)
    except Exception as e:
        print(f'{e} in {url+str(rank)}')
        continue

# 드라이버 종료
driver.quit()