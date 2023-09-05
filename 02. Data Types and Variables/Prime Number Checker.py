number = int(input())
number_is_prime = True
if number > 1:
    for i in range(2, number):
        if number % i == 0:
            number_is_prime = False
            break
if number_is_prime:
    print("True")
else:
    print("False")
