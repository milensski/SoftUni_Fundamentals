fires = input().split("#")  # | High = 89#Low = 28#Medium = 77#Low = 23
water = int(input())
cells = []
type_of_fire = []
value_of_fire = []

for cell in fires:
    cells.append(cell.split(" = "))

for element in cells:
    type_of_fire.append(element[0])
    value_of_fire.append(element[1])

for index in range(len(type_of_fire)):  # print(f"{type_of_fire[index]} = {value_of_fire[index]}")

    current_type = type_of_fire[index]
    current_value = int(value_of_fire[index])

    # WORKING WITH EACH CELL:


