list_of_sums = input().split(", ")
count_of_beggars = int(input())
counter = 0
list_amounts_colelcted = []
while counter < count_of_beggars:
    amount_collected = 0
    for current_beggar in range(counter, len(list_of_sums), count_of_beggars):
        amount_collected += int(list_of_sums[current_beggar])

    list_amounts_colelcted.append(amount_collected)
    counter += 1

print(list_amounts_colelcted)
