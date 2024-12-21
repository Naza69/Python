print("Hola usuario! Vamos a ver como funciona def!")
print("Ingrese un numero")
x=int(input())
def funcionbasica(x):
   if x==0:
      z=x+1
   else:
      z=x+2
   return z
y=funcionbasica(x)
print(y)
print("Entonces para que una funcion sea reconocida por python",
"tiene que definirse con la funcion def, seguido de su nombre,",
"seguida de la variable a copiar como parametro y dos puntos,",
"y un indentado para que el inteprete reconozca el codigo de la funcion.",
"Para que retorne un valor, tiene que usarse la funcion return seguido",
"de la variable a retornar, al final y adentro de la funcion.",
"NO SE PUEDE USAR RETURN FUERA DE UNA FUNCION")

