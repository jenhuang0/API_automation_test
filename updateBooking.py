import requests

# URL and authentication information from auth.json and booking_info.json
# extract the booking ID from booking_info.json
with open('booking_info.json', 'r') as f:
    booking_info = f.read()
    booking_id = booking_info[13:17]
url = 'https://restful-booker.herokuapp.com/booking/' + booking_id
with open('auth.json', 'r') as f:
    token = f.read()
    token = token[11:-2]
print(token)
# headers
headers = {'Content-Type': 'application/json'
            , 'Accept': 'application/json'
            , 'Cookie': 'token=' + token}
update_data = {
    "firstname": "James",
    "lastname": "Brown",
    "totalprice": 222,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2021-02-01",
        "checkout": "2021-02-02"
    },
    "additionalneeds": "Dinner"
}
print(url)
# Send the request
response = requests.put(url, headers=headers, json=update_data)

# check the response
if response.status_code == 200:
    print('Update successful')
    #split the response text into a list of lines and overwrite it into booking_info.json and print each line
    with open('booking_info.json', 'w') as f:
        f.write(response.text)
    response_lines = response.text.splitlines()
    for line in response_lines:
        print(line)
else:
    print('Update failed')
    print(response.text)
    print(response.status_code)