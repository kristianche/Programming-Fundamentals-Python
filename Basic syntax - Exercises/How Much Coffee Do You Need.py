command = input()
coffee = 0
list_of_commands = ["movie", "MOVIE", "CAT", "DOG", "CODING", "cat", "dog", "coding"]
while command != "END":
    if command in list_of_commands:
        x = command.isupper()
        if x:
            coffee += 2
        else:
            coffee += 1
    else:
        pass
    command = input()
if coffee > 5:
    print("You need extra sleep")
else:
    print(coffee)