
line = input()
explosion = 0
i=0
modified_text = ''
while i < len(line):

    char = line[i]

    if char == ">":
        explosion += int(line[i+1])
        i += 1
        modified_text += char
        continue

    if explosion > 0:
        i+= 1
        explosion -= 1
        continue

    modified_text += char
    i += 1

print(modified_text)