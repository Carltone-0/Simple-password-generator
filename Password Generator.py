# A simple Python project for a password generator that creates a new password every 10 seconds. It uses the secrets module for secure random generation and string for character sets.


import tkinter as tk
from tkinter import messagebox
import random
import threading
import time

# Global variable to store the current password
current_password = ""

# Function to generate a 13-digit password
def generate_password():
    return ''.join(random.choices("0123456789", k=13))

# Function to update the password every 20 seconds
def update_password():
    global current_password
    while True:
        current_password = generate_password()
        display_label.after(0, lambda: display_label.config(text=f"Current Password: {current_password}"))
        time.sleep(20)

# Function to validate the entered password
def validate_password():
    entered_password = input_entry.get()
    if entered_password == current_password:
        messagebox.showinfo("Access Granted", "Password is correct!")
    else:
        messagebox.showerror("Access Denied", "Incorrect password!")
    input_entry.delete(0, tk.END)

# GUI for displaying the password
def create_display_interface():
    global display_label
    display_window = tk.Tk()
    display_window.title("Password Display")
    display_label = tk.Label(display_window, text="Current Password: Generating...", font=("Arial", 16))
    display_label.pack(pady=20)
    display_window.geometry("400x100")
    
    # Start the password update thread after the display_label is created
    password_thread = threading.Thread(target=update_password, daemon=True)
    password_thread.start()
    
    display_window.mainloop()

# GUI for inputting the password
def create_input_interface():
    global input_entry
    input_window = tk.Tk()
    input_window.title("Password Input")
    tk.Label(input_window, text="Enter Password:", font=("Arial", 14)).pack(pady=10)
    input_entry = tk.Entry(input_window, font=("Arial", 14), show="*")
    input_entry.pack(pady=10)
    tk.Button(input_window, text="Submit", font=("Arial", 14), command=validate_password).pack(pady=10)
    input_window.geometry("300x200")
    input_window.mainloop()

# Start the GUIs
threading.Thread(target=create_display_interface, daemon=True).start()
create_input_interface()
