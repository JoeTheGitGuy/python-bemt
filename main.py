from src.load_polar import load_polar
from src.aerofoil import Aerofoil

def main():

    naca2412_il = [load_polar("data/xf-naca2412-il-50000-n5.csv"),
                   load_polar("data/xf-naca2412-il-100000-n5.csv"),
                   load_polar("data/xf-naca2412-il-500000-n5.csv")]

    aero1 = Aerofoil("2412_il",naca2412_il)
    print(aero1.name,":")
    polar = aero1.get_polar(500000)
    print(polar.coeff_calc('cl',11.001))

    return 0
main()