from src.load_polar import load_polar
from src.polar import polar

def main():

    naca_file="data/xf-naca2412-il-100000-n5.csv"
    testpolar = load_polar("naca_2412",naca_file)

    cl = testpolar.coeff_calc('cl',11.001)
    print(cl)

    return 0

main()