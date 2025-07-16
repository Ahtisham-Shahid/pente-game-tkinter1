SIZE = 13
EMPTY = "."
BLUE = "B"
YELLOW = "Y"

class PenteGame:
    def __init__(self):
        self.board = [[EMPTY for _ in range(SIZE)] for _ in range(SIZE)]
        self.turn = BLUE
        self.captures = {BLUE: 0, YELLOW: 0}

    def in_bounds(self, x, y):
        return 0 <= x < SIZE and 0 <= y < SIZE

    def switch_turn(self):
        self.turn = YELLOW if self.turn == BLUE else BLUE

    def place_stone(self, x, y):
        if not self.in_bounds(x, y) or self.board[x][y] != EMPTY:
            return False
        self.board[x][y] = self.turn
        return True

