class Elevator:
    def __init__(self, bottom_floor, top_floor):
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
        print(f"The elevator is now at floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
           self.current_floor -= 1
        print(f"The elevator is now at floor {self.current_floor}")

elevator = Elevator (0, 8)

print("Moving to floor 3:")
elevator.go_to_floor(8)

print("\nMoving back to floor:")
elevator.go_to_floor(4)