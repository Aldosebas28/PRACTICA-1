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

del teclado1 #Borramos teclado 1
del teclado2["Categoria"] #Borramos categoria del teclado 2
del teclado2["Precio"] #Borramos precio del teclado 2
print(teclado2["Modelo"]) #Imprimimos modelo de teclado 2




