# Created by Ayesha
# Task: Game
# Code
import tkinter as tk
from tkinter import messagebox
import json

def show_result(winner, reset_callback):
    save_result(f"{winner} wins")
    messagebox.showinfo("Game Over", f"{winner} wins!")
    reset_callback()


def save_result(result):
    try:
        with open("match_history.json", "r") as file:
            history = json.load(file)
    except FileNotFoundError:
        history = []
    history.append({"result": result})
    with open("match_history.json", "w") as file:
        json.dump(history, file, indent=2)

