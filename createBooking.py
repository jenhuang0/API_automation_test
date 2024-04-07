import requests

# URL and authentication information from auth.json
url = 'https://restful-booker.herokuapp.com/booking'

with open('auth.json', 'r') as f:
    token = f.read()
    token = token[11:-2]


headers = {'Content-Type': 'application/json'
            , 'Accept': 'application/json'
            , 'Cookie': 'token=' + token}

# Booking data
booking_data = {
    "firstname": "Jim",
    "lastname": "Brown",
    "totalprice": 111,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2021-01-01",
        "checkout": "2021-01-02"
    },
    "additionalneeds": "Breakfast"
}

# Send the request
response = requests.post(url, headers=headers, json=booking_data)

# check the response
if response.status_code == 200:
    print('Booking successful')
    #split the response text into a list of lines and save it into booking_info.json and print each line
    with open('booking_info.json', 'w') as f:
        f.write(response.text)
    response_lines = response.text.splitlines()
    for line in response_lines:
        print(line)
else:
    print('Booking failed')
    print(response.text)
    print(response.status_code)
    print(response.headers) 