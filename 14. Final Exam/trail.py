import re
data = input()
pattern = r"(\@{1,}|\#{1,})([a-z]{3,})(\1)(\D\W*?)(\/{1,})(\d+)(\)"
result = re.findall(pattern, data)
for elements in result:
    print(elements[-2])