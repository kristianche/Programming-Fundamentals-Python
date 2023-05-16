shopping_list = input().split("!")
command = input().split(" ")
while True:
    if command[0] == "Go":
        break
    if command[0] == "Urgent":
        if command[1] not in shopping_list:
            shopping_list.append(command[1])
    elif command[0] == "Unnecessary":
        if command[1] in shopping_list:
            shopping_list.remove(command[1])
    elif command[0] == "Correct":
        if command[1] in shopping_list:
            for index in range(len(shopping_list)):
                if shopping_list[index] == command[1]:
                    shopping_list[index] = command[2]
    elif command[0] == "Rearrange":
        if command[1] in shopping_list:
            last_value = shopping_list[-1]
            shopping_list[-1] = command[1]
            shopping_list.insert(-1, last_value)

    command = input().split(" ")
print(", ". join(shopping_list))