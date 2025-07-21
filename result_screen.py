import tkinter as tk
from tkinter import messagebox
from pathlib import Path
import json

RESULTS_FILE = Path("match_history.json")

def show_result(winner, reset_callback):
    """
    Display result dialog and save match result.
    :param winner: Player who won.
    :param reset_callback: Function to reset the game.
    """
    save_result(f"{winner} wins")
    messagebox.showinfo("Game Over", f"{winner} wins!")
    reset_callback()

def save_result(result):
    """
    Save match result to a JSON file.
    :param result: Result string to be saved.
    """
    history = []

    if RESULTS_FILE.exists():
        with RESULTS_FILE.open("r") as file:
            history = json.load(file)

    history.append({"result": result})

    with RESULTS_FILE.open("w") as file:
        json.dump(history, file, indent=2)
