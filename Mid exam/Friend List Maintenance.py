friends = input().split(", ")
command = input().split(" ")
blacklisted_counter = 0
lost_counter = 0
while True:
    if command[0] == "Report":
        break
    if command[0] == "Blacklist":
        if command[1] in friends:
            blacklisted_counter += 1
            index = friends.index(command[1])
            value = friends[index]
            friends[index] = "Blacklisted"
            print(f"{value} was blacklisted.")
        else:
            print(f"{command[1]} was not found.")
    elif command[0] == "Error":
        index = int(command[1])
        if 0 <= index <= len(friends) - 1 and friends[index] != "Blacklisted" and friends[index] != "Lost":
            lost_counter += 1
            value = friends[index]
            friends[index] = "Lost"
            print(f"{value} was lost due to an error.")
    elif command[0] == "Change":
        index = int(command[1])
        name = command[2]
        if 0 <= index <= len(friends) - 1:
            value = friends[index]
            friends[index] = command[2]
            print(f"{value} changed his username to {name}.")
    command = input().split(" ")
print(f"Blacklisted names: {blacklisted_counter}")
print(f"Lost names: {lost_counter}")
print(" ".join(friends))