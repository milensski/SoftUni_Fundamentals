n = int(input())

registered_vehicles = {}

for i in range(n):

    line = input().split()
    command = line[0]
    name = line[1]


    if command == "register":
        if name in registered_vehicles:
            print(f"ERROR: already registered with plate number {registered_vehicles[name]}")
        else:
            plate = line[2]
            registered_vehicles[name] = plate
            print(f"{name} registered {plate} successfully")
    elif command == "unregister":
        if name not in registered_vehicles:
            print(f"ERROR: user {name} not found")
        else:
            del registered_vehicles[name]
            print(f"{name} unregistered successfully")

var = {print(f"{username} => {plate_number}") for username, plate_number in registered_vehicles.items()}
