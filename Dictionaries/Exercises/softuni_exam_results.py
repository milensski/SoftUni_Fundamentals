def add_element(course, name, points, exam_results):
    if course not in exam_results:
        exam_results[course] = {}

    if name not in exam_results[course]:
        exam_results[course][name] = [points]
    else:
        exam_results[course][name].append(points)

    return exam_results


def banned(name, exam_results):
    for course in exam_results:
        if name in exam_results[course]:
            for i in range(len(exam_results[course][name])):
                exam_results[course][name][i] ='banned'
    return exam_results

exam_results = {}

while True:

    command = input()

    if command == "exam finished":
        break

    if "banned" in command:
        command = command.split("-")
        name = command[0]
        banned(name, exam_results)

    else:

        name, course, points = command.split("-")

        add_element(course, name, int(points), exam_results)

print("Results:")
for course_name, student_data in exam_results.items():

    for student_name, grades in student_data.items():
        if 'banned' in grades:
            continue
        else:
            print(f"{student_name} | {max(grades)}")

print("Submissions:")

for element in exam_results:
    count = 0
    for key, value in exam_results[element].items():
        count += len(value)
    print(f"{element} - {count}")
