import re
data = input()
pattern = r"www\.[A-Za-z0-9\-]+\.[a-z\.]+"
valid = []
while data:
    result = re.search(pattern, data)
    if result:
        email = result.group(0)
        valid.append(email)
    data = input()
for element in valid:
    print(element)