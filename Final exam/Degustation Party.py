def dislike_func(guest, meal, data):
    result = ""
    if guest in data:
        if meal in data[guest]:
            result = f"{guest} doesn't like the {meal}."
            data[guest].remove(meal)
        else:
            result = f"{guest} doesn't have the {meal} in his/her collection."
    else:
        result = f"{guest} is not at the party."
    return result


def like_func(guest, meal, data):
    if guest in data:
        if meal not in data[guest]:
            data[guest].append(meal)
    else:
        data[guest] = [meal]
    return data


def print_func(data):
    result = ""
    for guest in data:
        result += f"{guest}: {(', '.join(data[guest]))}\n"
    return result


command = input().split("-")
data = {}
unliked_meals = 0
while True:
    if command[0] == "Stop":
        print(print_func(data), end="")
        break
    if command[0] == "Like":
        guest = command[1]
        meal = command[2]
        like_func(guest, meal, data)
    elif command[0] == "Dislike":
        guest = command[1]
        meal = command[2]
        result = dislike_func(guest, meal, data)
        if result == f"{guest} doesn't like the {meal}.":
            unliked_meals += 1
            print(f"{guest} doesn't like the {meal}.")
        elif result == f"{guest} doesn't have the {meal} in his/her collection.":
            print(f"{guest} doesn't have the {meal} in his/her collection.")
        elif result == f"{guest} is not at the party.":
            print(f"{guest} is not at the party.")
    command = input().split("-")
print(f"Unliked meals: {unliked_meals}")



