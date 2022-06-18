people = int(input())
wagons = input().split()

wagons = list(map(int, wagons))

lift = []

for state in wagons:
    if int(state) >= 4:
        continue

    while state < 4:
        if people == 0:
            break
        state += 1
        people -= 1

    lift.append(state)

if people > 0:
    print(f"There isn't enough space!{people} people in a queue!\n{' '.join(map(str, lift))}")
else:
    print(f"The lift has empty spots!\n{' '.join(map(str, lift))}")