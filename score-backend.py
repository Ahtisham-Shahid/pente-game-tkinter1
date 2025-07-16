from game_board import PenteGame

class GameLogic:
    def __init__(self):
        self.game = PenteGame()

    def valid_move(self, x, y):
        return self.game.place_stone(x, y)

    def get_board(self):
        return self.game.board

    def get_turn(self):
        return self.game.turn

    def get_captures(self):
        return self.game.captures

    def switch_turn(self):
        self.game.switch_turn()

    def check_win_by_row(self, x, y):
        return self.game.check_five_in_a_row(x, y)

    def check_win_by_capture(self):
        return self.game.check_capture_win()

    def reset(self):
        self.__init__()
