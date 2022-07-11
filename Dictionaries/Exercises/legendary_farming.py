items = {"shards": 0, "fragments": 0, "motes": 0}
isobtained = False
while not isobtained:

    materials = input().split()

    for element in range(0, len(materials), 2):
        value = int(materials[element])
        key = materials[element + 1]
        key = key.lower()

        if key in items:
            items[key] += value

        else:
            items[key] = value

        if key == "shards" and items[key] >= 250:
            print(f"Shadowmourne obtained!")
            items[key] -= 250
            isobtained = True
            break
        elif key == "fragments" and items[key] >= 250:
            print(f"Valanyr obtained!")
            items[key] -= 250
            isobtained = True
            break
        elif key == "motes" and items[key] >= 250:
            print(f"Dragonwrath obtained!")
            items[key] -= 250
            isobtained = True
            break

    if isobtained:
        break

var = {print(f"{key}: {value}") for key, value in items.items()}
