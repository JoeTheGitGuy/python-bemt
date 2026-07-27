from src.aerofoil import Aerofoil
from src.blade_element import BladeElement

def build_blade_profile(aerofoil_brkpts:list[float,Aerofoil],n_elements:int,L:float,total_twist:float,root_chord:float,taper_ratio:float) -> list[BladeElement]:
    # code that generates a bunch of BladeElements and assigns them local twist, radial position (curr_r), local chord (based on linear taper)
    # unsure on how to implement being able to change aerofoil across the radius... accept list of [radial position end-points, NACA name] pairs? Would mean no need for total radial length as it's inferred from this value-name input

    # initialise
    blade_profile = []
    brkpts_idx = int(0)
    num_brkpts = len(aerofoil_brkpts[:][0])

    dr = L/n_elements
    dtheta = total_twist/n_elements
    dchord = root_chord*(taper_ratio-1)/n_elements # from c0+dc*n_el=cn=c0*taper_ratio
    curr_theta = total_twist - dtheta/2
    curr_r = dr/2
    curr_chord = root_chord + dchord/2

    for i in range(n_elements):
        # assign aerofoil based on position vs breakpoints
        # block incrementing brkpts if at end of list
        if (curr_r > aerofoil_brkpts[brkpts_idx][0]) and (brkpts_idx < num_brkpts):
            brkpts_idx = brkpts_idx+1
        aerofoil = aerofoil_brkpts[brkpts_idx][1]

        blade_profile.append(BladeElement(aerofoil,curr_r,dr,curr_theta,curr_chord))

        # increment properties
        curr_r      = curr_r + dr
        curr_theta  = curr_theta - dtheta
        curr_chord  = curr_chord + dchord

    return blade_profile