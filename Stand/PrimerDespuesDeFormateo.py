from tkinter import *
def tumama():
    print("Hola")
root = Tk()
button_1 = Button(text = "Boton", command = tumama).pack()
var_entry = Entry().pack()
root.mainloop()
