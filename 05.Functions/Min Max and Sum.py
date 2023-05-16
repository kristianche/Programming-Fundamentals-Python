def min_max_sum(numbers2):
    min = 20000000000
    max = 0
    list = []
    sum_of_numbers = 0
    for number in numbers2:
        if int(number) < min:
            min = int(number)
    list.append(min)
    for number in numbers2:
        if int(number) > max:
            max = int(number)
        sum_of_numbers += int(number)

    list.append(max)
    list.append(sum_of_numbers)
    return list


numbers = input().split(" ")
list_min_max_sum = min_max_sum(numbers)
minimum_number = list_min_max_sum[0]
maximum_number = list_min_max_sum[1]
sum_of_all_numbers = list_min_max_sum[2]
print(f"The minimum number is {minimum_number}")
print(f"The maximum number is {maximum_number}")
print(f"The sum number is: {sum_of_all_numbers}")
