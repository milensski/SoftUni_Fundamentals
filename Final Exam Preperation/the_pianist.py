def add(new_piece, new_composer, new_key, pieces):
    if new_piece not in pieces:
        pieces[new_piece] = {new_composer: new_key}
        return print(f"{new_piece} by {new_composer} in {new_key} added to the collection!")

    return print(f"{new_piece} is already in the collection!")


def remove(piece_remove, pieces):
    if piece_remove in pieces:
        del pieces[piece_remove]
        return print(f"Successfully removed {piece_remove}!")
    return print(f"Invalid operation! {piece_remove} does not exist in the collection.")


def changekey(existing_piece, new_key, pieces):
    if existing_piece in pieces:
        for key, value in pieces[existing_piece].items():
            pieces[existing_piece][key] = new_key
            return print(f"Changed the key of {existing_piece} to {new_key}!")
    return print(f"Invalid operation! {existing_piece} does not exist in the collection.")


n = int(input())
pieces = {}

for _ in range(n):
    piece, composer, key = input().split("|")
    pieces[piece] = {composer: key}

while True:

    command = input()

    if command == "Stop":
        break

    if "Add" in command:
        action, new_piece, new_composer, new_key = command.split("|")
        add(new_piece, new_composer, new_key, pieces)
    elif "Remove" in command:
        action, piece_remove = command.split("|")
        remove(piece_remove, pieces)
    elif "ChangeKey" in command:
        action, existing_piece, new_key = command.split("|")
        changekey(existing_piece, new_key, pieces)

for piece in pieces:
    for key, value in pieces[piece].items():
        print(f"{piece} -> Composer: {key}, Key: {value}")
