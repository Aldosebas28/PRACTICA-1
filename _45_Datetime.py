#Se importa la libreria datetime
import datetime

#Se declara e imprime la variable fecha con la fecha tomada del ordenador
fecha = datetime.datetime.now()
print("Esta es una fecha automatica: {}".format(fecha))

#Se declara e imprime una fecha personalizada
fecha2 = datetime.datetime(2001, 10, 9, 6, 30)
print("Esta es una fecha personalizada: {}".format(fecha2))

