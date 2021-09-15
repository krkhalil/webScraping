
from pyotp import *
from pyzbar.pyzbar import decode
from PIL import Image
import base64

def decode_string():
    aa = decode(Image.open('C:/Users/Caretek/Pythonwork/2021-09-15_10-06-37.png'))
    return aa

def code_generate_against_token():
    message = 'otpauth://totp/My%20CCM%20Health:tatiana.lozova@myccmhealth.net39b908bf-7661-4c42-8207-b964f89b2e91?secret=ORQXI2LBNZQS43DPPJXXMYKANV4WGY3NNBSWC3DUNAXG4ZLUGU2WKYTGGRQTSLJQMJTGCLJUHBSGKLLCGE3DALJZHFSTCMLGGRRDIMDFME&issuer=My%20CCM%20Health'
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    return base64_message

print(decode_string())