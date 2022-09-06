#Se importa la libreria math
import math
#Se define una funcion para calcular el area de un circulo
def area(radio):
	resultado = math.pi * radio * radio
	print(resultado)

area(6)
#Se define una funcion mediante la cual se calcula el area de un circulo con lambda
area2 = lambda radio:(math.pi * radio * radio)

print(area2 (2))