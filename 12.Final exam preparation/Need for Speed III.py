def revert_function(car, kilometers, data):
    car_fuel = int(data[car][1])
    car_mileage = int(data[car][0])
    amount_reverted = kilometers
    car_mileage -= amount_reverted
    if car_mileage < 10000:
        car_mileage = 10000
        data[car] = [car_mileage, car_fuel]
    else:
        data[car] = [car_mileage, car_fuel]
        print(f"{car} mileage decreased by {amount_reverted} kilometers")


def refuel_func(car, fuel, data):
    car_mileage = int(data[car][0])
    car_fuel = int(data[car][1])
    car_fuel += fuel
    if car_fuel > 75:
        car_fuel = 75
        fuel = fuel - (car_fuel - 75)
        data[car] = [car_mileage, car_fuel]
        print(f"{car} refueled with {fuel} liters")
    else:
        data[car] = [car_mileage, car_fuel]
        print(f"{car} refueled with {fuel} liters")


def drive_func(car, distance, fuel, data):
    car_fuel = int(data[car][1])
    car_mileage = int(data[car][0])
    if car_fuel < fuel:
        data[car] = [car_mileage, car_fuel]
        print("Not enough fuel to make that ride")
    else:
        car_mileage += distance
        car_fuel -= fuel
        data[car] = [car_mileage, car_fuel]
        print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
    if car_mileage >= 100000:
        del data[car]
        print(f"Time to sell the {car}!")


def print_function(data):
    result = ""
    for car in data:
        mileage = data[car][0]
        fuel = data[car][1]
        result += f"{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.\n"
    return result


def store_data_function(number):
    data = {}
    for _ in range(number):
        current_data = input().split("|")
        car = current_data[0]
        mileage = current_data[1]
        fuel = current_data[2]

        data[car] = [mileage, fuel]
    return data


def need_for_speed_func(number):
    data = store_data_function(number)
    while True:
        command = input().split(" : ")
        if command[0] == "Stop":
            print(print_function(data))
            break
        if command[0] == "Drive":
            car = command[1]
            distance = int(command[2])
            fuel = int(command[3])
            drive_func(car, distance, fuel, data)
        elif command[0] == "Refuel":
            car = command[1]
            fuel = int(command[2])
            refuel_func(car, fuel, data)
        elif command[0] == "Revert":
            car = command[1]
            kilometers = int(command[2])
            revert_function(car, kilometers, data)


number_of_cars = int(input())
need_for_speed_func(number_of_cars)