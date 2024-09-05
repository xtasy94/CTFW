# ICS CTF 2024 - Extend Your Stay 3

**Title:** Extend Your Stay - 3

**Description:** A second suspicious Chrome extension has been identified, this time on a computer used by the purchasing department to procure medical supplies. Based on posters and field guides identified in the purchasing office, it seems the purchasing staff are big birdwatchers. You suspect that this extension is attempting to steal sensitive financial data.  
  
What type of card does this extension collect numbers for?  
  
_Flag format: Card type. Example: **Gift card**_

**File:** [even_more_birds.crx](https://github.com/xtasy94/CTFW/blob/main/ICS%20CTF%202024/Extend%20Your%20Stay/Files_3_and_4/even_more_birds.crx)
## Solution:

I first extracted the extension and found the [background.js](https://github.com/xtasy94/CTFW/blob/main/ICS%20CTF%202024/Extend%20Your%20Stay/Files_3_and_4/background.js) file, I looked at the code and found this particular part a bit suspicious:
```javascript
var text = node.nodeValue;
var insertBirdHere = Math.floor(Math.random() * text.length);
var indexOfBird = Math.floor(Math.random() * BIRDS.length);
const birdIdentifier1 = /5[1-5]\d{14}/;
const birdIdentifier2 = /\d{2}\/\d{2}/;
const birdIdentifier3 = /\d{3}/;
```

It is most likely targeting Payment card numbers based on the patterns it looks for. here's the reasoning:

- `5[1-5]\d{14}` matches credit card numbers starting with 51-55.
- `\d{2}/\d{2}` matches expiration dates.
- `\d{3}` matches CVV codes.

Upon further Googling we found out that Mastercard starts with the number 5, and there's our flag: `Master card`
