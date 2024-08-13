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
