def shoot(targets_sequence, index2):
    value = targets_sequence[index2]
    targets_sequence[index2] = -1
    for i in range(len(targets_sequence)):
        if targets_sequence[i] == -1:
            continue
        elif targets_sequence[i] > value:
            targets_sequence[i] -= value
        elif targets_sequence[i] <= value:
            targets_sequence[i] += value
    return targets_sequence


def shoot_targets_function(targets_sequence):
    counter = 0
    while True:
        command = input()
        if command == "End":
            break
        else:
            index = int(command)
        if 0 <= int(index) <= len(targets_sequence) - 1 and targets_sequence[index] != -1:
            counter += 1
            shoot(targets_sequence, index)
    convert = [str(num) for num in targets_sequence]
    print(f"Shot targets: {counter} -> ", end="")
    print(" ".join(convert))


data = list(map(int, input().split(" ")))
shoot_targets_function(data)
