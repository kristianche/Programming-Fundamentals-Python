def factorial(number, result=1):
    for i in range(1, number + 1):
        result *= i
    return result


first_number = int(input())
second_number = int(input())
first_result = factorial(first_number)
second_result = factorial(second_number)
division = first_result / second_result
print(f"{division:.2f}")
