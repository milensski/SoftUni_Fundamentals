def check_status(name, hp, mp):
    pass


def max_stats(name):
    if heroes[name]['hp'] > 100:
        heroes[name]['hp'] = 100
    if heroes[name]['mp'] > 200:
        heroes[name]['mp'] = 200

    return heroes


heroes = {}

n = int(input())

for _ in range(n):
    name, hp, mp = input().split()

    heroes[name] = {'hp': int(hp), 'mp': int(mp)}

    heroes = max_stats(name)

while True:

    command = input().split(' - ')

    if command[0] == 'End':
        break

    if command[0] == 'CastSpell':
        name = command[1]
        mp_needed = int(command[2])
        spell_name = command[3]

        if mp_needed <= heroes[name]['mp']:
            heroes[name]['mp'] -= mp_needed
            print(f'{name} has successfully cast {spell_name} and now has {heroes[name]["mp"]} MP!')
        else:
            print(f'{name} does not have enough MP to cast {spell_name}!')

    elif command[0] == 'TakeDamage':
        name = command[1]
        damage = int(command[2])
        attacker = command[3]

        heroes[name]['hp'] -= damage

        if heroes[name]['hp'] <= 0:
            del heroes[name]
            print(f"{name} has been killed by {attacker}!")
        else:
            print(f"{name} was hit for {damage} HP by {attacker} and now has {heroes[name]['hp']} HP left!")

    elif command[0] == 'Recharge':
        name = command[1]
        amount = int(command[2])

        if heroes[name]['mp'] + amount > 200:
            print(f"{name} recharged for {200 - heroes[name]['mp']} MP!")
            heroes[name]['mp'] = 200
        else:
            heroes[name]['mp'] += amount
            print(f"{name} recharged for {amount} MP!")

    elif command[0] == 'Heal':
        name = command[1]
        amount = int(command[2])

        if heroes[name]['hp'] + amount > 100:
            print(f"{name} healed for {100 - heroes[name]['hp']} HP!")
            heroes[name]['hp'] = 100
        else:
            heroes[name]['hp'] += amount
            print(f"{name} healed for {amount} HP!")

for hero in heroes:
    print(hero)
    print(f'  HP: {heroes[hero]["hp"]}')
    print(f'  MP: {heroes[hero]["mp"]}')
