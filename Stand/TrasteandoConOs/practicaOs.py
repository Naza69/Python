import os

# El nombre del sistema operativo, los indexados son linux, nt y java
print(os.name)
# Un string de la ruta actual de trabajo, es decir, de donde se ejecuta este script
print(os.getcwd())

# Cambio de la ruta actual de trabajo, dos carpetas de nivel, cada ../ es un cambio de carpeta
os.chdir('../../')

print("Este script muestra el nombre del sistema operativo, imprime la ruta de trabajo actual, cambia la ruta de trabajo dos niveles hacia arriba, y finalmente muestra la nueva ruta de trabajo actual:", os.getcwd())
