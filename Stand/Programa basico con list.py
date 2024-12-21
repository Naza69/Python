print("Hola Usuario")
x=[]
print("Ingrese la cantidad de numeros que quiere ingresar a la lista")
y=int(input())
for z in range(y):
    print("Ingrese el valor de la casilla",str(z+1))
    x.append(int(input()))
print("Su lista es:")
for z in range(1):
    print(x)