# LIT CTF 2024:  crypto/pope shuffle
**Title:** crypto/pope shuffle

**Description:** it's like caesar cipher but better. Encoded: `࠴࠱࠼ࠫ࠼࠮ࡣࡋࡍࠨ࡛ࡍ࡚ࡇ࡛ࠩࡔࡉࡌ`
## Solution:
Looking at the description, we can understand that this involves shifting of characters.

### Step 1: Convert these unicode characters to decimal:
For this step, I used an online tool [Unicode Converter - encoding / decoding | CodersTool](https://www.coderstool.com/unicode-text-converter), converting these unicode characters to decimal, we get:
```
2100 2097 2108 2091 2108 2094 2147 2123 2125 2088 2139 2125 2138 2119 2139 2089 2132 2121 2124 2149
```

### Step 2: Shifting the Decimals:
Looking at the description, we can take the approach of shifting the Unicode characters to decrypt the message. Since a Caesar cipher typically shifts characters by a fixed number, we wrote a Python script to experiment with different shift values until the correct decryption was found.
### Step 3: Decryption Attempts:
Initially, I tried a range of shifts from 1 to 1000, but this didn't yield the correct decryption. I then expanded the range from 1000 to 2000, but still didn't find the correct result. Finally, I tried the range from 2000 to 3000, and eventually discovered that the correct shift value was **2024**.

[Here’s the Python script used for decryption:](https://github.com/xtasy94/CTFW/blob/main/LIT%20CTF/pope%20shuffle/Files/decode.py)
```
def decode_unicode_caesar_cipher(encoded_list, shift):
    decoded_chars = []
    for code in encoded_list:
        decoded_char = chr(code - shift)
        decoded_chars.append(decoded_char)
    return ''.join(decoded_chars)

unicode_codes = [2100, 2097, 2108, 2091, 2108, 2094, 2147, 2123, 2125, 2088, 2139, 2125, 2138, 2119, 2139, 2089, 2132, 2121, 2124, 2149]

for shift in range(2000, 3000):  # Adjust range as needed
    decoded_text = decode_unicode_caesar_cipher(unicode_codes, shift)
    if "LITCTF" in decoded_text:
        print(f"Shift {shift}: {decoded_text}")
        break
```

This script iterated through the possible shift values and printed the decoded text if it contained "LITCTF."
```
└─$ python3 decode.py
Shift 2024: LITCTF{ce@ser_sAlad}
```
And there's our flag: `LITCTF{ce@ser_sAlad}`
