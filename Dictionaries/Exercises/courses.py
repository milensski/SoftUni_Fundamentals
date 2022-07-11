
courses = {}


while True:
    data = input()

    if data == "end":
        break

    course, name = data.split(" : ")

    if course not in courses:
        courses[course] = []

    courses[course].append(name)


for course,names in courses.items():
    print(f"{course}: {len(names)}")
    [print(f"-- {name}") for name in names]
