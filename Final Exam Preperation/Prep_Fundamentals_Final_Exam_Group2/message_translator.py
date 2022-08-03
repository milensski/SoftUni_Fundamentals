import re

n = int(input())

for _ in range(n):

    message = input()

    pattern = r'!([A-Z][a-z]{2,})!:\[([A-Za-z]{8,})\]'

    all_letters = r''

    result = re.search(pattern, message)

    encrypted = []

    if result:
        command = result.group(1)

        for element in result.group(2):
            encrypted.append(ord(element))

        print(f'{command}: {" ".join(list(map(str, encrypted)))}')
    else:
        print("The message is invalid")
