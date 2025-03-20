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


    def __str__ (self):
        return (f"Car registration number: {self.registration_number}\n"
                f"Maximum speed: {self.maximum_speed} km/h\n"
                f"Current speed: {self.current_speed} km/h\n"
                f"Travelled distance: {self.travelled_distance} kmn\n")

car = Car("ABC-123", 142)

print(car)
print("The car accelerates first +30 km/h, then 70 km/h and finally +50km/h\n")

car.accelerate(30)
car.accelerate(70)
car.accelerate(50)

print(f"Current speed after accelerations: {car.current_speed} km/h\n")
print("Emergency break used to force -200 km/h change of speed\n")

car.accelerate(-200)

print(f"Final speed of the car after emergency brake: {car.current_speed} km/h")