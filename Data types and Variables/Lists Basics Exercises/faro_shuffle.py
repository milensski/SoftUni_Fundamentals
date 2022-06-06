cards = input().split()
shuffles = int(input())

for shuffle in range(shuffles):
    middle_of_deck = len(cards) // 2
    left_part = cards[0:middle_of_deck:]
    right_part = cards[middle_of_deck::]
    shuffled_deck = []

    for current_index in range(middle_of_deck):
        shuffled_deck.append(left_part[current_index])
        shuffled_deck.append(right_part[current_index])

    cards = shuffled_deck

print(shuffled_deck)
