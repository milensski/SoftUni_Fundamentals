list_of_numbers = input().split(" ")
n = int(input())

list_of_integers = [int(integer) for integer in list_of_numbers]

survivals = []

for _ in range(n):
    a = min(list_of_integers)
    list_of_integers.remove(a)

print(*list_of_integers, sep=', ')

