'''
Represents 2D aerofoil geometry
Owns linking to relevant datasets via reference to Polar class.
'''

from src.polar import Polar

class Aerofoil:
    """Owner of 2D geometry, referencing a Reynold number -> Polar class mapping"""
    def __init__(self,name:str,polars:list[Polar]):
        self.name = name
        self._polars = polars

    def get_polar(self,re:float) -> Polar:
        for polar in self._polars:
            if polar.reynolds == re:
                # note: if multiple polars found, only one returned. Order based.
                return polar

        raise ValueError(f"No data for Reynolds number: {re}")