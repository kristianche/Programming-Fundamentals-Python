word = input()
new_word = ""
for i in range(len(word) - 1, -1, -1):
    new_word += word[i]
print(new_word)