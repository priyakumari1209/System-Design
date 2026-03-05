# solution.py — Connect Four (Interactive)

from enum import Enum

class DiscColor(Enum):
    RED = "R"
    YELLOW = "Y"

class GameState(Enum):
    IN_PROGRESS = "in_progress"
    WIN = "win"
    DRAW = "draw"

class Player:
    def __init__(self, id, name, disc_color):
        self.id = id
        self.name = name
        self.disc_color = disc_color

class Board:
    ROWS = 6
    COLS = 7

    def __init__(self):
        self.grid = [[None] * self.COLS for _ in range(self.ROWS)]

    def print_board(self):
        print("\n  0   1   2   3   4   5   6")
        print("+" + "---+" * self.COLS)
        for row in self.grid:
            print("|", end="")
            for cell in row:
                if cell is None:
                    print("   |", end="")
                elif cell == DiscColor.RED:
                    print(" R |", end="")
                else:
                    print(" Y |", end="")
            print()
            print("+" + "---+" * self.COLS)

    def drop_disc(self, col, disc_color):
        for row in range(self.ROWS - 1, -1, -1):
            if self.grid[row][col] is None:
                self.grid[row][col] = disc_color
                return row
        return -1

    def is_full(self):
        return all(self.grid[0][col] is not None for col in range(self.COLS))

    def check_win(self, row, col):
        directions = [(0,1),(1,0),(1,1),(1,-1)]
        color = self.grid[row][col]
        for dr, dc in directions:
            count = 1
            count += self._count(row, col, dr, dc, color)
            count += self._count(row, col, -dr, -dc, color)
            if count >= 4:
                return True
        return False

    def _count(self, row, col, dr, dc, color):
        count = 0
        r, c = row + dr, col + dc
        while 0 <= r < self.ROWS and 0 <= c < self.COLS and self.grid[r][c] == color:
            count += 1
            r += dr
            c += dc
        return count

class Game:
    def __init__(self, player1, player2):
        self.board = Board()
        self.players = [player1, player2]
        self.current_player = player1
        self.game_state = GameState.IN_PROGRESS
        self.winner = None

    def make_move(self, col):
        row = self.board.drop_disc(col, self.current_player.disc_color)
        if row == -1:
            print("Column is full! Try another column.")
            return False
        if self.board.check_win(row, col):
            self.game_state = GameState.WIN
            self.winner = self.current_player
        elif self.board.is_full():
            self.game_state = GameState.DRAW
        else:
            self._switch_player()
        return True

    def _switch_player(self):
        self.current_player = (
            self.players[1]
            if self.current_player == self.players[0]
            else self.players[0]
        )

# --- Run the game ---
if __name__ == "__main__":
    player1 = Player(1, "Player 1", DiscColor.RED)
    player2 = Player(2, "Player 2", DiscColor.YELLOW)
    game = Game(player1, player2)

    print("🎮 Welcome to Connect Four!")
    print("Player 1 = R (RED)   Player 2 = Y (YELLOW)")
    print("Choose a column (0-6) to drop your disc\n")

    game.board.print_board()

    while game.game_state == GameState.IN_PROGRESS:
        player = game.current_player
        print(f"\n{player.name} ({player.disc_color.name}) - choose column (0-6): ", end="")

        try:
            col = int(input())
            if col < 0 or col > 6:
                print("Invalid! Enter a number between 0 and 6")
                continue
            game.make_move(col)
            game.board.print_board()
        except ValueError:
            print("Invalid input! Enter a number between 0 and 6")
            continue

    if game.game_state == GameState.WIN:
        print(f"\n🏆 {game.winner.name} ({game.winner.disc_color.name}) WINS!")
    else:
        print("\n🤝 It's a DRAW!")