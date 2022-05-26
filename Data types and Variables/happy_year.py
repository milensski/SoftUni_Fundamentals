year = int(input())

is_happy_year = False

while not is_happy_year:
    year += 1
    set_year = set()

    for i in range(len(str(year))):
        set_year.add(str(year)[i])

    is_happy_year = len(set_year) == len(str(year))

print(year)
