import math

number_of_people = int(input())
capacity_elevator = int(input())

total_courses = number_of_people / capacity_elevator

total_courses = math.ceil(total_courses)

print(total_courses)