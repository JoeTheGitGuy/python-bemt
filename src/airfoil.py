import csv

class Aerofoil:
    def __init__(self,name,alpha,cl,cd,cdp,cm):
        self.name = name;
        self.alpha = alpha;
        self.cl = cl;
        self.cd = cd;
        self.cdp = cdp;
        self.cm = cm;
        

with open("data/xf-naca2412-il-100000-n5.csv") as polar_csv:
    polar_reader = csv.DictReader(polar_csv, delimiter=",");
    alpha=[];cl=[];cd=[];cdp=[];cm=[];
    for r in polar_reader:
        alpha.append(float(r['Alpha']));
        cl.append(float(r['Cl']));
        cd.append(float(r['Cd']));
        cdp.append(float(r['Cdp']));
        cm.append(float(r['Cm']));

aerofoil1 = Aerofoil("naca_2412",alpha,cl,cd,cdp,cm);

#print(aerofoil1.name)
print(aerofoil1.alpha)
#print(aerofoil1.cl)
#print(aerofoil1.cd)