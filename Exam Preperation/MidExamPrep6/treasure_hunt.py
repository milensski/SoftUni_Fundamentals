

def total_sum(lst):
    total = 0
    for element in lst:
        total += len(element)
    return total





loot = input().split("|")

while True:
    command = input()

    if command == "Yohoho!":
        break

    command = command.split()

    if command[0] == "Loot":
        command.pop(0)
        for element in command:
            if element not in loot:
                loot.insert(0,element)

    if command[0] == "Drop":
        index = int(command[1])
        if index >=0 and index < len(loot):
            removed_element = loot.pop(index)
            loot.append(removed_element)
    if command[0] == "Steal":
        count = int(command[1])
        print(", ".join(loot[-count::]))
        for each in loot[-count::]:
            loot.remove(each)

if len(loot) == 0:
    print("Failed treasure hunt.")
else:
    print(f"Average treasure gain: {total_sum(loot) / len(loot):.2f} pirate credits.")