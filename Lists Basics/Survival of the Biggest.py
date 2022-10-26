list_of_numbers = input().split()
del_numbers_count = int(input())
list_of_numbers.sort(reverse=True)
counter = 0
final_list = []
for element in list_of_numbers:
    final_list.append(element)
while counter < del_numbers_count:
    counter += 1
    final_list.pop()
final_list.split(", ")
print(list_of_numbers)
