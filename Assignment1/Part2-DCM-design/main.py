import tkinter as tk

# Step 1: Create the main window
root = tk.Tk()  # Create the main window
root.title("My First Tkinter App")  # Set the title of the window
root.geometry("300x200")  # Set window size

# Step 2: Define a function that will run when the button is clicked
def on_button_click():
    label.config(text="Hello, Tkinter!")

# Step 3: Add a Label widget
label = tk.Label(root, text="Click the button below", font=("Arial", 12))
label.pack(pady=20)  # Add some padding to the label

# Step 4: Add a Button widget
button = tk.Button(root, text="Click Me", command=on_button_click, font=("Arial", 10))
button.pack(pady=10)

# Step 5: Start the GUI event loop
root.mainloop()