

raw_string = input()

while True:
    command = input()

    if command == 'Generate':
        print(f'Your activation key is: {raw_string}')
        break

    command = command.split('>>>')

    if command[0] == 'Contains':
        substring = command[1]
        if substring in raw_string:
            print(f'{raw_string} contains {substring}')
        else:
            print("Substring not found!")
    elif command[0] == 'Flip':
        action = command[1]
        start_index = int(command[2])
        end_index = int(command[3])
        substring = raw_string[start_index:end_index]
        if action == 'Upper':
            raw_string = raw_string[:start_index] + substring.upper() + raw_string[end_index:]
            print(raw_string)
        elif action == 'Lower':
            raw_string = raw_string[:start_index] + substring.lower() + raw_string[end_index:]
            print(raw_string)
    elif command[0] == 'Slice':
        start_index = int(command[1])
        end_index = int(command[2])
        raw_string = raw_string[:start_index] + raw_string[end_index:]
        print(raw_string)