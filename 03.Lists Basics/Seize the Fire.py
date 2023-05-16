list_of_fire = input().split("#")
amount_of_water = int(input())
high_fire = "High"
medium_fire = "Medium"
low_fire = "Low"
total_fire = 0
total_effort = 0
final_cells = []
for index in range(len(list_of_fire)):
    fire = list_of_fire[index]
    type_of_fire = fire[:2]
    amount_of_fire = int(fire[-3:])
    if type_of_fire in high_fire and 81 < amount_of_fire < 125 and amount_of_water >= amount_of_fire:
        total_fire += amount_of_fire
        amount_of_water -= amount_of_fire
        total_effort += amount_of_fire / 4
        final_cells.append(amount_of_fire)
    elif type_of_fire in medium_fire and 51 < amount_of_fire < 80 and amount_of_water >= amount_of_fire:
        total_fire += amount_of_fire
        amount_of_water -= amount_of_fire
        total_effort += amount_of_fire / 4
        final_cells.append(amount_of_fire)
    elif type_of_fire in low_fire and 1 < amount_of_fire < 50 and amount_of_water >= amount_of_fire:
        total_fire += amount_of_fire
        amount_of_water -= amount_of_fire
        total_effort += amount_of_fire / 4
        final_cells.append(amount_of_fire)


print("Cells:")
for cell in final_cells:
    print(f"- {cell}")
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")
