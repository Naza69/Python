print("Hola usuario! Vamos a usar un modulo para ejecutar este programa!")
x=input("Hasta ahora solo se tiene el modulo de una minicalculadora" 
    ", ingrese el numero de operacion que desea realizar"  
    "\n1)Suma"
    "\n2)Resta"
    "\n3)Multiplicacion"
    "\n4)Division\n")
if x=="1":
    import sys
    sys.path.append(r"C:\Users\NAZA\Desktop\CodPersonal\Python\Ejs\Mds")
    import MiniCalc 
    z=int(input("Ingrese el primer numero: "))
    y=int(input("Ingrese el segundo numero: "))
    MiniCalc.suma(z,y)
elif x=="2":
    import sys
    sys.path.append(r"C:\Users\NAZA\Desktop\CodPersonal\Python\Ejs\Mds")
    import MiniCalc 
    z=int(input("Ingrese el primer numero: "))
    y=int(input("Ingrese el segundo numero: "))
    MiniCalc.resta(z,y)
elif x=="3":
    import sys
    sys.path.append(r"C:\Users\NAZA\Desktop\CodPersonal\Python\Ejs\Mds")
    import MiniCalc 
    z=int(input("Ingrese el primer numero: "))
    y=int(input("Ingrese el segundo numero: "))
    MiniCalc.mult(z,y)
elif x=="4":
    import sys
    sys.path.append(r"C:\Users\NAZA\Desktop\CodPersonal\Python\Ejs\Mds")
    import MiniCalc 
    z=int(input("Ingrese el primer numero: "))
    y=int(input("Ingrese el segundo numero: "))
    MiniCalc.divi(z,y)
else:
    print("Ningun numero ingresado corresponde con las opciones dadas")
