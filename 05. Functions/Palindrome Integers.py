def palindrome(numbers2):
    list = []
    for number in numbers2:
        if number == number[::-1]:
            list.append("True")
        else:
            list.append("False")
    return list


numbers = input().split(", ")
list_of_flags = palindrome(numbers)
for flag in list_of_flags:
    print(flag)