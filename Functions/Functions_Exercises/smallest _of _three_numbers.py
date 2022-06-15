def smallest(a, b, c):
    to_list = [a, b, c]

    return min(map(int, to_list))


a = input()
b = input()
c = input()

print(smallest(a, b, c))
