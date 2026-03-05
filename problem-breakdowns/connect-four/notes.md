# Problem: Connect Four

## Requirements

### Functional
- 2 players take turns dropping a disc into a column
- Board is 6 rows x 7 columns
- Disc falls to the lowest available row in that column
- Player wins if they connect 4 discs in a row:
  - Horizontally
  - Vertically
  - Diagonally
- Game ends in a draw if board is full and no winner

### Non-Functional
- Two players only (no concurrency needed)
- In-memory game (no database)

---

## Core Entities

### Player
- id
- name
- discColor (RED / YELLOW)

### Board
- grid (6x7 2D array)
- lastMove (row, col)

### Game
- board
- players (list of 2)
- currentPlayer
- gameState (IN_PROGRESS / WIN / DRAW)

---

## APIs / Methods

| Class  | Method                        | Returns     |
|--------|-------------------------------|-------------|
| Game   | makeMove(player, col)         | bool        |
| Game   | getCurrentPlayer()            | Player      |
| Game   | getGameState()                | GameState   |
| Game   | getWinner()                   | Player?     |
| Board  | dropDisc(col, discColor)      | row (int)   |
| Board  | isFull()                      | bool        |
| Board  | checkWin(row, col)            | bool        |
| Board  | getCell(row, col)             | DiscColor?  |

---

## Design Decisions

- **Why does Board check for win, not Game?**
  - Board owns the grid data
  - Follows "Tell Don't Ask" — board knows its own state
  - Game just asks board: did that move win?

- **Why dropDisc returns the row?**
  - Board finds the lowest empty row
  - Returns row number so Game can pass it to checkWin

- **Why separate GameState enum?**
  - Cleaner than using strings like "win" or "draw"
  - Easy to extend later (e.g. PAUSED, ABANDONED)

- **Win check logic**
  - Only check from the last dropped disc position
  - No need to scan entire board every time
  - Check all 4 directions: horizontal, vertical, diagonal

---

## Win Check Logic (How it works)
```
For each direction (horizontal, vertical, diagonal):
  count = 1
  go forward in direction while same color → count++
  go backward in direction while same color → count++
  if count >= 4 → WIN
```

Directions to check:
```
Horizontal  → (0, +1) and (0, -1)
Vertical    → (+1, 0) and (-1, 0)
Diagonal 1  → (+1, +1) and (-1, -1)
Diagonal 2  → (+1, -1) and (-1, +1)
```

---

## Code
- See solution.py

---

## What I Learned
- "Rules live with entity that owns the data" → Board checks win
- How to check 4-directional win efficiently
- Difference between Game (orchestrator) and Board (data owner)
- GameState enum keeps game flow clean