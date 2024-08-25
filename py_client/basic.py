import requests

endpoint="https://httpbin.org/status/200"
endpoint="http://localhost:8000/api/"

get_response = requests.post(endpoint, json={"title":"hello world", 'price':'123'})
print(get_response.text)