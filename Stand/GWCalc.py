import tkinter as tk
import math

def on_button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

def clear():
    entry.delete(0, tk.END)

def delete():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

def add_equals():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + "=")

def calculate():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=20, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '(', '0', '.', '+', 
    ')', 'C', '⌫',
    'CE', '='
]

row = 1
col = 0

for button in buttons:
    if button == 'C':
        tk.Button(root, text=button, width=5, command=clear).grid(row=row, column=col)
    elif button == '⌫':
        tk.Button(root, text=button, width=5, command=delete).grid(row=row, column=col)
    elif button == 'CE':
        tk.Button(root, text=button, width=5, command=lambda: entry.delete(0, tk.END)).grid(row=row, column=col)
    elif button == '=':
        tk.Button(root, text=button, width=5, command=add_equals).grid(row=row, column=col)
    else:
        tk.Button(root, text=button, width=5, command=lambda b=button: on_button_click(b)).grid(row=row, column=col)
    
    col += 1
    if col > 3:
        col = 0
        row += 1

tk.Button(root, text="Calculate", width=30, command=calculate).grid(row=row, column=0, columnspan=4)

root.mainloop()