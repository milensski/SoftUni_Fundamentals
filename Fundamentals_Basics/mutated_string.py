first_string = input()
second_string = input()

current_string = first_string

for i in range(len(second_string)):
    mutated_string = second_string[:i+1] + first_string[i+1:]
    if current_string == mutated_string:
        continue
    print(mutated_string)
    current_string = mutated_string
