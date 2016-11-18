from time import gmtime
from pasajero import Pasajero
from generador import Congruencial

class Compra:

    ventas = 0
    lam = 0
    miu = 0
    cola_presencial = []

    def __init__(self):
        self.random = Congruencial(gmtime().tm_sec)

    def compra(self, pasajeros, cantidad, vuelos):

        for i in range(cantidad):
            num_rand = self.random.genera() % 100

            if num_rand > 19:
                pasajeros.append(self.enlinea(vuelos))
            elif num_rand > 4:
                pasajeros.append(self.agencia(vuelos))
            else:
                pasajeros.append(self.presencial(vuelos))

    def enlinea(self, vuelos):

        while True:
            vuelo_rand = (self.random.genera() % 30)
            vuelo = vuelos[vuelo_rand * 2]
            if vuelo.disponibilidad > 0:
                nada = None



        pasajero = Pasajero(self.random.genera() % 30)






    def presencial(self, vuelos):
        nada = None


    def agencia(self, vuelos):
        nada = None
