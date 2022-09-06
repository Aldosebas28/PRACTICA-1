#Creamos una clase de tipo usuario
class Usuario:
	nombre = ''
	apellidos = ''

	def imprime_datos(self):
		print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)

usuario20110199 = Usuario()

usuario20110199.nombre = 'Aldo Sebastian'
usuario20110199.apellidos = 'Villarreal Barrera'
#imprimimos usuario
usuario20110199.imprime_datos()