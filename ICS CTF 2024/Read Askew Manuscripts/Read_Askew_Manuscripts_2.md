# ICS CTF 2024 - Read Askew Manuscripts - 2

**Title:** Read Askew Manuscripts - 2

**Description:** It appears that the thief attempted to upload the stolen patient image to a cloud storage site via HTTPS but was unsuccessful as the X-Ray VM is blocked from accessing the internet.  
  
What password did they use to try to log into the site?  
  
_Flag format: Password for the file storage site. Example: **myp@ssw0rd**_
## Solution:

I tried running `strings` to the `memdump.raw` file and output it to `memdump_strings.txt` and after that I focused on the description a bit, since the thief attempted to upload the stolen patient image to a cloud storage via "HTTPS", I tried running `grep -i "https://" memdump_strings.txt`, and right at the bottom of the output, we get this URL:
```
https://www.ev1lf1lestorage.info/?directory=images&user=ominousnoteperson&passB64=aWxpa2V3cml0aW5nb21pbm91c25vdGVz&login=true
```

I decoded the password:
```
$ echo "aWxpa2V3cml0aW5nb21pbm91c25vdGVz" | base64 -d
ilikewritingominousnotes
```

And there's our password: `ilikewritingominousnotes`
