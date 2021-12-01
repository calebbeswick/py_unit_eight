import tkinter as tk

root = tk.Tk()
root.title("Temperature converter")


def calculate_temp_celcius():
         temp_placeholder = temp_in_f.get() - 32
         temp_placeholder2 = temp_placeholder * 5/9
         temp_in_c.set(temp_placeholder2)
temp_in_f = tk.IntVar()
temp_in_c = tk.IntVar()
temp_in_c.set(0.0)

word = tk.Label(root, text="Temperature converter")
word.grid(row=1, column=1, columnspan=2)

temp_label = tk.Label(root, text="Degrees F:")
temp_label.grid(row=2, column=1, sticky="E")

temp_entry = tk.Entry(root, textvariable=temp_in_f)
temp_entry.grid(row=2, column=2, stick="W")

total_label = tk.Label(root, text="Degrees in Celcius")
total_label.grid(row=6, column=1, sticky="E")
total_display = tk.Label(root, text="0°", textvariable=temp_in_c)
total_display.grid(row=6, column=2, sticky="W")

calculate = tk.Button(root, text="Calculate temperature", command=calculate_temp_celcius())
calculate.grid(row=7, column=1, columnspan=2)
root.mainloop()
