# LIT CTF 2024 - crypto/privatekey

**Title:** crypto/privatekey

**Description:** Something's smaller.

**Files:** [chal.txt](https://github.com/xtasy94/CTFW/blob/main/LIT%20CTF/FIles/chal.txt)
## Solution:
This challenge is clearly based on RSA encryption. To solve it, we used an online [RSA Cipher Calculator](https://www.dcode.fr/rsa-cipher) to decrypt the provided ciphertext. The decryption revealed the following hex string:

```
4C 49 54 43 54 46 7B 77 31 33 6E 33 72 5F 31 35 5F 34 6E 5F 75 6E 66 30 72 74 75 6E 34 74 33 5F 6E 34 6D 33 7D
```

Next, we converted this hex string to ASCII using a [Hex to ASCII Text Converter](https://www.rapidtables.com/convert/number/hex-to-ascii.html), which gave us the flag:

`LITCTF{w13n3r_15_4n_unf0rtun4t3_n4m3}`.
