# API automation test

This repository provides examples and documentation for using the Restful Booker API to perform create authentication token, create booking, and update booking.

[link](https://restful-booker.herokuapp.com/apidoc/)

## Authentication token

To authenticate with the Restful Booker API, you need to obtain an access token. You can do this by sending a POST request to the `/auth` endpoint with your credentials. The response will include an access token that you can use for subsequent requests.

## Create booking

To create a booking, send a POST request to the `/booking` endpoint with the required parameters. The request body should include the booking details such as the guest name, check-in date, check-out date, and room ID, please find more in code.

## Update booking

To update a booking, send a PUT request to the `/booking/{bookingId}` endpoint with the booking ID as a path parameter. The request body should include the updated booking details such as the guest name, check-in date, check-out date, and room ID.

