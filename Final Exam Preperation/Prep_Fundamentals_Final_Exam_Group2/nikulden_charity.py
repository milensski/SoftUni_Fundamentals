def is_valid(start, end, text):

    if start >= 0 and end < len(text):
        return True
    return False


def replace(current_char, new_char, text):
    text = text.replace(current_char, new_char)

    return text




def cut(start_index, end_index, text):
    return text[:start_index] + text[end_index+1:]


def sum_string(substring):
    sum = 0

    for char in substring:
        sum+=ord(char)

    return sum


text = input()


while True:

    command = input()

    if command == 'Finish':
        break

    command = command.split()

    action = command[0]

    if action == 'Replace':
        current_char = command[1]
        new_char = command[2]

        text = replace(current_char, new_char,text)
        print(text)

    elif action == 'Cut':
        start_index = int(command[1])
        end_index = int(command[2])

        if is_valid(start_index,end_index,text):
            text = cut(start_index,end_index,text)
            print(text)
        else:
            print('Invalid indexes!')

    elif action == 'Make':
        condition = command[1]

        if condition == 'Upper':
            text = text.upper()
        else:
            text = text.lower()

        print(text)

    elif action == 'Check':
        substring = command[1]

        if substring in text:
            print(f'Message contains {substring}')
        else:
            print(f"Message doesn't contain {substring}")

    elif action == 'Sum':
        start_index = int(command[1])
        end_index = int(command[2])

        if is_valid(start_index, end_index, text):
            substring = text[start_index:end_index+1]

            print(sum_string(substring))
        else:
            print("Invalid indexes!")

