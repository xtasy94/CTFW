# IIT BBS CTF: satellite
**Title:** IITBBS CTF: satellite

**Description:** From a secluded planet, aliens have transmitted a secret message containing vital information . As a skilled decoder, it’s your task to unravel the mysteries of this transmission and retrieve the flag. Will you be able to decipher her secrets before they fall into the wrong hands?

**File given to us:** [chall.wav](https://drive.google.com/file/d/1CM7TSidiiZ8X9xEKqxT7yl14jmTlsjMq/view?usp=sharing) 

## Solution: 
After listening to the audio file for a few seconds, it's clear that it can be decoded using SSTV decoders. I used an open-source repository found on GitHub: [colaclanth/sstv: SSTV Decoder](https://github.com/colaclanth/sstv), which works on audio files rather than a soundcard like most other decoders.

We clone the repository to our local machine and set it up. After setup, we run the following command:

```
sstv -d chall.wav -o result.png
```

And this is the output we get:

![cmd.png](https://github.com/xtasy94/CTFW/blob/main/IIT%20BBS%20CTF/satellite/Files/cmd.png)


![result.png](https://github.com/xtasy94/CTFW/blob/main/IIT%20BBS%20CTF/satellite/Files/result.png)

Hence, the flag is: `CTF{0x684736210}`
