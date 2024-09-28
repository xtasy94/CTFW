# PatriotCTF 2024 - Give me four words, Vasily
**Title:** Give me four words, Vasily

**Description:** We have been tracking a highly suspicious submarine believed to be harboring many enemy skiddies. Unfortunately, this satellite image is rather out of date. Your mission is to locate the submarines there using a more up-to-date image, and tell us what class they are with their NATO reporting name - a letter from the NATO phonetic alphabet, spelled out.

We want to know precisely where the aft end of northernmost submarine attached to the pier is. Communicate its location in three words. Include the NATO reporting name of the class of submarine in your answer.

Submission format: PCTF{three.position.words.class_name} Example submission: PCTF{employing.broken.imports.sierra}
**Files:**


![sbububmarine.png](https://github.com/xtasy94/CTFW/blob/main/PatriotCTF%202024/GiveMeFourWordsVasily/Files/sbububmarine.png)

## Solution:
First I started by searching for the image online hoping to find something similar in it, finding something similar to these highlighted things in the original image:



![highlighted.png](https://github.com/xtasy94/CTFW/blob/main/PatriotCTF%202024/GiveMeFourWordsVasily/Files/highlighted.png)

And this led to me this website which when translated said [India may lease Russian Navy's Kilo-class submarines](http://rybachii.blog84.fc2.com/blog-entry-1029.html), I scrolled down and found the image, now that we had the `class_name` from the title of the website, all I had to find now was the location, on the same website I also found geolocation of the place:



![highlighted2.png](https://github.com/xtasy94/CTFW/blob/main/PatriotCTF%202024/GiveMeFourWordsVasily/Files/highlighted2.png)

Entering the GPS coordinates in [what3words](https://what3words.com/) and now all I had to find where the aft end of northernmost submarine attached to the pier is:



![highlighted3.png](https://github.com/xtasy94/CTFW/blob/main/PatriotCTF%202024/GiveMeFourWordsVasily/Files/highlighted3.png)

And that's the last part of our flag: `bagels.light.vivid`, adding them all, this is our final flag:
`PCTF{bagels.light.vivid.Kilo}`
