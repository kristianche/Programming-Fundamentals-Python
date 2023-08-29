number = int(input())
position = int(input())

binary_number = bin(number)
binary_number = binary_number.replace('b', '')
binary_number_list = list(binary_number)
binary_number_list.reverse()
binary_number_list[position] = 0

binary_number = ''.join(map(str, reversed(binary_number_list)))

print(int(binary_number, 2))