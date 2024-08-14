# LIT CTF 2024: misc/a little bit of tomcroppery
**Title:** misc/a little bit of tomcroppery

**Description:** Once you crop an image, the cropped part is gone... right???

**Provided image:
![image.png](https://github.com/xtasy94/CTFW/blob/main/LIT%20CTF/a%20little%20bit%20of%20tomcroppery/Files/image.png)**


## Solution:
The description hints that the image may have been cropped, implying there could be hidden content within the file.
### Step 1: Analyze the Image with [Binwalk](https://www.kali.org/tools/binwalk/):
```
└─$ binwalk image.png 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 928 x 452, 8-bit/color RGBA, non-interlaced
41            0x29            Zlib compressed data, default compression
449394        0x6DB72         PNG image, 928 x 536, 8-bit/color RGBA, non-interlaced
449435        0x6DB9B         Zlib compressed data, compressed
```

The `binwalk` output reveals several interesting pieces of information:

- The main image is a PNG file with dimensions 928 x 452 pixels.
- There is some Zlib compressed data shortly after the image header.
- Importantly, there is another PNG image embedded within the file, starting at offset 449394, with dimensions 928 x 536 pixels.
- More Zlib compressed data is found right after this second PNG image.
### Step 2: Extract the Hidden PNG Image:
To investigate further, I extracted the hidden PNG image found at offset `449394`. This was done using the [dd](https://man7.org/linux/man-pages/man1/dd.1.html) command:
```
└─$ dd if=image.png of=extracted_image.png bs=1 skip=449394

770303+0 records in
770303+0 records out
770303 bytes (770 kB, 752 KiB) copied, 0.862148 s, 893 kB/s
```

This command successfully extracted the hidden image from the original `image.png` file and saved it as `extracted_image.png`:

![extracted_image.png](https://github.com/xtasy94/CTFW/blob/main/LIT%20CTF/a%20little%20bit%20of%20tomcroppery/Files/extracted_image.png)

And there's our flag: `LITCTF{4cr0p41yp5e_15_k1nd_0f_c001_j9g0s}`
