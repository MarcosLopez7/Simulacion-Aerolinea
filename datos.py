import json
from datetime import date, datetime, timedelta, time

class Datos:

    def __init__(self):
        self.archivo = None

    def datos(self):
        self.archivo = open('data.json', 'w')

        datos = {'vuelos': [], 'aviones': [
            {
                "tipo": "787 Dreamliner",
                "pasajeros": 243,
                "velocidad": 900
            },
            {
                "tipo": "B-737-800",
                "pasajeros": 160,
                "velocidad": 840
            },
            {
                "tipo": "EMB-170",
                "pasajeros": 76,
                "velocidad": 830
            }
        ]}

        for i in range(-20, 450):
            objecto1 = {
                'avion': {
                    'tipo': '787 Dreamliner',
                    'pasajeros': 243,
                    'disponibilidad': 243,
                    'velocidad': 900
                },
                'fecha': datetime.strftime(datetime.now() + timedelta(days=i), '%Y-%m-%d'),
                'origen': 'Mexico',
                'destino': 'Francia',
                'hora_salida': '800',
                'hora_llegada': '2000'
            }

            objecto2 = {
                'avion': {
                    'tipo': '787 Dreamliner',
                    'pasajeros': 243,
                    'disponibilidad': 243,
                    'velocidad': 900
                },
                'fecha': datetime.strftime(datetime.now() + timedelta(days=i), '%Y-%m-%d'),
                'origen': 'Francia',
                'destino': 'Mexico',
                'hora_salida': '2000',
                'hora_llegada': '800'
            }

            datos['vuelos'].append(objecto1)
            datos['vuelos'].append(objecto2)

        self.archivo.write(json.dumps(datos))