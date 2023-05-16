raw_activation_key = input()
print_flag = True
while True:
    command = input().split(">>>")
    print_flag = True
    if command[0] == "Generate":
        print(f"Your activation key is: {raw_activation_key}")
        break
    if command[0] == "Contains":
        substring = command[1]
        if substring in raw_activation_key:
            print(f"{raw_activation_key} contains {substring}")
        else:
            print(f"Substring not found!")
            print_flag = False
    elif command[0] == "Flip":
        startIndex = int(command[2])
        endIndex = int(command[3])
        change_string = raw_activation_key[startIndex:endIndex]
        if command[1] == "Upper":
            raw_activation_key = raw_activation_key.replace(change_string, change_string.upper())
        elif command[1] == "Lower":
            raw_activation_key = raw_activation_key.replace(change_string, change_string.lower())
    elif command[0] == "Slice":
        startIndex = int(command[1])
        endIndex = int(command[2])
        delete_string = raw_activation_key[startIndex:endIndex]
        raw_activation_key = raw_activation_key.replace(delete_string, "")
    if print_flag:
        print(f"{raw_activation_key}")
