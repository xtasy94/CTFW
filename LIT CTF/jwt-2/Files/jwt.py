import json
import base64
import hmac
import hashlib

jwt_secret = 'xook'

header = {
    'alg': 'HS256',
    'typ': 'JWT'
}
jwt_header = base64.urlsafe_b64encode(json.dumps(header).encode('utf-8')).decode('utf-8').rstrip('=')

payload = {
    'name': 'testuser',
    'admin': True
}
jwt_payload = base64.urlsafe_b64encode(json.dumps(payload).encode('utf-8')).decode('utf-8').rstrip('=')

signature = hmac.new(jwt_secret.encode('utf-8'), f'{jwt_header}.{jwt_payload}'.encode('utf-8'), hashlib.sha256).digest()
jwt_signature = base64.urlsafe_b64encode(signature).decode('utf-8').rstrip('=')

token = f'{jwt_header}.{jwt_payload}.{jwt_signature}'

print('Generated JWT Token:', token)

print('Header:', jwt_header)
print('Payload:', jwt_payload)
print('Signature:', jwt_signature)
