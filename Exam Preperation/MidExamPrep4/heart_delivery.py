sequence = input().split("@")
sequence = list(map(int, sequence))
last_index = 0
while True:
    command = input()

    if command == "Love!":
        break

    command = command.split()
    action = command[0]
    times = int(command[1])

    if action == "Jump":
        times += last_index
        if times >= 0 and times < len(sequence):

            if sequence[times] <= 0:
                print(f"Place {times} already had Valentine's day.")
                last_index = times
                continue
            else:
                sequence[times] -= 2

            if sequence[times] <= 0:
                print(f"Place {times} has Valentine's day.")

        else:
            if times >= len(sequence):
                times = 0

            if sequence[times] <= 0:
                print(f"Place {times} already had Valentine's day.")
                last_index = times
                continue
            else:
                sequence[times] -= 2
            if sequence[times] <= 0:
                print(f"Place {times} has Valentine's day.")

    last_index = times

count = [element for element in sequence if element != 0]

print(f"Cupid's last position was {last_index}.")
if sum(sequence) == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len(count)} places.")
