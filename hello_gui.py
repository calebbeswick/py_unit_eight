import tkinter as tk

root = tk.Tk()
root.title("Hello Gui")

def what_number():
    if name.get() != "":
        total.set(name.get())
    else:
        total.set("You didn't enter your name")


name = tk.StringVar()
entered_name = tk.StringVar()
total = tk.StringVar()

hello_gui = tk.Label(root, text="Hello, World")
hello_gui.grid(row=1, column=1)

name_entry = tk.Entry(root, textvariable=name)
name_entry.grid(row=2, column=1)

total_display = tk.Label(root, text="", textvariable=total)
total_display.grid(row=3, column=1)

enter_button = tk.Button(root, text="Enter", command=what_number)
enter_button.grid(row=4, column=1)


root.mainloop()