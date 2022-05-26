text = input().lower()

water = text.count("water")
sand = text.count("sand")
fish = text.count("fish")
sun = text.count("sun")

sum = water + sand + fish + sun

print(sum)