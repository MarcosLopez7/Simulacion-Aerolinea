from avion import Avion
from pasajero import Pasajero
from generador import Congruencial
from datetime import datetime, timedelta
from time import gmtime
class CheckIn:
	def __init__(self):
		pasajeros = 0

	def colaCheckIn(self,pasajeros,vuelos,num_pasajeros):
		generador = Congruencial(200)
		tiempo_total = 0
		hora_4_t = 0 
		hora_5_t = 0
		hora_6_t = 0 
		hora_7_t = 0
		hora_may_8_t = 0
		i = 0
		pasajeros_por_atender = 0
		num_pasajeros = 100
		print("num_pasajeros en proceso %d"%num_pasajeros)
		#while num_pasajeros > 0:
		for j in range(0,10):
			hora_4 = 0 
			hora_5 = 0
			hora_6 = 0 
			hora_7 = 0
			atendidos = 0
			hora_may_8 = 0
			print("------------%d-----------------"%j)
			print("Numero de pasajeros en cola %d" %num_pasajeros)
			#numero de pasajeros
			'''numero = (generador.genera() % 100)
			if numero < 30 and numero >= 0:
				pasajeros_por_atender = 1
			elif numero < 45 and numero >= 30:
				pasajeros_por_atender = 2
			elif numero < 66 and numero >= 45:
				pasajeros_por_atender = 3	
			elif numero < 77 and numero >= 66:
				pasajeros_por_atender = 4
			elif numero < 90 and numero >= 77:
				pasajeros_por_atender = 5
			else:
				pasajeros_por_atender = 6'''
			#hora en que llegan entre 20 a 0
			hora = int(datetime.strftime(datetime.now() + timedelta(hours=j), '%H'))
			if hora > 20:
				prob_solicitudes = 0.2
				hora_4 = 1
			elif hora > 21:
				prob_solicitudes = 0.3
				hora_5 = 1
			elif hora > 22:
				prob_solicitudes = 0.35
				hora_6 = 1
			elif hora > 23:
				prob_solicitudes = 0.1
				hora_7 = 1
			else:
				prob_solicitudes = 0.05
				hora_may_8 = 1
			#Tiempo de atencion por pasajero
			numero_t = generador.genera()%100
			if numero_t < 30 and numero_t >= 0:
				 tiempo_atencion = 5
			elif numero_t < 45 and numero_t >= 30:
				 tiempo_atencion = 10
			elif numero_t < 66 and numero_t >= 45:
				 tiempo_atencion = 7
			elif numero_t < 77 and numero_t >= 66:
				 tiempo_atencion = 13
			elif numero_t < 90 and numero_t >= 77:
				 tiempo_atencion = 3
			else:
				tiempo_atencion = 1
			#Tomando en cuenta la hora
			print("Resultado de la probabilidad %d" %(int(num_pasajeros * prob_solicitudes)))
			pasajeros_por_atender = (int(num_pasajeros * prob_solicitudes))
			num_pasajeros -= pasajeros_por_atender
			print("num_pasajeros despues de atender %d"%num_pasajeros)
			#i+=1
			#Comparaciones
			#200 usd por pasajero de perdida
			print("Atendiendo %d en %d tiempo" %(pasajeros_por_atender,tiempo_atencion))
			if atendidos < num_pasajeros:
				atendidos += pasajeros_por_atender
				tiempo_total += (pasajeros_por_atender*tiempo_atencion)
			else:
				print ("Faltaron de atender %d " %(num_pasajeros - (atendidos + pasajeros_por_atender)))

			if hora_4 == 1:
				hora_4_t += atendidos
			elif hora_5 == 1:
				hora_5_t += atendidos
			elif hora_6 == 1:
				hora_6_t += atendidos
			elif hora_7 == 1:
				hora_7_t += atendidos
			else:
				hora_may_8_t+=atendidos
		print ("El promedio de pasajeros es %d " %(atendidos/num_pasajeros))
		print ("El tiempo_total es %d" %tiempo_total)
		print ("Se atendieron %d pasajeros" %atendidos)
		
		print ("Atendidos a las 4: %d" %hora_4_t)
		print ("Atendidos a las 5: %d" %hora_5_t)
		print ("Atendidos a las 6: %d" %hora_6_t)
		print ("Atendidos a las 7: %d" %hora_7_t)
		print ("Atendidos a las 8 o mas: %d" %hora_may_8_t)

	def makeCheckInMexico(self,pasajeros,vuelos):
		print ("CheckIn de Mexico a Francia")
		for j in range(40,50,2):#len(vuelos)):
			num_pasajeros = 0
			for i in range(0,len(pasajeros)):
				if (pasajeros[i].vuelo_ida['fecha'] == vuelos[j]['fecha']):
					num_pasajeros += 1
			#print(num_pasajeros)
			print("Vuelo %d num_pasajeros %d" %(j,num_pasajeros))
			if num_pasajeros > 0:
				self.colaCheckIn(pasajeros,vuelos,num_pasajeros)
			else:
				print ("Para la fecha %s no hay pasajeros" %(vuelos[j]['fecha']))
		
		
	
    


		#for i in range(1,len(pasajeros),2):
		#	print ("El pasajero tiene el id %d" %(pasajeros[i].id))
			#print ("El vuelo que tiene el pasajero %d es %s" %(pasajeros[i].id,pasajeros[i].vuelo_ida))
			#print if vuelos[i]['fecha'] == datetime.strftime(datetime.now() + timedelta(days=vuelo_rand, hours=h),
                                                        #   '%Y-%m-%d'):