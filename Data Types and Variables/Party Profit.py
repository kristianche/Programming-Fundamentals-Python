group_size = int(input())
days = int(input())
coins = 0
for_food = 0
for_water = 0
for_monster = 0
for_party = 0
party = False
coins_received = 0
for day in range(1, days + 1):
    party = False
    if day % 10 == 0:
        group_size -= 2
    if day % 15 == 0:
        group_size += 5
    coins += 50
    for_food = 2 * group_size
    coins -= for_food
    if day % 3 == 0:
        for_water = 3 * group_size
        coins -= for_water
    if day % 5 == 0:
        for_monster = 20 * group_size
        coins += for_monster
        if day % 3 == 0:
            party = True
        if party:
            for_party = 2 * group_size
            coins -= for_party
coins_received = coins // group_size
print(f"{group_size} companions received {coins_received} coins each.")






