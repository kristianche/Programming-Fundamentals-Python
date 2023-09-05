import re
data = input()
pattern = r">>([A-Za-z]+)<<([0-9]+)!([0-9]+)"
result = re.findall(pattern, data)
print(result)