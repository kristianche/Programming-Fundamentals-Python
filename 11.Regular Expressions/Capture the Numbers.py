import re

text = input()
searched_pattern = r"\d+"
while text:
    result = re.findall(searched_pattern, text)
    if result:
        print(" ".join(result), end=" ")
    text = input()