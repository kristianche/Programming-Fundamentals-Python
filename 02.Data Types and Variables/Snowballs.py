number_of_snowballs = int(input())
max = 0
final_snowball_weight = 0
final_snowball_time = 0
final_snowball_quality = 0
snowball_value = 0
for snowball in range(1, number_of_snowballs + 1):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = (snowball_weight // snowball_time) ** snowball_quality
    if snowball_value > max:
        max = snowball_value
        final_snowball_weight = snowball_weight
        final_snowball_time = snowball_time
        final_snowball_quality = snowball_quality
print(f"{final_snowball_weight} : {final_snowball_time} = {max} ({final_snowball_quality})")

