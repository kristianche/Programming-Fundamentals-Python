def swap(list_of_numbers, index1, index2):
    value = list_of_numbers[index1]
    list_of_numbers[index1] = list_of_numbers[index2]
    list_of_numbers[index2] = value
    return list_of_numbers


def multiply(list_of_numbers, index1, index2):
    product = int(list_of_numbers[index1]) * int(list_of_numbers[index2])
    list_of_numbers.insert(2, product)
    return list_of_numbers


def decrease(list_of_numbers):
    for number in list_of_numbers:
        number -= 1
    return list_of_numbers


numbers = input().split(" ")
numbers_in_int = []
for number in numbers:
    number = int(number)
    numbers_in_int.append(number)
command = input().split(" ")
numbers = []
while True:
    if command[0] == "end":
        break
    if command[0] == "swap":
        command[1] = int(command[1])
        command[2] = int(command[2])
        numbers_in_int = swap(numbers_in_int, command[1], command[2])
    elif command[0] == "multiply":
        command[1] = int(command[1])
        command[2] = int(command[2])
        numbers_in_int = multiply(numbers_in_int, command[1], command[2])
    elif command[0] == "decrease":
        numbers_in_int = decrease(numbers_in_int)
    command = input().split(" ")
for number in numbers_in_int:
    numbers.append(str(number))
print(", ".join(numbers))