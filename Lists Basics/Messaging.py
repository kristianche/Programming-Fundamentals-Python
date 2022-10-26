numbers = input().split()
text = input()
sum_of_digits = 0
message = []
index = 0
list_of_text = []
for number in numbers:
    for element in text:
        list_of_text.append(element)
    for digit in number:
        digit = int(digit)
        sum_of_digits += digit
    if sum_of_digits <= len(text):
        message.append(list_of_text[sum_of_digits])

    else:
        index = len(text) - sum_of_digits
        message.append(list_of_text[index])


print("".join(message))


