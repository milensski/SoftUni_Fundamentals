empl_1 = int(input())
empl_2 = int(input())
empl_3 = int(input())
total_students = int(input())

result = 0
capacity_per_hour = empl_1 + empl_2 + empl_3
hour = 0
while result < total_students:
    hour += 1

    if hour % 4 == 0:
        hour += 1

    result += capacity_per_hour

print(f"Time needed: {hour}h.")
