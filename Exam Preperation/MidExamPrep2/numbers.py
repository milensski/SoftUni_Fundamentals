people = int(input())
wagons = input().split()

wagons = list(map(int, wagons))

lift = []

for wagon in wagons:

    while wagon < 4:

        wagon += 1
        people -= 1

        if people == 0:
            break

    lift.append(wagon)

    if people == 0:
        break

if people > 0:
    if sum(lift) == len(wagons) * 4:
        print(f"There isn't enough space! {people} people in a queue!")
        print(' '.join(map(str, lift)))
elif people == 0 and sum(lift) != len(wagons) * 4:
        print(f"The lift has empty spots!")
        print(' '.join(map(str, lift)))
else:
    print(' '.join(map(str, lift)))

