days = int(input())
number_of_players = int(input())
total_energy = float(input())
water_per_day_per_person = float(input())
food_per_day_per_person = float(input())
total_water = days * number_of_players * water_per_day_per_person
total_food = days * number_of_players * food_per_day_per_person
run_out_of_energy = False
for day in range(1, days + 1):
    energy_lost = float(input())
    total_energy -= energy_lost
    if total_energy <= 0:
        run_out_of_energy = True
        break
    if day % 2 == 0:
        total_energy = total_energy + 0.05 * total_energy
        total_water = total_water - 0.3 * total_water
    if day % 3 == 0:
        total_energy = total_energy + 0.1 * total_energy
        total_food = total_food - (total_food / number_of_players)
if run_out_of_energy:
    print(f"You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.")
else:
    print(f"You are ready for the quest. You will be left with - {total_energy:.2f} energy!")