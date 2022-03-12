import requests

url = 'http://localhost:8000/api/products/'
response = requests.get(url)
response_on_python = response.json()
with open('products.txt', 'w') as file:
    for product in response_on_python:
        file.write(
            f"The {product['name']} is "
            f"{product['amount_in_stock']}\n"
        )
