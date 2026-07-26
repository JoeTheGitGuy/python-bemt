from src.rotor import Rotor

def build_rotor(n_blades,blade_profile,r_disc,r_hub,n_elements) -> Rotor:
    n_blades = 4
    n_elements = 10
    r_disc = 1.5
    r_hub = 0.15
    blade_profile = blade_profile
    return Rotor(n_blades,n_elements,r_disc,r_hub,blade_profile)