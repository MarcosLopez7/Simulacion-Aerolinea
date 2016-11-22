import json
from datetime import date, datetime, timedelta, time

class Datos:

    def __init__(self):
        self.archivo = None

    def datos(self):

        id = 1

        self.archivo = open('data.json', 'w')

        datos = {'vuelos': [], 'aviones': [
            {
                "tipo": "787 Dreamliner",
                "pasajeros": 243,
                "velocidad": 900,
                "mantenimiento": False,
                "enuso": True
            },
            {
                "tipo": "B-737-800",
                "pasajeros": 160,
                "velocidad": 840,
                "mantenimiento": False,
                "enuso": False
            },
            {
                "tipo": "EMB-170",
                "pasajeros": 76,
                "velocidad": 830,
                "mantenimiento": False,
                "enuso": False
            }
        ]}

        avion = 1

        for i in range(-20, 450):

            objecto1 = {
                'id': id,
                'avion': {
                    'tipo': '787 Dreamliner',
                    'pasajeros': 243,
                    'disponibilidad': 243,
                    'velocidad': 900,
                    'id': avion
                },
                'fecha': datetime.strftime(datetime.now() + timedelta(days=i), '%Y-%m-%d'),
                'origen': 'Mexico',
                'destino': 'Francia',
                'hora_salida': '2345',
                'hora_llegada': '1100',
                'hora_real_s': '2345',
                'hora_real_l': '1100',
                't_retraso': 0,
                'cancelado': False
            }

            id += 1
            avion *= -1

            objecto2 = {
                'id': id,
                'avion': {
                    'tipo': '787 Dreamliner',
                    'pasajeros': 243,
                    'disponibilidad': 243,
                    'velocidad': 900,
                    'id': avion
                },
                'fecha': datetime.strftime(datetime.now() + timedelta(days=i), '%Y-%m-%d'),
                'origen': 'Francia',
                'destino': 'Mexico',
                'hora_salida': '1500',
                'hora_llegada': '400',
                'hora_real_s': '1500',
                'hora_real_l': '400',
                't_retraso': 0,
                'cancelado': False
            }

            datos['vuelos'].append(objecto1)
            datos['vuelos'].append(objecto2)

            id += 1

        self.archivo.write(json.dumps(datos))