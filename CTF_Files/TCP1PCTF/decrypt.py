from Crypto.Cipher import AES
import zstandard
from PIL import Image
import io

def read_skibidi_file(file_path):
    with open(file_path, 'rb') as file:
        magic_number = file.read(4)
        if magic_number != b'SKB1':
            raise ValueError("Invalid Skibidi file format")
        
        width = int.from_bytes(file.read(4), 'little')
        height = int.from_bytes(file.read(4), 'little')
        channels = int.from_bytes(file.read(1), 'little')
        compression_method = int.from_bytes(file.read(1), 'little')
        aes_key = file.read(32)
        aes_iv = file.read(12)
        
        encrypted_data = file.read()
    
    print(f"Image dimensions: {width}x{height}")
    print(f"Channels: {channels}")
    print(f"Compression method: {compression_method}")
    
    cipher = AES.new(aes_key, AES.MODE_GCM, nonce=aes_iv)
    decrypted_data = cipher.decrypt(encrypted_data)
    
    decompression_methods = [
        lambda d: zstandard.ZstdDecompressor().decompress(d),
        lambda d: zstandard.ZstdDecompressor().decompress(d, max_output_size=width*height*channels),
        lambda d: d  
    ]
    
    for method in decompression_methods:
        try:
            decompressed_data = method(decrypted_data)
            break
        except Exception as e:
            print(f"Decompression attempt failed: {str(e)}")
    else:
        raise ValueError("All decompression attempts failed")
    
    print(f"Decompressed data size: {len(decompressed_data)} bytes")
    expected_size = width * height * channels
    print(f"Expected data size: {expected_size} bytes")
    
    if len(decompressed_data) != expected_size:
        print("Warning: Decompressed data size does not match expected size")
    
    mode = {1: 'L', 3: 'RGB', 4: 'RGBA'}.get(channels)
    if not mode:
        raise ValueError(f"Unsupported number of channels: {channels}")
    
    try:
        image = Image.frombytes(mode, (width, height), decompressed_data)
    except Exception as e:
        print(f"Error creating image: {str(e)}")
        with open('raw_data.bin', 'wb') as f:
            f.write(decompressed_data)
        print("Raw decompressed data saved to 'raw_data.bin'")
        raise
    
    return image

def main():
    input_file = 'suisei.skibidi'   
    output_file = 'output.png'      
    
    try:
        image = read_skibidi_file(input_file)
        image.save(output_file)
        print(f"Successfully decoded {input_file} and saved as {output_file}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
