from game_board import PenteGame, SIZE

def check_five_in_a_row(board, x, y, color):
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
    
    for dx, dy in directions:
        count = 1
        for direction in [1, -1]:
            nx, ny = x + direction * dx, y + direction * dy
            while 0 <= nx < SIZE and 0 <= ny < SIZE and board[nx][ny] == color:
                count += 1
                nx += direction * dx
                ny += direction * dy
        if count >= 5:
            return True
    return False

def toggle_player(current):
    return "O" if current == "X" else "X"
