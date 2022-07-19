from math import ceil
students = int(input())
lectures = int(input())
bonus = int(input())

max_bonus = 0.
top_student_lectures = 0

for student in range(1, students + 1):
    student_attendances = int(input())
    totalbonus = student_attendances / lectures * (5 + bonus)
    if totalbonus > max_bonus:
        max_bonus = totalbonus
        top_student_lectures = student_attendances

print(f"Max Bonus: {ceil(max_bonus)}.")
print(f"The student has attended {top_student_lectures} lectures.")
