import requests

product_id = input("What is the product u wanna destroy: ")
try:
    product_id = int(product_id)
except:
    print('product not found')

if product_id:
    endpoint=f"http://localhost:8000/api/products/{product_id}/delete"

    get_response = requests.delete(endpoint)
    print(get_response.status_code)