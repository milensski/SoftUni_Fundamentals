sequence = input().split()

sequence = list(map(int, sequence))

avg_sum = sum(sequence) / len(sequence)

lst = list(filter(lambda x: x > avg_sum, (sorted(sequence, reverse=True))))[:5]

if len(lst) < 1:
    print("No")
else:
    print(" ".join(list(map(str, lst))))
