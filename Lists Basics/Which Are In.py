first_sequence = input().split(", ")
second_sequence = input().split(", ")
substrings = []
for first_word in first_sequence:
    for second_word in second_sequence:
        if first_word in second_word and not first_word in substrings:
            substrings.append(first_word)
print(substrings)