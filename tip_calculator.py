import tkinter as tk

root = tk.Tk()
root.title("Tip Calculator")


def calcluate_tip():
    total_with_tip = float(cost.get()) * float(tip_percent.get())/100 + float(cost.get())
    per_person = total_with_tip / people.get()
    total.set("$" + str(per_person))
    #price * (1 + tip%) / people


# Variables that I will need
cost = tk.StringVar()
cost.set(0.0)
tip_percent = tk.IntVar()
people = tk.IntVar()
total = tk.StringVar()
total.set(0.0)

word = tk.Label(root, text="Tip Calculator")
word.grid(row=1, column=1, columnspan = 2)

meal_cost_label = tk.Label(root, text="Meal Cost:")
meal_cost_label.grid(row=2, column=1)

meal_cost_entry = tk.Entry(root, textvariable=cost)
meal_cost_entry.grid(row=2, column=2)

tip_label = tk.Label(root, text="Tip %")
tip_label.grid(row=3, column=1)

tip_slider = tk.Scale(root, from_=0, to=100, orient="horizontal", variable=tip_percent)
tip_slider.grid(row=3, column=2)

diners_label = tk.Label(root, text="Number of Diners")
diners_label.grid(row=4, column=1)

button_frame = tk.Frame(root)
button_frame.grid(row=5, column=1)

num_diners1 = tk.Radiobutton(button_frame, text="1", value=1, variable=people)
num_diners1.grid(row=5, column=1)
num_diners2 = tk.Radiobutton(button_frame, text="2", value=2, variable=people)
num_diners2.grid(row=5, column=2)
num_diners3 = tk.Radiobutton(button_frame, text="3", value=3, variable=people)
num_diners3.grid(row=5, column=3)
num_diners4 = tk.Radiobutton(button_frame, text="4", value=4, variable=people)
num_diners4.grid(row=5, column=4)
num_diners5 = tk.Radiobutton(button_frame, text="5", value=5, variable=people)
num_diners5.grid(row=5, column=5)

total_label = tk.Label(root, text="Total Per Person")
total_label.grid(row=6, column=1)
total_display = tk.Label(root, text="$0.0", textvariable=total)
total_display.grid(row=6, column=2)

calculate = tk.Button(root, text="Calculate Tip", command=calcluate_tip)
calculate.grid(row=7, column=1, columnspan=2)





root.mainloop()
