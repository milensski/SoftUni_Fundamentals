n = int(input())

students = {}

for _ in range(n):

    name = input()
    grade = float(input())

    if name not in students:
        students[name] = []
    students[name].append(grade)


for student in students:

    avrg_grade = sum(students[student]) / len(students[student])


    if avrg_grade >= 4.50:
        print(f"{student} -> {avrg_grade:.2f}")


