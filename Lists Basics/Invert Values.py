my_list = input().split()
opposite_numbers = []
for element in my_list:
    current_number = -int(element)
    opposite_numbers.append(current_number)
print(opposite_numbers)
