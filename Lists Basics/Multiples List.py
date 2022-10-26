list_of_numbers = []
factor = int(input())
count = int(input())
number = 0
while len(list_of_numbers) < count:
    number += factor
    list_of_numbers.append(number)
print(list_of_numbers)