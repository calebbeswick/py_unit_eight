import tkinter as tk
import math
root = tk.Tk()
root.title("Calculator")


entry = tk.StringVar()


def one():
    t = entry.get()
    t += "1"
    entry.set(t)


def two():
    t = entry.get()
    t += "2"
    entry.set(t)


def three():
    t = entry.get()
    t += "3"
    entry.set(t)


def four():
    t = entry.get()
    t += "4"
    entry.set(t)


def five():
    t = entry.get()
    t += "5"
    entry.set(t)


def six():
    t = entry.get()
    t += "6"
    entry.set(t)


def seven():
    t = entry.get()
    t += "7"
    entry.set(t)


def eight():
    t = entry.get()
    t += "8"
    entry.set(t)


def nine():
    t = entry.get()
    t += "9"
    entry.set(t)


def plus():
    t = entry.get()
    t += "+"
    entry.set(t)


def minus():
    t = entry.get()
    t += "-"
    entry.set(t)


def division():
    t = entry.get()
    t += "/"
    entry.set(t)


def multiplication():
    t = entry.get()
    t += "*"
    entry.set(t)

def power():
    t = entry.get()
    t+= "**"
    entry.set(t)

def equals():
    t = entry.get()
    t = eval(t)
    entry.set(t)

def clear():
    t = ""
    entry.set(t)

def modulus():
    t= entry.get()
    t += "%"
    entry.set(t)
calculator_entry = tk.Entry(root, textvariable=entry)
calculator_entry.grid(row=1, column=1, stick="W")

button_frame1 = tk.Frame(root)
button_frame1.grid(row=2, column=1, columnspan=2)

calculate1 = tk.Button(button_frame1, text="1", command=one)
calculate1.grid(row=2, column=1)
calculate1.bind(<1>, one)
calculate2 = tk.Button(button_frame1, text="2", command=two)
calculate2.grid(row=2, column=2)

calculate3 = tk.Button(button_frame1, text="3", command=three)
calculate3.grid(row=2, column=3)

calculate4 = tk.Button(button_frame1, text="4", command=four)
calculate4.grid(row=3, column=1)

calculate5 = tk.Button(button_frame1, text="5", command=five)
calculate5.grid(row=3, column=2)

calculate6 = tk.Button(button_frame1, text="6", command=six)
calculate6.grid(row=3, column=3)

calculate7 = tk.Button(button_frame1, text="7", command=seven)
calculate7.grid(row=4, column=1)

calculate8 = tk.Button(button_frame1, text="8", command=eight)
calculate8.grid(row=4, column=2)

calculate9 = tk.Button(button_frame1, text="9", command=nine)
calculate9.grid(row=4, column=3)

calculate_mult = tk.Button(button_frame1, text="*", command=multiplication)
calculate_mult.grid(row=5, column=1)

calculate_add = tk.Button(button_frame1, text="+", command=plus)
calculate_add.grid(row=5, column=2)

calculate_minus = tk.Button(button_frame1, text="-", command=minus)
calculate_minus.grid(row=5, column=3)

calculate_divide = tk.Button(button_frame1, text="/", command=division)
calculate_divide.grid(row=6, column=1)

calculate_equals = tk.Button(button_frame1, text="=", command=equals)
calculate_equals.grid(row=6, column=2)

calculate_clear = tk.Button(button_frame1, text="C", command=clear)
calculate_clear.grid(row=6, column=3)

calculate_power = tk.Button(button_frame1, text="^", command=power)
calculate_power.grid(row=7, column=1)

calculate_modulus = tk.Button(button_frame1, text="R", command=modulus)
calculate_modulus.grid(row=7, column=2)

root.mainloop()

