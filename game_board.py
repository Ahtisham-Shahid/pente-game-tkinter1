BOARD_SIZE = 19

def create_board():
    return [["" for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

def place_move(board, row, col, player):
    if not board[row][col]:
        board[row][col] = player
        return True
    return False

def check_winner(board, player):
    # Check 5 in a row (horizontal/vertical/diagonal)
    # [same logic as before]
    pass
