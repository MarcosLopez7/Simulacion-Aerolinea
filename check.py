from avion import Avion
from aerolinea import Aerolinea
from pasajero import Pasajero
from generador import Congruencial
from datetime import datetime, timedelta
from time import gmtime
from abordaje import Abordaje
from shuttle import Shuttle
from depegue import Despegue
from falla import Falla

class CheckIn:
	def __init__(self):
		pasajeros = 0
	def sobrepeso(self,num,pasajeros):
		peso_excedente = 0
		costo_pk_exc = 100
		generador = Congruencial(100)
		for i in range(0,num+1):
			rand = generador.genera()%len(pasajeros)
			if pasajeros[rand].equipaje > 25:
				peso_excedente += pasajeros[rand].equipaje - 25
		print("Dinero por sobrepeso (%d) Kg: $%d"%(peso_excedente,peso_excedente*costo_pk_exc))
		
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
		num_pasajeros_iniciales = num_pasajeros
		while num_pasajeros > 0:
			hora_4 = 0 
			hora_5 = 0
			hora_6 = 0 
			hora_7 = 0
			atendidos = 0
			hora_may_8 = 0
			#print("------------%d-----------------"%i)
			#print("Numero de pasajeros en cola %d" %num_pasajeros)
			rand = int(datetime.strftime(datetime.now(), '%H'))
			hora = ((generador.genera())*(rand*(i*2))) % 100
			if hora < 20 and hora >= 0:
				prob_solicitudes = 0.2
				hora_4 = 1
			elif hora < 50 and hora >= 20:
				prob_solicitudes = 0.3
				hora_5 = 1
			elif hora < 85 and hora >=50:
				prob_solicitudes = 0.35
				hora_6 = 1
			elif hora < 95 and hora >= 85:
				prob_solicitudes = 0.1
				hora_7 = 1
			elif hora <= 100 and hora >= 95:
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
			elif numero_t <= 100 and numero_t >= 90:
				tiempo_atencion = 1
			#Tomando en cuenta la hora
			#print("Resultado de la probabilidad %d" %(int(num_pasajeros * prob_solicitudes)))
			pasajeros_por_atender = (int(num_pasajeros * prob_solicitudes))
			num_pasajeros -= pasajeros_por_atender
			#print("num_pasajeros despues de atender %d"%num_pasajeros)
			i+=1
			#Comparaciones
			#print("Atendiendo %d en %d tiempo" %(pasajeros_por_atender,tiempo_atencion))
			if atendidos < num_pasajeros:
				if num_pasajeros > 0 and pasajeros_por_atender < 1:
					#print("Entre en esto")
					atendidos += num_pasajeros
					num_pasajeros = 0
				else:
					atendidos += pasajeros_por_atender
				tiempo_total += (pasajeros_por_atender*tiempo_atencion)
			else:
				print("Algo salio mal")
				#print ("Faltaron de atender %d " %(num_pasajeros - (atendidos + pasajeros_por_atender)))

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
			#print("[%d] atendidos: %d" %(i,atendidos))
			#print ("[%d]: El promedio de llegada pasajeros es %f " %(i,(atendidos/num_pasajeros_iniciales)))
		#print ("Se atendieron %d pasajeros" %atendidos)
		perdidos = int(num_pasajeros_iniciales*0.10)
		#print (" %d pasajeros tendran sobrepeso: %f" %(perdidos,perdidos*200)) #200 USD por cada pasajero
		#print ("El tiempo_total es %d" %tiempo_total)
		
		#self.sobrepeso(perdidos,pasajeros)
		print ("--------- Check In --------")
		print ("Atendidos a las 5 horas antes del vuelo: %d" %hora_4_t)
		print ("Atendidos a las 4 %d" %hora_5_t)
		print ("Atendidos a las 3 %d" %hora_6_t)
		print ("Atendidos a las 2 %d" %hora_7_t)
		print ("Atendidos a las 1 o menos: %d" %hora_may_8_t)

	def makeCheckInMexico(self,pasajeros,vuelos):
		shut = Shuttle()
		abor = Abordaje()
		des = Despegue()
		fallas = Falla()
		abordaje_total = 0
		comb_total = 0
		serv_total = 0
		shuttle_total = 0
		descon_total = 0
		tax_at_total = 0
		mantto_total = 0
		abordaje_avg = 0
		serv_avg = 0
		shuttle_avg = 0
		descon_avg = 0
		tax_at_avg = 0
		mantto_avg = 0
		comb_avg = 0
		num_pasajeros_avg = 0
		print ("CheckIn de Mexico a Francia")
		for j in range(44,len(vuelos),2):#len(vuelos)):
			num_pasajeros = 0
			pasajeros_en_vuelo = []
			for i in range(0,len(pasajeros)):
				if (pasajeros[i].vuelo_ida['fecha'] == vuelos[j]['fecha']):
					num_pasajeros += 1
					pasajeros_en_vuelo.append(pasajeros[i])
			#print(num_pasajeros)
			

			if num_pasajeros > 0:
				self.colaCheckIn(pasajeros_en_vuelo,vuelos,num_pasajeros)
			else:
				print ("Para la fecha %s no hay pasajeros" %(vuelos[j]['fecha']))
			comb_total = abor.repostajeCombustible(vuelos[j])
			comb_avg += comb_total
			descon_total = abor.descongelamiento(vuelos[j])
			descon_avg += descon_total
			abordaje_total = self.makeBoarding(pasajeros_en_vuelo,vuelos[j])
			abordaje_avg += abordaje_total
			tax_at_total = 	des.taxing(vuelos[j])
			tax_at_avg += tax_at_total
			serv_total = abor.servicioDeAeromozas(vuelos[j],pasajeros_en_vuelo)
			serv_avg += serv_total
			shuttle_total = shut.cargarShuttle(vuelos[j],pasajeros_en_vuelo)
			shuttle_avg += shuttle_total
			num_pasajeros_avg += num_pasajeros
			#falla_meca = fallas.mecanica()
			print("-----------------------------")
			print("Vuelo %d" %(j))
			print("-----------------------------")
			print("Fecha: %s"%vuelos[j]['fecha'])
			print("Mes: %s"%(vuelos[j]['fecha'])[5:7])
			print("Boletos comprados: %d"%num_pasajeros)
			#print("Tiempo de Check In: %d minutos"%checkin_total)
			#if falla_meca == 0:
		#		print("Hay falla mecanica")
			#if mal_clima == True:
	#			print("Hay mal clima")
			#print("Vuelo cancelado? %d"%cancelado)
			#print("Tiempo atrasado"%tiempo_atraso)
			print("Tiempo de Repostaje de Combustible %d"%comb_total)
			print("Tiempo de Descongelamiento: %d" %descon_total)
			print("Tiempo de Abordaje: %d minutos"%abordaje_total)
			#print("Tiempo de Mantenimiento: %d minutos"%mantto_total)
			print("Tiempo de espera a despegar: %d minutos"%tax_at_total)
			print("Tiempo de Servicio: %d minutos"%serv_total)
			print("Tiempo de Shuttle: %d minutos" %shuttle_total)

		print("-----Fin Mexico-----")
		print("Promedio Boletos comprados: %d"%(int(num_pasajeros_avg)/730))
		print("Promedio de tiempo de Repostaje de Combustible %d"%(int(comb_avg)/730))
		print("Promedio de tiempo de Descongelamiento: %d" %(int(descon_avg)/730))
		print("Promedio de tiempo de Abordaje: %d minutos"%(int(abordaje_avg)/730))
		#print("Tiempo de Mantenimiento: %d minutos"%mantto_total)
		print("Promedio de tiempo de espera a despegar: %d minutos"%(int(tax_at_avg)/730))
		print("Promedio de tiempo de Servicio: %d minutos"%(int(serv_avg)/730))
		print("Promedio de tiempo de Shuttle: %d minutos" %(int(shuttle_avg)/730))

	def makeCheckInFrancia(self,pasajeros,vuelos):
		shut = Shuttle()
		abor = Abordaje()
		des = Despegue()
		fallas = Falla()
		abordaje_total = 0
		comb_total = 0
		serv_total = 0
		shuttle_total = 0
		descon_total = 0
		tax_at_total = 0
		mantto_total = 0
		abordaje_avg = 0
		serv_avg = 0
		shuttle_avg = 0
		descon_avg = 0
		tax_at_avg = 0
		mantto_avg = 0
		comb_avg = 0
		num_pasajeros_avg = 0
		print ("CheckIn de Francia a Mexico")
		for j in range(45,len(vuelos),2):#len(vuelos)):
			pasajeros_en_vuelo = []
			num_pasajeros = 0
			for i in range(0,len(pasajeros)):
				if (pasajeros[i].vuelo_ida['fecha'] == vuelos[j]['fecha']):
					num_pasajeros += 1
					pasajeros_en_vuelo.append(pasajeros[i])
			#print(num_pasajeros)
			print("Vuelo %d" %(j))
			if num_pasajeros > 0:
				self.colaCheckIn(pasajeros_en_vuelo,vuelos,num_pasajeros)
			else:
				print ("Para la fecha %s no hay pasajeros" %(vuelos[j]['fecha']))
			comb_total = abor.repostajeCombustible(vuelos[j])
			comb_avg += comb_total
			descon_total = abor.descongelamiento(vuelos[j])
			descon_avg += descon_total
			abordaje_total = self.makeBoarding(pasajeros_en_vuelo,vuelos[j])
			abordaje_avg += abordaje_total
			tax_at_total = 	des.taxing(vuelos[j])
			tax_at_avg += tax_at_total
			serv_total = abor.servicioDeAeromozas(vuelos[j],pasajeros_en_vuelo)
			serv_avg += serv_total
			shuttle_total = shut.cargarShuttle(vuelos[j],pasajeros_en_vuelo)
			shuttle_avg += shuttle_total
			num_pasajeros_avg += num_pasajeros
			print("-----------------------------")
			print("Vuelo %d" %(j))
			print("-----------------------------")
			print("Fecha: %s"%vuelos[j]['fecha'])
			print("Mes: %s"%(vuelos[j]['fecha'])[5:7])
			print("Origen: %s"%vuelos[j]['origen'])
			print("Destino: %s"%vuelos[j]['destino'])
			print("Boletos comprados: %d"%num_pasajeros)
			#print("Tiempo de Check In: %d minutos"%checkin_total)
			#if falla_meca == 0:
			#	print("Hay falla mecanica")
			#if mal_clima == True:
			#	print("Hay mal clima")
			#print("Vuelo cancelado? %d"%cancelado)
			#print("Tiempo atrasado"%tiempo_atraso)
			print("Tiempo de Repostaje de Combustible %d"%comb_total)
			print("Tiempo de Descongelamiento: %d" %descon_total)
			print("Tiempo de Abordaje: %d minutos"%abordaje_total)
			#print("Tiempo de Mantenimiento: %d minutos"%mantto_total)
			print("Tiempo de espera a despegar: %d minutos"%tax_at_total)
			print("Tiempo de Servicio: %d minutos"%serv_total)
			print("Tiempo de Shuttle: %d minutos" %shuttle_total)
		print("-----Fin Francia-----")
		print("Promedio Boletos comprados: %d"%(int(num_pasajeros_avg)/730))
		print("Promedio de tiempo de Repostaje de Combustible %d"%(int(comb_avg)/730))
		print("Promedio de tiempo de Descongelamiento: %d" %(int(descon_avg)/730))
		print("Promedio de tiempo de Abordaje: %d minutos"%(int(abordaje_avg)/730))
		#print("Tiempo de Mantenimiento: %d minutos"%mantto_total)
		print("Promedio de tiempo de espera a despegar: %d minutos"%(int(tax_at_avg)/730))
		print("Promedio de tiempo de Servicio: %d minutos"%(int(serv_avg)/730))
		print("Promedio de tiempo de Shuttle: %d minutos" %(int(shuttle_avg)/730))
	def makeBoarding(self,pasajeros,vuelo):
		abordaje = Abordaje()
		return abordaje.abordar(pasajeros,vuelo)
		

		