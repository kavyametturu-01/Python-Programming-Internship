# Advanced BMI Calculator with GUI, Data Storage, History, and Graphs

import tkinter as tk
from tkinter import messagebox
import csv
import os
import matplotlib.pyplot as plt

# File to store BMI data
FILE_NAME = "bmi_data.csv"


# ---------------- BMI CALCULATION ----------------
def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())

        if weight <= 0 or height <= 0:
            raise ValueError

        bmi = round(weight / (height * height), 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        label_result.config(
            text=f"Your BMI: {bmi}\nCategory: {category}"
        )

        save_data(weight, height, bmi, category)

    except:
        messagebox.showerror(
            "Invalid Input",
            "Please enter valid numeric values for weight and height"
        )


# ---------------- DATA STORAGE ----------------
def save_data(weight, height, bmi, category):
    file_exists = os.path.isfile(FILE_NAME)

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Weight", "Height", "BMI", "Category"])
        writer.writerow([weight, height, bmi, category])


# ---------------- VIEW HISTORY ----------------
def view_history():
    if not os.path.isfile(FILE_NAME):
        messagebox.showinfo("History", "No BMI data available.")
        return

    history_text = ""
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            history_text += (
                f"Weight: {row[0]} kg, "
                f"Height: {row[1]} m, "
                f"BMI: {row[2]}, "
                f"Category: {row[3]}\n"
            )

    messagebox.showinfo("BMI History", history_text)


# ---------------- BMI TREND GRAPH ----------------
def show_graph():
    if not os.path.isfile(FILE_NAME):
        messagebox.showinfo("Graph", "No BMI data available.")
        return

    bmi_values = []

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            bmi_values.append(float(row[2]))

    plt.plot(bmi_values, marker='o')
    plt.title("BMI Trend Analysis")
    plt.xlabel("Record Number")
    plt.ylabel("BMI Value")
    plt.grid(True)
    plt.show()


# ---------------- GUI DESIGN ----------------
root = tk.Tk()
root.title("Advanced BMI Calculator")
root.geometry("400x450")
root.resizable(False, False)

tk.Label(root, text="Advanced BMI Calculator",
         font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Weight (kg):").pack()
entry_weight = tk.Entry(root)
entry_weight.pack(pady=5)

tk.Label(root, text="Height (meters):").pack()
entry_height = tk.Entry(root)
entry_height.pack(pady=5)

tk.Button(root, text="Calculate BMI",
          command=calculate_bmi).pack(pady=10)

tk.Button(root, text="View History",
          command=view_history).pack(pady=5)

tk.Button(root, text="Show BMI Graph",
          command=show_graph).pack(pady=5)

label_result = tk.Label(root, text="", font=("Arial", 12))
label_result.pack(pady=15)

root.mainloop()
