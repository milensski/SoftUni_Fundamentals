fires = input().split("#")  # | High = 89#Low = 28#Medium = 77#Low = 23
water = int(input())
cells = []
type_of_fire = []
value_of_fire = []
for cell in fires:
    cells.append(cell.split(" = "))

print(type_of_fire)
print(value_of_fire)
