import requests

response = requests.delete('http://localhost:5000/products/1')
if response.status_code == 204:
    print('Product deleted')
else:
    print('Error:', response.text)
