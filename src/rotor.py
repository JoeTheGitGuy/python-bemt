'''
Represent complete wing geometry.
Owns interface to bem_solver and multi-element interactions
(eg. total lift, tip loss adjustment).
References BladeElement class to consolidate a system of elements
into a single object.
'''

from src.blade_element import BladeElement

class Rotor:
    """Single interface to bem_solver and owns multi-element interactions"""
    def __init__(self,n_blades:int,n_elements:int,r_disc:float,r_hub:float,blade_elements:list[BladeElement]):
        self.n_blades = n_blades
        self.n_elements = n_elements
        self.r_disc = r_disc
        self.r_hub = r_hub
        self.blade_elements = blade_elements