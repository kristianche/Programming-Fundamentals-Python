n = int(input())
pure = True
for i in range(1, n + 1):
    string = input()
    for character_index in string:
        if character_index == "_" or character_index == "," or character_index == ".":
            pure = False
    if pure:
        print(f"{string} is pure.")
    elif not pure:
        print(f"{string} is not pure!")