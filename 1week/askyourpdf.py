import requests
import brotli
import gzip
import zlib

# API endpoint
url = "https://auth-service.askyourpdf.com/gpt/oauth?client_id=dee4fdb8-2fa5-4113-a7e9-010d53ead270&redirect_uri=https:%2F%2Fchat.openai.com%2Faip%2Fg-e5bcd4d33dafc38618e2a010322bddaf00d3a004%2Foauth%2Fcallback&state=26719291-5acf-47d0-96b7-c2491feb80e9"

# 요청에 필요한 데이터
params = {
    "client_id": "dee4fdb8-2fa5-4113-a7e9-010d53ead270",
    "redirect_uri": "https://chat.openai.com/aip/g-e5bcd4d33dafc38618e2a010322bddaf00d3a004/oauth/callback",
    "state": "b33faa26-5a35-4e1c-a8ca-f950dad9aeba"
}

# 헤더 설정
headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NjczZTc4NDhlYTA3YWZlMDQ1MDdjNDAiLCJhdWQiOlsiYXNrcGRmLXVzZXJzOmF1dGgiXSwidHlwZSI6ImFjY2VzcyIsInJvbGVzIjpbImJhc2ljIiwiYXBpX2ZyZWUiXSwiZXhwIjoxNzUwNDA3OTkzfQ.crqwfvhUwbqjFT2hJjFNah7l00y-DvYWfqSHXdj2il4",
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Origin": "https://secure.askyourpdf.com",
    "Referer": "https://secure.askyourpdf.com/",
    "Sec-Ch-Ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}
# 요청 보내기
response = requests.get(url, headers=headers, params=params)

# 응답 확인
if response.status_code == 200:
    print("Magic email code 요청 성공!")
    content_encoding = response.headers.get('Content-Encoding')
    if content_encoding == 'gzip':
        response_data = gzip.decompress(response.content).decode('utf-8')
    elif content_encoding == 'deflate':
        response_data = zlib.decompress(response.content, -zlib.MAX_WBITS).decode('utf-8')
    elif content_encoding == 'br':
        response_data = brotli.decompress(response.content).decode('utf-8')
    else:
        response_data = response.text

    print("응답 데이터:", response_data)
else:
    print("요청 실패:", response.status_code)
    print("응답 데이터:", response.text)
