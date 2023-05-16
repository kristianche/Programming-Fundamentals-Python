numbers = input().split(" ")
numbers.filter()
numbers[0] = f"[{numbers[0]}"
numbers[-1] = f"{numbers[-1]}]"
print(",".join(numbers))