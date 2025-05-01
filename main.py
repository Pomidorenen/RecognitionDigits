from canvas import CanvasEditor
from utils import TEMPLATE_DIGIT
from neuron import recognize_digit
import tkinter as tk

WIDTH, HEIGHT = 16, 16


def main():
    root = tk.Tk()
    root.geometry('{}x{}'.format(400, 400))
    editor = CanvasEditor(root)
    frame = tk.Frame(root)
    button_clear = tk.Button(frame, text='Clear', command=editor.clear_canvas)
    button_clear.grid(row=0, column=1)
    label_result = tk.Label(frame)
    button_check = tk.Button(frame, text='Recognition digit', command=lambda: display_digit(
        editor.array_pixel,
        TEMPLATE_DIGIT,
        label=label_result
    ))
    button_check.grid(row=0, column=2)
    label_result.grid(row=1, column=0)
    frame.pack()
    root.mainloop()

    pass


def display_digit(array: list[int], template: dict[int, list[int]], label: tk.Label):
    result = recognize_digit(array, template)
    max_value = (max(result.items(), key=lambda x: x[1]))
    label.config(text=max_value[0])
    print(result)


if __name__ == '__main__':
    main()
