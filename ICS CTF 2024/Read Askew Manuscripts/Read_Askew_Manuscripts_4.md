# ICS CTF 2024 - Read Askew Manuscripts - 4

**Title:** Read Askew Manuscripts - 4

**Description:** What is the flag in Phoenix's image?  
  
_Flag format: Traditional CTF flag. Example: **flag{th1s_1$_n0t_th3_fl@g}**_
## Solution:

Now, since we know the patient name, let's just search for it: 
```
$ volatility -f memdump.raw --profile=WinXPSP3x86 filescan | grep Phoenix

Volatility Foundation Volatility Framework 2.6.1
0x00000000096959b0      1      0 RW-rw- \Device\HarddiskVolume1\Documents and Settings\Administrator\Recent\Phoenix_Wright.lnk
0x0000000009769228      1      0 R--r-- \Device\DP(1)0-0+3\Phoenix_Wright.png
0x000000000978c820      1      0 R--r-- \Device\HarddiskVolume1\Documents and Settings\Administrator\Desktop\patient_images\Phoenix_Wright.png
```

Now, to extract the image `Phoenix_Wright.png` from the memory dump using the `dumpfiles` plugin with the appropriate offset. Here’s the command I used to extract the image:
```
$ volatility -f memdump.raw --profile=WinXPSP3x86 dumpfiles -Q 0x000000000978c820 -D /mnt/e/CTF/memory/
Volatility Foundation Volatility Framework 2.6.1
DataSectionObject 0x0978c820   None   \Device\HarddiskVolume1\Documents and Settings\Administrator\Desktop\patient_images\Phoenix_Wright.png
```

```
$ file file.None.0x89790b60.dat
file.None.0x89790b60.dat: PNG image data, 1024 x 1024, 8-bit grayscale, non-interlaced
```

After changing the file extension, this is what we see:

![image](https://github.com/user-attachments/assets/b0e6b83a-28aa-4531-8e7f-1e47ce26a0d7)


And there's our flag: `flag{0bj3ct10n_$t0p_l00k1ng_@_my_b0n3s}`
