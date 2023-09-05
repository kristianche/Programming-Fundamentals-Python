strings = input().split(" ")
first_string = strings[0]
second_string = strings[1]
first_string_finished = False
second_string_finished = False
counter = 0
multi = 0
total_sum = 0
while True:
    if counter > len(second_string) - 1:
        second_string_finished = True
        break
    elif counter > len(first_string) - 1:
        first_string_finished = True
        break
    multi = ord(first_string[counter]) * ord(second_string[counter])
    total_sum += multi
    counter += 1
if second_string_finished:
    sliced_first_string = first_string[counter:]
    for ch in sliced_first_string:
        total_sum += ord(ch)
elif first_string_finished:
    sliced_second_string = second_string[counter:]
    for ch in sliced_second_string:
        total_sum += ord(ch)
print(total_sum)