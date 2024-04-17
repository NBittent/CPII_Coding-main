import requests

data = {
    "name": " desodorante ",
    "price": 000.00,
   "stock": 10
}

response = requests.put('http://localhost:5000/products/2', json=data)
if response.status_code == 200:
    task = response.json()
    print(task)
else:
    print('Error:', response.text)
