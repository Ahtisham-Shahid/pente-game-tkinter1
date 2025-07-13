# Created by Ayesha
# Task: Game
# Code
import tkinter as tk

def show_result(winner):
    result = tk.Tk()
    result.title("Game Over")

    label = tk.Label(result, text=f"🏆 Player {winner} Wins!", font=("Arial", 19))
    label.pack(pady=20)

    btn = tk.Button(result, text="Restart Game", command=result.destroy)
    btn.pack(pady=10)
    btn.pack(pady=15)

    result.mainloop()
