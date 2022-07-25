def rate(plant, rating, plant_dict):
    if plant in plant_dict:
        if 'rating' not in plant_dict[plant]:
            plant_dict[plant]['rating'] = [rating]
        else:
            plant_dict[plant]['rating'].append(rating)

    else:
        print('error')

    return plant_dict


def update(plant, new_rarity, plant_dict):
    if plant in plant_dict:

        plant_dict[plant]['rarity'] = new_rarity

    else:
        print('error')

    return plant_dict


def reset(plant, plant_dict):

    if plant in plant_dict:
        if 'rating' in plant_dict[plant]:
            plant_dict[plant]['rating'] = []
    else:
        print('error')

    return plant_dict


n = int(input())

plant_dict = {}

for _ in range(n):

    plant, rarity = input().split('<->')

    plant_dict[plant] = {'rarity': rarity,'rating' : []}


while True:

    command = input()

    if command == 'Exhibition':
        break

    command = command.split(': ')

    if 'Rate' in command:

        plant, rating = command[1].split(' - ')

        plant_dict = rate(plant, int(rating), plant_dict)


    elif 'Update' in command:

        plant, new_rarity = command[1].split(' - ')
        plant_dict = update(plant, new_rarity, plant_dict)


    elif 'Reset' in command:

        plant = command[1].strip()
        plant_dict = reset(plant, plant_dict)

print('Plants for the exhibition:')

for key in plant_dict:

    RARE = plant_dict[key]['rarity']

    if not plant_dict[key]['rating']:
        RATE = 0
    else:
        RATE = sum(plant_dict[key]['rating']) / len(plant_dict[key]['rating'])

    print(f'- {key}; Rarity: {RARE}; Rating: {RATE:.2f}')
