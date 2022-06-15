def in_range(start, finish):
    to_list = []
    for i in range(ord(start)+1, ord(finish)):
        to_list.append(chr(i))
    return to_list


a = input()
b = input()

print(*in_range(a, b), sep=" ")
