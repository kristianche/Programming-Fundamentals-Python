usernames = input().split(", ")
valid_usernames = []
first_check = False
second_check = False
third_check = False
for username in usernames:
    first_check = False
    second_check = False
    # noinspection PyRedeclaration
    third_check = False
    if 3 < len(username) < 16:
        first_check = True
    for ch in username:
        if ch.isalpha() or ch.isdigit() or ch == "-" or ch == "_":
            continue
        else:
            break
    else:
        second_check = True
    if " " not in username:
        third_check = True
    if first_check and second_check and third_check:
        valid_usernames.append(username)
for username in valid_usernames:
    print(username)

