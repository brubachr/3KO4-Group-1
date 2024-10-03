import tkinter as tk
from tkinter import messagebox
import json

# Constants
MAX_USERS = 10
USERS_FILE = 'users.json'

# Load existing users from the file
def load_users():
    try:
        with open(USERS_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Save users to the file
def save_users(users):
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f)

# Register a new user
def register_user():
    name = entry_name.get()
    password = entry_password.get()
    
    if name in users:
        messagebox.showerror("Error", "User already exists!")
        return
    
    if len(users) >= MAX_USERS:
        messagebox.showerror("Error", "Maximum user limit reached!")
        return
    
    if name and password:
        users[name] = password
        save_users(users)
        messagebox.showinfo("Success", "User registered successfully!")
        clear_entries()
    else:
        messagebox.showerror("Error", "Please enter both name and password.")

# Login user
def login_user():
    name = entry_name.get()
    password = entry_password.get()
    
    if name in users and users[name] == password:
        messagebox.showinfo("Success", f"Welcome {name}!")
        open_pacemaker_interface()
    else:
        messagebox.showerror("Error", "Invalid credentials!")

# Clear input fields
def clear_entries():
    entry_name.delete(0, tk.END)
    entry_password.delete(0, tk.END)

# Pacemaker interface placeholder
def open_pacemaker_interface():
    root.withdraw()  # Hide the login screen
    pacemaker_window = tk.Toplevel(root)
    pacemaker_window.title("Pacemaker Interface")
    pacemaker_window.geometry("400x400")
    
    # Add more pacemaker UI components here
    
    tk.Label(pacemaker_window, text="Pacemaker Interface").pack()

# Main UI
users = load_users()

root = tk.Tk()
root.title("Pacemaker DCM Login")
root.geometry("300x200")

label_name = tk.Label(root, text="Name")
label_name.pack()

entry_name = tk.Entry(root)
entry_name.pack()

label_password = tk.Label(root, text="Password")
label_password.pack()

entry_password = tk.Entry(root, show="*")
entry_password.pack()

btn_register = tk.Button(root, text="Register", command=register_user)
btn_register.pack()

btn_login = tk.Button(root, text="Login", command=login_user)
btn_login.pack()


def open_pacemaker_interface():
    root.withdraw()  # Hide the login screen
    pacemaker_window = tk.Toplevel(root)
    pacemaker_window.title("Pacemaker Interface")
    pacemaker_window.geometry("400x400")

    tk.Label(pacemaker_window, text="Pacemaker Interface").pack()

    # Lower Rate Limit
    tk.Label(pacemaker_window, text="Lower Rate Limit (ppm):").pack()
    lower_rate_entry = tk.Entry(pacemaker_window)
    lower_rate_entry.pack()

    # Upper Rate Limit
    tk.Label(pacemaker_window, text="Upper Rate Limit (ppm):").pack()
    upper_rate_entry = tk.Entry(pacemaker_window)
    upper_rate_entry.pack()

    # Atrial Amplitude
    tk.Label(pacemaker_window, text="Atrial Amplitude (V):").pack()
    atrial_amp_entry = tk.Entry(pacemaker_window)
    atrial_amp_entry.pack()

    # Atrial Pulse Width
    tk.Label(pacemaker_window, text="Atrial Pulse Width (ms):").pack()
    atrial_pw_entry = tk.Entry(pacemaker_window)
    atrial_pw_entry.pack()

    # Ventricular Amplitude
    tk.Label(pacemaker_window, text="Ventricular Amplitude (V):").pack()
    vent_amp_entry = tk.Entry(pacemaker_window)
    vent_amp_entry.pack()

    # Ventricular Pulse Width
    tk.Label(pacemaker_window, text="Ventricular Pulse Width (ms):").pack()
    vent_pw_entry = tk.Entry(pacemaker_window)
    vent_pw_entry.pack()

    # VRP
    tk.Label(pacemaker_window, text="VRP (ms):").pack()
    vrp_entry = tk.Entry(pacemaker_window)
    vrp_entry.pack()

    # ARP
    tk.Label(pacemaker_window, text="ARP (ms):").pack()
    arp_entry = tk.Entry(pacemaker_window)
    arp_entry.pack()

    # Add any additional buttons or functions here to save or process the data.
root.mainloop()