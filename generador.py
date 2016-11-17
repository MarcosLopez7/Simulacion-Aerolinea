class Congruencial:

    numeros = []
    a = 0
    c = 0
    m = 0

    def __init__(self, x0):
        self.x0 = x0
        self.xn = x0
        self.numeros.append(self.x0)

    def genera(self):
        numero = (self.a * self.xn + self.c) % self.m

        if numero in self.numeros:
            print("Error: El generador acaba de cumplir su ciclo")
            self.xn = numero
            return numero
        else:
            self.numeros.append(numero)
            self.xn = numero
            return numero