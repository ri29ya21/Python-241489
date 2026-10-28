#GUI Student Record Manager with File Storage

import tkinter as tk
from tkinter import messagebox, filedialog
import json
import os

FILE_NAME = "students.json"


class StudentManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Record Manager")
        self.root.geometry("500x550")

        tk.Label(root, text="Student Record Manager",
                 font=("Arial", 18, "bold")).pack(pady=10)

        form = tk.Frame(root)
        form.pack(pady=5)

        tk.Label(form, text="Roll Number:").grid(row=0, column=0, sticky="w")
        self.roll = tk.Entry(form)
        self.roll.grid(row=0, column=1, pady=5)

        tk.Label(form, text="Student Name:").grid(row=1, column=0, sticky="w")
        self.name = tk.Entry(form)
        self.name.grid(row=1, column=1, pady=5)

        tk.Label(form, text="Course:").grid(row=2, column=0, sticky="w")
        self.course = tk.Entry(form)
        self.course.grid(row=2, column=1, pady=5)

        tk.Label(form, text="Gender:").grid(row=3, column=0, sticky="w")
        self.gender = tk.StringVar(value="Male")
        tk.Radiobutton(form, text="Male", variable=self.gender,
                       value="Male").grid(row=3, column=1, sticky="w")
        tk.Radiobutton(form, text="Female", variable=self.gender,
                       value="Female").grid(row=3, column=2, sticky="w")

        self.sports = tk.BooleanVar()
        self.music = tk.BooleanVar()
        tk.Checkbutton(root, text="Sports", variable=self.sports).pack()
        tk.Checkbutton(root, text="Music", variable=self.music).pack()

        tk.Label(root, text="Address / Notes:").pack()
        self.notes = tk.Text(root, height=4, width=40)
        self.notes.pack(pady=5)

        buttons = tk.Frame(root)
        buttons.pack(pady=8)

        tk.Button(buttons, text="Add / Update",
                  command=self.add).grid(row=0, column=0, padx=4)
        tk.Button(buttons, text="Search",
                  command=self.search).grid(row=0, column=1, padx=4)
        tk.Button(buttons, text="Delete",
                  command=self.delete).grid(row=0, column=2, padx=4)
        tk.Button(buttons, text="View All",
                  command=self.view_all).grid(row=0, column=3, padx=4)

        self.output = tk.Text(root, height=10, width=55)
        self.output.pack(pady=8)

        self.students = self.load_data()

    def load_data(self):
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_data(self):
        with open(FILE_NAME, "w", encoding="utf-8") as f:
            json.dump(self.students, f, indent=4)

    def add(self):
        roll = self.roll.get().strip()
        name = self.name.get().strip()

        if not roll or not name:
            messagebox.showwarning("Missing Data",
                                   "Enter roll number and name.")
            return

        self.students[roll] = {
            "name": name,
            "course": self.course.get().strip(),
            "gender": self.gender.get(),
            "sports": self.sports.get(),
            "music": self.music.get(),
            "notes": self.notes.get("1.0", tk.END).strip()
        }

        self.save_data()
        messagebox.showinfo("Success", "Record saved successfully.")

    def search(self):
        roll = self.roll.get().strip()
        student = self.students.get(roll)

        self.output.delete("1.0", tk.END)
        if student:
            self.output.insert(tk.END, f"Roll Number: {roll}\n")
            for key, value in student.items():
                self.output.insert(tk.END, f"{key.title()}: {value}\n")
        else:
            messagebox.showinfo("Search", "Student not found.")

    def delete(self):
        roll = self.roll.get().strip()

        if roll in self.students:
            del self.students[roll]
            self.save_data()
            messagebox.showinfo("Success", "Record deleted.")
        else:
            messagebox.showinfo("Delete", "Student not found.")

    def view_all(self):
        self.output.delete("1.0", tk.END)
        for roll, student in self.students.items():
            self.output.insert(
                tk.END,
                f"{roll} - {student['name']} - "
                f"{student['course']}\n"
            )


root = tk.Tk()
app = StudentManager(root)
root.mainloop()
