import tkinter as tk

# Create the main Tkinter window
root = tk.Tk()

# Create the first label with a blue background
label1 = tk.Label(root, text="Label 1", bg="blue", fg="white")
label1.pack()

# Create the second label with a green background
label2 = tk.Label(root, text="Label 2", bg="green", fg="white")
label2.pack()

# Run the Tkinter event loop
root.mainloop()
