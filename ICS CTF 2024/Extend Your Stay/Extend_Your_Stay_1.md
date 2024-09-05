# ICS CTF 2024 - Extend Your Stay 1

**Title:** Extend Your Stay - 1
**Description:** Despite Virbank Medical's quarterly cybersecurity reminders and strong policies against installing unapproved software, users just keep doing it. A suspicious browser extension was recently identified on a user's workstation.  
  
What flag does the extension print to the console when it is installed?  
  
_Flag format: Traditional CTF flag. Example: **flag{th1s_1$_n0t_th3_fl@g}**_

**File:** [no_more_rodents.crx](https://github.com/xtasy94/CTFW/blob/main/ICS%20CTF%202024/Extend%20Your%20Stay/Files_1_and_2/no_more_rodents.crx)
## Solution:

First, I extracted the Chrome extension and listed its contents:

```bash
$ ls
background.js  logo_128.png  logo_16.png  logo_32.png  logo_48.png  manifest.json
```

According to the problem statement, the extension prints the flag to the console upon installation. To locate this flag, I examined the [background.js](https://github.com/xtasy94/CTFW/blob/main/ICS%20CTF%202024/Extend%20Your%20Stay/Files_1_and_2/background.js) file and found the following code:

```javascript
// Executes when the extension is first installed
chrome.runtime.onInstalled.addListener(() => {
    var val = "ZmxhZ3toeXAzcjN4dDNuZDNkfQ==";
    console.log("NO MORE RODENTS!!!!!!!!!!");
    console.log(atob(val));
});
```

The code includes a Base64-encoded string. To decode it, I ran:

```bash
$ echo "ZmxhZ3toeXAzcjN4dDNuZDNkfQ==" | base64 -d
flag{hyp3r3xt3nd3d}
```

The decoded flag is: `flag{hyp3r3xt3nd3d}`.
