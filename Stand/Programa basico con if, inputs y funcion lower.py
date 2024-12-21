print("Hola usuario")
print("Como se llama?")
name=input()
print("Es un placer conocerte",name)
print("Como estas el dia de hoy",name+"?")
resp=input()
resplower=resp.lower()
if resplower=="mal":
    print("Lamento escuchar eso",name)
else:
    print("Me alegro!")


