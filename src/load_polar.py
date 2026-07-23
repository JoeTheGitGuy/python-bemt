import csv

# [Input]
#   string  name        [1,1] name of aerofoil
#   string  polar_file  [1,1] filepath to polar csv with headers: 'Alpha' 'Cl' 'Cd' 'Cdp' 'Cm'
# [Output]
#   class   LoadPolar   {6,1} name + values from csv for alpha cl cd cdp cm
class LoadPolar:
    def __init__(self,name,polar_file):
        # open and parse NACA polar data
        with open(polar_file) as polar_csv:
            polar_reader = csv.DictReader(polar_csv, delimiter=",")
            alpha=[];cl=[];cd=[];cdp=[];cm=[]
            for r in polar_reader:
                alpha.append(float(r['Alpha']))
                cl.append(float(r['Cl']))
                cd.append(float(r['Cd']))
                cdp.append(float(r['Cdp']))
                cm.append(float(r['Cm']))

        self.name=name
        self.alpha=alpha
        self.cl=cl
        self.cd=cd
        self.cdp=cdp
        self.cm=cm