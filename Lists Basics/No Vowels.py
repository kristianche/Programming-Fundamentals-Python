text = input().lower()
vowels = ["a", "o", "e", "u", "i"]
result = [ch for ch in text if ch not in vowels]
print("".join(result))