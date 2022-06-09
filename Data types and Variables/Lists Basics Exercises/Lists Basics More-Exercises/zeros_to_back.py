single_string = input().split(", ")

for element in single_string:
    if element == "0":
        element_index = single_string.index(element)
        single_string.append(element)
        single_string.pop(element_index)

print(list(map(int, single_string)))
