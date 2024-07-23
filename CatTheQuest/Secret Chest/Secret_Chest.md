# CatTheQuest: Secret Chest
**Title:** Secret Chest

**Description:** A secure chest containing a precious document is protected by a special request. Your mission is to unlock this chest by sending a POST request containing a unique and secret parameter. The document is well-guarded, and only the word can reveal it.

<b>Challenge Help:</b>
![Challenge Help Image]()

Use this information to achieve the resolution of the challenge
165.227.157.253:5000/flag - HTTP POST with token.

<b>Hint: </b>
A and M in uppercase.

## Solution:
### Solving the puzzle:
1. The month when spring starts in the northen hemisphere is March, so the first part would be 3. 
2. The first vowel of the alphabet is "A", which is the second part.
3. The planet closest to the sun is Mercury, reversing which we'll get "yrucreM", which is the third part.
4. The first industrial revolution began in the year 1760. The product of the digits in 1760 is 1 * 7 * 6 * 0, which equals 0, which would be our 4th part.
5. The fifth part according to the challenge help is "key" followed by the number of letters in the word, giving us the answer: "key3", which is our last part.

Combining all of them, we get: <b>3AyrucreM0key3</b>
### Sending the POST request:
According to the challenge instructions, we have to send an HTTP POST request containing a unique and secret parameter to get the flag, here's the cURL request would look like:
```
curl --request POST \
  --url http://165.227.157.253:5000/flag \
  --header 'Content-Type: application/json' \
  --data '{"token":"3AyrucreM0key3"}'
```
Sending this request using [Insomnia](https://docs.insomnia.rest/insomnia/get-started), we get the following response: 
```
{
	"flag": "CAT{S3cr3t_Ch3st_B4D_S4f3tY}"
}
```
And there's our flag: `CAT{S3cr3t_Ch3st_B4D_S4f3tY}`
