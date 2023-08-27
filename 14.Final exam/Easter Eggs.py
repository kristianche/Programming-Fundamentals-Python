import re
data = input()
pattern = r"(\@{1,}|\#{1,})([a-z]{3,})(\@{1,}|\#{1,})(\W*?)(\/{1,})(\d+)(\/{1,})"
result = re.findall(pattern, data)
print_result = ""
for elements in result:
    print_result += f"You found {elements[-2]} {elements[1]} eggs!\n"
print(print_result)

