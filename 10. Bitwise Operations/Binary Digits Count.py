number = int(input())
binary_digit = int(input())
ones_counter = 0
zeroes_counter = 0


while True:
    if number == 1:
        ones_counter += 1
        break
    elif number == 2:
        zeroes_counter += 1
        break

    if number % 2 == 1:
        ones_counter += 1
    elif number % 2 == 0:
        zeroes_counter += 1

    number = number // 2

if binary_digit == 1:
    print(ones_counter)
else:
    print(zeroes_counter)
