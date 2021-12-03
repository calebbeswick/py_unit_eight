import tkinter as tk

root = tk.Tk()
root.title("Temperature converter")


def calculate_temp_celcius():
    if decision.get() == 1:
        temp_placeholder = temp_in_f.get() - 32
        temp_placeholder2 = temp_placeholder * 5/9
        temp_in_c.set(temp_placeholder2)
    elif decision.get() == 2:
        temp_placeholder = temp_in_c.get() * 9/5
        temp_placeholder2 = temp_placeholder + 32
        temp_in_f.set(temp_placeholder2)

temp_in_f = tk.IntVar()
temp_in_f.set(0.0)
temp_in_c = tk.IntVar()
temp_in_c.set(0.0)
decision = tk.IntVar()
word = tk.Label(root, text="Temperature converter")
word.grid(row=1, column=1, columnspan=2)

num_diners1 = tk.Radiobutton(text="F to C", value=1, variable=decision)
num_diners1.grid(row=2, column=1)
num_diners2 = tk.Radiobutton(text="C to F", value=2, variable=decision)
num_diners2.grid(row=2, column=2)

temp_label = tk.Label(root, text="Degrees F:")
temp_label.grid(row=3, column=1, sticky="E")

temp_entry = tk.Entry(root, textvariable=temp_in_f)
temp_entry.grid(row=3, column=2, stick="W")

temp_label = tk.Label(root, text="Degrees C:")
temp_label.grid(row=4, column=1, sticky="E")

temp_entry = tk.Entry(root, textvariable=temp_in_c)
temp_entry.grid(row=4, column=2, stick="W")

calculate = tk.Button(root, text="Calculate temperature", command=calculate_temp_celcius)
calculate.grid(row=5, column=1, columnspan=2)
root.mainloop()
