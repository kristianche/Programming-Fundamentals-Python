name = input()
bool = True
while name != "Welcome!":
    if name == "Voldemort":
        bool = False
        print("You must not speak of that name!")
        break
    elif len(name) < 5:
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
    else:
        print(f"{name} goes to Hufflepuff.")
    name = input()
if bool:
    print("Welcome to Hogwarts.")
