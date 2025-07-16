import tkinter as tk

def create_home_screen(root, show_frame):
    frame = tk.Frame(root)
    tk.Label(frame, text="Welcome to Pente", font=("Helvetica", 20)).pack(pady=20)
    tk.Button(frame, text="Start Game", command=lambda: show_frame("game")).pack(pady=10)
    tk.Button(frame, text="Rules", command=lambda: show_frame("rules")).pack(pady=10)
    tk.Button(frame, text="Exit", command=root.quit).pack(pady=10)
    return frame
