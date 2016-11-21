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
		atendidos = 0
		tiempo_total = 0
		for i in range(0,num_pasajeros):
			numero = (generador.genera() % 100)
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
				pasajeros_por_atender = 6
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
			hora = int(datetime.strftime(datetime.now() + timedelta(hours=i), '%H'))
			if hora == 4:
				prob_solicitudes = 20/100
			elif hora == 5:
				prob_solicitudes = 30/100
			elif hora == 6:
				prob_solicitudes = 35/100
			elif hora == 7:
				prob_solicitudes = 10/100
			else:
				prob_solicitudes = 5/100
			'''	
			if hora == 4:
           		prob_solicitudes = 20/100
            elif hora == 5:
            	prob_solicitudes = 30/100
            elif hora == 6:
            	prob_solicitudes = 35/100
            elif hora == 7:
            	prob_solicitudes = 10/100
            else:
            	prob_solicitudes = 5/100
            '''
            pasajeros_por_atender = ((pasajeros_por_atender * prob_solicitudes) * 100)
			#Comparaciones
			print("Atendiendo %d en %d tiempo" %(pasajeros_por_atender,tiempo_atencion))
			if atendidos < num_pasajeros:
				atendidos += pasajeros_por_atender
				tiempo_total += (pasajeros_por_atender*tiempo_atencion)
			else:
				print ("Faltaron de atender %d " %((atendidos + pasajeros_por_atender)-num_pasajeros))

		print ("El promedio de pasajeros es %d " %(atendidos/num_pasajeros))
		print ("El tiempo_total es %d" %tiempo_total)
		print ("Se atendieron %d pasajeros" %atendidos)

	def makeCheckInMexico(self,pasajeros,vuelos):
		print ("CheckIn de Mexico")
		for j in range(40,60,2):#len(vuelos)):
			num_pasajeros = 0
			for i in range(0,len(pasajeros)):
				if (pasajeros[i].vuelo_ida['fecha'] == vuelos[j]['fecha']):
					num_pasajeros += 1
			print(num_pasajeros)
			print("Vuelo %d" %j)
			if num_pasajeros > 0:
				self.colaCheckIn(pasajeros,vuelos,num_pasajeros)
			else:
				print ("Para la fecha %s no hay pasajeros" %(vuelos[j]['fecha']))
		
			
	



		#for i in range(1,len(pasajeros),2):
		#	print ("El pasajero tiene el id %d" %(pasajeros[i].id))
			#print ("El vuelo que tiene el pasajero %d es %s" %(pasajeros[i].id,pasajeros[i].vuelo_ida))
			#print if vuelos[i]['fecha'] == datetime.strftime(datetime.now() + timedelta(days=vuelo_rand, hours=h),
                                                        #   '%Y-%m-%d'):