data = input()
while True:
    command = input().split("|")
    if command[0] == "Decode":
        print(f"The decrypted message is: {data}")
        break
    if command[0] == "Move":
        number = int(command[1])
        changed_letters = data[:number]
        data = data.replace(changed_letters, "")
        data += changed_letters

    elif command[0] == "Insert":
        index = int(command[1])
        character = command[2]
        data = data[:index] + character + data[index:]

    elif command[0] == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        data = data.replace(substring, replacement)

