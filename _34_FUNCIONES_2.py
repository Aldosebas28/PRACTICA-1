#Utilizamos argumentos para mandar llamar datos
def colores(*args):
    print('El color', args[1],'es mi favorito','el color',args[0],'tambien me gusta')

colores('rojo','azul')

def suma(*args):
    resultado = args[0] + args[1] + args[2] + args[3] + args[4]
    print('El resultado de sumar es:',resultado)

suma(6,11,22,34,21,57)