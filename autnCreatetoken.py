import requests

# URL and authentication information
url = 'https://restful-booker.herokuapp.com/auth'
headers = {'Content-Type': 'application/json'}
autn_data = '{"username": "admin", "password": "password123"}'

# Send the request
response = requests.post(url, headers=headers, data=autn_data)

# Print the response
print(response.text)
print(response.status_code)
print(response.headers)

# Extract the token and save it in auth.json
token = response.json()['token']
with open('auth.json', 'w') as f:
    f.write('{"token": "' + token + '"}')
    