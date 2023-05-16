n = int(input())
result = 0
for i in range(n):
    string = input()
    char = ord(string)
    result += char
print(f"The sum equals: {result}")
