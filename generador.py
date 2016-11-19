class Congruencial:

    a = 21
    c = 471
    m = 1000000000

    def __init__(self, x0):
        self.x0 = x0
        self.xn = x0

    def genera(self):
        numero = (self.a * self.xn + self.c) % self.m

        if numero == self.x0:
            print("Error: El generador acaba de cumplir su ciclo")
            self.xn = numero
            return numero
        else:
            self.xn = numero
            return numero