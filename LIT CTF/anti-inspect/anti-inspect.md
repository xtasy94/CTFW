# LIT CTF 2024: web/anti-inspect
**Title:** web/anti-inspect

**Description:** can you find the answer? **WARNING: do not open the link your computer will not enjoy it much.** URL: [http://litctf.org:31779/](http://litctf.org:31779/) Hint: If your flag does not work, think about how to style the output of console.log.
## Solution:
To see what's inside the website we just do run the following command:
```
└─$ wget -q -O - http://litctf.org:31779/
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <script>
      const flag = "LITCTF{your_%cfOund_teh_fI@g_94932}";
      while (true)
        console.log(
          flag,
          "background-color: darkblue; color: white; font-style: italic; border: 5px solid hotpink; font-size: 2em;"
        );
    </script>
  </body>
</html>
```

And there's our flag: `LITCTF{your_fOund_teh_fI@g_94932}`
