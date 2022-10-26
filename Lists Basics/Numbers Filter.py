n = int(input())
filtered_numbers = []
unfiltered_numbers = []
for _ in range(n):
    numbers = int(input())
    unfiltered_numbers.append(numbers)
command = input()
for number in unfiltered_numbers:
    if command == "even" and (number == 0 or number % 2 == 0):
        filtered_numbers.append(number)
    elif command == "odd" and number % 2 != 0:
        filtered_numbers.append(number)
    elif command == "negative" and number < 0:
        filtered_numbers.append(number)
    elif command == "positive" and number >= 0:
        filtered_numbers.append(number)
print(filtered_numbers)