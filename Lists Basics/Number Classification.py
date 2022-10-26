numbers = input().split(", ")
positives = [number for number in numbers if int(number) >= 0]
negatives = [number for number in numbers if int(number) < 0]
even = [number for number in numbers if int(number) % 2 == 0]
odd = [number for number in numbers if int(number) % 2 != 0]
positive = ", ".join(positives)
negative = ", ".join(negatives)
evens = ", ".join(even)
odds = ", ".join(odd)
print(f"Positive: {positive}")
print(f"Negative: {negative}")
print(f"Even: {evens}")
print(f"Odd: {odds}")