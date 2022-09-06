#Se cre una clase tipo usuario
class Usuarios():
    def __init__(self, nombre, apellidos,instagram):
        self.nombre = nombre
        self.apellidos = apellidos
        self.instagram = instagram 
    
    def imprime_datos(self):
	    print('Nombre:', self.nombre, '\nApellidos:', self.apellidos,'\nInstagram:', self.instagram)

#Se proveen dadtos
class Usuariospremiun(Usuarios):
    def __init__(self, nombre, apellidos, instagram):
        self.nombre = nombre
        self.apellidos = apellidos
        self.instagram = instagram
    

