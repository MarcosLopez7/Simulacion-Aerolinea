from time import gmtime
from .pasajero import Pasajero
from .generador import Congruencial

class Compra:

    ventas = 0
    lam = 0
    miu = 0
    cola_presencial = []

    def __init__(self):
        self.random = Congruencial(gmtime().tm_sec)

    def compra(self):
        personas = 100

        for i in range(personas):




    def enlinea(self):


    def presencial(self):


    def agencia(self):

