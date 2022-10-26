phones = input().split(", ")
command = input().split(" - ")
while True:
    if command[0] == "End":
        break
    if command[0] == "Add":
        phone = command[1]
        if phone not in phones:
            phones.append(phone)
    elif command[0] == "Remove":
        phone = command[1]
        if phone in phones:
            phones.remove(phone)
    elif command[0] == "Bonus phone":
        phones2 = command[1].split(":")
        old_phone = phones2[0]
        new_phone = phones2[1]
        if old_phone in phones:
            index = phones.index(old_phone)
            phones.insert(index + 1, new_phone)
    elif command[0] == "Last":
        if command[1] in phones:
            index = phones.index(command[1])
            last_value = phones[-1]
            phones[-1] = command[1]
            phones.insert(-1, last_value)
            phones.remove(phones[index])
    command = input().split(" - ")
print(", ".join(phones))
