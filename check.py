from avion import Avion
from pasajero import Pasajero
class CheckIn:
	def __init__(self):
		pasajeros = 0


	def makeCheckInMexico(self,pasajeros,vuelos):
		print "CheckIn de Mexico"
		print vuelos[0].fecha
		for i in range(1,len(pasajeros)+1,2):
			print "El pasajero tiene el id %d" %(pasajeros[i].id)
			print "El vuelo que tiene el pasajero %d es %s" %(pasajeros[i].id,pasajeros[i].vuelo_ida)
			#print if vuelos[i]['fecha'] == datetime.strftime(datetime.now() + timedelta(days=vuelo_rand, hours=h),
                                                        #   '%Y-%m-%d'):