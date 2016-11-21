from avion import Avion
from pasajero import Pasajero
class CheckIn:
	def __init__(self):
		pasajeros = 0


	def makeCheckInMexico(self,pasajeros,vuelos):
		print ("CheckIn de Mexico")
		num_pasajeros = 0
		for i in range(0,len(pasajeros)):
			#print (vuelos[0]['fecha'])
			#print ("%d %s" %(i, vuelos[i]['fecha']))#pasajeros[i].vuelo_ida['fecha']))
			if (pasajeros[i].vuelo_ida['fecha'] == vuelos[1]['fecha']):
				num_pasajeros += 1
		print(num_pasajeros)
		#for i in range(1,len(pasajeros),2):
		#	print ("El pasajero tiene el id %d" %(pasajeros[i].id))
			#print ("El vuelo que tiene el pasajero %d es %s" %(pasajeros[i].id,pasajeros[i].vuelo_ida))
			#print if vuelos[i]['fecha'] == datetime.strftime(datetime.now() + timedelta(days=vuelo_rand, hours=h),
                                                        #   '%Y-%m-%d'):