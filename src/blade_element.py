'''
Represents a geometrically uniform, thin 3D segment of a rotor.
Owns radial length, position, twist.
References the Aerofoil class for aerodynamic datasets.
'''

from src.aerofoil import Aerofoil

class BladeElement:
    """Owns position, and orientation of a thin blade section,
    referencing aerodynamic characteristics via Aerofoil class"""
    def __init__(self,aerofoil:Aerofoil,r:float,dr:float,twist:float,chord:float,alpha:float):
        self.aerofoil = aerofoil
        self.r = r
        self.dr = dr
        self.twist = twist
        self.chord = chord
        self.alpha = alpha