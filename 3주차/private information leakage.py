import requests

url = "http://34.134.116.133:8000/gather"
payload = {"text": "This is private information"}
response = requests.post(url, json=payload)

print(response.text)
