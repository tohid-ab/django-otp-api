from kavenegar import *


# try:
#   api = KavenegarAPI('your apikey here')
#   params = {
#       'receptor': '',
#       'template': '',
#       'token': '',
#       'type': 'sms',  # sms vs call
#   }
#   response = api.verify_lookup(params)
#   print(response)
# except APIException as e:
#   print(e)
# except HTTPException as e:
#   print(e)

def kavenegar_token_send(token):
    print('OTP USER')
    print(f'code: {token.password}')
    print(f'token: {token}')
