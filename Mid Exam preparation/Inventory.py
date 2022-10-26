items = input().split(", ")
command = input().split(" - ")
command_of_combined_items = []
while True:
    if command[0] == "Craft!":
        break
    if command[0] == "Collect":
        if command[1] not in items:
            items.append(command[1])
    elif command[0] == "Drop":
        if command[1] in items:
            items.remove(command[1])
    elif command[0] == "Combine Items":
        old_item, new_item = command[1].split(":")
        if old_item in items:
            index = items.index(old_item)
            items.insert(index + 1, new_item)
    elif command[0] == "Renew":
        if command[1] in items:
            for index in range(len(items)):
                if command[1] == items[index]:
                    last_value = items[-1]
                    items[-1] = command[1]
                    items.insert(-1, last_value)
                    del items[index]
    command = input().split(" - ")
print(", ".join(items))

