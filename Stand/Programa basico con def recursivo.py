def funcionsumar(x):
  if x>0:
    print(x)
    funcionsumar(x-1)
  else:
    print(x)
print("Hola usuario!")
print("Vamos a ver una funcion recursiva")
print("Ingrese un numero")
x=int(input())
funcionsumar(x)
suma=lambda x,y: x+y #Funcion anonima usando Lambda


