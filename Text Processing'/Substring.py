remove_word = input()
word = input()
while remove_word in word:
    word = word.replace(remove_word, "")
print(word)
