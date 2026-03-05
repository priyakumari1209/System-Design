# solution.py — Parking Lot

from enum import Enum
from datetime import datetime
from threading import Lock
import math
import uuid

class VehicleType(Enum):
    MOTORCYCLE = "MOTORCYCLE"
    CAR = "CAR"
    TRUCK = "TRUCK"

class SpotSize(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

# vehicle type → minimum spot size needed
VEHICLE_SPOT_MAP = {
    VehicleType.MOTORCYCLE: SpotSize.SMALL,
    VehicleType.CAR:        SpotSize.MEDIUM,
    VehicleType.TRUCK:      SpotSize.LARGE,
}

class Vehicle:
    def __init__(self, license_plate, vehicle_type):
        self.license_plate = license_plate
        self.type = vehicle_type

class ParkingSpot:
    def __init__(self, id, floor, spot_number, size):
        self.id = id
        self.floor = floor
        self.spot_number = spot_number
        self.size = size
        self.vehicle = None

    def is_available(self):
        return self.vehicle is None

    def assign_vehicle(self, vehicle):
        self.vehicle = vehicle

    def remove_vehicle(self):
        self.vehicle = None

class Ticket:
    def __init__(self, vehicle, spot):
        self.id = str(uuid.uuid4())[:8]
        self.vehicle = vehicle
        self.spot = spot
        self.entry_time = datetime.now()
        self.exit_time = None
        self.fee = 0.0

class FeeCalculator:
    RATE_PER_HOUR = 2.0

    def calculate_fee(self, entry_time, exit_time):
        duration = (exit_time - entry_time).seconds / 3600
        hours = math.ceil(duration)  # round up to next hour
        return hours * self.RATE_PER_HOUR

class ParkingFloor:
    def __init__(self, floor_number, spots):
        self.floor_number = floor_number
        self.spots = spots

    def get_available_spot(self, required_size):
        # find smallest available spot that fits the vehicle
        fit = [
            s for s in self.spots
            if s.is_available() and s.size.value >= required_size.value
        ]
        fit.sort(key=lambda s: s.size.value)
        return fit[0] if fit else None

class ParkingLot:
    def __init__(self, floors):
        self.floors = floors
        self.active_tickets = {}  # license_plate → Ticket
        self.fee_calculator = FeeCalculator()
        self.lock = Lock()

    def enter(self, vehicle):
        with self.lock:
            required_size = VEHICLE_SPOT_MAP[vehicle.type]
            spot = self.find_available_spot(required_size)
            if not spot:
                raise Exception("Parking lot is full")
            spot.assign_vehicle(vehicle)
            ticket = Ticket(vehicle, spot)
            self.active_tickets[vehicle.license_plate] = ticket
            print(f"Vehicle {vehicle.license_plate} parked at "
                  f"floor {spot.floor} spot {spot.spot_number}")
            return ticket

    def exit(self, ticket):
        with self.lock:
            ticket.exit_time = datetime.now()
            ticket.fee = self.fee_calculator.calculate_fee(
                ticket.entry_time, ticket.exit_time
            )
            ticket.spot.remove_vehicle()
            del self.active_tickets[ticket.vehicle.license_plate]
            print(f"Vehicle {ticket.vehicle.license_plate} exited. "
                  f"Fee: ${ticket.fee:.2f}")
            return ticket.fee

    def find_available_spot(self, required_size):
        for floor in self.floors:
            spot = floor.get_available_spot(required_size)
            if spot:
                return spot
        return None

    def is_full_for(self, vehicle_type):
        required_size = VEHICLE_SPOT_MAP[vehicle_type]
        return self.find_available_spot(required_size) is None


# --- Run it ---
if __name__ == "__main__":
    # setup spots on floor 1
    spots_floor1 = [
        ParkingSpot("S1", floor=1, spot_number=1, size=SpotSize.SMALL),
        ParkingSpot("S2", floor=1, spot_number=2, size=SpotSize.SMALL),
        ParkingSpot("M1", floor=1, spot_number=3, size=SpotSize.MEDIUM),
        ParkingSpot("M2", floor=1, spot_number=4, size=SpotSize.MEDIUM),
        ParkingSpot("L1", floor=1, spot_number=5, size=SpotSize.LARGE),
    ]

    # setup spots on floor 2
    spots_floor2 = [
        ParkingSpot("M3", floor=2, spot_number=1, size=SpotSize.MEDIUM),
        ParkingSpot("L2", floor=2, spot_number=2, size=SpotSize.LARGE),
    ]

    floors = [
        ParkingFloor(floor_number=1, spots=spots_floor1),
        ParkingFloor(floor_number=2, spots=spots_floor2),
    ]

    lot = ParkingLot(floors)

    # vehicles enter
    car        = Vehicle("KA-01-1234", VehicleType.CAR)
    motorcycle = Vehicle("KA-02-5678", VehicleType.MOTORCYCLE)
    truck      = Vehicle("KA-03-9999", VehicleType.TRUCK)

    ticket1 = lot.enter(car)
    ticket2 = lot.enter(motorcycle)
    ticket3 = lot.enter(truck)

    # vehicles exit
    lot.exit(ticket1)
    lot.exit(ticket2)
    lot.exit(ticket3)