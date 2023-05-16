neighborhood = input().split("@")
neighborhood2 = []
command = input().split(" ")
for house in neighborhood:
    house = int(house)
    neighborhood2.append(house)
last_position = 0
cupid_position = neighborhood2[0]
while True:
    if command[0] == "Love!":
        break
    if cupid_position < len(neighborhood2):
        neighborhood2[cupid_position] -= 2
        if neighborhood2[cupid_position] == 0:
            print(f"Place {cupid_position} has Valentine's day.")
    else:
        cupid_position = neighborhood2[0]
        neighborhood2[cupid_position] -= 2
        if neighborhood2[cupid_position] == 0:
            print(f"Place {cupid_position} has Valentine's day.")
    last_position = int(cupid_position)
    command = input().split(" ")
    cupid_position = neighborhood2[last_position + int(command[1])]
counter = neighborhood2.count(0)
failed_positions = len(neighborhood2) - counter
if counter == len(neighborhood2):
    print(f"Cupid's last position was {last_position}")
    print("Mission was successful.")
else:
    print(f"Cupid's last position was {last_position}")
    print(f"Cupid has failed {failed_positions} places.")






