import tkinter as tk

# Función para calcular el resultado
def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except Exception as e:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Error")

# Función para añadir caracteres a la entrada
def agregar_caracter(caracter):
    entrada.insert(tk.END, caracter)

# Función para borrar el último caracter de la entrada
def borrar_caracter():
    entrada.delete(len(entrada.get()) - 1, tk.END)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")

# Crear entrada
entrada = tk.Entry(ventana, font=("Arial", 20))
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Botones numéricos
for i in range(10):
    tk.Button(ventana, text=str(i), padx=20, pady=10, font=("Arial", 15),
            command=lambda num=i: agregar_caracter(str(num))).grid(row=(i//3)+1, column=i%3)

# Botones de operaciones
botones_operaciones = ["+", "-", "*", "/"]
for i, operacion in enumerate(botones_operaciones):
    tk.Button(ventana, text=operacion, padx=20, pady=10, font=("Arial", 15),
            command=lambda op=operacion: agregar_caracter(op)).grid(row=i+1, column=3)

# Botones especiales
tk.Button(ventana, text="=", padx=20, pady=10, font=("Arial", 15),
        command=calcular).grid(row=4, column=2)
tk.Button(ventana, text="C", padx=20, pady=10, font=("Arial", 15),
        command=lambda: entrada.delete(0, tk.END)).grid(row=4, column=0)
tk.Button(ventana, text="⌫", padx=20, pady=10, font=("Arial", 15),
        command=borrar_caracter).grid(row=4, column=1)

# Ejecutar aplicación
ventana.mainloop()
