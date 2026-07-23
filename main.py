from src.load_polar import LoadPolar
from src.aerofoil import Aerofoil

def main():

    naca_file="data/xf-naca2412-il-100000-n5.csv"
    polar = LoadPolar("naca_2412",naca_file)
    TestAerofoil = Aerofoil(polar);

    cl = TestAerofoil.cl(11.001)
    print(cl)

    return 0

main()