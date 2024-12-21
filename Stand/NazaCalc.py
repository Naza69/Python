from tkinter import *
def resolve_sequence():
    sequence = fill.get()
    try:
        fill.set(eval(sequence))
    except Exception:
        fill.set("SyntaxERROR")

def delete_sequence():
    fill.set("")

def delete_one_char():
    sequence = fill.get()
    sequence_lenght = len(fill.get())
    fill.set(sequence[0:(sequence_lenght-1)])

def fill_entry(text):
    insert = fill.get()
    if insert == "SyntaxERROR":
        fill.set(text)
    else:
        new_insert = fill.get()+text
        fill.set(new_insert)

root = Tk()
root.geometry("320x400")
frame_calc = Frame(root)
root.title("NazaCalc")
root.iconbitmap(r"Personal\Python\Grafico\Importables\vector-calculator-icon.ico")
root.resizable(False, False)
button1 = Button(frame_calc, text = "1", command = lambda: fill_entry("1"), width=10, height=5)
button1.grid(row=0, column=0)
button2 = Button(frame_calc, text = "2", command = lambda: fill_entry("2"), width=10, height=5)
button2.grid(row=0, column=1)
button3 = Button(frame_calc, text = "3", command = lambda: fill_entry("3"), width=10, height=5)
button3.grid(row=0, column=2)
button4 = Button(frame_calc, text = "4", command = lambda: fill_entry("4"), width=10, height=5)
button4.grid(row=1, column=0)
button5 = Button(frame_calc, text = "5", command = lambda: fill_entry("5"), width=10, height=5)
button5.grid(row=1, column=1)
button6 = Button(frame_calc, text = "6", command = lambda: fill_entry("6"), width=10, height=5)
button6.grid(row=1, column=2)
button7 = Button(frame_calc, text = "7", command = lambda: fill_entry("7"), width=10, height=5)
button7.grid(row=2, column=0)
button8 = Button(frame_calc, text = "8", command = lambda: fill_entry("8"), width=10, height=5)
button8.grid(row=2, column=1)
button9 = Button(frame_calc, text = "9", command = lambda: fill_entry("9"), width=10, height=5)
button9.grid(row=2, column=2)
button0 = Button(frame_calc, text = "0", command = lambda: fill_entry("0"), width=10, height=5)
button0.grid(row=3, column=1)
frame_fourth = Frame(frame_calc)
frame_fourth.grid(row=0, column=4)
button_dot = Button(frame_calc, text = ".", command = lambda: fill_entry("."), width=10, height=5)
button_dot.grid(row=3, column=2)
button_equal = Button(frame_calc, text = "=", command = resolve_sequence, width=10, height=5)
button_equal.grid(row=3, column=4)
button_plus = Button(frame_fourth, text = "+", command = lambda: fill_entry("+"), width=4, height=5)
button_plus.grid(row=0, column=0)
button_minus = Button(frame_fourth, text = "-", command = lambda: fill_entry("-"), width=4, height=5)
button_minus.grid(row=0, column=1)
button_multiplication = Button(frame_calc, text = "x", command = lambda: fill_entry("*"), width=10, height=5)
button_multiplication.grid(row=1, column=4)
button_division = Button(frame_calc, text = "÷", command = lambda: fill_entry("/"), width=10, height=5)
button_division.grid(row=2, column=4)
frame_calc.place(x=0, y=55)
frame_second = Frame(frame_calc)
frame_second.grid(row=3, column=0)
frame_third = Frame(root)
frame_third.place(x=250, y=0)

button_left_bracket = Button(frame_second, text="(", command = lambda: fill_entry("("), width=4, height=5).grid(row=0, column=0)
button_right_bracket = Button(frame_second, text=")", command = lambda: fill_entry(")"), width=4, height=5).grid(row=0, column=1)
button_delete_all = Button(frame_third, text="BORRAR", command = delete_sequence, width=6, height=1).grid(row=0)
button_delete_one_char = Button(frame_third, text="<---", command = delete_one_char, width=6, height=1).grid(row=1)
fill = StringVar()
entry_to_fill = Entry(state = "readonly", textvariable = fill, width = 13, font=("ComicSans", 25)).place(x=0, y=5)
root.mainloop()
