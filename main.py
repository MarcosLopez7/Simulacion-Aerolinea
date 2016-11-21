from aerolinea import Aerolinea
from check import CheckIn

def main():
    aerolinea = Aerolinea()
    checkin = CheckIn()
    aerolinea.compras()
    checkin.makeCheckInMexico(aerolinea.pasajeros,aerolinea.vuelos)

if __name__ == "__main__":
    main()
