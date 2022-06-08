fires = input().split("#")  # | High = 89#Low = 28#Medium = 77#Low = 23
water = int(input())
cells = []
type_of_fire = []
value_of_fire = []

valid_cells = []
total_effort = 0
total_fire = 0

for cell in fires:
    cells.append(cell.split(" = "))

for element in cells:
    type_of_fire.append(element[0])
    value_of_fire.append(element[1])

for index in range(len(type_of_fire)):  # print(f"{type_of_fire[index]} = {value_of_fire[index]}")

    current_type = type_of_fire[index]
    current_value = int(value_of_fire[index])

    # WORKING WITH EACH CELL:

    if current_type == "High" and 81 <= current_value <= 125 and current_value <= water:
        valid_cells.append(int(current_value))
        water -= current_value
        total_fire += current_value
        total_effort += current_value * 0.25
    elif current_type == "Medium" and 51 <= current_value <= 80 and current_value <= water:
        valid_cells.append(int(current_value))
        water -= current_value
        total_fire += current_value
        total_effort += current_value * 0.25
    elif current_type == "Low" and 1 <= current_value <= 50 and current_value <= water:
        valid_cells.append(int(current_value))
        water -= current_value
        total_fire += current_value
        total_effort += current_value * 0.25

print(f"Cells: ")
for valid in valid_cells:
    print(f" - {valid}")
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")
