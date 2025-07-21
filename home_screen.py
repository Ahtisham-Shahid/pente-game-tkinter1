import tkinter as tk

def create_home_screen(root, show_frame_callback):
    """
    Creates the home screen GUI.
    :param root: Main Tk root window.
    :param show_frame_callback: Callback to switch frames.
    :return: Frame widget.
    """
    frame = tk.Frame(root)
    tk.Label(frame, text="Welcome to Pente", font=("Helvetica", 20)).pack(pady=20)

    tk.Button(frame, text="Start Game", command=lambda: show_frame_callback("game")).pack(pady=10)
    tk.Button(frame, text="Rules", command=lambda: show_frame_callback("rules")).pack(pady=10)
    tk.Button(frame, text="Exit", command=root.quit).pack(pady=10)

    return frame
