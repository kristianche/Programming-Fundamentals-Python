word = input()
my_dict = {}
for char in word:
    if char == " ":
        continue
    if char in my_dict.keys():
        my_dict[char] += 1

    else:
        my_dict[char] = 1
for key, value in my_dict.items():
    print(f"{key} -> {value}")
