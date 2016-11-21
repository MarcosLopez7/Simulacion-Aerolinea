class Pasajero:

    equi_perdido = False
    id = 1

    def __init__(self, equipaje, vuelo_ida, vuelo_vuelta, discapacidad):
        self.id = Pasajero.id
        self.equipaje = equipaje
        self.vuelo_ida = vuelo_ida
        self.vuelo_vuelta = vuelo_vuelta
        self.discapacidad = discapacidad
        Pasajero.id += 1

    def __str__(self):
        if self.vuelo_vuelta != None:
            return "pasajero {0}, vuelo ida: {1} vuelo vuelta: {2}".format(self.id, self.vuelo_ida['origen'], self.vuelo_vuelta['origen'])
        else:
            return "pasajero {0}, vuelo ida: {1}".format(self.id, self.vuelo_ida['origen'])