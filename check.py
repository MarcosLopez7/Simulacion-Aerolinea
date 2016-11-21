from avion import Avion
from pasajero import Pasajero
from generador import Congruencial
class CheckIn:
	def __init__(self):
		pasajeros = 0

	def colaCheckIn(self,pasajeros,vuelos,num_pasajeros):
		generador = Congruencial(200)
		atendidos = 0
		tiempo_total = 0
		for i in range(0,num_pasajeros):
			numero = generador.genera()
			numero = (numero/(generador.m/100))/100
			numero = numero * 1.0
			print("El numero generado de pasajeros es %.2f" %numero)
			if numero < 0.30 and numero >= 0.0:
				pasajeros_por_atender = 1
			elif numero < 0.45 and numero >= 0.3:
				pasajeros_por_atender = 2
			elif numero < 0.66 and numero >= 0.45:
				pasajeros_por_atender = 3	
			elif numero < 0.77 and numero >= 0.66:
				pasajeros_por_atender = 4
			elif numero < 0.9 and numero >= 0.77:
				pasajeros_por_atender = 5
			else:
				pasajeros_por_atender = 6
			#Tiempo de atencion por pasajero
			numero_t = generador.genera()
			numero_t = (numero_t/(generador.m/100))/100
			if numero_t < 0.3 and numero_t >= 0.0:
				 tiempo_atencion = 5
			elif numero_t < 0.45 and numero_t >= 0.3:
				 tiempo_atencion = 10
			elif numero_t < 0.66 and numero_t >= 0.45:
				 tiempo_atencion = 7
			elif numero_t < 0.77 and numero_t >= 0.66:
				 tiempo_atencion = 13
			elif numero_t < 0.9 and numero_t >= 0.77:
				 tiempo_atencion = 3
			else:
				tiempo_atencion = 1
			#Comparaciones
			print("Atendiendo %d en %f tiempo" %(pasajeros_por_atender,tiempo_atencion))
			if atendidos < num_pasajeros:
				atendidos += pasajeros_por_atender
				tiempo_total += (pasajeros_por_atender*tiempo_atencion)
			else:
				print ("Faltaron de atender %d " %((atendidos + pasajeros_por_atender)-num_pasajeros))

		print ("El promedio de pasajeros es %f " %(atendidos/num_pasajeros))
		print ("El tiempo_total es %f" %tiempo_total)
		print ("Se atendieron %d pasajeros" %atendidos)

	def makeCheckInMexico(self,pasajeros,vuelos):
		print ("CheckIn de Mexico")
		for j in range(40,60,2):#len(vuelos)):
			num_pasajeros = 0
			for i in range(0,len(pasajeros)):
			#print ("%d %s %s" %(i, pasajeros[i].vuelo_ida['fecha'],vuelos[100]['fecha']))#pasajeros[i].vuelo_ida['fecha']))
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