# ICS CTF 2024 - Register the Dots - 2A and 2B

**Title:** Register the Dots - 2A & 2B
**Description:** `2A:` Using the `C:\Users\Benji\AppData\Local\Temp\ditto.exe` executable you found in `Register the Dots - 1`, Benji would like your assistance finding the password was used in this suspicious network connection.  
  
What is the password that is sent by the ditto.exe application?  
  
_Flag format: password. Example: **p@ssword123**_

`2B:` Using the `C:\Users\Benji\AppData\Local\Temp\ditto.exe` executable you found in `Register the Dots - 1`, Benji would like your assistance finding what this network connection was reaching out to.  
  
What is the IP address the ditto.exe application connects to?  
  
_Flag format: IP address. Example: **192.168.1.1**_

## Solution:
Now that we've found the executable, let's send it over to [Virustotal](https://www.virustotal.com/gui/file/aed7837875c59c1d98a9dde8f05c3521e7ac53c5f940f57d333950cfe1792f71/behavior) for dynamic analysis:

![Image](https://github.com/xtasy94/CTFW/blob/main/ICS%20CTF%202024/Register%20the%20Dots/Files/ditto.png?raw=true)

We see that it tries accessing the file `%appdata%\FileZilla\SiteManager.xml`, let's a have look at that:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<FileZilla3 version="3.53.0" platform="windows">
        <Servers>
                <Server>
                        <Host>165.227.251.182</Host>
                        <Port>21</Port>
                        <Protocol>0</Protocol>
                        <Type>0</Type>
                        <User>lass</User>
                        <Pass encoding="base64">ZWFzeTJXM2Fy</Pass>
                        <Logontype>1</Logontype>
                        <PasvMode>MODE_DEFAULT</PasvMode>
                        <EncodingType>Auto</EncodingType>
                        <BypassProxy>0</BypassProxy>
                        <Name>New site</Name>
                        <SyncBrowsing>0</SyncBrowsing>
                        <DirectoryComparison>0</DirectoryComparison>
                </Server>
        </Servers>
</FileZilla3>
```

And we have a bunch of information that would be sufficient for us to close this:
- Password (base64)
	```
	$ echo "ZWFzeTJXM2Fy" | base64 -d
	easy2W3ar
	```
- IP address: `165.227.251.182`

Flag for:
- 2A - `easy2W3ar`
- 2B - `165.227.251.182`
