import random

class Car:
    def __init__ (self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        new_speed = self.current_speed + speed_change

        if new_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif new_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = new_speed

    def drive(self, hours):
        distance_travelled = self.current_speed * hours
        self.travelled_distance += distance_travelled

    def __str__(self):
        return f"{self.registration_number:<20}{self.maximum_speed:<15}{self.current_speed:<15}{self.travelled_distance:<10}"

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(-20,20)
            car.accelerate(speed_change)
            car.drive(1)

    def print_status(self):
        print(f"\nRace: {self.name}")
        print(f"Distance: {self.distance} km")
        print(f"{'Registration':<15}{'Max speed':<10}{'Current speed':<15}{'Travelled distance':<20}")
        print("-" * 60)

        for car in self.cars:
            print(car)

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False


def main():
    cars = []
    for i in range(1, 11):
        registration_number = f"ABC-{i}"
        maximum_speed = random.randint(100,200)
        car = Car(registration_number, maximum_speed)
        cars.append(car)

    race = Race("Grand Demolition Derby", 8000, cars)

    hours = 0
    winner = None

    while not race.race_finished():
        hours += 1
        race.hour_passes()

        if hours % 10 == 0:
            race.print_status()

    race.print_status()

    print(f"Race finished! After {hours} hours.")
    for car in race.cars:
        if car.travelled_distance >= race.distance:
            winner = car
            break

    print(f"\nThe winner is {winner.registration_number} with {winner.travelled_distance} km travelled!")

main()