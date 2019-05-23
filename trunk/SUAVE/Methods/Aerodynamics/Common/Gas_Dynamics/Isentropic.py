## @ingroup Methods-Aerodynamics-Common-Gas_Dynamics
# isentropic.py
#
# Created:  May 2019, M. Dethy
# Modified:  
#           

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

import numpy as np
from sympy import Symbol
from sympy.solvers import solve
# ----------------------------------------------------------------------
#  Isentropic Flow Relations
# ----------------------------------------------------------------------

## @ingroup Methods-Aerodynamics-Common-Gas_Dynamics
def isentropic_relations(M,gamma):
    """Computes isentropic flow quantites

    Assumptions:
    None

    Source:
    https://www.grc.nasa.gov/www/k-12/airplane/isentrop.html

    
    Inputs:
    Mach, M                              [-]
    Isentropic Expansion Factor, gamma   [-]

    Outputs:
    Temperature Ratio, T_o_Tt            [-]
    Pressure Ratio, P_o_Pt               [-]
    Density ratio, rho_o_rhot            [-]
    Area ratio, A_o_Astar                [-]
    Area-mach relation, f_m              [-]

    
    Properties Used:
    N/A
    """

    # Standard isentropic flow equations
    T_o_Tt       = (1 + (gamma - 1)/2 * M**2) ** (-1)
    P_o_Pt       = (1 + (gamma - 1)/2 * M**2) ** (-gamma/(gamma-1))
    rho_o_rhot   = (1 + (gamma - 1)/2 * M**2) ** (-1/(gamma-1))
    A_o_Astar    = 1/M * ((gamma+1)/2)**(-(gamma+1)/(2*(gamma-1))) * (1 + (gamma - 1)/2 * M**2) ** ((gamma+1)/(2*(gamma-1)))
    f_m          = 1/A_o_Astar

    return T_o_Tt, P_o_Pt, rho_o_rhot, A_o_Astar, f_m

def get_m(f_m, gamma, subsonic_flag):
    """The mach number from a given area-mach relation value

    Assumptions:
    None

    Source:
    Chapter 10 of:
    https://web.stanford.edu/~cantwell/AA210A_Course_Material/AA210A_Course_Notes/

    
    Inputs:
    Area-mach relation, f_m                             [-]
    Isentropic Expansion Factor, gamma                  [-]
    subsonic_flag (=1 if subsonic mach, = 0 otherwise)  [-]

    Outputs:
    Mach, M                                             [-]

    
    Properties Used:
    N/A
    """

    # Symbolically solve for mach number
    M = Symbol("M",real=True)
    A_o_Astar    = 1/M * ((gamma+1)/2)**(-(gamma+1)/(2*(gamma-1))) * (1 + (gamma - 1)/2 * M**2) ** ((gamma+1)/(2*(gamma-1)))
    M = np.array(solve(A_o_Astar**(-1) - f_m, M))
    
    if subsonic_flag == 1:
        return float(M[M <= 1])
    else:
        return float(M[M >= 1])

if __name__ == "__main__":
    gnew = get_m(0.25, 1.4, 1)
    T_o_Tt, P_o_Pt, rho_o_rhot, A_o_Astar, f_m = isentropic_relations(0.8, 1.4)
    





