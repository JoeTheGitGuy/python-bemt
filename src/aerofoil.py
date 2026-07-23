class Aerofoil:
    def __init__(self,polar):
        self.name = polar.name;
        self.alpha_polar = polar.alpha;
        self.cl_polar = polar.cl;
        self.cd_polar = polar.cd;
        self.cdp_polar = polar.cdp;
        self.cm_polar = polar.cm;

    # calculate CL via interpolation for given AoA
    def cl(self,alpha):
        # check alpha in polar range
        if alpha < min(self.alpha_polar) or alpha > max(self.alpha_polar):
            raise Exception("Error: argument 'alpha' out of polar bounds.")

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