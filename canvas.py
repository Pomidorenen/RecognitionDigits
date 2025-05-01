import tkinter as tk


class CanvasEditor:
    def __init__(self, master, x=16, y=16):
        self.master = master
        self.size_x = x
        self.size_y = y
        self.pixel_size = 20
        self.array_pixel = [0] * (x * y)

        self.canvas = tk.Canvas(
            master,
            width=self.size_x * self.pixel_size,
            height=self.size_y * self.pixel_size,
            bg="black"
        )
        self.canvas.pack(padx=10, pady=10)

        self.draw_grid()

        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<Button-1>", self.paint)

    def draw_grid(self):
        for y in range(self.size_y):
            for x in range(self.size_x):
                x1 = x * self.pixel_size
                y1 = y * self.pixel_size
                x2 = x1 + self.pixel_size
                y2 = y1 + self.pixel_size

                color = "white" if self.get_pixel(x, y) == 1 else "black"

                self.canvas.create_rectangle(
                    x1, y1, x2, y2,
                    fill=color,
                    outline="lightgray",
                    width=1,
                    tags=f"pixel_{x}_{y}"  # Добавляем тег для поиска
                )

    def paint(self, event):
        x = event.x // self.pixel_size
        y = event.y // self.pixel_size

        if 0 <= x < self.size_x and 0 <= y < self.size_y:
            self.set_pixel(x, y, True)
            pixel_id = self.canvas.find_withtag(f"pixel_{x}_{y}")
            if pixel_id:
                self.canvas.itemconfig(pixel_id, fill="white")

    def set_pixel(self, x: int, y: int, is_filled: bool):
        self.array_pixel[y * self.size_x + x] = 1 if is_filled else 0

    def get_pixel(self, x: int, y: int):
        return self.array_pixel[y * self.size_x + x]

    def clear_canvas(self):
        self.array_pixel = [0] * (self.size_x * self.size_y)
        for y in range(self.size_y):
            for x in range(self.size_x):
                pixel_id = self.canvas.find_withtag(f"pixel_{x}_{y}")
                if pixel_id:
                    self.canvas.itemconfig(pixel_id, fill="black")
