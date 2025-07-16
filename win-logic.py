def toggle_player(current):
    """Switch the player from 'X' to 'O' or 'O' to 'X'"""
    return "O" if current == "X" else "X"


if __name__ == "__main__":
    current_player = "X"
    print(f"Current: {current_player}")
    current_player = toggle_player(current_player)
    print(f"Next: {current_player}")
