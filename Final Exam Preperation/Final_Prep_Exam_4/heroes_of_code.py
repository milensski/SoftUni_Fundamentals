def check_maximum(name):
    if hero_stats[name]['hp'] > 100 or hero_stats[name]['mana'] > 200:
        if hero_stats[name]['hp'] > 100:
            hero_stats[name]['hp'] = 100

        if hero_stats[name]['mana'] > 200:
            hero_stats[name]['mana'] = 200

        return True

    return False


def cast_spell(name, mp_needed, spell_name):
    if hero_stats[name]['mana'] >= mp_needed:
        hero_stats[name]['mana'] -= mp_needed
        print(f'{name} has successfully cast {spell_name} and now has {hero_stats[name]["mana"]} MP!')
    else:
        print(f"{name} does not have enough MP to cast {spell_name}!")

    return hero_stats


def take_damage(name, damage, attacker_name):
    hero_stats[name]['hp'] -= damage

    if hero_stats[name]['hp'] > 0:
        print(f"{name} was hit for {damage} HP by {attacker_name} and now has {hero_stats[name]['hp']} HP left!")

    else:
        del hero_stats[name]
        print(f"{name} has been killed by {attacker_name}!")

    return hero_stats


def recharge(name, amount):
    recharged = 0
    current_mana = hero_stats[name]['mana']
    hero_stats[name]['mana'] += amount
    if check_maximum(name):
        recharged = 200 - current_mana
    else:
        recharged = amount
    print(f"{name} recharged for {recharged} MP!")

    return hero_stats


def heal(name, amount):
    recharged = 0
    current_hp = hero_stats[name]['hp']
    hero_stats[name]['hp'] += amount
    if check_maximum(name):
        recharged = 100 - current_hp
    else:
        recharged = amount
    print(f"{name} healed for {recharged} HP!")

    return hero_stats


n = int(input())

hero_stats = {}

for _ in range(n):
    line = input().split()

    name, hp, mana = line
    hp = int(hp)
    mana = int(mana)

    if name not in hero_stats:
        hero_stats[name] = {'hp': hp, 'mana': mana}
    else:
        hero_stats[name]['hp'] += hp
        hero_stats[name]['mana'] += mana

    check_maximum(name)

while True:

    command = input().split(' - ')

    if command[0] == 'End':
        break

    if command[0] == 'CastSpell':
        name = command[1]
        mp_needed = int(command[2])
        spell_name = command[3]

        hero_stats = cast_spell(name, mp_needed, spell_name)

    elif command[0] == 'TakeDamage':
        name = command[1]
        damage = int(command[2])
        attacker_name = command[3]

        hero_stats = take_damage(name, damage, attacker_name)

    elif command[0] == 'Recharge':
        name = command[1]
        amount = int(command[2])

        hero_stats = recharge(name, amount)

    elif command[0] == 'Heal':
        name = command[1]
        amount = int(command[2])

        hero_stats = heal(name, amount)

for hero in hero_stats:
    print(hero)
    print(f'  HP: {hero_stats[hero]["hp"]}')
    print(f'  MP: {hero_stats[hero]["mana"]}')
