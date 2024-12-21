#Este es un codigo para llenar un tanque de agua
print("Hola Usuario!")
print("Vamos a llenar un tanque con agua!")
print("Que capacidad quiere que el tanque tenga?")
tankcapacity=int(input())
print("El tanque de agua tiene una capacidad de", tankcapacity ,"ml")
choice="si"
waterintank=0
while choice.lower()!="no":
    print("Ingrese la cantidad de ml que quiere vertir en el tanque")
    waterdeposit=int(input())
    print("Llenando...")
    for z in range(waterintank, (waterintank+waterdeposit+10), 10):
        print(z)
    print("Agua vertida con exito!")
    waterintank=waterdeposit+waterintank
    while choice.lower()!="si" or choice.lower()!="no":
      if waterintank>=tankcapacity or choice.lower()=="no":
        break
      print("Quiere seguir?")
      choice=input()
      if choice.lower()!="no" and choice.lower()!="si":
        print("Respuesta invalida, solo se acepta si o no")
        break
    print("El tanque tiene", waterintank, "ml de agua!")
if waterintank>=tankcapacity:
  print("Ha llenado o superado la capacidad del tanque!")
if waterintank>tankcapacity:
  print("El tanque se lleno y se rebalzo, hay", (waterintank-tankcapacity), "ml sobrantes!")
else:
  print("El tanque quedo con", waterintank, "ml de agua!")