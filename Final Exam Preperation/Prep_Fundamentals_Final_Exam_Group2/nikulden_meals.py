meals = {}
unliked_meals = 0
while True:

    command = input()

    if command == 'Stop':
        break

    action, guest, meal = command.split('-')

    if action == 'Like':
        if guest not in meals:
            meals[guest] = []

        if meal not in meals[guest]:
            meals[guest].append(meal)

    elif action == 'Unlike':
        if guest not in meals:
            print(f"{guest} is not at the party.")
            continue
        else:
            if meal not in meals[guest]:
                print(f"{guest} doesn't have the {meal} in his/her collection.")
                continue
            else:
                meals[guest].remove(meal)
                unliked_meals += 1
                print(f'{guest} doesn\'t like the {meal}.')

meals = sorted(meals.items(), key=lambda x: x, reverse=False)
meals = sorted(meals, key=lambda e: len(e[1]),reverse=True)



for element in meals:
    print(f'{element[0]}: {", ".join(element[1])}')
print(f'Unliked meals: {unliked_meals}')