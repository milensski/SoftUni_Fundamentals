food = float(input()) * 1000
hay = float(input()) * 1000
cover = float(input()) * 1000
weight = float(input()) * 1000

day = 1

while day != 31:
    food -= 300
    if food <= 0:
        print(f"Merry must go to the pet store!")
        break
    if day % 2 == 0:
        hay -= food * 0.05
        if hay <= 0:
            print(f"Merry must go to the pet store!")
            break
    if day % 3 == 0:
        cover -= weight * 1 / 3
        if cover <= 0:
            print(f"Merry must go to the pet store!")
            break
    day += 1
if food >= 0 and hay >= 0 and cover >= 0 and day == 31:
    print(f"Everything is fine! Puppy is happy! Food: {food/1000:.2f}, Hay: {hay/1000:.2f}, Cover: {cover/1000:.2f}.")
