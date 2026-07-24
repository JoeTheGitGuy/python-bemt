# [Input]
#   string  name    [1,1] name of aerofoil
#   string  alpha   [1,1] angle of attack polar
#   string  cl      [1,1] lift coeff polar
#   string  cd      [1,1] drag coeff polar
#   string  cdp     [1,1] ? coeff polar
#   string  cm      [1,1] moment coeff polar
class Polar:
    def __init__(self,name:str,alpha:float,cl:float,cd:float,cdp:float,cm:float):
        """Owns aerofoil data for alpha vs force/moment coefficient lookup/interpolation"""
        self.name = name
        self.alpha = alpha
        self.cl = cl
        self.cd = cd
        self.cdp = cdp
        self.cm = cm

    def coeff_calc(self,coeff:str,curr_alpha:float):
        """calculate CL via interpolation for given AoA"""
        # get specified polar data:
        try:
            coeff_polar = getattr(self,coeff)
        except AttributeError:
            raise AttributeError("Error: argument 'coeff' set to invalid option '%s'.\nValid options: ['cl' 'cd' 'cdp' 'cm']." % coeff)

        # check alpha in polar range
        if curr_alpha < min(self.alpha) or curr_alpha > max(self.alpha):
            raise ValueError("Error: argument 'curr_alpha=%.2f' out of polar bounds." % curr_alpha)

        # find interpolation bounds
        n = len(self.alpha)-1
        for i in range(n):
            if abs(self.alpha[i] - curr_alpha) < 0.00001:
                return coeff_polar[i]
            elif (self.alpha[i] > curr_alpha):
                lb_ind = i-1
                ub_ind = i
                break

        # interpolate CL
        dalpha  = self.alpha[ub_ind]-self.alpha[lb_ind]
        dcl     = coeff_polar[ub_ind]-coeff_polar[lb_ind]

        return coeff_polar[lb_ind] + (curr_alpha-self.alpha[lb_ind])*(dcl/dalpha)