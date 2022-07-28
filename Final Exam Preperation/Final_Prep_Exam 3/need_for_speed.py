def drive(car, distance, fuel, car_data):
    if car_data[car]['fuel'] >= fuel:

        car_data[car]['fuel'] -= fuel

        car_data[car]['distance'] += distance

        print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")

        if car_data[car]['distance'] >= 100000:
            print(f"Time to sell the {car}!")
            del car_data[car]
    else:
        print('Not enough fuel to make that ride')

    return car_data


def refuel(car, fuel, car_data):
    current_fuel = car_data[car]['fuel']
    liters_filled = 0
    if car_data[car]['fuel'] <= 75:
        car_data[car]['fuel'] += fuel

        if car_data[car]['fuel'] >= 75:
            car_data[car]['fuel'] = 75
            liters_filled = 75 - current_fuel
        else:
            liters_filled = fuel

    print(f"{car} refueled with {liters_filled} liters")

    return car_data


def revert(car, kilometers, car_data):
    car_data[car]['distance'] -= kilometers

    if car_data[car]['distance'] < 10000:
        car_data[car]['distance'] = 10000
        return car_data
    else:
        print(f'{car} mileage decreased by {kilometers} kilometers')
        return car_data


n = int(input())

car_data = {}

for _ in range(n):
    info = input().split('|')

    car = info[0]
    mileage = int(info[1])
    fuel = int(info[2])

    car_data[car] = {'distance': mileage, 'fuel': fuel}

while True:

    command = input()

    if command == 'Stop':
        break

    command = command.split(' : ')

    if command[0] == 'Drive':

        car = command[1]
        distance = int(command[2])
        fuel = int(command[3])

        car_data = drive(car, distance, fuel, car_data)

    elif command[0] == 'Refuel':

        car = command[1]
        fuel = int(command[2])

        car_data = refuel(car, fuel, car_data)

    elif command[0] == 'Revert':

        car = command[1]
        kilometers = int(command[2])

        car_data = revert(car, kilometers, car_data)

for car in car_data:
    print(f'{car} -> Mileage: {car_data[car]["distance"]} kms, Fuel in the tank: {car_data[car]["fuel"]} lt.')
