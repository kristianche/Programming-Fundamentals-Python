list_of_numbers = input().split(", ")
new_list_of_numbers = []
zeros = []
for number in list_of_numbers:
    number = int(number)
    if number == 0:
        zeros.append(number)
    else:
        new_list_of_numbers.append(number)
for zero in zeros:
    new_list_of_numbers.insert(len(new_list_of_numbers), zero)
print(new_list_of_numbers)