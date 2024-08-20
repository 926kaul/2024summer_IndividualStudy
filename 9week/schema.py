import requests
import string
import random
import xml.etree.ElementTree as ET

def generate_random_string(length=10):
    # 사용할 수 있는 문자들 (대문자, 소문자, 숫자)
    characters = string.ascii_letters + string.digits
    # 지정된 길이의 랜덤 문자열 생성
    random_string = ''.join(random.choice(characters) for i in range(length))
    return random_string


for i in range(1):
    # API 엔드포인트
    url = "https://chat-prompt.com/youtube/SearchVideos"

    random_string = generate_random_string(12)
    # 요청 매개변수
    params = {
        "query": f"{random_string}",  # 원하는 주제
        "botname": f"{random_string}"  # GPT의 이름
    }

    params_finance_1 = {
        "Links" : "https://www.investing.com/news/cryptocurrency-news/bitcoin-rises-above-30000, https://www.coindesk.com/markets/2024/08/18/ethereum-price-surges/, https://cryptonews.com/news/solana-adoption-rate-increases.htm",
        "nextIntentPrediction" : "analyze and summarize the cryptocurrency market based on these articles.",
        "v2" : True
    }

    params_textto_1 = {
        "keyword" : "hello"
    }

    # API 키가 필요한 경우 헤더에 추가
    headers = {
    }

    # GET 요청 보내기
    prms = params_textto_1
    response = requests.get(url, headers=headers, params=prms)
    print(prms)

    # 응답 확인
    if response.status_code == 200:
        # JSON 응답 파싱
        try:
            product_info = response.json()
            print("Product Information:", product_info)
        except:
            try:
                print(response)
            except:
                pass
    else:
        print(f"Failed to get product info. Status code: {response.status_code}, Response: {response.text}")
