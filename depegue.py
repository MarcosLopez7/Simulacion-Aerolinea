from avion import Avion
from aerolinea import Aerolinea
from pasajero import Pasajero
from generador import Congruencial
from datetime import datetime, timedelta
from time import gmtime
class Despegue:
	def __init__(self):
		aviones_en_cola = 0
	def taxing(self,vuelo):
		tiempo_espera = 0
		aero = Aerolinea()
		generador = Congruencial(vuelo['id']*3)
		for i in range(1,13):
			mes = datetime.strftime(datetime.now() + timedelta(hours=i), '%%m')
			if mes == '12' or mes == '08' or mes == '06' or mes == '07':
                aero.temporada_alta = True
			if aero.temporada_alta == True:
				#Procedimiento para random, aviones por aterrizar
				rand = generador.genera()%100
				if rand < 30 and rand >= 0:
					aviones_en_cola_at = 4
				elif rand < 55 and rand >=30:
					aviones_en_cola_at = 3
				elif rand < 75 and rand >=55:
					aviones_en_cola_at = 2
				elif rand < 90 and rand >= 75:
					aviones_en_cola_at = 1
				elif rand <= 100 and rand >= 90:
					aviones_en_cola_at = 0
				#Procedimiento para random de aviones en rodaje
				rand_2 = generador.genera()%100
				if rand_2 < 30 and rand_2 >= 0:
					aviones_en_cola_tax = 10
				elif rand_2 < 55 and rand_2 >=30:
					aviones_en_cola_tax = 5
				elif rand_2 < 75 and rand_2 >=55:
					aviones_en_cola_tax = 3
				elif rand_2 < 90 and rand_2 >= 75:
					aviones_en_cola_tax = 2
				elif rand_2 <= 100 and rand_2 >= 90:
					aviones_en_cola_tax = 0
			else:
				rand = ((generador.genera()%100)*vuelo['id']) - 100
				#Procedimiento para random, aviones por aterrizar
				print("Numero generado %d" %rand)
				if rand < 60 and rand >= 0:
					aviones_en_cola_at = 2
				elif rand < 90 and rand >=60:
					aviones_en_cola_at = 1
				elif rand <= 100 and rand >=90:
					aviones_en_cola_at = 0
				#Procedimiento para random de aviones en rodaje
				rand_2 = generador.genera()%100
				if rand_2 < 50   and rand_2 >= 0:
					aviones_en_cola_tax = 3
				elif rand_2 < 75 and rand_2 >=50:
					aviones_en_cola_tax = 2
				elif rand_2 < 90 and rand_2 >=75:
					aviones_en_cola_tax = 1
				elif rand_2 < 100 and rand_2 >= 90:
					aviones_en_cola_tax = 0
		#Tomando en cuenta 2 minutos por cada avion en cola de aterrizar y 3 por cada despegue
			print("Hay que esperar a %d aviones un tiempo de %d que aterricen" %(aviones_en_cola_at,aviones_en_cola_at*2))
			print("Hay que esperar a %d aviones un tiempo de %d que roden" %(aviones_en_cola_tax,aviones_en_cola_tax*3))
			print("El tiempo total de espera para el vuelo %d en pista es: %d" %(vuelo['id'],(aviones_en_cola_at*2)+(aviones_en_cola_tax*3)))
