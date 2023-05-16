import re

text = input()
searched_pattern = r""
result = re.findall(searched_pattern, text)
print(", ".join(result))