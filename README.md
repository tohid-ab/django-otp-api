# django-otp-api
$ Hi

## API
GET
This is to register the mobile number into the database and generate OTP.

http://127.0.0.1:8000/api/v1/users/otp?receiver=999999999

POST
This is to verify the mobile number using OTP.

http://127.0.0.1:8000/api/v1/users/otp?receiver=999999999
