number = int(input())
binary_number = []


while True:
    if number < 1:
        break
    if number % 2 == 1:
        binary_number.append(1)
    elif number % 2 == 0:
        binary_number.append(0)

    number = number // 2

binary_digit = binary_number[1]
print(binary_digit)