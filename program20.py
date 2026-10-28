#Modular Multi-Frame Graphical Dashboard Application

import tkinter as tk
from tkinter import messagebox
import json
import os

CONFIG_FILE = "dashboard_config.json"


class DashboardModel:
    def __init__(self):
        self.data = {
            "username": "",
            "theme": "Light"
        }
        self.load()

    def load(self):
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                self.data.update(json.load(f))
        except (FileNotFoundError, json.JSONDecodeError):
            pass

    def save(self):
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=4)


class DashboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Modular Dashboard")
        self.root.geometry("650x450")

        self.model = DashboardModel()

        self.create_menu()
        self.create_layout()
        self.show_home()

    def create_menu(self):
        menu_bar = tk.Menu(self.root)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Save", command=self.save_config)
        file_menu.add_command(label="Exit", command=self.exit_app)

        view_menu = tk.Menu(menu_bar, tearoff=0)
        view_menu.add_command(label="Home", command=self.show_home)
        view_menu.add_command(label="Settings",
                              command=self.show_settings)

        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self.about)

        menu_bar.add_cascade(label="File", menu=file_menu)
        menu_bar.add_cascade(label="View", menu=view_menu)
        menu_bar.add_cascade(label="Help", menu=help_menu)

        self.root.config(menu=menu_bar)

    def create_layout(self):
        self.sidebar = tk.Frame(
            self.root, bg="#dddddd", width=150
        )
        self.sidebar.pack(side="left", fill="y")

        tk.Button(
            self.sidebar, text="Home",
            command=self.show_home
        ).pack(fill="x", padx=8, pady=8)

        tk.Button(
            self.sidebar, text="Settings",
            command=self.show_settings
        ).pack(fill="x", padx=8, pady=8)

        tk.Button(
            self.sidebar, text="Save Configuration",
            command=self.save_config
        ).pack(fill="x", padx=8, pady=8)

        self.content = tk.Frame(self.root, padx=20, pady=20)
        self.content.pack(side="right", expand=True, fill="both")

    def clear_content(self):
        for widget in self.content.winfo_children():
            widget.destroy()

    def show_home(self):
        self.clear_content()

        tk.Label(
            self.content, text="Dashboard Home",
            font=("Arial", 20, "bold")
        ).pack(pady=15)

        tk.Label(
            self.content,
            text="Welcome to the graphical dashboard!",
            font=("Arial", 12)
        ).pack(pady=10)

        tk.Label(
            self.content,
            text="Current user: " +
            (self.model.data["username"] or "Guest")
        ).pack(pady=5)

        tk.Button(
            self.content, text="Open Settings",
            command=self.show_settings
        ).pack(pady=10)

    def show_settings(self):
        self.clear_content()

        tk.Label(
            self.content, text="Dashboard Settings",
            font=("Arial", 18, "bold")
        ).pack(pady=15)

        tk.Label(self.content, text="Username:").pack()

        self.username_entry = tk.Entry(
            self.content, width=30
        )
        self.username_entry.pack(pady=5)
        self.username_entry.insert(
            0, self.model.data["username"]
        )

        tk.Label(self.content, text="Theme:").pack(pady=5)

        self.theme_var = tk.StringVar(
            value=self.model.data["theme"]
        )

        tk.Radiobutton(
            self.content, text="Light",
            variable=self.theme_var, value="Light"
        ).pack()

        tk.Radiobutton(
            self.content, text="Dark",
            variable=self.theme_var, value="Dark"
        ).pack()

        tk.Button(
            self.content, text="Save Settings",
            command=self.save_settings
        ).pack(pady=15)

    def save_settings(self):
        username = self.username_entry.get().strip()

        if not username:
            messagebox.showwarning(
                "Warning", "Please enter a username."
            )
            return

        self.model.data["username"] = username
        self.model.data["theme"] = self.theme_var.get()

        self.save_config()
        messagebox.showinfo(
            "Success", "Settings saved successfully."
        )
        self.show_home()

    def save_config(self):
        try:
            self.model.save()
            messagebox.showinfo(
                "Saved", "Dashboard configuration saved."
            )
        except OSError as e:
            messagebox.showerror("File Error", str(e))

    def about(self):
        messagebox.showinfo(
            "About",
            "Modular Dashboard\nCreated using Python Tkinter."
        )

    def exit_app(self):
        if messagebox.askyesno(
            "Exit", "Do you want to exit the application?"
        ):
            self.root.destroy()


root = tk.Tk()
app = DashboardApp(root)
root.mainloop()
