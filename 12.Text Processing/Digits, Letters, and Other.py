text = input()
digits = ""
letters = ""
others = ""
for symbol in text:
    if symbol.isdigit():
        digits += symbol
    elif symbol.isalpha():
        letters += symbol
    else:
        others += symbol
print(digits)
print(letters)
print(others)