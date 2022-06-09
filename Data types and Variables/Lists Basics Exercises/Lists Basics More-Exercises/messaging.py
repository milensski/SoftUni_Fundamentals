sequence_of_numbers = input().split()
chars = input()

queue_of_sums = []

for sequence in sequence_of_numbers:
    sum_of_sequence = 0
    for element in sequence:
        sum_of_sequence += int(element)

    sum_of_sequence %= 28
    print(chars[sum_of_sequence], end="")
    chars = chars.replace(chars[sum_of_sequence], "", 1)
