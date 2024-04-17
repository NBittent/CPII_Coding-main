import requests

def read_and_post_users(file_path, api_url="http://localhost:5000/users"):
    """Reads user data from a text file and adds users via a POST request.

    Args:
        file_path (str): Path to the text file containing user data.
        api_url (str, optional): URL of the API endpoint to create users. Defaults to "http://localhost:5000/users".

    Returns:
        int: Number of users successfully added.
    """

    users_added = 0
    try:
        with open(file_path, 'r') as file:
            for line in file:
                name, email, idade = line.strip().split(',')

                data = {
                    "name": name,
                    "email": email,
                    "idade": int(idade)
                }

                response = requests.post(api_url, json=data)

                if response.status_code == 201:
                    users_added += 1
                    print(f"User added: {name}")  # Print success message
                else:
                    print(f"Error adding user: {name} - {response.text}")

    except Exception as e:
        print(f"An error occurred while reading the file: {str(e)}")

    return users_added

# Example usage (replace with your actual file path)
users_added = read_and_post_users("users.txt")
print(f"{users_added} users added from the file.")
