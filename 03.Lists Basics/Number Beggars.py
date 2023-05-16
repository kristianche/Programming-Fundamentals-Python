money_list = input().split(", ")
money_list_as_digit = []
for element in money_list:
    money_list_as_digit.append(int(element))
number_of_beggars = int(input())
final_sums = []
starting_index = 0
while starting_index < number_of_beggars:
    sum_for_current_beggar = 0
    for current_index in range(starting_index, len(money_list_as_digit), number_of_beggars):
        sum_for_current_beggar += money_list_as_digit[current_index]
    final_sums.append(sum_for_current_beggar)
    starting_index += 1
print(final_sums)