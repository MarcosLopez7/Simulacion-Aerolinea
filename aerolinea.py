import json, math
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
    temporada_alta = False

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
                temporada_alta = True

            random = (self.random.genera() % 100) + 1

            if prob_solicitudes > random:
                if 100 > random:
                    compra.compra(self.pasajeros, 40, self.vuelos, i)
                elif 90 > random:
                    compra.compra(self.pasajeros, 36, self.vuelos, i)
                elif 60 > random:
                    compra.compra(self.pasajeros, 24, self.vuelos, i)
                elif 30 > random:
                    compra.compra(self.pasajeros, 20, self.vuelos, i)
                elif 15 > random:
                    compra.compra(self.pasajeros, 8, self.vuelos, i)
                else:
                    compra.compra(self.pasajeros, 5, self.vuelos, i)


        print(len(self.pasajeros))

    def procesos(self):

        falla_mexico = Falla()
        falla_francia = Falla()

        indice_vuelo_mex = 44
        indice_vuelo_fra = 45
        fecha = datetime.strftime(datetime.now(), '%Y-%m-%d')
        avion_mex = self.vuelos[indice_vuelo_mex]
        avion_fra = self.vuelos[indice_vuelo_fra]

        for i in range(1, 366 * 24):

            fecha_i = datetime.strftime(datetime.now() + timedelta(hours=i), '%Y-%m-%d')

            if fecha != fecha_i:
                indice_vuelo_mex += 2
                indice_vuelo_fra += 2
                avion_mex = self.vuelos[indice_vuelo_mex]['avion']['id']
                avion_fra = self.vuelos[indice_vuelo_fra]['avion']['id']

            hora = int(datetime.strftime(datetime.now() + timedelta(hours=i), '%H'))

            if hora == 22 and not self.vuelos[indice_vuelo_mex - 1]['avion']['cancelado']:
                rand_falla_mecanica = (self.random.genera() % 100)

                if 1 > rand_falla_mecanica:
                    falla_mexico.falla = True
                    falla_mexico.mecanica()

            if hora == 13 and (self.vuelos[indice_vuelo_fra - 3]['t_retraso'] / 60 < 2):
                rand_falla_mecanica = (self.random.genera() % 100)

                if 1 > rand_falla_mecanica:
                    falla_francia.falla = True
                    falla_francia.mecanica()
            elif hora == 13 + math.ceil(self.vuelos[indice_vuelo_fra - 3]['t_retraso'] / 60) - 2:
                rand_falla_mecanica = (self.random.genera() % 100)

                if 1 > rand_falla_mecanica:
                    falla_francia.falla = True
                    falla_francia.mecanica()

            if hora == 23 and not falla_mexico.matenimiento and not self.vuelos[indice_vuelo_fra]['avion']['cancelado']:
                rand_clima = (self.random.genera() % 100)

                if 5 > rand_clima:
                    falla_mexico.mal_clima = True
                    falla_mexico.climatico()
            elif hora == 23 and falla_mexico.matenimiento and not self.vuelos[indice_vuelo_fra]['avion']['cancelado']:
                fecha = datetime.strftime(datetime.now() + timedelta(hours=i), '%Y-%m-%d')
                indice = 0
                for i in range(0, len(self.vuelos), 2):
                    if fecha == self.vuelos[i]['fecha']:
                        indice = i
                        break

                if falla_mexico.matenimiento:
                    self.vuelos[indice]['cancelacion'] = True
                    falla_mexico.cancelacion()


            if hora == 14:
                rand_clima = (self.random.genera() % 100)

                if 5 > rand_clima:
                    falla_francia.mal_clima = True
                    falla_francia.climatico()





