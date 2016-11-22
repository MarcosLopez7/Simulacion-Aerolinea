from datetime import datetime, timedelta
from time import gmtime
from generador import Congruencial

class Falla:

    def __init__(self):
        self.random = Congruencial(gmtime().tm_sec)
        self.falla = False
        self.mal_clima = False
        self.tiempo = 0
        self.matenimiento = False
        self.perdidas = 0
        self.congelamiento = False

    def mecanica(self):
        random = self.random.genera() % 100

        if 1 > random:
            return (self.random.genera() % 10) + 2
        else:
            return 0


    def climatico(self, h, indice):

        mes = datetime.strftime(datetime.now() + timedelta(hours=h), '%m')
        probabilidad_mal_clima = 1
        if mes == '08' or mes == '06' or mes == '07':
            probabilidad_mal_clima *= 5

        random = self.random.genera() % 100

        if probabilidad_mal_clima > random:
            self.tiempo = (self.random.genera() % 8) + 1
            self.mal_clima = True

        if indice % 2 == 1:
            if mes == '12' or mes == '01' or mes == '02':
                proba_congelamiento = 25
                random = self.random.genera() % 100
                if proba_congelamiento > random:
                    self.congelamiento = True

        return self.tiempo


    def cancelacion(self, vuelos, pasajeros, indice, h):

        num_pasajeros = vuelos[indice]['avion']['pasajeros'] - vuelos[indice]['disponibilidad']
        disponibilidad_aerolineas = self.random.genera() % 100
        num_pasajeros -= disponibilidad_aerolineas
        mes = datetime.strftime(datetime.now() + timedelta(hours=h), '%m')
        if mes == '12' or mes == '08' or mes == '06' or mes == '07':
            self.perdidas += 18000 * 2 * disponibilidad_aerolineas
        else:
            self.perdidas += 18000 * disponibilidad_aerolineas

        indice += 2

        while num_pasajeros > 0:
            if vuelos[indice]['disponibilidad'] > 0:
                num_pasajeros -= vuelos[indice]['disponibilidad']
                self.perdidas += 2000 * disponibilidad_aerolineas
            else:
                indice += 2