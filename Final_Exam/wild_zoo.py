zoo = {}
regions = {}


def add(name, needed_food, area):

    if area not in regions:

        regions[area] = [name]
    else:
        if name not in regions[area]:
            regions[area].append(name)

    if name not in zoo:
        zoo[name] = [needed_food,area]
    else:
        zoo[name][0] += needed_food

    return zoo


def feed(name,food):

    if name in zoo:
        zoo[name][0] -= food

        if zoo[name][0] <= 0:
            area = zoo[name][1]
            regions[area].remove(name)
            del zoo[name]

            print(f'{name} was successfully fed')

    return zoo

while True:

    command = input().split(': ')

    if command[0] == 'EndDay':
        break

    if command[0] == 'Add':
        name,needed_food,area = command[1].split('-')

        zoo = add(name,int(needed_food),area)

    elif command[0] == 'Feed':

        name,food = command[1].split('-')

        zoo = feed(name,int(food))


print('Animals:')
for animal,food in zoo.items():
    print(f' {animal} -> {food[0]}g')

print('Areas with hungry animals:')
for area,animals in regions.items():
    if len(animals) == 0:
        continue
    print(f' {area}: {len(animals)}')
