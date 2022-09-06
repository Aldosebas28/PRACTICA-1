#Se importa la libreria REGEX
import re

#Se define una frase para ser usada y comparada mediante el metodo split
texto = "tres tristes tigres comen trigo en un trigal"
busqueda = re.split("ri", texto)
print(busqueda)