lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
helmet_broken_count = 0
sword_broken_count = 0
shield_broken_count = 0
armor_broken_count = 0
for lost_fight in range(1, lost_fights + 1):
    if lost_fight % 2 == 0 and lost_fight % 3 == 0:
        shield_broken_count += 1
        if shield_broken_count % 2 == 0:
            armor_broken_count += 1
    if lost_fight % 2 == 0:
        helmet_broken_count += 1
    if lost_fight % 3 == 0:
        sword_broken_count += 1
helmet_price_total = helmet_price * helmet_broken_count
sword_price_total = sword_price * sword_broken_count
shield_price_total = shield_price * shield_broken_count
armor_price_total = armor_price * armor_broken_count
total_price = helmet_price_total + sword_price_total + shield_price_total + armor_price_total
print(f"Gladiator expenses: {total_price:.2f} aureus")
