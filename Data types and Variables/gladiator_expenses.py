lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

trashed_helmet_count = 0
trashed_sword_count = 0
trashed_shield_count = 0
trashed_armor_count = 0

for lost_fight in range(1, lost_fights_count +1):
    if lost_fight % 2 == 0:
        trashed_helmet_count += 1
    if lost_fight % 3 == 0:
        trashed_sword_count += 1
    if lost_fight % 2 == 0 and lost_fight % 3 == 0:
        trashed_shield_count += 1

trashed_armor_count = trashed_shield_count // 2

trashed_helmet_price = helmet_price * trashed_helmet_count
trashed_sword_price = sword_price * trashed_sword_count
trashed_shield_price = shield_price * trashed_shield_count
trashed_armor_price = armor_price * trashed_armor_count

expenses = trashed_helmet_price + trashed_sword_price + trashed_shield_price + trashed_armor_price

print(f"Gladiator expenses: {expenses:.2f} aureus")

