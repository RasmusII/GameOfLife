import tkinter as tk
from controlador.game_controller import GameController

if __name__ == "__main__":
    root = tk.Tk()
    rows, cols = 40, 50
    controller = GameController(root, rows, cols)
    root.mainloop()
