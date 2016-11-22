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
		generador = Congruencial(vuelo['id'])
		rand = generador.genera()%100
		if rand < 50 and rand >= 0:
			pasajeros_por_minuto = 20
		elif rand < 80 and rand>=50:
			pasajeros_por_minuto = 10
		elif rand < 95 and rand>=80:
			pasajeros_por_minuto = 5
		elif rand <= 100  and rand >= 95:
			pasajeros_por_minuto = 1
		if dis > 0 :
			pasajeros_por_minuto -= 5
		print("Tiempo total en abordaje %f minutos" %(len(pasajeros)/pasajeros_por_minuto))
	def repostajeCombustible(self,vuelo):
		print("Repostando vuelo %s "%(vuelo['id']))
		generador = Congruencial(vuelo['id'])
		rand_2 = generador.genera()%100
		if rand_2 < 65 and rand_2 >= 0:
			aviones_en_cola = 0
		elif rand_2 < 80 and rand_2 >= 65:
			aviones_en_cola = 1
		elif rand_2 < 93 and rand_2 >= 80:
			aviones_en_cola = 2
		elif rand_2 < 98  and rand_2 >=93:
			aviones_en_cola = 3
		elif rand_2 <= 100   and rand_2 >=98:
			aviones_en_cola = 4
		print("Hay %d aviones en cola" %(aviones_en_cola))
		rand = generador.genera()%100
		if rand < 30 and rand >= 0:
			tiempo_carga = 3
		elif rand < 50 and rand >= 30:
			tiempo_carga = 5
		elif rand < 70 and rand >= 50:
			tiempo_carga = 7
		elif rand < 90  and rand >=70:
			tiempo_carga = 9
		elif rand <= 100   and rand >=90:
			tiempo_carga = 10
		print("Tiempo total de repostaje %d minutos" %(tiempo_carga*(aviones_en_cola+1)))
	def servicioDeAeromozas(self,vuelo,num):
		print("Sirviendo pasajeros del vuelo %s "%(vuelo['id']))
		generador = Congruencial(vuelo['id'])
		tiempo_de_servicio_t = 0 
		for i in range(0,num):
			rand = generador.genera()%100
			if rand < 65 and rand >= 0:
				tiempo_de_servicio = 1
			elif rand < 80 and rand >= 65:
				tiempo_de_servicio = 2
			elif rand < 93 and rand >= 80:
				tiempo_de_servicio = 3
			elif rand < 98  and rand >=93:
				tiempo_de_servicio = 4
			elif rand <= 100   and rand >=98:
				tiempo_de_servicio = 5
			tiempo_de_servicio_t+= tiempo_de_servicio
		print("Tiempo de servicio total %d" %(tiempo_de_servicio_t))
		