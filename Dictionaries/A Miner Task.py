my_dict = {}
while True:
    resource = input()
    if resource == "stop":
        break
    resource_amount = int(input())
    if resource in my_dict.keys():
        my_dict[resource] += resource_amount

    else:
        my_dict[resource] = resource_amount
for key, value in my_dict.items():
    print(f"{key} -> {value}")