def plunder(town,people,gold):
    cities[town]['population'] -= people
    cities[town]['gold'] -= gold
    print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
    if cities[town]['population'] <=0 or cities[town]['gold'] <=0:
        del cities[town]
        print(f"{town} has been wiped off the map!")
    return cities


def prosper(town,gold):
    if gold >= 0:
        cities[town]['gold'] += gold
        print(f"{gold} gold added to the city treasury. {town} now has {cities[town]['gold']} gold.")
    else:
        print(f"Gold added cannot be a negative number!")
    return cities
cities = {}

while True:

    command = input()

    if command == 'Sail':
        break

    name,population,gold = command.split('||')

    if name not in cities:
        cities[name] = {'population':int(population),'gold':int(gold)}
    else:
        cities[name]['population'] += int(population)
        cities[name]['gold'] += int(gold)



while True:
    command = input()

    if command == 'End':
        break

    command = command.split('=>')

    if command[0] == 'Plunder':
        town = command[1]
        people = int(command[2])
        gold = int(command[3])
        cities = plunder(town,people,gold)
    elif command[0] == 'Prosper':

        town=command[1]
        gold = int(command[2])

        cities = prosper(town,gold)

if len(cities) > 0:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for town in cities:
        print(f"{town} -> Population: {cities[town]['population']} citizens, Gold: {cities[town]['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")