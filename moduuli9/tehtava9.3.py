class Car:
    def __init__ (self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 150

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


    def __str__ (self):
        return (f"Car registration number: {self.registration_number}\n"
                f"Maximum speed: {self.maximum_speed} km/h\n"
                f"Current speed: {self.current_speed} km/h\n"
                f"Travelled distance: {self.travelled_distance} km")

car = Car("ABC-123", 142)

print(car)

car.accelerate(80)
print(f"The current speed of the car after accelerating to 80 km/h: {car.current_speed} km/h")

car.drive(2)
print(f"Travelled distance after driving for 2 hours: {car.travelled_distance} km")