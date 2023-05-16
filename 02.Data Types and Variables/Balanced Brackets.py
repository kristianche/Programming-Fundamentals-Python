n = int(input())
bracket_open_counter = 0
bracket_close_counter = 0
flag = True
for i in range(1, n + 1):
    command = input()
    if command == "(":
        bracket_open_counter += 1
    elif command == ")":
        bracket_close_counter += 1
    if bracket_open_counter > bracket_close_counter:
        flag = False
    if bracket_open_counter < bracket_close_counter:
        flag = False
if bracket_open_counter == bracket_close_counter:
    print("BALANCED")
elif not flag:
    print("UNBALANCED")
