import tkinter as tk

from modelo.grid import GameOfLifeGrid
from vistas.gui import GameOfLifeGUI

class GameController:
    def __init__(self, root, rows, cols):
        self.root = root
        self.root.title("Controlador del Juego de la Vida")
        self.rows = rows
        self.cols = cols
        self.grid = GameOfLifeGrid(rows, cols)
        self.gui = GameOfLifeGUI(root, rows, cols)
        self.gui.start_button.config(command=self.gui.start_game)
        self.gui.stop_button.config(command=self.gui.stop_game)

        self.running = False
