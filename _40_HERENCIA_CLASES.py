#Se cre una clase tipo usuario
class Usuarios():
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos
    
    def imprime_datos(self):
	    print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)

#Se proveen dadtos
usuario01 = Usuarios("Aldo", 22)

usuario01.imprime_datos()

class Usuarios_premiun(Usuarios):
    pass
    
usuario02 = Usuarios_premiun("Alika", 23)

usuario02.imprime_datos()