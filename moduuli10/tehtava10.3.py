class Elevator:
    def __init__(self, name, bottom_floor, top_floor):
        self.name = name
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def go_to_floor(self, target_floor):
        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
        print(f"{self.name} is now at floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
           self.current_floor -= 1
        print(f"{self.name} is now at floor {self.current_floor}")

class Building:
    def __init__(self, bottom_floor, top_floor, number_of_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = []

        for i in range(number_of_elevators):
            elevator_name = f"Elevator_{i +1}"
            elevator =  Elevator(elevator_name, bottom_floor, top_floor)
            self.elevators.append(elevator)

    def get_elevator(self, elevator_name):
        for elevator in self.elevators:
            if elevator.name == elevator_name:
                return elevator

    def run_elevator(self, elevator_name, destination_floor):
        elevator = self.get_elevator(elevator_name)
        if elevator:
            print(f"\nRunning {elevator_name} to floor {destination_floor}:")
            elevator.go_to_floor(destination_floor)

    def fire_alarm(self):
        print("\nFire alarm activated!\n")
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom_floor)

def main():
    building = Building (0,8,2)
    building.run_elevator("Elevator_1", 4)
    building.run_elevator("Elevator_2", 2)
    building.fire_alarm()
main()