#Se cre una clase tipo usuario
class Usuario():
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos
    
    def imprime_datos(self):
	    print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)
#Se proveen dadtos
usuario01 = Usuario('Aldo', 'Villarreal Barrera')

usuario02 = Usuario('Alika', 'Lopez Perez')

usuario01.nombre= 'Giselle'
#Se imprimen los datos
usuario02.imprime_datos()