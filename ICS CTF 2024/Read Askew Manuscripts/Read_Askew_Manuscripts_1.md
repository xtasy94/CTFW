# ICS CTF 2024 - Read Askew Manuscripts - 1

**Title:** Read Askew Manuscripts - 1

**Description:** Medical equipment is extremely expensive and Virbank Medical can't always afford to upgrade to the latest and greatest. The chest X-ray machine, for example, is from 2004 and can only be controlled using a computer running Windows XP SP3. When the previous X-ray PC's motherboard died, the IT team made the decision to virtualize its hard drive on a more modern machine.  
  
The Driftveil Police Department called this morning with troubling news. It appears that a patient's image was stolen from the hospital. With no forensics team available locally, the task has fallen to you. The IT department has provided you with a [memory dump from the X-Ray VM](https://drive.google.com/file/d/1cYH5fPGhYEf1xDcPhzk7RovJjvpy46PI/view?usp=sharing) to analyze. From reading the manufacturer's documentation, you know that the serial number of the X-Ray machine is stored in the registry key `Software\ACME_XRay`.  
  
What is the flag in this key?  
  
_Flag format: Traditional CTF flag. Example: **flag{th1s_1$_n0t_th3_fl@g}**_

**File:** `memdump.raw`
## Solution:

Okay, this kind of troubled me, I have not done any challenge till now which involves analyzing memory dumps.
I had to study around about it and eventually I was able to do it, let's take a look how I did it.
We needed a tool named ["Volatility 3"](https://volatility3.readthedocs.io/en/latest/) for this, the most advanced memory forensics framework in the world. 
Since we know the registry key, we can run `volatility -f ./memdump.raw printkey --key 'SOFTWARE\ACME_XRAY'`:
```bash
$ volatility -f ./memdump.raw printkey --key 'SOFTWARE\ACME_XRAY'
Volatility Foundation Volatility Framework 2.6.1
Legend: (S) = Stable   (V) = Volatile

----------------------------
Registry: \Device\HarddiskVolume1\Documents and Settings\Administrator\NTUSER.DAT
Key name: ACME_XRay (S)
Last updated: 2024-04-10 15:49:26 UTC+0000

Subkeys:

Values:
REG_SZ        xray_sn         : (S) ZmxhZ3tmMzNsMW5nX3YwbEB0MWwzfQ==
```

We get a base64 encoded string, let's decode it:
```bash
$ echo "ZmxhZ3tmMzNsMW5nX3YwbEB0MWwzfQ==" | base64 -d
flag{f33l1ng_v0l@t1l3}
```

And there's our flag: `flag{f33l1ng_v0l@t1l3}`
