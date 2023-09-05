import re
data = input()
pattern = r">>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)"
total_price = 0
print_result = []
while data != "Purchase":
    result = re.search(pattern, data)
    if result:
        furniture, price, quantity = result.groups()
        print_result.append(furniture)
        total_price += float(price) * int(quantity)
    data = input()
print("Bought furniture:")
for object in print_result:
    print(object)
print(f"Total money spend: {total_price:.2f}")