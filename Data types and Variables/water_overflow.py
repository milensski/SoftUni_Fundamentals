n = int(input())
water_tank_capacity = 255
poured_water = 0
for i in range(n):
    liters_of_water = int(input())
    if liters_of_water > water_tank_capacity:
        print("Insufficient capacity!")
        continue
    else:
        poured_water += liters_of_water
    water_tank_capacity -= liters_of_water
print(poured_water)
