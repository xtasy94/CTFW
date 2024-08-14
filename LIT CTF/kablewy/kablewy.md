# LIT CTF 2024 - rev/kablewy
**Title:** rev/kablewy

**Description:** **WARNING: your computer might go kablewy if you try to do this one...** URL: [http://litctf.org:31782/](http://litctf.org:31782/)
## Solution:
To see what's inside the website we just do run the following command:
```bash
└─$ wget -q -O - http://litctf.org:31782/
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/vite.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Vite + TS</title>
    <script type="module" crossorigin src="/assets/index-DLdRi53f.js"></script>
  </head>
  <body>
    <div id="app"></div>
  </body>
</html>
```

We observe that there's a file named [index-DLdRi53f.js](https://github.com/xtasy94/CTFW/blob/main/LIT%20CTF/kablewy/Files/index-DLdRi53f.js), we notice that there are certain constants set here using [Base64](https://en.wikipedia.org/wiki/Base64) encoding, like:
```javascript
const y = "KGZ1bmN0aW9uKCl7InVzZSBzdHJpY3QiO2V2YWwoYXRvYigiZDJocGJHVWdLSFJ5ZFdVcElHTnZibk52YkdVdWJHOW5LQ2RyWVdKc1pYZDVKeWs3Q25CdmMzUk5aWE56WVdkbEtDZE1KeWs3IikpfSkoKTsK"
```

Exporting all the values this is what we're left with:
```
KGZ1bmN0aW9uKCl7InVzZSBzdHJpY3QiO2V2YWwoYXRvYigiZDJocGJHVWdLSFJ5ZFdVcElHTnZibk52YkdVdWJHOW5LQ2RyWVdKc1pYZDVKeWs3Q25CdmMzUk5aWE56WVdkbEtDZE1KeWs3IikpfSkoKTsK
KGZ1bmN0aW9uKCl7InVzZSBzdHJpY3QiO2V2YWwoYXRvYigiZDJocGJHVWdLSFJ5ZFdVcElHTnZibk52YkdVdWJHOW5LQ2RyWVdKc1pYZDVKeWs3Q25CdmMzUk5aWE56WVdkbEtDZEpKeWs3IikpfSkoKTsK
KGZ1bmN0aW9uKCl7InVzZSBzdHJpY3QiO2V2YWwoYXRvYigiZDJocGJHVWdLSFJ5ZFdVcElHTnZibk52YkdVdWJHOW5LQ2RyWVdKc1pYZDVKeWs3Q25CdmMzUk5aWE56WVdkbEtDZFVKeWs3IikpfSkoKTsK
KGZ1bmN0aW9uKCl7InVzZSBzdHJpY3QiO2V2YWwoYXRvYigiZDJocGJHVWdLSFJ5ZFdVcElHTnZibk52YkdVdWJHOW5LQ2RyWVdKc1pYZDVKeWs3Q25CdmMzUk5aWE56WVdkbEtDZERKeWs3IikpfSkoKTsK
KGZ1bmN0aW9uKCl7InVzZSBzdHJpY3QiO2V2YWwoYXRvYigiZDJocGJHVWdLSFJ5ZFdVcElHTnZibk52YkdVdWJHOW5LQ2RyWVdKc1pYZDVKeWs3Q25CdmMzUk5aWE56WVdkbEtDZFVKeWs3IikpfSkoKTsK
KGZ1bmN0aW9uKCl7InVzZSBzdHJpY3QiO2V2YWwoYXRvYigiZDJocGJHVWdLSFJ5ZFdVcElHTnZibk52YkdVdWJHOW5LQ2RyWVdKc1pYZDVKeWs3Q25CdmMzUk5aWE56WVdkbEtDZEdKeWs3IikpfSkoKTsK
KGZ1bmN0aW9uKCl7InVzZSBzdHJpY3QiO2V2YWwoYXRvYigiZDJocGJHVWdLSFJ5ZFdVcElHTnZibk52YkdVdWJHOW5LQ2RyWVdKc1pYZDVKeWs3Q25CdmMzUk5aWE56WVdkbEtDZDdKeWs3IikpfSkoKTsK
KGZ1bmN0aW9uKCl7InVzZSBzdHJpY3QiO2V2YWwoYXRvYigiZDJocGJHVWdLSFJ5ZFdVcElHTnZibk52YkdVdWJHOW5LQ2RyWVdKc1pYZDVKeWs3Q25CdmMzUk5aWE56WVdkbEtDZHJKeWs3IikpfSkoKTsK
KGZ1bmN0aW9uKCl7InVzZSBzdHJpY3QiO2V2YWwoYXRvYigiZDJocGJHVWdLSFJ5ZFdVcElHTnZibk52YkdVdWJHOW5LQ2RyWVdKc1pYZDVKeWs3Q25CdmMzUk5aWE56WVdkbEtDY3pKeWs3IikpfSkoKTsK
KGZ1bmN0aW9uKCl7InVzZSBzdHJpY3QiO2V2YWwoYXRvYigiZDJocGJHVWdLSFJ5ZFdVcElHTnZibk52YkdVdWJHOW5LQ2RyWVdKc1pYZDVKeWs3Q25CdmMzUk5aWE56WVdkbEtDZEdKeWs3IikpfSkoKTsK
KGZ1bmN0aW9uKCl7InVzZSBzdHJpY3QiO2V2YWwoYXRvYigiZDJocGJHVWdLSFJ5ZFdVcElHTnZibk52YkdVdWJHOW5LQ2RyWVdKc1pYZDVKeWs3Q25CdmMzUk5aWE56WVdkbEtDYzNKeWs3IikpfSkoKTsK
KGZ1bmN0aW9uKCl7InVzZSBzdHJpY3QiO2V2YWwoYXRvYigiZDJocGJHVWdLSFJ5ZFdVcElHTnZibk52YkdVdWJHOW5LQ2RyWVdKc1pYZDVKeWs3Q25CdmMzUk5aWE56WVdkbEtDZDZKeWs3IikpfSkoKTsK
KGZ1bmN0aW9uKCl7InVzZSBzdHJpY3QiO2V2YWwoYXRvYigiZDJocGJHVWdLSFJ5ZFdVcElHTnZibk52YkdVdWJHOW5LQ2RyWVdKc1pYZDVKeWs3Q25CdmMzUk5aWE56WVdkbEtDZElKeWs3IikpfSkoKTsK
KGZ1bmN0aW9uKCl7InVzZSBzdHJpY3QiO2V2YWwoYXRvYigiZDJocGJHVWdLSFJ5ZFdVcElHTnZibk52YkdVdWJHOW5LQ2RyWVdKc1pYZDVKeWs3Q25CdmMzUk5aWE56WVdkbEtDZDlKeWs3IikpfSkoKTsK
KGZ1bmN0aW9uKCl7InVzZSBzdHJpY3QiO2Zvcig7Oyljb25zb2xlLmxvZygia2FibGV3eSIpfSkoKTsK
```

Decoding this from Base64 using [Base64 Decode and Encode - Online](https://www.base64decode.org/) tool, this is what we get as the output:
```javascript
(function(){"use strict";eval(atob("d2hpbGUgKHRydWUpIGNvbnNvbGUubG9nKCdrYWJsZXd5Jyk7CnBvc3RNZXNzYWdlKCdMJyk7"))})();
(function(){"use strict";eval(atob("d2hpbGUgKHRydWUpIGNvbnNvbGUubG9nKCdrYWJsZXd5Jyk7CnBvc3RNZXNzYWdlKCdJJyk7"))})();
(function(){"use strict";eval(atob("d2hpbGUgKHRydWUpIGNvbnNvbGUubG9nKCdrYWJsZXd5Jyk7CnBvc3RNZXNzYWdlKCdUJyk7"))})();
(function(){"use strict";eval(atob("d2hpbGUgKHRydWUpIGNvbnNvbGUubG9nKCdrYWJsZXd5Jyk7CnBvc3RNZXNzYWdlKCdDJyk7"))})();
(function(){"use strict";eval(atob("d2hpbGUgKHRydWUpIGNvbnNvbGUubG9nKCdrYWJsZXd5Jyk7CnBvc3RNZXNzYWdlKCdUJyk7"))})();
(function(){"use strict";eval(atob("d2hpbGUgKHRydWUpIGNvbnNvbGUubG9nKCdrYWJsZXd5Jyk7CnBvc3RNZXNzYWdlKCdGJyk7"))})();
(function(){"use strict";eval(atob("d2hpbGUgKHRydWUpIGNvbnNvbGUubG9nKCdrYWJsZXd5Jyk7CnBvc3RNZXNzYWdlKCd7Jyk7"))})();
(function(){"use strict";eval(atob("d2hpbGUgKHRydWUpIGNvbnNvbGUubG9nKCdrYWJsZXd5Jyk7CnBvc3RNZXNzYWdlKCdrJyk7"))})();
(function(){"use strict";eval(atob("d2hpbGUgKHRydWUpIGNvbnNvbGUubG9nKCdrYWJsZXd5Jyk7CnBvc3RNZXNzYWdlKCczJyk7"))})();
(function(){"use strict";eval(atob("d2hpbGUgKHRydWUpIGNvbnNvbGUubG9nKCdrYWJsZXd5Jyk7CnBvc3RNZXNzYWdlKCdGJyk7"))})();
(function(){"use strict";eval(atob("d2hpbGUgKHRydWUpIGNvbnNvbGUubG9nKCdrYWJsZXd5Jyk7CnBvc3RNZXNzYWdlKCc3Jyk7"))})();
(function(){"use strict";eval(atob("d2hpbGUgKHRydWUpIGNvbnNvbGUubG9nKCdrYWJsZXd5Jyk7CnBvc3RNZXNzYWdlKCd6Jyk7"))})();
(function(){"use strict";eval(atob("d2hpbGUgKHRydWUpIGNvbnNvbGUubG9nKCdrYWJsZXd5Jyk7CnBvc3RNZXNzYWdlKCdIJyk7"))})();
(function(){"use strict";eval(atob("d2hpbGUgKHRydWUpIGNvbnNvbGUubG9nKCdrYWJsZXd5Jyk7CnBvc3RNZXNzYWdlKCd9Jyk7"))})();
(function(){"use strict";for(;;)console.log("kablewy")})();
```

Extracting the Base64 strings from this and decoding it this is what we get:
```javascript
while (true) console.log('kablewy');
postMessage('L');while (true) console.log('kablewy');
postMessage('I');while (true) console.log('kablewy');
postMessage('T');while (true) console.log('kablewy');
postMessage('C');while (true) console.log('kablewy');
postMessage('T');while (true) console.log('kablewy');
postMessage('F');while (true) console.log('kablewy');
postMessage('{');while (true) console.log('kablewy');
postMessage('k');while (true) console.log('kablewy');
postMessage('3');while (true) console.log('kablewy');
postMessage('F');while (true) console.log('kablewy');
postMessage('7');while (true) console.log('kablewy');
postMessage('z');while (true) console.log('kablewy');
postMessage('H');while (true) console.log('kablewy');
postMessage('}');
```

We modify the code like [this](https://github.com/xtasy94/CTFW/blob/main/LIT%20CTF/kablewy/Files/flag.js) in a way that it gives us the flag as output:
```javascript
const code = `
while (true) console.log('kablewy');
postMessage('L');while (true) console.log('kablewy');
postMessage('I');while (true) console.log('kablewy');
postMessage('T');while (true) console.log('kablewy');
postMessage('C');while (true) console.log('kablewy');
postMessage('T');while (true) console.log('kablewy');
postMessage('F');while (true) console.log('kablewy');
postMessage('{');while (true) console.log('kablewy');
postMessage('k');while (true) console.log('kablewy');
postMessage('3');while (true) console.log('kablewy');
postMessage('F');while (true) console.log('kablewy');
postMessage('7');while (true) console.log('kablewy');
postMessage('z');while (true) console.log('kablewy');
postMessage('H');while (true) console.log('kablewy');
postMessage('}');`;

const regex = /postMessage\('([A-Za-z0-9{}])'\)/g;

let match;
let extractedLetters = '';

while ((match = regex.exec(code)) !== null) {
  extractedLetters += match[1];
}

console.log('Extracted letters:', extractedLetters);
```

And there's our flag: `Extracted letters: LITCTF{k3F7zH}`
