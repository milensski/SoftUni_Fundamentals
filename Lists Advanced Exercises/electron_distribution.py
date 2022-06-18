electrons = int(input())
count = 1


shells = []

while electrons != 0:
    current_shell = 0
    while current_shell != 2 * (count ** 2):
        current_shell += 1
        electrons -= 1
        if electrons == 0:
            break
    shells.append(current_shell)
    count += 1

print(shells)