import requests
endpoint = "http://localhost:8000/api/products/"

get_response = requests.post(endpoint, data={'title':'probanco fbv', 'price':100})
print(get_response.json())