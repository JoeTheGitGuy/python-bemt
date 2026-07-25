import csv
from src.polar import Polar
# [Input]
#   string  path    [1,1] filepath to polar csv with headers: 'Alpha' 'Cl' 'Cd' 'Cdp' 'Cm'
# [Output]
#   class   polar   {6,1} name + values from csv for alpha cl cd cdp cm
def load_polar(path: str) -> Polar:
    """Loads a csv of an alpha vs force/moment coefficients into a Polar class"""
    alpha=[]
    cl=[]
    cd=[]
    cdp=[]
    cm=[]
    # open and parse NACA polar data
    with open(path) as polar_csv:
        # extract header info
        header = metadata(csv.reader(polar_csv))

        name = header["Airfoil"]
        reynolds = float(header["Reynolds number"])
        ncrit = int(header["Ncrit"])

        # extract data info
        # reader obj 'polar_csv' has moved over metadata already
        polar_reader = csv.DictReader(polar_csv, delimiter=",")
        for r in polar_reader:
            alpha.append(float(r['Alpha']))
            cl.append(float(r['Cl']))
            cd.append(float(r['Cd']))
            cdp.append(float(r['Cdp']))
            cm.append(float(r['Cm']))

    return Polar(name,reynolds,ncrit,alpha,cl,cd,cdp,cm)

def metadata(file:csv.Reader):
    curr_line = 0
    header = {}    
    for r in file:
        curr_line = curr_line+1
        # skip special case first line
        if curr_line == 1:
            continue
        # check for empty line
        # (expected to be the break between header & dataset)
        if not r:
            break
        # require header to be name-value
        if len(r) != 2:
            raise ValueError(f"Unexpected metadata row: {r}")

        key, value = r[:2]
        header[key] = value
    return header
