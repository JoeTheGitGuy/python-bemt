class Environment:
    def __init__(self,g:float,rho:float,gamma:float,mu0:float,T0:float,u_inf:float,z:float):
        self.g = g # gravity
        self.rho = rho # density
        self.gamma = gamma
        self.mu0 = mu0 # dynamic viscocity @ sea lvl reference
        self.T0 = T0
        self.u_inf = u_inf # upstream forward velocity
        self.z = z # altitude

    def T_inf(self):
        # temp lookup as function of altitude
        return self.T0 - (0.0065 * self.z)

    def T(self,V):
        # assume isentropic
        #T_calc = self.T_inf \
        #     + (self.T_inf*0.5*(self.gamma)*(self.M**2))
        #return T_calc
        cp = (self.gamma * self.R) / (self.gamma - 1)
        return self.T0 - (V**2 / (2 * cp))

    def mu(self):
        # https://www.grc.nasa.gov/www/k-12/airplane/viscosity.html
        # mu = mu0 * ((T / T0)^1.5) * ((T0 + 198.72) / (T + 198.72))
        mu_calc = self.mu0 * ((self.T / T0)**1.5) \
            * ((self.T0 + 198.72) / (self.T + 198.72))
        return mu_calc