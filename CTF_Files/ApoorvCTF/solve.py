#!/usr/bin/env python3
from pwn import remote
import sys

HOST = "chals1.apoorvctf.xyz"
PORT = 4001

# Connect to the remote service.
r = remote(HOST, PORT)
print(f"[+] Connected to {HOST}:{PORT}")

def oracle(data: bytes) -> bytes:
    """
    Sends hex-encoded data to the oracle and returns the raw ciphertext.
    The service prints a line like:
         "Ciphertext: <hex ciphertext>"
    """
    r.recvuntil(b"Enter your input:")
    r.sendline(data.hex().encode())
    line = r.recvline()
    if b"Ciphertext:" in line:
        ct_hex = line.split(b"Ciphertext:")[1].strip()
        return bytes.fromhex(ct_hex.decode())
    else:
        print("Error in response:", line)
        sys.exit(1)

block_size = 16
# fixed prefix: choose one full block to force flag alignment.
fixed = b"A" * block_size

secret = b""
max_len = 50  # adjust maximum expected flag length

print("[*] Starting byte-at-a-time attack...")
for i in range(max_len):
    # Determine the additional pad length so that:
    # (len(fixed) + len(pad) + i) mod block_size == block_size - 1.
    n = (block_size - 1 - ((len(fixed) + i) % block_size)) % block_size
    pad = b"A" * n
    prefix = fixed + pad

    # Query the oracle with our current prefix.
    ct = oracle(prefix)
    # Split ciphertext into 16-byte blocks.
    blocks = [ct[j:j+block_size] for j in range(0, len(ct), block_size)]
    # The unknown flag starts immediately after our fixed+pad.
    target_block_index = (len(prefix) + i) // block_size
    if target_block_index >= len(blocks):
        print("[-] Target block index out of range, breaking...")
        break
    target_block = blocks[target_block_index]

    # Build dictionary for candidate bytes.
    dictionary = {}
    for c in range(256):
        test_input = prefix + secret + bytes([c])
        ct_test = oracle(test_input)
        blocks_test = [ct_test[j:j+block_size] for j in range(0, len(ct_test), block_size)]
        dictionary[blocks_test[target_block_index]] = c

    if target_block not in dictionary:
        print("[-] No matching candidate found (perhaps reached padding); breaking...")
        break

    next_byte = dictionary[target_block]
    secret += bytes([next_byte])
    print(f"[*] Recovered so far: {secret}")

    # Stop if the flag appears to be complete.
    if secret.endswith(b"}"):
        break

print("\n[+] Flag:", secret.decode())
r.close()
