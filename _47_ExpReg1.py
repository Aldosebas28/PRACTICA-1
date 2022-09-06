#Se importa la libreria reserch
import re

#Se define el texto a comparar y se realiza la busqueda, posteriormente se imprime el resultado
texto = "Bienvenidos a Programación fácil"
busqueda = re.search("c", texto)
print(busqueda)