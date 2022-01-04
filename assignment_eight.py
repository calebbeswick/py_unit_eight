#Calculator by Caleb Beswick for unit 8
#last edited 1-04-22
import tkinter as tk
from tkinter import *
root = tk.Tk()
root.title("Calculator")


entry = tk.StringVar()

#These are the functions that the buttons actually execute
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

#sets the entry field and text size/font
calculator_entry = tk.Entry(root, font=("Calibri",20), textvariable=entry)
calculator_entry.grid(row=1, column=1, stick="W")


#pulls the photos from my computer for the buttons to use
photo1 = PhotoImage(file = "/Users/calebsmacbookpro/PycharmProjects/py_unit_eight/unit 8 images/number1.png")
photo2 = PhotoImage(file = "/Users/calebsmacbookpro/PycharmProjects/py_unit_eight/unit 8 images/number2.png")
photo3 = PhotoImage(file = "/Users/calebsmacbookpro/PycharmProjects/py_unit_eight/unit 8 images/number3.png")
photo4 = PhotoImage(file = "/Users/calebsmacbookpro/PycharmProjects/py_unit_eight/unit 8 images/number4.png")
photo5 = PhotoImage(file = "/Users/calebsmacbookpro/PycharmProjects/py_unit_eight/unit 8 images/number5.png")
photo6 = PhotoImage(file = "/Users/calebsmacbookpro/PycharmProjects/py_unit_eight/unit 8 images/number6.png")
photo7 = PhotoImage(file = "/Users/calebsmacbookpro/PycharmProjects/py_unit_eight/unit 8 images/number7.png")
photo8 = PhotoImage(file = "/Users/calebsmacbookpro/PycharmProjects/py_unit_eight/unit 8 images/number8.png")
photo9 = PhotoImage(file = "/Users/calebsmacbookpro/PycharmProjects/py_unit_eight/unit 8 images/number9.png")
photo_equal = PhotoImage(file = "/Users/calebsmacbookpro/PycharmProjects/py_unit_eight/unit 8 images/number_equal.png")
photo_mult = PhotoImage(file = "/Users/calebsmacbookpro/PycharmProjects/py_unit_eight/unit 8 images/number_mult.png")
photo_divide = PhotoImage(file = "/Users/calebsmacbookpro/PycharmProjects/py_unit_eight/unit 8 images/number_divide.png")
photo_add = PhotoImage(file = "/Users/calebsmacbookpro/PycharmProjects/py_unit_eight/unit 8 images/number_add.png")
photo_subtract = PhotoImage(file = "/Users/calebsmacbookpro/PycharmProjects/py_unit_eight/unit 8 images/number_minus.png")

#creates new frame to make the buttons neater and more centered
button_frame1 = tk.Frame(root)
button_frame1.grid(row=2, column=1, columnspan=2)

#The following grids the buttons
calculate1 = tk.Button(button_frame1, text="1", image=photo1, command=one)
calculate1.grid(row=2, column=1)

calculate2 = tk.Button(button_frame1, text="2", image=photo2, command=two)
calculate2.grid(row=2, column=2)


calculate3 = tk.Button(button_frame1, text="3", image=photo3, command=three)
calculate3.grid(row=2, column=3)


calculate4 = tk.Button(button_frame1, text="4", image=photo4, command=four)
calculate4.grid(row=3, column=1)


calculate5 = tk.Button(button_frame1, text="5", image=photo5, command=five)
calculate5.grid(row=3, column=2)


calculate6 = tk.Button(button_frame1, text="6", image=photo6, command=six)
calculate6.grid(row=3, column=3)


calculate7 = tk.Button(button_frame1, text="7", image=photo7, command=seven)
calculate7.grid(row=4, column=1)


calculate8 = tk.Button(button_frame1, text="8", image=photo8, command=eight)
calculate8.grid(row=4, column=2)


calculate9 = tk.Button(button_frame1, text="9", image=photo9, command=nine)
calculate9.grid(row=4, column=3)


calculate_mult = tk.Button(button_frame1, text="*", image=photo_mult, command=multiplication)
calculate_mult.grid(row=5, column=1)


calculate_add = tk.Button(button_frame1, text="+", image=photo_add, command=plus)
calculate_add.grid(row=5, column=2)


calculate_minus = tk.Button(button_frame1, text="-", image=photo_subtract, command=minus)
calculate_minus.grid(row=5, column=3)


calculate_divide = tk.Button(button_frame1, text="/", image=photo_divide, command=division)
calculate_divide.grid(row=6, column=1)


calculate_equals = tk.Button(button_frame1, text="=", image = photo_equal, command=equals)
calculate_equals.grid(row=6, column=2)


calculate_clear = tk.Button(button_frame1, text="C", command=clear)
calculate_clear.grid(row=6, column=3)


calculate_power = tk.Button(button_frame1, text="^", command=power)
calculate_power.grid(row=7, column=1)


calculate_remainder = tk.Button(button_frame1, text="R", command=modulus)
calculate_remainder.grid(row=7, column=2)


root.mainloop()