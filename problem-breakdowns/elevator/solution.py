# solution.py — Elevator System

from enum import Enum
from threading import Lock

class Direction(Enum):
    UP = "UP"
    DOWN = "DOWN"
    IDLE = "IDLE"

class DoorState(Enum):
    OPEN = "OPEN"
    CLOSED = "CLOSED"

class ElevatorStatus(Enum):
    MOVING = "MOVING"
    STOPPED = "STOPPED"
    MAINTENANCE = "MAINTENANCE"

class Request:
    def __init__(self, from_floor, direction):
        self.from_floor = from_floor
        self.direction = direction

class Elevator:
    def __init__(self, id, total_floors):
        self.id = id
        self.current_floor = 0
        self.direction = Direction.IDLE
        self.status = ElevatorStatus.STOPPED
        self.door_state = DoorState.CLOSED
        self.destinations = []
        self.lock = Lock()

    def add_destination(self, floor):
        with self.lock:
            if floor not in self.destinations:
                self.destinations.append(floor)
                self.destinations.sort()

    def is_available(self):
        return self.direction == Direction.IDLE

    def open_door(self):
        self.door_state = DoorState.OPEN
        print(f"Elevator {self.id} door OPEN at floor {self.current_floor}")

    def close_door(self):
        self.door_state = DoorState.CLOSED
        print(f"Elevator {self.id} door CLOSED")

    def move(self):
        if not self.destinations:
            self.direction = Direction.IDLE
            return

        next_floor = self.destinations[0]

        if next_floor > self.current_floor:
            self.direction = Direction.UP
            self.current_floor += 1
        elif next_floor < self.current_floor:
            self.direction = Direction.DOWN
            self.current_floor -= 1

        if self.current_floor == next_floor:
            self.destinations.pop(0)
            self.stop()

    def stop(self):
        self.status = ElevatorStatus.STOPPED
        self.open_door()
        self.close_door()
        print(f"Elevator {self.id} stopped at floor {self.current_floor}")


class ElevatorController:
    def __init__(self, elevators):
        self.elevators = elevators
        self.pending_requests = []

    def request_elevator(self, floor, direction):
        request = Request(floor, direction)
        elevator = self.assign_elevator(request)
        if elevator:
            elevator.add_destination(floor)
            print(f"Elevator {elevator.id} assigned to floor {floor}")
        else:
            self.pending_requests.append(request)
            print(f"No elevator available, request queued for floor {floor}")

    def assign_elevator(self, request):
        # Priority 1: idle elevator closest to request floor
        idle = [e for e in self.elevators if e.is_available()]
        if idle:
            return min(idle, key=lambda e: abs(e.current_floor - request.from_floor))

        # Priority 2: elevator moving in same direction and will pass the floor
        if request.direction == Direction.UP:
            passing = [
                e for e in self.elevators
                if e.direction == Direction.UP
                and e.current_floor <= request.from_floor
            ]
        else:
            passing = [
                e for e in self.elevators
                if e.direction == Direction.DOWN
                and e.current_floor >= request.from_floor
            ]

        if passing:
            return min(passing, key=lambda e: abs(e.current_floor - request.from_floor))

        return None  # will be queued


# --- Run it ---
if __name__ == "__main__":
    elevators = [Elevator(id=1, total_floors=10),
                 Elevator(id=2, total_floors=10)]

    controller = ElevatorController(elevators)

    controller.request_elevator(floor=3, direction=Direction.UP)
    controller.request_elevator(floor=7, direction=Direction.DOWN)

    # simulate movement
    for _ in range(5):
        for e in elevators:
            e.move()