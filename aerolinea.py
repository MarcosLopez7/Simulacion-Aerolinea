import json
from datetime import datetime, timedelta
from time import gmtime
from compra import Compra
from avion import Avion
from falla import Falla
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
            self.vuelos = data['vuelos']
            self.aviones = data['aviones']

    def compras(self):
        compra = Compra()

        for i in range(1, 366 * 24):
            hora = int(datetime.strftime(datetime.now() + timedelta(hours=i), '%H'))

            if hora > 5:
                prob_solicitudes = 1
            elif hora > 7:
                prob_solicitudes = 10
            elif hora > 9:
                prob_solicitudes = 40
            elif hora > 11:
                prob_solicitudes = 55
            elif hora > 18:
                prob_solicitudes = 80
            elif hora > 20:
                prob_solicitudes = 60
            elif hora > 22:
                prob_solicitudes = 30
            else:
                prob_solicitudes = 20

            mes = datetime.strftime(datetime.now() + timedelta(hours=i), '%%m')

            if mes == '12' or mes == '08' or mes == '06' or mes == '07':
                prob_solicitudes *= 4

            random = (self.random.genera() % 100) + 1

            if prob_solicitudes > random:
                if 10 > random:
                    compra.compra(self.pasajeros, 5, self.vuelos, i)
                elif 25 > random:
                    compra.compra(self.pasajeros, 4, self.vuelos, i)
                elif 50 > random:
                    compra.compra(self.pasajeros, 3, self.vuelos, i)
                elif 75 > random:
                    compra.compra(self.pasajeros, 2, self.vuelos, i)
                else:
                    compra.compra(self.pasajeros, 1, self.vuelos, i)

            #print(i)

        #print(len(self.pasajeros))

    def procesos(self):

        falla_mexico = Falla()
        falla_francia = Falla()


        for i in range(1, 366 * 24):
            hora = int(datetime.strftime(datetime.now() + timedelta(hours=i), '%H'))


            if hora == 6:
                rand_falla_mecanica = (self.random.genera() % 100)

                if 1 > rand_falla_mecanica:
                    falla_mexico.falla = True
                    falla_mexico.mecanica()

            if hora == 18:
                rand_falla_mecanica = (self.random.genera() % 100)

                if 1 > rand_falla_mecanica:
                    falla_francia.falla = True
                    falla_francia.mecanica()

            if hora == 7 and not falla_mexico.matenimiento:
                rand_clima = (self.random.genera() % 100)

                if 5 > rand_clima:
                    falla_mexico.mal_clima = True
                    falla_mexico.climatico()
            elif hora == 7 and falla_mexico.matenimiento:
                fecha = datetime.strftime(datetime.now() + timedelta(hours=i), '%Y-%m-%d')
                for i in range(0, len(self.vuelos), 2):
                    if fecha == self.vuelos[i]['fecha']:
                        if self.aviones[1]['mantenimiento'] and self.aviones[1]['enuso']:
                            self.vuelos[i]['avion']


            if hora == 19:
                rand_clima = (self.random.genera() % 100)

                if 5 > rand_clima:
                    falla_francia.mal_clima = True
                    falla_francia.climatico()









