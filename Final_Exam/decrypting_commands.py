text = input()

while True:

    command = input().split()

    if command[0] == 'Finish':
        break

    if command[0] == 'Replace':
        current_char = command[1]
        new_char = command[2]

        text = text.replace(current_char, new_char)
        print(text)

    elif command[0] == 'Cut':
        start_index = int(command[1])
        end_index = int(command[2])

        if start_index < 0 or end_index >= len(text):
            print('Invalid indices!')
        else:
            text = text[:start_index] + text[end_index + 1:]
            print(text)

    elif command[0] == 'Make':

        if command[1] == 'Upper':
            text = text.upper()
        else:
            text = text.lower()

        print(text)

    elif command[0] == 'Check':
        substring = command[1]

        if substring in text:
            print(f'Message contains {substring}')
        else:
            print(f'Message doesn\'t contain {substring}')

    elif command[0] == 'Sum':
        start_index = int(command[1])
        end_index = int(command[2])

        if start_index < 0 or end_index >= len(text):
            print('Invalid indices!')
        else:
            substring = text[start_index:end_index + 1]
            sum_substring = 0
            for char in substring:
                sum_substring += ord(char)
            print(sum_substring)
