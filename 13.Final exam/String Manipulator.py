string = input()
command = input().split(" ")
while True:
    if command[0] == "End":
        break
    if command[0] == "Translate":
        char = command[1]
        replacement = command[2]
        string = string.replace(char, replacement)
        print(string)
    elif command[0] == "Includes":
        substring = command[1]
        if substring in string:
            print(True)
        else:
            print(False)
    elif command[0] == "Start":
        substring = command[1]
        flag = string.startswith(substring)
        print(flag)
    elif command[0] == "Lowercase":
        string = string.lower()
        print(string)
    elif command[0] == "FindIndex":
        char = command[1]
        index = string.rfind(char)
        print(index)
    elif command[0] == "Remove":
        startIndex = int(command[1])
        count = int(command[2])
        removed_string = string[startIndex:startIndex + count]
        string = string.replace(removed_string, "")
        print(string)
    command = input().split(" ")