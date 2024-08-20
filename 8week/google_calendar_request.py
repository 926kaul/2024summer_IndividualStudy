import requests

# 액세스 토큰 (OAuth 인증 후 받은 토큰)
access_token = 'CNjq7fez7ocDENjq7fez7ocDGAUggMfYugIogMfYugI'

# API 엔드포인트 URL
url = 'https://www.googleapis.com/calendar/v3/users/me/calendarList'

# HTTP 헤더 설정
headers = {
    'Authorization': f'Bearer {access_token}',
    'Accept': 'application/json'
}

# API 요청 보내기
response = requests.get(url, headers=headers)

# 응답 처리
if response.status_code == 200:
    # 요청이 성공했을 경우, 캘린더 목록을 JSON 형식으로 파싱
    calendar_list = response.json()
    print(calendar_list)
else:
    # 에러 발생 시 에러 코드와 메시지 출력
    print(f'Error: {response.status_code} - {response.text}')
