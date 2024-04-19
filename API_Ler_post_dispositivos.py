import requests

def read_and_post_users(file_path, api_url="http://localhost:5000/products"):
  
    users_added = 0
    try:
        with open(file_path, 'r') as file:
            for line in file:
                name, price, stock = line.strip().split('; ')

                data = {
                    "name": name,
                    "price": price,
                    "stock": stock
                }

                response = requests.post(api_url, json=data)

                if response.status_code == 201:
                    users_added += 1
                    print(f"Product added: {name}")  # Print success message
                else:
                    print(f"Error adding product: {name} - {response.text}")

    except Exception as e:
        print(f"An error occurred while reading the file: {str(e)}")

    return users_added

# Example usage (replace with your actual file path)
users_added = read_and_post_users("dispositivos.txt")
print(f"{users_added} products added from the file.")


