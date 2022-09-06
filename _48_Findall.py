#Se importa la libreria reserch
import re

#Se define el texto a comparar y se realiza la busqueda mediante el metodo "Findall", posteriormente se imprime el resultado
texto = "Bienvenidos a Programación fácil"
busqueda = re.findall("e", texto)
print(busqueda)