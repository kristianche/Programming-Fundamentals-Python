first_string = input()
final_string = ""
for ch in first_string:
    final_string += chr(ord(ch) + 3)
print(final_string)