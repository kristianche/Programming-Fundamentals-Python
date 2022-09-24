key = int(input())
n = int(input())
word = 0
this_list = [""]
for i in range(1, n + 1):
    letter = input()
    string = ord(letter) + key
    new_letter = chr(string)
    this_list.append(new_letter)
this_list.pop(0)
for item in this_list:
    print(item, end="")