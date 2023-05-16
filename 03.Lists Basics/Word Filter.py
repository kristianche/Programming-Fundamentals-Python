words = input().split(" ")
even_len_words = [word for word in words if len(word) % 2 == 0]
for word2 in even_len_words:
    print(word2)
