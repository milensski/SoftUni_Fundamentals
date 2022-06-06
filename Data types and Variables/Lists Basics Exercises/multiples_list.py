factor = int(input())
count = int(input())

multiples_list = []

for i in range(1, count + 1):
    x = factor * i
    multiples_list.append(x)

print(multiples_list)
