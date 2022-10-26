version = input().split(".")
next_version = []
last_number = int(version[2])
mid_number = int(version[1])
first_number = int(version[0])
if last_number >= 9:
    last_number = 0
    next_version.append(str(last_number))
    mid_number += 1
    if mid_number >= 9:
        mid_number = 0
        next_version.append(str(mid_number))
        first_number += 1
        next_version.append(str(first_number))
    else:
        next_version.append(str(mid_number))
        next_version.append(str(first_number))
else:
    last_number += 1
    next_version.append(str(last_number))
    next_version.append(str(mid_number))
    next_version.append(str(first_number))
next_version = reversed(next_version)
print("." .join(next_version))


