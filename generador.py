class Congruencial:

    numeros = []
    a = 21
    c = 471
    m = 10000

    def __init__(self, x0):
        self.x0 = x0
        self.xn = x0
        Congruencial.numeros.append(self.x0)

    def genera(self):
        numero = (Congruencial.a * self.xn + Congruencial.c) % Congruencial.m

        if numero in self.numeros:
            print("Error: El generador acaba de cumplir su ciclo")
            self.xn = numero
            return numero
        else:
            Congruencial.numeros.append(numero)
            self.xn = numero
            return numero