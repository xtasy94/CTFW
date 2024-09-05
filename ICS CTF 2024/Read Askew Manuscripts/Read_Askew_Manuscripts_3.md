# ICS CTF 2024 - Read Askew Manuscripts - 3

**Title:** Read Askew Manuscripts - 3
**Description:** What is the name of the patient whose image the thief stole?  
  
_Flag format: First and last name of the patient. Example: **Jane Doe**_
## Solution:

Now, for this I just logically thought, yeah, let's just do a strings on the same .txt file searching for image file extensions like .dcm, .jpg or .png like this: `grep -E "\.dcm|\.jpg|\.png" memdump_strings.txt`
And this is what we found:
```
Visited: Administrator@file:///E:/Phoenix_Wright.png
```

And that's our flag: `Phoenix Wright`
