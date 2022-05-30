group_size = int(input())
days = int(input())
coins = 0

for current_day in range(1, days + 1):
    coins += 50  # received each day
    if current_day % 10 == 0:
        group_size -= 2
    if current_day % 15 == 0:
        group_size += 5
    coins -= 2 * group_size  # spent for food each day per companion
    if current_day % 3 == 0:
        coins -= 3 * group_size
    if current_day % 5 == 0:
        coins += 20 * group_size
        if current_day % 3 == 0:
            coins -= 2 * group_size


print(f"{group_size} companions received {int(coins / group_size)} coins each.")
