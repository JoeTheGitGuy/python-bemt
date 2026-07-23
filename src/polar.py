# [Input]
#   string  name    [1,1] name of aerofoil
#   string  alpha   [1,1] angle of attack polar
#   string  cl      [1,1] lift coeff polar
#   string  cd      [1,1] drag coeff polar
#   string  cdp     [1,1] ? coeff polar
#   string  cm      [1,1] moment coeff polar
class Polar:
    def __init__(self,name:str,alpha:float,cl:float,cd:float,cdp:float,cm:float):
        self.name = name
        self.alpha = alpha
        self.cl = cl
        self.cd = cd
        self.cdp = cdp
        self.cm = cm

    # calculate CL via interpolation for given AoA
    def coeff_calc(self,coeff:str,curr_alpha:float):

        # get specified polar data:
        try:
            coeff_polar = getattr(self,coeff)
        except:
            raise Exception("Error: argument 'coeff' invalid option of ['cl' 'cd' 'cdp' 'cm'].")

        # check alpha in polar range
        if curr_alpha < min(self.alpha) or curr_alpha > max(self.alpha):
            raise Exception("Error: argument 'alpha' out of polar bounds.")

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