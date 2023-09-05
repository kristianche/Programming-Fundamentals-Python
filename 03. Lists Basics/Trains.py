wagons_counter = int(input())
wagons = []
for i in range(wagons_counter):
    wagons.append(0)
command = input()
while command[0] != "End":
    if command[0] == "add":
        people_to_add = int(command[1])
        wagons[-1] += people_to_add
    elif command[0] == "insert":
        index = int(command[1])
        people_to_add = int(command[2])
        wagons[index] += people_to_add
    elif command[0] == "insert":
        index = int(command[1])
        people_to_remove = int(command[2])
        wagons[index] -= people_to_remove

print(wagons)