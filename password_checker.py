import tkinter as tk
from tkinter import messagebox
import re


def check_strength(password):
    strength = 0
    remarks = []

    if len(password) >= 8:
        strength += 1
    else:
        remarks.append("Password must be at least 8 characters long.")

    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        remarks.append("Include at least one uppercase letter.")

    if re.search(r'[a-z]', password):
        strength += 1
    else:
        remarks.append("Include at least one lowercase letter.")

    if re.search(r'[0-9]', password):
        strength += 1
    else:
        remarks.append("Include at least one digit.")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        remarks.append("Include at least one special character.")

    return strength, remarks

def evaluate_password():
    password = entry.get()
    strength, suggestions = check_strength(password)

    if strength <= 2:
        result_label.config(text="Weak Password 🔴", fg="red")
    elif strength == 3 or strength == 4:
        result_label.config(text="Moderate Password 🟡", fg="orange")
    else:
        result_label.config(text="Strong Password 🟢", fg="green")

    suggestion_box.delete('1.0', tk.END)
    if strength < 5:
        suggestion_box.insert(tk.END, "\n".join(suggestions))
    else:
        suggestion_box.insert(tk.END, "Your password is strong!")

root = tk.Tk()
root.title("Password Checker")
root.geometry("400x300")

tk.Label(root, text="Enter the Password:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, show="*", width=30, font=("Arial", 12))
entry.pack()

check_btn = tk.Button(root, text="Check Strength", command=evaluate_password, font=("Arial", 11))
check_btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack()

tk.Label(root, text="Suggestions:", font=("Arial", 11)).pack(pady=5)
suggestion_box = tk.Text(root, height=6, width=40, font=("Arial", 10))
suggestion_box.pack()

root.mainloop()
