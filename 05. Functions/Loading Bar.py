def bar(percent: int):
    index = int(percent / 10 - 1)
    for i in range(0, index + 1):
        bar2[i] = "%"
    if bar2[0] == "%":
        bar2[0] = "[%"
    else:
        bar2[0] = "[."
    if bar2[-1] == "%":
        bar2[-1] = "%]"
    else:
        bar2[-1] = ".]"
    return bar2


percentage = int(input())
bar2 = [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
loading_bar = bar(percentage)
points_counter = bar2.count(".")
if points_counter == 0:
    print("100% Complete!")
    print(*loading_bar, sep="")
else:
    print(f"{percentage}% ", end="")
    print(*loading_bar, sep="")
    print("Still loading...")
