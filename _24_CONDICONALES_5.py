print("Saludos caballero,¿Que deseas comprar?\n\n"+
      "Items disponibles\n\n"+
      "Espadas:\n\n"+
      "1)Espadas nivel 1;200 Monedas de oro.\n"+
      "2)Espadas nivel 2:1500 Monedas de oro\n\n"+
      "Escudos:\n\n"+
      "3)Escudos nivel 1;150 Monedas de oro\n"+
      "4)Escudos nivel 2;650 Monedas de oro\n")


comprar=[1]

dinero = 2000 

espadaLV1 = 200

espadaLV2 = 1500

escudoLV1 = 150

escudoLV2 = 650

if 0 in comprar or comprar ==[]:
    print("Valor no valido")
if 1 in comprar:
    dinero = dinero - espadaLV1
if 2 in comprar:
    dinero = dinero - espadaLV2
if 3 in comprar:
    dinero = dinero - escudoLV1
if 4 in comprar:
    dinero = dinero - escudoLV2
if dinero <= 0:
    print("No te alcanza para comprar esto")
if comprar == [1] or comprar == [2] or comprar == [3] or comprar == [4]:
    print ("Te quedan" + str(dinero) +"monedas de oro")
    print ("Se añadio el objeto(s) a tu inventario")


