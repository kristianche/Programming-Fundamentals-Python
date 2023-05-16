numbers = input().split(" ")
int_numbers = []
for number in numbers:
    int_numbers.append(int(number))

int_numbers.sort()
print(int_numbers)