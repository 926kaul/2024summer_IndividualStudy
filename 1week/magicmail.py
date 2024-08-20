import requests

# API endpoint
url = "https://auth.pluginlab.ai/oauth/authorize"

# 요청에 필요한 데이터
payload = {"clientId":"10bdad977b77b8faed28fc5bf1c2bf6b",
           "redirectUri":"https://chat.openai.com/aip/g-0ed7079e98c454ec612805f33063573da019f6b8/oauth/callback",
           "responseType":"code",
           "memberId":"mem_b06e74e3d249e9519b6fb7ee2a6c1e3d7b7ca102"}

# 헤더 설정
headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJ1aWQiOiJtZW1fMDdmOWNkZDQyOTFkMDUxNDRjZGE2YTc1N2EwOTU3ZDkzNjY4ZjEzMyIsImlhdCI6MTcxODg2ODkxNSwiaXNzIjoidXJuOnBsdWdpbmxhYjppc3N1ZXIiLCJhdWQiOiJ1cm46YzdkNTkyMTZlZThlYzU5YmRhNWU1MWZmYzE3YTk5NGQ6YXVkaWVuY2UiLCJleHAiOjE3MTkwNDE3MTV9.RuHWzUaoIqpe43qzE0Y0eC1lLNibNjwcPr1X5L2RLsA",
    "Content-Type": "application/json"
}

# 요청 보내기
response = requests.post(url, json=payload, headers=headers)

# 응답 확인
if response.status_code == 200:
    print("Magic email code 요청 성공!")
    print("응답 데이터:", response.json())
else:
    print("요청 실패:", response.status_code)
    print("응답 데이터:", response.text)
