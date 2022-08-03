def check_entry(course_name, course_password):
    if course_name in contest and course_password == contest[course_name]['password']:
        return True
    return False


contest = {}
best_score = 0
best_player = {}
while True:

    exercises = input()

    if exercises == "end of contests":
        break

    course, password = exercises.split(':')

    contest[course] = {'password': password}

students_courses = {}

while True:

    entry = input()

    if entry == 'end of submissions':
        break

    course_name, course_password, name, points = entry.split('=>')
    points = int(points)
    if check_entry(course_name, course_password):
        if name not in students_courses:
            students_courses[name] = {course_name: points}
        else:
            if course_name not in students_courses[name]:
                students_courses[name].update({course_name: points})
            else:
                if students_courses[name][course_name] < points:
                    students_courses[name][course_name] = points

students_courses = sorted(students_courses.items(), key=lambda x: x[0], reverse=False)

for each in students_courses:
    score = 0
    for key, value in each[1].items():
        score += value
    if score > best_score:
        best_score = score
        best_player = [each, score]

print(f"Best candidate is {best_player[0][0]} with total {best_player[1]} points.")
print("Ranking:")

for element in students_courses:
    print(element[0])
    sorted_list = (sorted(element[1].items(), key=lambda x: x[1], reverse=True))
    for value in sorted_list:
        print(f'#  {value[0]} -> {value[1]}')
