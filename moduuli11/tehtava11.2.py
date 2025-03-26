class Car:
    def __init__ (self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0


    def accelerate(self, increment):
        if self.current_speed + increment > self.maximum_speed:
            self.current_speed = self.maximum_speed
        else:
            self.current_speed += increment

    def brake(self):
        self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

    def get_status(self):
        return f"Speed: {self.current_speed} km/h, Distance travelled: {self.travelled_distance} km"

class ElectricCar(Car):
    def __init__(self, registration_number, maximum_speed, battery_capacity):
        super().__init__(registration_number, maximum_speed)
        self.battery_capacity = battery_capacity

    def get_status(self):
        return f"Electric car - {super().get_status()}, Battery capacity: {self.battery_capacity} kWh"

class GasolineCar(Car):
    def __init__(self, registration_number, maximum_speed, tank_volume):
        super().__init__(registration_number, maximum_speed)
        self.tank_volume = tank_volume

    def get_status(self):
        return f"Gasoline car - {super().get_status()}, Tank volume: {self.tank_volume} liters"

def main():
    electric_car = ElectricCar("ABC-15", 180, 52.5)
    gasoline_car = GasolineCar("ACD-123", 165, 32.3)

    electric_car.accelerate(150)
    gasoline_car.accelerate(140)

    electric_car.drive(3)
    gasoline_car.drive(3)

    print(electric_car.get_status())
    print(gasoline_car.get_status())

main()