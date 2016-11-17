from .compra import Compra
from .avion import Avion

class Aerolinea:

    dinero_ganado = 0
    dinero_gastado = 0

    avion1 = Avion("787 Dreamliner", 243, 900)
    avion2 = Avion("B-737-800", 160, 840)
    avion3 = Avion("EMB-170", 76, 830)

    def __init__(self):
