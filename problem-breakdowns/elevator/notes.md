# Problem: Elevator System

## Requirements

### Functional
- Building has multiple elevators and multiple floors
- User can press UP or DOWN button on any floor
- User can press a floor number inside the elevator
- System assigns the best elevator to handle the request
- Elevator moves up or down, stops at requested floors
- Elevator has a door (open / close)

### Non-Functional
- Multiple elevators running at same time (concurrency)
- Should be efficient — minimize wait time for users

---

## Core Entities

### Elevator
- id
- currentFloor
- direction (UP / DOWN / IDLE)
- status (MOVING / STOPPED / MAINTENANCE)
- doorState (OPEN / CLOSED)
- destinationFloors (list of floors to stop at)

### Floor
- floorNumber
- upButton (pressed or not)
- downButton (pressed or not)

### Request
- fromFloor
- toFloor
- direction (UP / DOWN)

### ElevatorController
- elevators (list of all elevators)
- pendingRequests (queue)

---

## APIs / Methods

| Class              | Method                              | Returns    |
|--------------------|-------------------------------------|------------|
| ElevatorController | requestElevator(floor, direction)   | void       |
| ElevatorController | assignElevator(request)             | Elevator   |
| ElevatorController | selectFloor(elevatorId, floor)      | void       |
| Elevator           | move()                              | void       |
| Elevator           | stop()                              | void       |
| Elevator           | openDoor()                          | void       |
| Elevator           | closeDoor()                         | void       |
| Elevator           | addDestination(floor)               | void       |
| Elevator           | isAvailable()                       | bool       |

---

## Design Decisions

- **Why ElevatorController assigns elevators, not the Floor?**
  - Controller has visibility of ALL elevators
  - Floor only knows its own buttons
  - Follows Single Responsibility — controller manages routing

- **Why destinationFloors is a sorted list?**
  - Elevator moving UP → serve floors in ascending order
  - Elevator moving DOWN → serve floors in descending order
  - Avoids unnecessary back and forth (SCAN algorithm)

- **How to pick the best elevator?**
  - Priority 1: Idle elevator closest to request floor
  - Priority 2: Moving elevator already going in same direction
    and will pass through request floor
  - Priority 3: Any other idle elevator

- **Why separate Request class?**
  - Decouples the floor button press from elevator logic
  - Easy to queue and retry if no elevator available immediately

- **Concurrency concern**
  - Multiple people pressing buttons at same time
  - Fix: use lock when modifying destinationFloors list

---

## Elevator Assignment Logic (How it works)
```
When request comes in (floor=3, direction=UP):

1. Find all IDLE elevators
   → pick closest one to floor 3

2. If no idle elevator:
   Find elevators moving UP that are BELOW floor 3
   → they will pass floor 3 on the way up
   → pick closest one

3. If still none:
   Queue the request
   → assign when an elevator becomes free
```

---

## SCAN Algorithm (how elevator decides next floor)
```
Moving UP:
  → keep going up, stop at each requested floor
  → when no more floors above, switch direction to DOWN

Moving DOWN:
  → keep going down, stop at each requested floor
  → when no more floors below, switch direction to UP

When no requests → go IDLE
```

---

## Code
- See solution.py

---

## What I Learned
- ElevatorController is the orchestrator — owns assignment logic
- Elevator owns its own movement and door state
- SCAN algorithm minimizes travel distance
- Importance of direction state for efficient routing
- Concurrency needed when multiple elevators modify shared queues