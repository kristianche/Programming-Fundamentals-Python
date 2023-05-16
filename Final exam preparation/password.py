password = input()
new_raw_password = ""
while True:
    command = input().split(" ")
    if command[0] == "Done":
        if new_raw_password != "":
            print(f"Your password is: {new_raw_password}")
        else:
            print(f"Your password is: {password}")
        break
    if command[0] == "TakeOdd" and new_raw_password == "":
        for i in range(0, len(password)):
            if i % 2 != 0:
                character = password[i]
                new_raw_password += character
    elif command[0] == "Cut" and new_raw_password != "":
        index = int(command[1])
        length = int(command[2])
        cut_string = new_raw_password[index:index + length]
        new_raw_password = new_raw_password.replace(cut_string, "")
    elif command[0] == "Cut" and new_raw_password == "":
        index = int(command[1])
        length = int(command[2])
        cut_string = password[index:index + length]
        password = password.replace(cut_string, "")
    elif command[0] == "Substitute" and new_raw_password != "":
        substring = command[1]
        substitute = command[2]
        if substring in new_raw_password:
            new_raw_password = new_raw_password.replace(substring, substitute)
        else:
            print("Nothing to replace!")
            continue
    elif command[0] == "Substitute" and new_raw_password == "":
        substring = command[1]
        substitute = command[2]
        if substring in password:
            password = password.replace(substring, substitute)
        else:
            print("Nothing to replace!")
            continue
    if new_raw_password != "":
        print(new_raw_password)
    else:
        print(password)