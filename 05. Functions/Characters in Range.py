def characters_in_range(character1, character2):
    number1 = ord(character1)
    number2 = ord(character2)
    characters = []
    for current_character in range(number1 + 1, number2):
        characters.append(chr(current_character))
    return characters


first_character = input()
second_character = input()
result = characters_in_range(first_character, second_character)
print(" ".join(result))