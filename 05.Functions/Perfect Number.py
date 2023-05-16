def per_number(number2):
    number2 = int(number2)
    sum_of_number = 0
    for i in range(1, number2 + 1):
        if sum_of_number >= number2:
            break
        if number % i == 0:
            sum_of_number += i
    return sum_of_number


number = int(input())
sum_of_numbers = per_number(number)
if sum_of_numbers == number:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")