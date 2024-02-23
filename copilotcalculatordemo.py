import tkinter as tk
import math

def calculate(operation):
    if operation in ['+', '-', '*', '/']:
        first_number = float(first_entry.get())
        second_number = float(second_entry.get())

        if operation == '+':
            result = first_number + second_number
        elif operation == '-':
            result = first_number - second_number
        elif operation == '*':
            result = first_number * second_number
        elif operation == '/':
            if second_number != 0:
                result = first_number / second_number
            else:
                result = 'Error'
    elif operation == 'sqrt':
        number = float(first_entry.get())
        result = math.sqrt(number)
    elif operation == '^':
        base = float(first_entry.get())
        exponent = float(second_entry.get())
        result = math.pow(base, exponent)
    else:
        result = 'Error'

    result_label.config(text = str(result))

root = tk.Tk()

first_entry = tk.Entry(root)
first_entry.pack()

second_entry = tk.Entry(root)
second_entry.pack()

add_button = tk.Button(root, text='+', command=lambda: calculate('+'))
add_button.pack()

subtract_button = tk.Button(root, text='-', command=lambda: calculate('-'))
subtract_button.pack()

multiply_button = tk.Button(root, text='*', command=lambda: calculate('*'))
multiply_button.pack()

divide_button = tk.Button(root, text='/', command=lambda: calculate('/'))
divide_button.pack()

sqrt_button = tk.Button(root, text='sqrt', command=lambda: calculate('sqrt'))
sqrt_button.pack()

pow_button = tk.Button(root, text='^', command=lambda: calculate('^'))
pow_button.pack()

result_label = tk.Label(root)
result_label.pack()

root.mainloop()