import re

text = input()
searched_pattern = r"\b_([A-Za-z0-9]+)\b"
result = re.findall(searched_pattern, text)
print(",".join(result))