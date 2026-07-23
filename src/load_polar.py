import csv
from src.polar import polar
# [Input]
#   string  name    [1,1] name of aerofoil
#   string  path    [1,1] filepath to polar csv with headers: 'Alpha' 'Cl' 'Cd' 'Cdp' 'Cm'
# [Output]
#   class   polar   {6,1} name + values from csv for alpha cl cd cdp cm
def load_polar(name: str, path: str) -> polar:
    alpha=[]
    cl=[]
    cd=[]
    cdp=[]
    cm=[]
    # open and parse NACA polar data
    with open(path) as polar_csv:
        polar_reader = csv.DictReader(polar_csv, delimiter=",")
        for r in polar_reader:
            alpha.append(float(r['Alpha']))
            cl.append(float(r['Cl']))
            cd.append(float(r['Cd']))
            cdp.append(float(r['Cdp']))
            cm.append(float(r['Cm']))

    return polar(name,alpha,cl,cd,cdp,cm)