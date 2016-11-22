from avion import Avion
from pasajero import Pasajero
from generador import Congruencial
from datetime import datetime, timedelta
from time import gmtime
class Shuttle:
	def cargarShuttle(self,vuelo,pasajeros):
		print("Mis pasajeros %d"%len(pasajeros))
		#Ver cuantos aviones llegaron
		generador = Congruencial(20)
		rand = generador.genera()%100
		if rand < 50 and rand >= 0:
			aviones_por_llegar = 2
		elif rand < 80 and rand>=50:
			aviones_por_llegar = 3
		elif rand < 95 and rand>=80:
			aviones_por_llegar = 4
		elif rand <= 100  and rand >= 95:
			aviones_por_llegar = 5
		#Pasajeros promedio por vuelo
		rand_2 = generador.genera()%100
		if rand_2 < 50 and rand_2 >= 0:
			pasajeros_promedio = 243
		elif rand_2 < 80 and rand_2>=50:
			pasajeros_promedio = 175
		elif rand_2 < 95 and rand_2>=80:
			pasajeros_promedio = 76
		elif rand_2 <= 100  and rand_2 >= 95:
			pasajeros_promedio = 30
		#Porcentaje de pasajeros en vuelo
		rand_3 = generador.genera()%100
		if rand_3 < 50 and rand_3 >= 0:
			porcentaje = 0.7
		elif rand_3 < 80 and rand_3>=50:
			porcentaje = 1
		elif rand_3 < 95 and rand_3>=80:
			porcentaje = 0.5
		elif rand_3 <= 100  and rand_3 >= 95:
			porcentaje = 0.7	
		total = int(pasajeros_promedio*porcentaje)
		total += len(pasajeros)
		total = int(total * 0.2) #20 % toma shuttle
		print("Pasajeros que necesitan shuttle: %d" %(total))
		viajes_por_hacer = (total / 10) #10 pasajeros maximo por camioneta
		print ("Se haran %d viajes de llenos" %viajes_por_hacer)
		remaining = total % 10 
		print ("Remanente: %d" %remaining)
		rem = False
		if remaining > 0:
			viajes_por_hacer_t = viajes_por_hacer + 1
			rem = True
		else:
			viajes_por_hacer_t = viajes_por_hacer
			rem = False
		tiempo_t = 0
		for i in range(1,viajes_por_hacer_t+1):
			if rem == True and i < viajes_por_hacer_t:
				tiempo = self.viaje(10,gmtime().tm_sec)
			else:
				tiempo = self.viaje(remaining,gmtime().tm_sec)
			tiempo_t += tiempo
		print("Tiempo total de viajes %d" %tiempo_t)

	def viaje(self,pasajeros,rand_n):
		generador = Congruencial(rand_n)
		tiempo_viaje_t = 0
		frec_3m = 0
		frec_5m = 0
		frec_8m = 0
		frec_10m = 0
		for i in range(1,pasajeros+1):
			rand_4 = (generador.genera())%100
			print("Numero Rand %d"%rand_4)
			if rand_4 < 40 and rand_4 >=0:
				frec_3m += 1
			elif rand_4 < 70 and rand_4 >= 40:
				frec_5m += 1
			elif rand_4 < 90 and rand_4 >= 70:
				frec_8m += 1
			elif rand_4 <= 100 and rand_4 >= 90:
				frec_10m += 1

			if frec_3m > 0:
				tiempo_viaje_t = (3*frec_3m)
			elif frec_5m > 0 and frec_3m > 0:
				tiempo_viaje_t += (2*frec_5m)
			elif frec_5m > 0 and frec_3m > 0 and frec_8m > 0:
				tiempo_viaje_t += (3*frec_8m)
			elif frec_5m > 0 and frec_3m > 0 and frec_8m > 0 and frec_10m > 0:
				tiempo_viaje_t += (2*frec_10m)
			elif not frec_3m > 0 and frec_5m >0:
				tiempo_viaje_t += (5*frec_5m)
			elif not frec_3m > 0 and not frec_5m > 0 and frec_8m > 0:
				tiempo_viaje_t += (8*frec_8m)
			elif not frec_3m > 0 and not frec_5m > 0 and not frec_8m > 0 and frec_10m:
				tiempo_viaje_t += (10*frec_10m)


		print ("Frecuencia 3 min: %d" %frec_3m)
		print ("Frecuencia 5 min: %d" %frec_5m)
		print ("Frecuencia 8 min: %d" %frec_8m)
		print ("Frecuencia 10 min: %d" %frec_10m)
		print ("Tiempo total de viaje %d" %tiempo_viaje_t)

		return tiempo_viaje_t


