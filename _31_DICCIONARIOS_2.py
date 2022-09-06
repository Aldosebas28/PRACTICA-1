#Creamos diccionario 1
teclado1 = {
    "Categoria": "Teclados",
    "Modelo": "HyperX Alloy FPS Pro",
    "Precio": "89,99"
    }   
#creamos diccionario 2
teclado2 = {
    "Categoria": "Teclados",
    "Modelo": "Corsair k55 RGB",
    "Precio": "59,99"
    }

#Obtener solo los valores 
for x in teclado2.values():
    print(x) 
#Obtener valores y nombres
for x, y in teclado2.items():
    print(x,y)