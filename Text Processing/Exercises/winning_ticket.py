def valid_ticket(element):
    if len(element) == 20:
        return True
    return False


def winning_ticket(element):
    first_half = element[0:10]
    second_half = element[10::]

    for winning_char in winnig_symbols:
        for repetition in range(10,5,-1):
            winning_streak = winning_char * repetition
            if winning_streak in first_half and winning_streak in second_half:
                if repetition == 10:
                    return f"ticket \"{element}\" - {repetition}{winning_char} Jackpot!"
                return f"ticket \"{element}\" - {repetition}{winning_char}"
    return f"ticket \"{ticket}\" - no match"


tickets = input().split(", ")

winnig_symbols = ['@', '#', '$', '^']

for element in tickets:
    ticket = element.strip()

    if valid_ticket(ticket):
        print(winning_ticket(ticket))
    else:
        print("invalid ticket")
