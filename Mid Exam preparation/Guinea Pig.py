quantity_of_food = float(input()) * 1000
quantity_of_hay = float(input()) * 1000
quantity_of_cover = float(input()) * 1000
weight = float(input()) * 1000
flag = True
for day in range(1, 31):
    quantity_of_food -= 300
    if day % 2 == 0:
        quantity_of_hay -= (5*quantity_of_food) // 100
    if day % 3 == 0:
        quantity_of_cover -= weight//3
    if quantity_of_food < 0 or quantity_of_cover < 0 or quantity_of_hay < 0:
        flag = False
        break
quantity_of_hay_in_kilograms = quantity_of_hay / 1000
quantity_of_food_in_kilograms = quantity_of_food / 1000
quantity_of_cover_in_kilograms = quantity_of_cover / 1000

if flag:
    print(f"Everything is fine! Puppy is happy!", end="")
    print(f" Food: {quantity_of_food_in_kilograms:.2f}, Hay: {quantity_of_hay_in_kilograms:.2f}, ", end="")
    print(f"Cover: {quantity_of_cover_in_kilograms:.2f}.")
else:
    print("Merry must go to the pet store!")