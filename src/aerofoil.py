from src.polar import Polar

class Aerofoil:
    """Owner of 2D geometry, referencing a Reynold number -> Polar class mapping"""
    def __init__(self,name:str,polars:list[Polar]):
        self.name = name
        self._polars = polars

    def get_polar(self,re) -> Polar:
        # get all list of polars' reynolds numbers
        re_sets = [obj.reynolds for obj in self._polars]
        if re not in re_sets:
            raise ValueError(f"No data for Reynolds number: {re}")
        
        # index polar list by reynold number match & return
        re_polar = self._polars[re_sets == re]
        return re_polar