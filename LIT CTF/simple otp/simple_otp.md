# LIT CTF: crypto/simple otp
**Title:** crypto/simple otp

**Description:** We all know OTP is unbreakable...

**Provided code, [main.py](https://github.com/xtasy94/CTFW/blob/main/LIT%20CTF/simple%20otp/Files/main.py):**
```
import random

encoded_with_xor = b'\x81Nx\x9b\xea)\xe4\x11\xc5 e\xbb\xcdR\xb7\x8f:\xf8\x8bJ\x15\x0e.n\\-/4\x91\xdcN\x8a'

random.seed(0)
key = random.randbytes(32)
```

## Solution:
To decode the encoded message, we need to perform the XOR operation again with the same key that was used during encoding. Since the key is generated using a seeded random number generator, we can regenerate the exact same key by setting the random seed to the same value.
#### Decoding Script, [decode.py](https://github.com/xtasy94/CTFW/blob/main/LIT%20CTF/simple%20otp/Files/decode.py):
```
import random

encoded_with_xor = b"\x81Nx\x9b\xea)\xe4\x11\xc5 e\xbb\xcdR\xb7\x8f:\xf8\x8bJ\x15\x0e.n\\-/4\x91\xdcN\x8a"

random.seed(0)

key = random.randbytes(32)

decoded_message = bytes([a ^ b for a, b in zip(encoded_with_xor, key)])

print(decoded_message.decode())
```

Running the script, and there's our flag:
```
└─$ python3 decode.py
LITCTF{sillyOTPlol!!!!sdfsgvkhf}
```
