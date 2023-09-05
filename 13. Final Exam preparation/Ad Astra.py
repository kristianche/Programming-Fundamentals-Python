import re
data = input()
pattern = r"(\#|\|)([a-z A-Z]+)(\#|\|)(\d{2}\/\d{2}\/\d{2})(\#|\|)(\d+)(\#|\|)"
result = re.findall(pattern, data)
print_result = ""
calories = 0
for elements in result:
    print_result += f"Item: {elements[1]}, Best before: {elements[3]}, Nutrition: {elements[5]}\n"
    calories += int(elements[5])
days = calories // 2000
print(f"You have food to last you for: {days} days!")
print(print_result)