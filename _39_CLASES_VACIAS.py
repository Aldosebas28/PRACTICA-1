class Usuario():
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos
    
    def imprime_datos(self):
	    print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)

usuario01 = Usuario('Aldo', 'Villarreal Barrera')

usuario02 = Usuario('Alika', 'Lopez Perez')

usuario01.nombre= 'Giselle'

print(usuario02.nombre)

del usuario02

usuario02.imprime_datos()


