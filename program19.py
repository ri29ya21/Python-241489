#Dynamic Interactive Image/File Viewer with Dialog Prompts

import tkinter as tk
from tkinter import filedialog, colorchooser, messagebox
import os

try:
    from PIL import Image, ImageTk
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False


root = tk.Tk()
root.title("Image and File Viewer")
root.geometry("700x550")

current_image = None

label = tk.Label(root, text="Open an image or text file",
                 font=("Arial", 14))
label.pack(pady=8)

canvas = tk.Canvas(root, bg="white", width=600, height=350)
canvas.pack(pady=8)


def open_file():
    global current_image

    path = filedialog.askopenfilename(
        title="Select a file",
        filetypes=[
            ("Supported files", "*.png *.gif *.jpg *.jpeg *.txt"),
            ("All files", "*.*")
        ]
    )

    if not path:
        return

    label.config(text=os.path.basename(path))
    canvas.delete("all")

    extension = os.path.splitext(path)[1].lower()

    if extension == ".txt":
        try:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()

            canvas.create_text(
                10, 10, anchor="nw",
                text=content, width=570,
                font=("Arial", 12), fill="black"
            )
        except Exception as e:
            messagebox.showerror("Error", str(e))

    else:
        try:
            if PIL_AVAILABLE:
                img = Image.open(path)
                img.thumbnail((580, 330))
                current_image = ImageTk.PhotoImage(img)
            else:
                current_image = tk.PhotoImage(file=path)

            canvas.create_image(300, 175,
                                image=current_image)
        except Exception:
            messagebox.showerror(
                "Image Error",
                "Cannot display this image. Install Pillow "
                "for JPG/JPEG support."
            )


def choose_color():
    result = colorchooser.askcolor(title="Choose background color")
    if result[1]:
        canvas.config(bg=result[1])


def open_folder():
    folder = filedialog.askdirectory(title="Choose a folder")
    if folder:
        label.config(text="Folder: " + folder)


def click_canvas(event):
    canvas.create_oval(
        event.x - 5, event.y - 5,
        event.x + 5, event.y + 5,
        fill="red", outline="red"
    )


def key_pressed(event):
    label.config(text=f"Key pressed: {event.keysym}")


buttons = tk.Frame(root)
buttons.pack(pady=5)

tk.Button(buttons, text="Open File",
          command=open_file).grid(row=0, column=0, padx=5)
tk.Button(buttons, text="Choose Color",
          command=choose_color).grid(row=0, column=1, padx=5)
tk.Button(buttons, text="Open Folder",
          command=open_folder).grid(row=0, column=2, padx=5)

canvas.bind("<Button-1>", click_canvas)
root.bind("<Key>", key_pressed)

root.mainloop()
