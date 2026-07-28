from src.environment import Environment
from src.load_polar import load_polar
from src.aerofoil import Aerofoil
from src.build_blade_elements import build_blade_elements
from src.rotor import Rotor

def main():

    test = False

    #environment = Environment(9.81,1.225,1.79*(10**-5),343,50,20)

    naca2412_il = [load_polar("data/xf-naca2412-il-50000-n5.csv"),
                   load_polar("data/xf-naca2412-il-100000-n5.csv"),
                   load_polar("data/xf-naca2412-il-500000-n5.csv")]

    aerofoil_2412_il = Aerofoil("2412_il",naca2412_il)
    blade = build_blade_elements([[100,aerofoil_2412_il]],10,1,10,1,0.8)
    rotor = Rotor(4,10,3,0.15,blade)

    #solver = bem_solver(enviroment,blade)

    if test == True:
        # blade element factory testing
        for i in blade:
            print("chord ", i.chord)
            print("dr ", i.dr)
            print("r ", i.r)
            print("twist ", i.twist)

        print(aerofoil_2412_il.name)

        # reynolds fetching testing
        if aerofoil_2412_il.get_polar(500000).reynolds == 500000:
            print("Polar for Re=500000 fetches correctly!")
        if aerofoil_2412_il.get_polar(100000).reynolds == 100000:
            print("Polar for Re=100000 fetches correctly!")
        if aerofoil_2412_il.get_polar(50000).reynolds == 50000:
            print("Polar for Re=100000 fetches correctly!")

        # polar interp testing
        test_tolerance = 0.001
        polar = aerofoil_2412_il.get_polar(500000)
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