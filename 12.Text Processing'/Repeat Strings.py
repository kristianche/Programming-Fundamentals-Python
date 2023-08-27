strings = input().split(" ")
final_string = ""
for string in strings:
    N = len(string)
    final_string += string * N
print(final_string)
