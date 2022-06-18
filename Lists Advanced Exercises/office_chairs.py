rooms = int(input())

free_chairs = 0
for room in range(1,rooms+1):
    command = input().split()
    chairs = len(command[0])
    people = int(command[1])

    if people > chairs:
        print(f"{people-chairs} more chairs needed in room {room}")
        free_chairs -= people-chairs
    else:

        free_chairs += chairs - people

if free_chairs >= 0:
    print(f"Game On, {free_chairs} free chairs left")

