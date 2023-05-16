string = input()
for index in range(len(string)):
    if string[index] == ":" and string[index + 1] != " ":
        print(string[index], end="")
        print(string[index+1])