
students = {}

while True:
    command = input()

    if ":" not in command:
        break

    name, id_number, course = command.split(":")
    course = course.replace(" ", "_")

    if course not in students.keys():
        students[course] = {}

    students[course][name] = id_number

[print(f"{name} - {id_number}") for name, id_number in students[command].items()]
