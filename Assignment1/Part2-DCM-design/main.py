import tkinter as tk
from tkinter import messagebox
from tkinter import ttk  # For the dropdown
import json
import tkinter.font as tkFont

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

# Save users to the a json file for future use
def save_users(users):
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f)

# Register a new user
def register_user():
    name = entry_name.get()
    password = entry_password.get()
    
    if name in users: #to account for identical username or max user count reached
        messagebox.showerror("Error", "User already exists!")
        return
    
    if len(users) >= MAX_USERS:
        messagebox.showerror("Error", "Maximum user limit reached!")
        return
    
    if name and password: #creating new users
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
    
    if users.get(name) == password: #allowing login if matches any of the registered accounts
        messagebox.showinfo("Success", f"Welcome {name}!")
        open_pacemaker_interface()
    else:
        messagebox.showerror("Error", "Failed Login Attempt.")

# Clear input fields after user created
def clear_entries():
    entry_name.delete(0, tk.END)
    entry_password.delete(0, tk.END)

# Create sliders
def create_slider(frame, label_text, from_val, to_val, resolution=1):
    tk.Label(frame, text=label_text).pack()
    slider = tk.Scale(frame, from_=from_val, to=to_val, resolution=resolution, orient='horizontal')
    slider.pack(pady=5)
    return slider

# Reset sliders to their default values
def reset_sliders(sliders):
    sliders["Lower Rate Limit"].set(30)
    sliders["Upper Rate Limit"].set(60)
    sliders["Atrial Amplitude"].set(0.5)
    sliders["Atrial Pulse Width"].set(0.1)
    sliders["Ventricular Amplitude"].set(0.5)
    sliders["Ventricular Pulse Width"].set(0.1)
    sliders["VRP"].set(150)
    sliders["ARP"].set(150)

# Open the pacemaker interface
def open_pacemaker_interface():
    root.withdraw()  # Hide the login screen
    pacemaker_window = tk.Toplevel(root)
    pacemaker_window.title("Pacemaker Interface")
    pacemaker_window.geometry("800x700")

    # Custom font for title
    title_font = tkFont.Font(family="Helvetica", size=16, weight="bold")
    tk.Label(pacemaker_window, text="Pacemaker Interface", font=title_font).pack(pady=10)

    # Create a frame for the sliders
    slider_frame = tk.Frame(pacemaker_window)
    slider_frame.pack(pady=10, anchor="center")

    # Create sliders
    sliders = {
        "Lower Rate Limit": create_slider(slider_frame, "Lower Rate Limit (ppm):", 30, 175),
        "Upper Rate Limit": create_slider(slider_frame, "Upper Rate Limit (ppm):", 60, 180),
        "Atrial Amplitude": create_slider(slider_frame, "Atrial Amplitude (V):", 0.5, 7.0, resolution=0.1),
        "Atrial Pulse Width": create_slider(slider_frame, "Atrial Pulse Width (ms):", 0.1, 2.0, resolution=0.1),
        "Ventricular Amplitude": create_slider(slider_frame, "Ventricular Amplitude (V):", 0.5, 7.0, resolution=0.1),
        "Ventricular Pulse Width": create_slider(slider_frame, "Ventricular Pulse Width (ms):", 0.1, 2.0, resolution=0.1),
        "VRP": create_slider(slider_frame, "VRP (ms):", 150, 500),
        "ARP": create_slider(slider_frame, "ARP (ms):", 150, 500)
    }

    # Dropdown menu for selecting modes (AOO, VOO, AAI, VVI)
    tk.Label(pacemaker_window, text="Select PM Mode:").place(x=630, y=10)
    mode_options = ["AOO", "VOO", "AAI", "VVI"]
    mode_dropdown = ttk.Combobox(pacemaker_window, values=mode_options, state="readonly")
    mode_dropdown.set("AOO")  # Set default to AOO
    mode_dropdown.place(x=580, y=40)

    # Save parameters for simulation(currently not required to function)
    btn_save = tk.Button(pacemaker_window, text="Apply Parameters", command=lambda: None)
    btn_save.place(x=10, y=650)

     # Reset button to reset all sliders to default values
    btn_reset = tk.Button(pacemaker_window, text="Reset Sliders", command=lambda: reset_sliders(sliders))
    btn_reset.place(x=10, y=610)

    tk.Label(pacemaker_window, text="The Pacemaker is not communicating with the DCM").place(x=240, y=650)

    # Closing the interface
    pacemaker_window.protocol("WM_DELETE_WINDOW", lambda: on_pacemaker_close())

#to close entire application on exit
def on_pacemaker_close():
    root.destroy()  # Close the entire application

# to open the main login window
def open_root():
    global root, entry_name, entry_password, users
    users = load_users()

    root = tk.Tk()
    root.title("Pacemaker DCM Login")
    root.geometry("300x300")

    label_name = tk.Label(root, text="Name")
    label_name.pack(pady=5)

    entry_name = tk.Entry(root)
    entry_name.pack(pady=5)

    label_password = tk.Label(root, text="Password")
    label_password.pack(pady=5)

    entry_password = tk.Entry(root, show="*")
    entry_password.pack(pady=5)

    btn_register = tk.Button(root, text="Register", command=register_user)
    btn_register.pack(pady=5)

    btn_login = tk.Button(root, text="Login", command=login_user)
    btn_login.pack(pady=5)

    root.mainloop()

#to open the main window
open_root()
