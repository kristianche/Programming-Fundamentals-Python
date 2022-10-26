total_electrons = int(input())
electrons_in_shell = []
number_of_shell = 0
current_electrons_count = 0
while True:
    if total_electrons == 0:
        break
    current_electrons_count = 0
    number_of_shell += 1
    max_number_electrons = 2 * (number_of_shell ** 2)
    for electron in range(max_number_electrons):
        current_electrons_count += 1
        total_electrons -= 1
        if total_electrons == 0:
            break
    electrons_in_shell.append(current_electrons_count)
print(electrons_in_shell)
