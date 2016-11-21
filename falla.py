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
        congelamiento_rand = self.random.genera() % 100

        if 30 > congelamiento_rand:
            self.tiempo = (self.random.genera() % 3) + 1
        else:
            self.tiempo = (self.random.genera() % 3) + 3
            self.matenimiento = True


    def climatico(self):
        nada = True

