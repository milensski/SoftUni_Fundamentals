cards = input()

list_players = cards.split(" ")

# print(list_players)

team_a_count = 11
team_b_count = 11

team_a = []
team_b = []

for element in list_players:
    if "A" in element:
        if element in team_a:
            continue
        team_a.append(element)
        team_a_count -= 1
        if team_a_count < 7:
            break
    elif "B" in element:
        if element in team_b:
            continue
        team_b.append(element)
        team_b_count -= 1
        if team_b_count < 7:
            break


# print(team_a)
# print(team_b)

print(f"Team A - {team_a_count}; Team B - {team_b_count}")
if team_a_count < 7 or team_b_count < 7:
    print("Game was terminated")
