from src.load_polar import load_polar
from src.aerofoil import Aerofoil

def main():

    naca2412_il = [load_polar("data/xf-naca2412-il-50000-n5.csv"),
                   load_polar("data/xf-naca2412-il-100000-n5.csv"),
                   load_polar("data/xf-naca2412-il-500000-n5.csv")]

    aero1 = Aerofoil("2412_il",naca2412_il)

    if aero1.get_polar(500000).reynolds == 500000:
        print("Polar for Re=500000 fetches correctly!")
    if aero1.get_polar(100000).reynolds == 100000:
            print("Polar for Re=100000 fetches correctly!")
    if aero1.get_polar(50000).reynolds == 50000:
                print("Polar for Re=100000 fetches correctly!")

    print(aero1.name,":")

    # test suite
    test_tolerance = 0.001
    polar = aero1.get_polar(500000)
    if polar.coeff_calc('cl',11) - 1.3005 <= test_tolerance:
        print("Polar correctly looked up known datapoint!")
    else:
        raise ValueError("Polar FAILED to looked up known datapoint!")
    if polar.coeff_calc('cl',0.5*(11.000+11.250)) - 0.5*(1.3005+1.3156) <= test_tolerance:
        print("Polar correctly interpolated between datapoints!")
    else:
        raise ValueError("Polar FAILED to interpolate datapoints!")
    return 0

# if someone wants to import this for some reason, do not run on import.
if __name__ == '__main__':
    main()