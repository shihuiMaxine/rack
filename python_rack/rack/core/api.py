import requests

# Define the API endpoint and authentication credentials
endpoint = 'https://api.example.com/authenticate'
username = 'your_username_here'
password = 'your_password_here'

# Make a request to the authentication endpoint to obtain a token
response = requests.post(endpoint, auth=(username, password))
if response.status_code == 200:
    # Extract the token from the response
    token = response.json().get('token')
    print(f'Token: {token}')
else:
    print(f'Authentication failed with status code {response.status_code}')

