# solution.py — Connect Four

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

    def drop_disc(self, col, disc_color):
        # find lowest empty row in this column
        for row in range(self.ROWS - 1, -1, -1):
            if self.grid[row][col] is None:
                self.grid[row][col] = disc_color
                return row
        return -1  # column full

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
            return False  # column full
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

    def get_game_state(self):
        return self.game_state

    def get_winner(self):
        return self.winner