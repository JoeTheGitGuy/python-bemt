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
        header_data = metadata(csv.reader(polar_csv))
        header = header_data[0]
        header_end_line = header_data[1]

        name = header["Airfoil"]
        reynolds = float(header["Reynolds number"])
        ncrit = int(header["Ncrit"])

        # extract data info
        polar_reader = csv.DictReader(polar_csv, delimiter=",")
        curr_line = 0
        for r in polar_reader:
            curr_line = curr_line+1
            # skip until header end
            if curr_line <= header_end_line:
                continue
            alpha.append(float(r['Alpha']))
            cl.append(float(r['Cl']))
            cd.append(float(r['Cd']))
            cdp.append(float(r['Cdp']))
            cm.append(float(r['Cm']))

    return Polar(name,reynolds,ncrit,alpha,cl,cd,cdp,cm)

def metadata(file:csv.Reader):
    curr_line = 0
    header_end_line = 1
    header = {}    
    for r in file:
        curr_line = curr_line+1
        # skip special case first line
        if curr_line == 1:
            continue
        # mark end of header
        if not r:
            header_end_line = curr_line
            break
        # require header to be name-value
        if len(r) != 2:
            raise ValueError(f"Unexpected metadata row: {r}")

        key, value = r[:2]
        header[key] = value
        curr_line = curr_line+1
    return header,header_end_line
