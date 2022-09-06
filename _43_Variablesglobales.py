#Se define la funcion que contiene variables globales
def funcion1():
	global n1
	n1 = 10

funcion1()

print(n1)

#Se define una funcion en la cual se anidara otra
def funcion3():
    pass
def funcion3():
    print("Este string se encuentra en una funcion anidada.")
     
funcion1()     