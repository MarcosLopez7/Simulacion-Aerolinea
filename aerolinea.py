import json
from time import gmtime
from compra import Compra
from avion import Avion
from generador import Congruencial

class Aerolinea:

    dinero_ganado = 0
    dinero_gastado = 0
    pasajeros = []
    vuelos = []
    aviones = []

    def __init__(self):
        with open('data.json') as data_file:
            data = json.load(data_file)
            self.random = Congruencial(gmtime().tm_sec)

    def compras(self):
        compra = Compra()

        for i in range(1, 366 * 24):
            compra.compra(self.pasajeros, self.random.genera() % 100, self.vuelos)

