n = int(input())
word = input()
strings = []
new_strings = []
for i in range(n):
    string = input()
    strings.append(string)
    if word in string or word == string:
        new_strings.append(string)
print(strings)
print(new_strings)