list_gifts = input().split()
command = input()
commands = ["OutOfStock", "Required", "JustInCase"]
first_command = commands[0]
second_command = commands[1]
third_command = commands[2]
while command != "No Money":
    slice_of_command = command[:7]
    if slice_of_command in first_command:
        no_this_gift = command[11:]
        for gift in list_gifts:
            if gift == no_this_gift:
                index = list_gifts.index(gift)
                list_gifts[index] = "None"
    elif slice_of_command in second_command:
        change_gift_name = command[9:-2]
        index = command[-1]
        index = int(index)
        if index <= len(list_gifts) - 1:
            list_gifts[index] = change_gift_name
    elif slice_of_command in third_command:
        replace_name = command[11:]
        list_gifts[-1] = replace_name
    command = input()
for element in list_gifts:
    if element != "None":
        print(element, end=" ")

