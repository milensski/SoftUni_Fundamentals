sequence = input().split(".")
sequence = list(map(int, sequence))
sequence[-1] += 1
for i in range(len(sequence)-1, -1, -1):
    if sequence[i] > 9:
        sequence[i] = 0
        sequence[i - 1] += 1

print(*sequence, sep=".")
