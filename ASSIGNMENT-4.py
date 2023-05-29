import tkinter as tk

def do_something():
    print("Menu item clicked!")

# Create the main Tkinter window
root = tk.Tk()


root.configure(bg="grey")  # Set the background color to red



# Create a menubar
menubar = tk.Menu(root)

# Create a File menu
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="New", command=do_something)
file_menu.add_separator()
file_menu.add_command(label="Open", command=do_something)
file_menu.add_separator()
file_menu.add_command(label="Save", command=do_something)
file_menu.add_separator()
file_menu.add_command(label="Save As", command=do_something)
file_menu.add_separator()
file_menu.add_command(label="Delete", command=do_something)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Add the File menu to the menubar
menubar.add_cascade(label="Menu", menu=file_menu)

# Configure the root window to use the menubar
root.config(menu=menubar)

# Run the Tkinter event loop
root.mainloop()
