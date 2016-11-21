from time import gmtime
from datetime import datetime, timedelta
from pasajero import Pasajero
from generador import Congruencial

class Compra:

    ventas = 0
    miu = 2
    cola_presencial = 0
    pasaje = 16000

    def __init__(self):
        self.atencion = False
        self.random = Congruencial(gmtime().tm_sec)

    def compra(self, pasajeros, cantidad, vuelos, h):

        for i in range(cantidad):
            num_rand = self.random.genera() % 100

            if num_rand > 19:
                self.enlinea(vuelos, pasajeros, h)
            elif num_rand > 4:
                self.agencia(vuelos, pasajeros, h)
            else:
                self.cola_presencial += 1

        self.vaciar_cola(vuelos, pasajeros, h)

    def vaciar_cola(self, vuelos, pasajeros, h):

        if self.cola_presencial >= 2:
            self.presencial(vuelos, pasajeros, h)
            self.presencial(vuelos, pasajeros, h)
            self.cola_presencial -= 2
        elif self.cola_presencial == 1:
            self.presencial(vuelos, pasajeros, h)
            self.cola_presencial -= 1

    def enlinea(self, vuelos, pasajeros, h):
        personas = self.random.genera() % 5 + 1
        redondo = True
        random = self.random.genera() % 100

        if 20 > random:
            redondo = False

        while True:
            vuelo_rand = (self.random.genera() % 30) + 1
            vuelo = None
            for i in range(len(vuelos)):
                if vuelos[i]['fecha'] == datetime.strftime(datetime.now() + timedelta(days=vuelo_rand, hours=h), '%Y-%m-%d'):
                    vuelo = vuelos[i]
                    break

            if vuelo != None and vuelo['avion']['disponibilidad'] - personas >= 0:
                vuelo['avion']['disponibilidad'] -= personas
                if not redondo:
                    for i in range(personas):
                        discapacidad_rand = self.random.genera() % 100
                        discapacidad = False
                        if 1 > discapacidad_rand:
                            discapacidad = True
                        pasajero = Pasajero(self.random.genera() % 30, vuelo, None, discapacidad)
                        pasajeros.append(pasajero)
                        mes = datetime.strftime(datetime.now() + timedelta(days=vuelo_rand, hours=h), '%Y-%m-%d')
                        if mes == '12' or mes == '08' or mes == '06' or mes == '07':
                            self.ventas += self.pasaje * 2
                        else:
                            self.ventas += self.pasaje
                break
            else:
                print("Si estas funcionando?")

        if redondo:
             while True:
                vacaciones = (self.random.genera() % 30) + 1
                vuelo_vuelta = None
                for i in range(len(vuelos)):
                    if vuelos[i]['fecha'] == datetime.strftime(datetime.now() + timedelta(days=vuelo_rand + vacaciones, hours=h), '%Y-%m-%d'):
                        vuelo_vuelta = vuelos[i + 1]
                        break

                if vuelo_vuelta['avion']['disponibilidad'] - personas >= 0:
                    vuelo_vuelta['avion']['disponibilidad'] -= personas
                    for i in range(personas):
                        discapacidad_rand = self.random.genera() % 100
                        discapacidad = False
                        if 1 > discapacidad_rand:
                            discapacidad = True
                        pasajero = Pasajero(self.random.genera() % 30, vuelo, vuelo_vuelta, discapacidad)
                        pasajeros.append(pasajero)
                        mes = datetime.strftime(datetime.now() + timedelta(days=vuelo_rand, hours=h), '%Y-%m-%d')
                        if mes == '12' or mes == '08' or mes == '06' or mes == '07':
                            self.ventas += self.pasaje * 4
                        else:
                            self.ventas += self.pasaje * 2
                    break
                else:
                    print("Si estas funcionando?")

    def presencial(self, vuelos, pasajeros, h):

        personas = self.random.genera() % 5 + 1
        redondo = True
        random = self.random.genera() % 100

        if 20 > random:
            redondo = False

        while True:
            vuelo_rand = (self.random.genera() % 30) + 1
            vuelo = None
            for i in range(len(vuelos)):
                if vuelos[i]['fecha'] == datetime.strftime(datetime.now() + timedelta(days=vuelo_rand, hours=h),
                                                           '%Y-%m-%d'):
                    vuelo = vuelos[i]
                    break

            if vuelo != None and vuelo['avion']['disponibilidad'] - personas >= 0:
                vuelo['avion']['disponibilidad'] -= personas
                if not redondo:
                    for i in range(personas):
                        discapacidad_rand = self.random.genera() % 100
                        discapacidad = False
                        if 1 > discapacidad_rand:
                            discapacidad = True
                        pasajero = Pasajero(self.random.genera() % 30, vuelo, None, discapacidad)
                        pasajeros.append(pasajero)
                        mes = datetime.strftime(datetime.now() + timedelta(days=vuelo_rand, hours=h), '%Y-%m-%d')
                        if mes == '12' or mes == '08' or mes == '06' or mes == '07':
                            self.ventas += self.pasaje * 2
                        else:
                            self.ventas += self.pasaje
                break
            else:
                print("Si estas funcionando?")

        if redondo:
            while True:
                vacaciones = (self.random.genera() % 30) + 1
                vuelo_vuelta = None
                for i in range(len(vuelos)):
                    if vuelos[i]['fecha'] == datetime.strftime(
                                    datetime.now() + timedelta(days=vuelo_rand + vacaciones, hours=h), '%Y-%m-%d'):
                        vuelo_vuelta = vuelos[i + 1]
                        break

                if vuelo_vuelta['avion']['disponibilidad'] - personas >= 0:
                    vuelo_vuelta['avion']['disponibilidad'] -= personas
                    for i in range(personas):
                        discapacidad_rand = self.random.genera() % 100
                        discapacidad = False
                        if 1 > discapacidad_rand:
                            discapacidad = True
                        pasajero = Pasajero(self.random.genera() % 30, vuelo, vuelo_vuelta, discapacidad)
                        pasajeros.append(pasajero)
                        mes = datetime.strftime(datetime.now() + timedelta(days=vuelo_rand, hours=h), '%Y-%m-%d')
                        if mes == '12' or mes == '08' or mes == '06' or mes == '07':
                            self.ventas += self.pasaje * 4
                        else:
                            self.ventas += self.pasaje * 3
                    break
                else:
                    print("Si estas funcionando?")


    def agencia(self, vuelos, pasajeros, h):
        personas = self.random.genera() % 5 + 1
        redondo = True
        random = self.random.genera() % 100

        if 20 > random:
            redondo = False

        while True:
            vuelo_rand = (self.random.genera() % 30) + 1
            vuelo = None
            for i in range(len(vuelos)):
                if vuelos[i]['fecha'] == datetime.strftime(datetime.now() + timedelta(days=vuelo_rand, hours=h), '%Y-%m-%d'):
                    vuelo = vuelos[i]
                    break

            if vuelo['avion']['disponibilidad'] - personas >= 0:
                vuelo['avion']['disponibilidad'] -= personas
                if not redondo:
                    for i in range(personas):
                        discapacidad_rand = self.random.genera() % 100
                        discapacidad = False
                        if 1 > discapacidad_rand:
                            discapacidad = True
                        pasajero = Pasajero(self.random.genera() % 30, vuelo, None, discapacidad)
                        pasajeros.append(pasajero)
                        mes = datetime.strftime(datetime.now() + timedelta(days=vuelo_rand, hours=h), '%Y-%m-%d')
                        if mes == '12' or mes == '08' or mes == '06' or mes == '07':
                            self.ventas += self.pasaje * 2
                        else:
                            self.ventas += self.pasaje
                break
            else:
                print("Si estas funcionando?")

        if redondo:
            while True:
                vacaciones = (self.random.genera() % 30) + 1
                vuelo_vuelta = None
                for i in range(len(vuelos)):
                    if vuelos[i]['fecha'] == datetime.strftime(datetime.now() + timedelta(days=vuelo_rand + vacaciones, hours=h),
                                                               '%Y-%m-%d'):
                        vuelo_vuelta = vuelos[i + 1]
                        break

                if vuelo_vuelta['avion']['disponibilidad'] - personas >= 0:
                    vuelo_vuelta['avion']['disponibilidad'] -= personas
                    for i in range(personas):
                        discapacidad_rand = self.random.genera() % 100
                        discapacidad = False
                        if 1 > discapacidad_rand:
                            discapacidad = True
                        pasajero = Pasajero(self.random.genera() % 30, vuelo, vuelo_vuelta, discapacidad)
                        pasajeros.append(pasajero)
                    break
                else:
                    print("Si estas funcionando?")

