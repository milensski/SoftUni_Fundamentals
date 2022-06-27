travel_route = input().split("||")
fuel = int(input())
ammunition = int(input())

for route in travel_route:
    route = route.split()

    if route[0] == "Titan":
        print("You have reached Titan, all passengers are safe.")
        break


    command = route[0]
    value = int(route[1])

    if command == "Travel":
        if fuel < value:
            print("Mission failed.")
            break
        else:
            fuel -= value
            print(f"The spaceship travelled {value} light-years.")

    elif command == "Enemy":
        if ammunition >= value:
            ammunition -= value
            print(f"An enemy with {value} armour is defeated.")
        elif ammunition < value:
            if fuel >= value * 2:
                fuel -= value * 2
                print(f"An enemy with {value} armour is outmaneuvered.")
            else:
                print("Mission failed.")
                break
    elif command == "Repair":
        fuel += value
        ammunition += value * 2
        print(f"Ammunitions added: {value*2}.")
        print(f"Fuel added: {value}.")
