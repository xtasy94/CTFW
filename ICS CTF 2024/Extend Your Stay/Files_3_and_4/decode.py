import base64

def extract_bird_initials(file_path):
    bird_initials = []
    
    with open(file_path, 'r') as file:
        for line in file:
            bird_name = line.strip().strip('"')
            if bird_name:  
                bird_initials.append(bird_name[0]) 

    initials_string = ''.join(bird_initials)
    return initials_string

def encode_to_base64(initials_string):
    encoded_bytes = base64.b64encode(initials_string.encode('utf-8'))
    encoded_string = encoded_bytes.decode('utf-8')
    return encoded_string

def main():
    file_path = 'birds.txt'  
    initials_string = extract_bird_initials(file_path)
    encoded_string = encode_to_base64(initials_string)

    print("Concatenated Initials String:", initials_string)
    print("Base64 Encoded String:", encoded_string)

if __name__ == "__main__":
    main()