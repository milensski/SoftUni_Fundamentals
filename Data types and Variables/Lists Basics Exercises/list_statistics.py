n = int(input())
list_positive = []
list_negative = []

for _ in range(n):
    number = int(input())
    if number > 0:
        list_positive.append(number)
    else:
        list_negative.append(number)

count_positives = len(list_positive)
sum_negatives = sum(list_negative)

print(f"{list_positive}\n{list_negative}\nCount of positives: {count_positives}\nSum of negatives: {sum_negatives}")
