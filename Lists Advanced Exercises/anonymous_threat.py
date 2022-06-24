def isvalid(ind, lenght):
    if ind < 0 or ind >= lenght:
        return False
    else:
        return True


def merge(start_index, end_index, sequence):
    if isvalid(start_index, len(sequence)) and isvalid(end_index, len(sequence)):
        return sequence[:start_index:] + ["".join(sequence[start_index:end_index + 1])] + sequence[end_index + 1::]
    elif isvalid(start_index, len(sequence)):
        return sequence[:start_index:] + ["".join(sequence[start_index::])]
    elif isvalid(end_index, len(sequence)):
        return ["".join(sequence[:end_index + 1:])] + sequence[end_index + 1::]

    return sequence


def divide(index: int, partition: int, str_list: list):
    str_on_index = str_list[index]
    divisor = len(str_on_index) // partition
    str_on_index = [str_on_index[i:i + divisor] for i in range(0, len(str_on_index), divisor)]
    str_list = str_list[:index] + str_on_index[:partition - 1] + ["".join(str_on_index[partition - 1:])] + str_list[
                                                                                                           index + 1:]
    return str_list


# def divide(index, partions, sequence):
#     word = sequence[index]
#     divisor = len(word) // partions
#
#     word = [word[i:i+divisor] for i in range(0,len(word),divisor)]
#
#     sequence = sequence[:index] + sequence[:partions - 1] + ["".join(word[partions - 1:])] + sequence[index + 1:]
#
#     # sequence = sequence[:index] + word   + sequence[index+1:len(sequence)]
#     return sequence


sequence = input().split()

while True:
    command = input()

    if command == "3:1":
        break

    if "merge" in command:
        command = command.split()
        start_index = int(command[1])
        end_index = int(command[2])
        sequence = merge(start_index, end_index, sequence)




    elif "divide" in command:
        command = command.split()
        index = command[1]
        partitions = command[2]
        sequence = divide(int(index), int(partitions), sequence)


print(*sequence, sep=" ")
