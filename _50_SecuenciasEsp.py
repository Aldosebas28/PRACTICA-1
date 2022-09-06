#Se importa la libreria REGEX
import re

#Se define una oracion para ser usada
texto = "Me gusta jugar FIFA."
buscar = re.findall("jugar", texto)

#Se define un condicional en cual si se encuentra una coincidencia imprimirá una confirmación y si no la hay lo dirá
if buscar:
	print("Hay al menos una coincidencia.")
else:
	print("No hay coincidencias.")