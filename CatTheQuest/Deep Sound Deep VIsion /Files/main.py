import re

with open("MONSTERS.txt", "r") as file:
    content = file.read()
pattern = r"\d{2,}"
matches = re.findall(pattern, content)
for match in matches:
    print(match)