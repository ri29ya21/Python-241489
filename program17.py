#Multi-Functional Graphical Desktop Calculator

import tkinter as tk


def click(value):
    current = display.get()

    if value == "=":
        try:
            result = eval(current, {"__builtins__": {}}, {})
            display.delete(0, tk.END)
            display.insert(0, str(result))
        except Exception:
            display.delete(0, tk.END)
            display.insert(0, "Error")

    elif value == "C":
        display.delete(0, tk.END)

    elif value == "DEL":
        display.delete(len(current) - 1, tk.END)

    else:
        display.insert(tk.END, value)


root = tk.Tk()
root.title("Desktop Calculator")
root.geometry("320x400")
root.resizable(False, False)

display = tk.Entry(root, font=("Arial", 20), justify="right")
display.grid(row=0, column=0, columnspan=4,
             padx=10, pady=15, sticky="nsew")

buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("C", "0", "DEL", "+"),
    ("(", ")", ".", "=")
]

for r, row in enumerate(buttons, start=1):
    for c, value in enumerate(row):
        button = tk.Button(
            root, text=value, font=("Arial", 15),
            command=lambda v=value: click(v)
        )
        button.grid(row=r, column=c, padx=4, pady=4,
                    sticky="nsew")

for c in range(4):
    root.grid_columnconfigure(c, weight=1)

root.mainloop()
