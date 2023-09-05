import math

students = int(input())
lectures = int(input())
additional_bonus = int(input())
max = 0
max_attendances = 0
for student in range(1, students + 1):
    student_attendances = int(input())
    total_bonus = student_attendances / lectures * (5 + additional_bonus)
    if total_bonus > max:
        max = total_bonus
        max_attendances = student_attendances
print(f"Max Bonus: {math.ceil(max)}.")
print(f"The student has attended {max_attendances} lectures.")
