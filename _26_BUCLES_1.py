x = 1

while x < 10:
   print(x)
   x = x + 1

frase = "Lo que es escribas lo repito:"
frase +="\n Introduce el comando 'salir'para finalizar el programa:\n"

mensaje=""

while mensaje != "salir":
    mensaje = input(frase)
    print(mensaje)

print("se ha salido del bucle :)")


