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

def main():
    cars = []
    for i in range(1, 11):
        registration_number = f"ABC-{i}"
        maximum_speed = random.randint(100,200)
        car = Car(registration_number, maximum_speed)
        cars.append(car)

    race_over = False
    hours = 0
    winner = None

    while not race_over:
        hours += 1

        for car in cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)

            car.drive(1)

            if car.travelled_distance >= 10000:
                race_over = True
                winner = car
                break

    print(f"Race finished! After {hours} hours.")
    print(f"{'Registration':<15}{'Max speed':<10} {'Current speed':<15}{'Travelled distance': <20}")
    print("-" * 60)

    for car in cars:
        print(f"{car.registration_number:<20}{car.maximum_speed:<15}{car.current_speed:<15}{car.travelled_distance:<10}")

    print(f"\nThe winner is {winner.registration_number} with {winner.travelled_distance} km travelled!")

main()