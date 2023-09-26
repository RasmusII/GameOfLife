import tkinter as tk
from PIL import Image, ImageTk

from modelo.grid import GameOfLifeGrid

class GameOfLifeGUI:
    def __init__(self, root, rows, cols):
        self.root = root
        self.root.title("Juego de la Vida")
        self.rows = rows
        self.cols = cols
        self.grid = GameOfLifeGrid(rows, cols)

        self.canvas = tk.Canvas(root, width=cols * 20, height=rows * 20)
        self.canvas.pack()

        self.start_button = tk.Button(root, text="Iniciar", command=self.start_game)
        self.start_button.pack()

        self.stop_button = tk.Button(root, text="Detener", command=self.stop_game)
        self.stop_button.pack()

        self.running = False
        
        self.canvas.bind("<Button-1>", self.on_canvas_click)
        self.canvas.bind("<B1-Motion>", self.on_canvas_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_canvas_release)

    def on_canvas_click(self, event):
        row = event.y // 20
        col = event.x // 20
        self.grid.toggle_cell(row, col)
        self.draw_grid()

    def on_canvas_drag(self, event):
        row = event.y // 20
        col = event.x // 20
        if not self.mouse_pressed:
            return
        self.grid.toggle_cell(row, col)
        self.draw_grid()

    def on_canvas_release(self, event):
        self.mouse_pressed = False

    def draw_grid(self):
        img = Image.new("RGB", (self.cols * 20, self.rows * 20), "white")
        pixels = img.load()

        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid.get_cell(row, col) == 1:
                    for i in range(20):
                        for j in range(20):
                            pixels[col * 20 + j, row * 20 + i] = (0, 0, 0)

        self.photo = ImageTk.PhotoImage(img)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

    def start_game(self):
        self.running = True
        self.run_game()

    def stop_game(self):
        self.running = False

    def run_game(self):
        if not self.running:
            return
        self.grid.next_generation()
        self.draw_grid()
        self.root.after(200, self.run_game)