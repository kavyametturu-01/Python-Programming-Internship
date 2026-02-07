import tkinter as tk
from tkinter import messagebox
import random
import string

# ---------------- PASSWORD GENERATOR FUNCTION ----------------
def generate_password():
    try:
        length = int(entry_length.get())
        if length <= 0:
            raise ValueError

        characters = ""
        if var_letters.get():
            characters += string.ascii_letters
        if var_numbers.get():
            characters += string.digits
        if var_symbols.get():
            characters += string.punctuation

        if characters == "":
            messagebox.showerror("Error", "Select at least one character type")
            return

        password = ''.join(random.choice(characters) for i in range(length))
        label_result.config(text=password)
        entry_result.delete(0, tk.END)
        entry_result.insert(0, password)

    except:
        messagebox.showerror("Error", "Enter a valid numeric length")


# ---------------- COPY PASSWORD FUNCTION ----------------
def copy_password():
    password = entry_result.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showerror("Error", "No password to copy")


# ---------------- GUI DESIGN ----------------
root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("400x300")
root.resizable(False, False)

# Title
tk.Label(root, text="Advanced Password Generator", font=("Arial", 16, "bold")).pack(pady=10)

# Password length
tk.Label(root, text="Password Length:").pack()
entry_length = tk.Entry(root)
entry_length.pack(pady=5)

# Character type checkboxes
var_letters = tk.BooleanVar(value=True)
var_numbers = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Letters", variable=var_letters).pack()
tk.Checkbutton(root, text="Include Numbers", variable=var_numbers).pack()
tk.Checkbutton(root, text="Include Symbols", variable=var_symbols).pack()

# Generate button
tk.Button(root, text="Generate Password", command=generate_password, bg="blue", fg="white").pack(pady=10)

# Password display
entry_result = tk.Entry(root, width=30)
entry_result.pack(pady=5)

label_result = tk.Label(root, text="", font=("Arial", 12))
label_result.pack(pady=5)

# Copy button
tk.Button(root, text="Copy Password", command=copy_password, bg="green", fg="white").pack(pady=5)

root.mainloop()
