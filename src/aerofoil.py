import csv

class Aerofoil:
    def __init__(self,name,alpha,cl,cd,cdp,cm):
        self.name = name;
        self.alpha_polar = alpha;
        self.cl_polar = cl;
        self.cd_polar = cd;
        self.cdp_polar = cdp;
        self.cm_polar = cm;

    # calculate CL via interpolation for given AoA
    def cl(self,alpha):
        # check alpha in polar range
        if alpha < min(self.alpha_polar) or alpha > max(self.alpha_polar):
            return 0

        # find interpolation bounds
        n = len(self.alpha_polar)-1
        for i in range(n):
            if abs(self.alpha_polar[i] - alpha) < 0.00001:
                return self.cl_polar[i]
            elif (self.alpha_polar[i] > alpha):
                lb_ind = i-1;
                ub_ind = i;
                break

        # interpolate CL
        dalpha  = self.alpha_polar[ub_ind]-self.alpha_polar[lb_ind];
        dcl     = self.cl_polar[ub_ind]-self.cl_polar[lb_ind];

        return self.cl_polar[lb_ind] + (alpha-self.alpha_polar[lb_ind])*(dcl/dalpha);
        
        
        
# open and parse NACA polar data
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
#print(aerofoil1.alpha_polar)
#print(aerofoil1.cl_polar)
#print(aerofoil1.cd_polar)

cl = aerofoil1.cl(11.001)
print(cl)