num1 = ["1","2","3","4","5"] #Ecribimos 5 numeros 
num2 = "0"  #La segunda cifra
num3 = "7"  #La tercer cifra

#ciclo for anidado para repetir los 3 numeros hasta realizarlo 5 veces
for x in num1:
    for y in num2:
        for z in num3:
            print(x + y + z)


print("Se acabo")