# 🧠 System Design Mastery — 3 to 4 Month Roadmap

> Based on HelloInterview's Low Level Design (LLD) curriculum.
> Follow this guide week by week, commit your notes and code to Git,
> and you'll have solid system design skills in 3–4 months.

---

## 📁 Folder Structure

```
system-design/
├── README.md
├── low-level-design/
│   ├── 01-introduction/
│   │   └── notes.md
│   ├── 02-delivery-framework/
│   │   └── notes.md
│   ├── 03-design-principles/
│   │   └── notes.md
│   ├── 04-oop-concepts/
│   │   └── notes.md
│   ├── 05-design-patterns/
│   │   └── notes.md
│   └── concurrency/
│       ├── 01-introduction/
│       │   └── notes.md
│       ├── 02-correctness/
│       │   └── notes.md
│       ├── 03-coordination/
│       │   └── notes.md
│       └── 04-scarcity/
│           └── notes.md
├── problem-breakdowns/
│   ├── TEMPLATE.md
│   ├── connect-four/
│   │   ├── notes.md
│   │   └── solution.py
│   ├── amazon-locker/
│   │   ├── notes.md
│   │   └── solution.py
│   ├── elevator/
│   │   ├── notes.md
│   │   └── solution.py
│   ├── parking-lot/
│   │   ├── notes.md
│   │   └── solution.py
│   └── file-system/
│       ├── notes.md
│       └── solution.py
└── high-level-design/
    └── (add HLD topics later)
```

---

## 🚀 Git Setup — Do This First

```bash
# 1. Create the project folder
mkdir system-design
cd system-design

# 2. Initialize Git
git init

# 3. Create all folders
mkdir -p low-level-design/01-introduction
mkdir -p low-level-design/02-delivery-framework
mkdir -p low-level-design/03-design-principles
mkdir -p low-level-design/04-oop-concepts
mkdir -p low-level-design/05-design-patterns
mkdir -p low-level-design/concurrency/01-introduction
mkdir -p low-level-design/concurrency/02-correctness
mkdir -p low-level-design/concurrency/03-coordination
mkdir -p low-level-design/concurrency/04-scarcity
mkdir -p problem-breakdowns/connect-four
mkdir -p problem-breakdowns/amazon-locker
mkdir -p problem-breakdowns/elevator
mkdir -p problem-breakdowns/parking-lot
mkdir -p problem-breakdowns/file-system
mkdir -p high-level-design

# 4. Create all notes.md files
touch README.md
touch low-level-design/01-introduction/notes.md
touch low-level-design/02-delivery-framework/notes.md
touch low-level-design/03-design-principles/notes.md
touch low-level-design/04-oop-concepts/notes.md
touch low-level-design/05-design-patterns/notes.md
touch low-level-design/concurrency/01-introduction/notes.md
touch low-level-design/concurrency/02-correctness/notes.md
touch low-level-design/concurrency/03-coordination/notes.md
touch low-level-design/concurrency/04-scarcity/notes.md
touch problem-breakdowns/TEMPLATE.md
touch problem-breakdowns/connect-four/notes.md
touch problem-breakdowns/connect-four/solution.py
touch problem-breakdowns/amazon-locker/notes.md
touch problem-breakdowns/amazon-locker/solution.py
touch problem-breakdowns/elevator/notes.md
touch problem-breakdowns/elevator/solution.py
touch problem-breakdowns/parking-lot/notes.md
touch problem-breakdowns/parking-lot/solution.py
touch problem-breakdowns/file-system/notes.md
touch problem-breakdowns/file-system/solution.py
touch high-level-design/.gitkeep

# 5. First commit
git add .
git commit -m "init: setup system design learning repo"

# 6. Push to GitHub (create repo on github.com first)
git remote add origin https://github.com/YOUR_USERNAME/system-design.git
git branch -M main
git push -u origin main
```

---

## 📅 Month-by-Month Plan

---

### 🟢 Month 1 — LLD Foundations (Weeks 1–4)

| Week   | Topic            | File                                            |
|--------|------------------|-------------------------------------------------|
| Week 1 | Introduction     | `low-level-design/01-introduction/notes.md`     |
| Week 1 | Delivery Framework | `low-level-design/02-delivery-framework/notes.md` |
| Week 2 | Design Principles | `low-level-design/03-design-principles/notes.md` |
| Week 3 | OOP Concepts     | `low-level-design/04-oop-concepts/notes.md`     |
| Week 4 | Design Patterns  | `low-level-design/05-design-patterns/notes.md`  |

```bash
git add low-level-design/
git commit -m "lld: completed month 1 foundations"
git push
```

---

### 🟡 Month 2 — Concurrency (Weeks 5–8)

| Week   | Topic         | File                                                   |
|--------|---------------|--------------------------------------------------------|
| Week 5 | Introduction  | `low-level-design/concurrency/01-introduction/notes.md` |
| Week 6 | Correctness   | `low-level-design/concurrency/02-correctness/notes.md`  |
| Week 7 | Coordination  | `low-level-design/concurrency/03-coordination/notes.md` |
| Week 8 | Scarcity      | `low-level-design/concurrency/04-scarcity/notes.md`     |

```bash
git add low-level-design/concurrency/
git commit -m "concurrency: completed month 2"
git push
```

---

### 🟠 Month 3 — Problem Breakdowns (Weeks 9–13)

| Week    | Problem       | Files                                          |
|---------|---------------|------------------------------------------------|
| Week 9  | Connect Four  | `problem-breakdowns/connect-four/`             |
| Week 10 | Amazon Locker | `problem-breakdowns/amazon-locker/`            |
| Week 11 | Elevator      | `problem-breakdowns/elevator/`                 |
| Week 12 | Parking Lot   | `problem-breakdowns/parking-lot/`              |
| Week 13 | File System   | `problem-breakdowns/file-system/`              |

```bash
# after each problem
git add problem-breakdowns/connect-four/
git commit -m "problem: connect-four complete"
git push
```

---

### 🔵 Month 4 — Review + High Level Design (Weeks 14–16)

- Revisit all 5 problem breakdowns
- Re-solve 2–3 problems without looking at notes
- Start High Level Design basics

```bash
mkdir -p high-level-design/01-hld-basics
touch high-level-design/01-hld-basics/notes.md
git add high-level-design/
git commit -m "hld: starting high level design"
git push
```

---

## 📝 What Each notes.md Contains

---

### `01-introduction/notes.md`
- What is LLD vs HLD
- Key questions to ask in an interview
- What entities, state, behavior mean

---

### `02-delivery-framework/notes.md`
- 4-Step Framework: Requirements → Entities → APIs → Code
- How to gather requirements
- How to define core entities
- How to define APIs per class
- Tell Don't Ask principle

---

### `03-design-principles/notes.md`
- SOLID (S, O, L, I, D — one line each with example)
- DRY — Don't Repeat Yourself
- KISS — Keep It Simple
- YAGNI — You Aren't Gonna Need It
- Tell Don't Ask

---

### `04-oop-concepts/notes.md`
- 4 Pillars: Encapsulation, Abstraction, Inheritance, Polymorphism
- Class vs Object
- Abstract Class vs Interface
- When to use each

---

### `05-design-patterns/notes.md`
- Creational: Singleton, Factory, Builder
- Structural: Adapter, Decorator, Composite
- Behavioral: Observer, Strategy, Command, State
- For each pattern: problem it solves + real example

---

### `concurrency/01-introduction/notes.md`
- What is concurrency
- Thread vs Process
- Race condition, Deadlock, Starvation

---

### `concurrency/02-correctness/notes.md`
- Race conditions
- Atomic operations
- Visibility problem
- volatile keyword

---

### `concurrency/03-coordination/notes.md`
- Mutex / Lock
- Synchronized blocks
- ReentrantLock
- Semaphore
- CountDownLatch

---

### `concurrency/04-scarcity/notes.md`
- Thread Pool
- Bounded Queue
- Rate Limiting
- Backpressure

---

### `connect-four/notes.md`
**Entities:** Player, Board, Game
**Key Methods:** makeMove, dropDisc, checkWin
**Key Pattern:** Board owns win check (has the data)
**Concurrency:** Not needed (2 players, turn based)
**Win Logic:** Check 4 directions from last dropped disc

---

### `amazon-locker/notes.md`
**Entities:** Locker, Package, LockerStation, Reservation
**Key Methods:** depositPackage, pickupPackage, findAvailableLocker
**Key Pattern:** LockerStation assigns lockers (owns the list)
**Concurrency:** Lock during findAvailableLocker + assign
**Assignment Logic:** Smallest available locker that fits package

---

### `elevator/notes.md`
**Entities:** Elevator, Floor, Request, ElevatorController
**Key Methods:** requestElevator, assignElevator, move, openDoor
**Key Pattern:** Controller assigns (sees all elevators)
**Concurrency:** Lock when modifying destinationFloors
**Algorithm:** SCAN — serve floors in current direction first

---

### `parking-lot/notes.md`
**Entities:** Vehicle, ParkingSpot, Ticket, ParkingFloor, ParkingLot, FeeCalculator
**Key Methods:** enter, exit, findAvailableSpot, calculateFee
**Key Pattern:** Floor finds spot (owns spot list), FeeCalculator separate
**Concurrency:** Lock during spot assignment
**Fee Logic:** Round up hours × rate per hour

---

### `file-system/notes.md`
**Entities:** FileSystemItem (abstract), File, Folder, FileSystem
**Key Methods:** createFile, createFolder, delete, move, rename, search, getSize
**Key Pattern:** Composite Pattern — File and Folder both have getSize()
**Concurrency:** Lock folder's children list during add/remove
**Search Logic:** Recursive DFS from root

---

## 🔁 Daily Git Habit

```bash
# Start of session
git pull

# End of session
git add .
git commit -m "study: [topic] - [what you did today]"
git push
```

**Good commit message examples:**
```
study: OOP concepts - finished inheritance and polymorphism
problem: parking-lot - completed class diagram and solution
concurrency: correctness - notes on race conditions and mutex
lld: delivery framework - added API design notes
```

---

## ✅ Completion Checklist

### 🟢 Month 1 — LLD Foundations
- [ ] Introduction
- [ ] Delivery Framework
- [ ] Design Principles
- [ ] OOP Concepts
- [ ] Design Patterns

### 🟡 Month 2 — Concurrency
- [ ] Introduction
- [ ] Correctness
- [ ] Coordination
- [ ] Scarcity

### 🟠 Month 3 — Problem Breakdowns
- [ ] Connect Four
- [ ] Amazon Locker
- [ ] Elevator
- [ ] Parking Lot
- [ ] File System

### 🔵 Month 4 — Review + HLD
- [ ] Re-solve 3 problems from scratch
- [ ] HLD Basics

---

## 💡 Golden Rules

- **Don't skip Delivery Framework** — most important for interviews
- **Code every problem** — don't just read the solution
- **Commit daily** — Git history = your progress tracker
- **Review every Sunday** — go through last week's notes before new week
- **Copy TEMPLATE.md** for every new problem — never start from blank

---

*Happy Learning! You've got this. 🚀*
