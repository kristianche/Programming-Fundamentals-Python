number = int(input())
position = int(input())
binary_number = []


while True:
    if number == 0:
        break
    if number % 2 == 1:
        binary_number.append(1)
    elif number % 2 == 0:
        binary_number.append(0)

    number = number // 2

try:
    binary_digit = binary_number[position]
    print(binary_digit)
    print(binary_number)
except IndexError:
    print(0)