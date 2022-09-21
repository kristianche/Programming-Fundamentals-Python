divisor = int(input())
boundary = int(input())
max = 0
for i in range(1, boundary + 1):
    if i % divisor == 0:
        if i > max:
            max = i
print(max)