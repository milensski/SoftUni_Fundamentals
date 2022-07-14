def force_side(side, user, force_book):
    present = False
    for value in force_book.values():
        if user in value:
            present = True
            break
    if not present:
        if side not in force_book:
            force_book[side] = [user]
        else:
            force_book[side].append(user)

    return force_book


def switch_side(side, user, force_book):
    present = False
    for value in force_book.values():
        if user in value:
            value.remove(user)
            present = True
            break
    if present:
        if side not in force_book:
            force_book[side] = [user]
        else:
            force_book[side].append(user)
    else:
        if side not in force_book:
            force_book[side] = [user]
        else:
            force_book[side].append(user)



    return f"{user} joins the {side} side!"


force_book = {}

while True:

    command = input()
    if command == "Lumpawaroo":
        break

    if " | " in command:
        side, user = command.split(" | ")
        force_side(side, user, force_book)
    elif " -> " in command:
        user, side = command.split(" -> ")
        print(switch_side(side, user, force_book))


for key,value in force_book.items():
    if len(force_book[key]) > 0:
        print(f"Side: {key}, Members: {len(force_book[key])}")
        [print(f"! {user}") for user in value]