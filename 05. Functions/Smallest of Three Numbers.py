def smallest_number(number1, number2, number3):

    if number1 < number2 and number1 < number3:
        return number1
    if number2 < number1 and number2 < number3:
        return number2
    if number3 < number1 and number3 < number2:
        return number3


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(smallest_number(first_number, second_number, third_number))