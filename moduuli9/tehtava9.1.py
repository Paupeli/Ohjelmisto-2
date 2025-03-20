class Car:
    def __init__ (self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0


    def __str__ (self):
        return (f"Car registration number: {self.registration_number}\n"
                f"Maximum speed: {self.maximum_speed} km/h\n"
                f"Current speed: {self.current_speed} km/h\n"
                f"Travelled distance: {self.travelled_distance} km")

car = Car("ABC-123", 142)

print(car)