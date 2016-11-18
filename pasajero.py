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