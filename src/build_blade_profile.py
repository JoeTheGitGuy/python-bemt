from src.aerofoil import Aerofoil
from src.blade_element import BladeElement

def build_blade_profile(aerofoil_brkpts:list[float,Aerofoil],n_elements:int,dr:float,total_twist:float,chord:float,taper_ratio:float) -> list[BladeElement]:
    # code that generates a bunch of BladeElements and assigns them local twist, radial position (r), local chord (based on linear taper)
    # unsure on how to implement being able to change aerofoil across the radius... accept list of [radial position end-points, NACA name] pairs? Would mean no need for total radial length as it's inferred from this value-name input
    for i in range(n_elements):
        aerofoil = aerofoil_brkpts[0][0]
        r = (dr*i)+(dr/2)
        blade_profile = [BladeElement(aerofoil,r)]

    return blade_profile