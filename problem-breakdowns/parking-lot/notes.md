# Problem: Parking Lot

## Requirements

### Functional
- Vehicle enters parking lot → gets a ticket
- Vehicle exits → pays fee → barrier opens
- Parking lot has multiple floors
- Each floor has multiple parking spots
- Spot sizes: SMALL, MEDIUM, LARGE
- Vehicle types: MOTORCYCLE, CAR, TRUCK
  - Motorcycle → SMALL spot
  - Car        → MEDIUM spot
  - Truck      → LARGE spot
- System finds the nearest available spot for the vehicle
- Calculate parking fee based on hours parked

### Non-Functional
- Multiple vehicles entering/exiting at same time (concurrency)
- Multiple floors and spots (scale)

---

## Core Entities

### Vehicle
- licensePlate
- type (MOTORCYCLE / CAR / TRUCK)

### ParkingSpot
- id
- floor
- spotNumber
- size (SMALL / MEDIUM / LARGE)
- isOccupied (bool)
- vehicle (current vehicle parked)

### Ticket
- id
- vehicle
- spot
- entryTime
- exitTime
- fee

### ParkingFloor
- floorNumber
- spots (list of ParkingSpots)

### ParkingLot
- id
- floors (list of ParkingFloors)
- activeTickets (map of licensePlate → Ticket)

### FeeCalculator
- calculates fee based on hours parked

---

## APIs / Methods

| Class          | Method                              | Returns       |
|----------------|-------------------------------------|---------------|
| ParkingLot     | enter(vehicle)                      | Ticket        |
| ParkingLot     | exit(ticket)                        | float (fee)   |
| ParkingLot     | findAvailableSpot(vehicleType)      | ParkingSpot   |
| ParkingLot     | isFullFor(vehicleType)              | bool          |
| ParkingFloor   | getAvailableSpot(size)              | ParkingSpot   |
| ParkingSpot    | assignVehicle(vehicle)              | void          |
| ParkingSpot    | removeVehicle()                     | void          |
| ParkingSpot    | isAvailable()                       | bool          |
| FeeCalculator  | calculateFee(entryTime, exitTime)   | float         |

---

## Design Decisions

- **Why ParkingFloor finds the spot, not ParkingLot directly?**
  - ParkingFloor owns the list of spots on that floor
  - ParkingLot loops through floors and asks each floor
  - Follows "Tell Don't Ask" — floor manages its own spots

- **Why separate Ticket class?**
  - Tracks entry time separately from the spot
  - Spot can be reused after vehicle leaves
  - Ticket is the receipt — holds full history of the visit

- **Why separate FeeCalculator class?**
  - Fee logic can change (hourly, flat rate, per minute)
  - Keeping it separate means you change one class only
  - Single Responsibility Principle

- **Vehicle → Spot size mapping**
  - Motorcycle → SMALL
  - Car        → MEDIUM
  - Truck      → LARGE
  - A larger spot can fit a smaller vehicle if needed
    (e.g. no SMALL spots left → motorcycle gets MEDIUM)

- **Concurrency concern**
  - Two vehicles entering at same time could get same spot
  - Fix: lock the spot assignment inside findAvailableSpot

---

## Spot Assignment Logic
```
Vehicle enters (type = CAR):

1. Get required size → MEDIUM
2. Loop through each floor:
   → ask floor for available MEDIUM spot
   → if found → assign → return ticket
3. If no MEDIUM spot:
   → try LARGE spot (upgrade)
4. If nothing found:
   → parking lot is full → reject entry
```

---

## Fee Calculation Logic
```
Entry time  = 10:00 AM
Exit time   = 1:30 PM
Hours parked = 3.5 hours

Rate = $2 per hour
Fee  = 3.5 x 2 = $7.00

Always round UP to next hour:
3.5 hours → charged for 4 hours → $8.00
```

---

## Code
- See solution.py

---

## What I Learned
- Composite structure: ParkingLot → Floors → Spots
- Ticket decouples visit history from spot state
- FeeCalculator separation follows Single Responsibility
- Spot upgrade logic (motorcycle in medium if small full)
- Concurrency lock needed during spot assignment