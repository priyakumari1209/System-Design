# Problem: Amazon Locker

## Requirements

### Functional
- Customer can deposit a package into a locker
- Customer can pick up a package using a code
- System assigns the smallest available locker that fits the package
- Locker has 3 sizes: Small, Medium, Large
- Each package gets a unique pickup code when deposited
- Code expires after X days if not picked up

### Non-Functional
- Multiple people can deposit/pickup at the same time (concurrency)
- System should work across multiple locker stations

---

## Core Entities

### Locker
- id
- size (SMALL / MEDIUM / LARGE)
- status (AVAILABLE / OCCUPIED)
- package (current package inside)

### Package
- id
- size (SMALL / MEDIUM / LARGE)
- customerId

### LockerStation
- id
- location
- list of Lockers

### Reservation / Order
- pickupCode
- lockerId
- packageId
- expiryDate
- status (ACTIVE / COMPLETED / EXPIRED)

---

## APIs / Methods

| Class         | Method                              | Returns      |
|---------------|-------------------------------------|--------------|
| LockerStation | depositPackage(package)             | pickupCode   |
| LockerStation | pickupPackage(pickupCode)           | Package      |
| LockerStation | findAvailableLocker(packageSize)    | Locker       |
| Locker        | isAvailable()                       | bool         |
| Locker        | assignPackage(package)              | void         |
| Locker        | releasePackage()                    | Package      |

---

## Design Decisions

- **Why LockerStation handles assignment?**
  - It owns the list of lockers, so it knows which are free
  - Follows "Tell Don't Ask" — station manages its own lockers

- **Why smallest locker that fits?**
  - Efficient use of space, saves large lockers for large packages

- **Why a separate Reservation class?**
  - Tracks pickup code + expiry separately from the Locker
  - Locker doesn't need to know about codes or expiry

- **Concurrency concern**
  - Two customers depositing at same time could get same locker
  - Fix: use a lock when calling findAvailableLocker + assignPackage

---

## Code
- See solution.py

---

## What I Learned
- Importance of separating concerns (Locker vs Reservation)
- "Rules live with the entity that owns the data"
- How to handle concurrency with locks in assignment logic
- Size matching logic: package size <= locker size