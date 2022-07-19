sequence = input().split("|")
health = 100
bitcoin = 0
count = 1

for element in sequence:
    command, value = element.split()

    if command == "potion":
        health += int(value)
        if health > 100:
            healed_with = health - 100 - int(value)
            health = 100
        else:
            healed_with = int(value)

        print(f"You healed for {abs(healed_with)} hp.")
        print(f"Current health: {health} hp.")
    elif command == "chest":
        bitcoin += int(value)
        print(f"You found {int(value)} bitcoins.")
    else:
        health -= int(value)
        if health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {count}")
            exit()
    count += 1

print(f"You've made it!")
print(f"Bitcoins: {bitcoin}")
print(f"Health: {health}")
