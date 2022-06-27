def add(book_title, lst):
    if book_title not in lst:
        lst.insert(0,book_title)

    return lst

def insert(book_title, lst):
    if book_title not in lst:
        lst.append(book_title)

    return lst

def remove(book_title, lst):

    if book_title in lst:
        lst.remove(book_title)

    return lst


def swap(book_1, book_2, lst):

    if book_1 in lst and book_2 in lst:
        first_index = lst.index(book_1)
        second_index = lst.index(book_2)
        lst[first_index] = book_2
        lst[second_index] = book_1


    return lst


def check(index,lst):
    if index >= 0 and index < len(lst):
        book_name = lst[index]
        print(book_name)
    return lst

sequence = input().split("&")

while True:
    command = input().split(" | ")

    if command[0] == "Done":
        break

    if command[0] == "Add Book":
        sequence = add(command[1],sequence)
        # print(sequence)
    elif command[0] == 'Take Book':
        sequence = remove(command[1],sequence)
        # print(sequence)
    elif command[0] == "Swap Books":
        sequence = swap(command[1],command[2],sequence)
        # print(sequence)
    elif command[0] == "Insert Book":
        sequence = insert(command[1],sequence)

    elif command[0] == "Check Book":
        check(int(command[1]),sequence)

print(", ".join(sequence))