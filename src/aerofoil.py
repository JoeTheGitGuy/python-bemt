from src.polar import Polar

class Aerofoil:
    """Owner of 2D geometry, referencing a Reynold number -> Polar class mapping"""
    def __init__(self,name:str,polars:list[Polar]):
        self.name = name
        self._polars = polars

    def get_polar(self,re) -> Polar:
        return self._polars[0]
        #re_known = []
        #for i in range(len(self._polars)):
        #    re_known[i] = self._polars[i].reynolds 