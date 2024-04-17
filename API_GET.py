import requests

response = requests.get('http://127.0.0.1:5000/products')
if response.status_code == 200:
    tasks = response.json()
    print(tasks)
else:
    print('Error:', response.text)
