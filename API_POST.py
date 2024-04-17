import requests

data = {
    "name": " teste ",
    "price": 000.00,
    "stock": 10
}

response = requests.post('http://localhost:5000/products', json=data)
if response.status_code == 201:
    task = response.json()
    print(task)
else:
    print('Error:', response.text)

