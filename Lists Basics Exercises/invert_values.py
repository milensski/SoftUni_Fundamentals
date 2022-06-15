string_line = input()

to_list = string_line.split(" ")
new_list = []

def inverted(value):
    x = -1 * value
    return x


for element in to_list:
    new_list.append(inverted(int(element)))

print(new_list)
