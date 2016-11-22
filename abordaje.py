from avion import Avion
from pasajero import Pasajero
from generador import Congruencial
from datetime import datetime, timedelta
from time import gmtime
class Abordaje:

	def __init__(self):
		pasajeros = 0

	def abordar(self,pasajeros,vuelo):
		#Considerar pasajeros con discapacidad
		print("Bienvenidos al vuelo de la fecha %s" %vuelo['fecha'])
		dis = 0
		for i in range(0,len(pasajeros)):
			if pasajeros[i].discapacidad == True:
				dis += 1
		print("Hay %d discapacitados" %dis)
