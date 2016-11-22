from time import gmtime
from generador import Congruencial

class Falla:

    def __init__(self):
        self.random = Congruencial(gmtime().tm_sec)
        self.falla = False
        self.mal_clima = False
        self.tiempo = 0
        self.matenimiento = False

    def mecanica(self):
        self.tiempo = (self.random.genera() % 10) + 2
        if self.tiempo > 7:
            self.matenimiento = True


    def climatico(self):
        nada = True


    def cancelacion(self):
        nada = True