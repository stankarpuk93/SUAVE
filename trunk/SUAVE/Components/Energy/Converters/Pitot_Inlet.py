## @ingroup Components-Energy-Converters
# Generic_Inlet.py
#
# Created:  May 2019, M. Dethy

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

import SUAVE

# python imports
from warnings import warn

# package imports
import numpy as np

from SUAVE.Components.Energy.Energy_Component import Energy_Component
from SUAVE.Methods.Aerodynamics.Common.Gas_Dynamics import Oblique_Shock, Isentropic

# ----------------------------------------------------------------------
#  Generic Inlet Component
# ----------------------------------------------------------------------
## @ingroup Components-Energy-Converters
class Pitot_Inlet(Energy_Component):
    """This is a pitot inlet component intended for use in compression.
    Calling this class calls the compute function.

    Source:
    https://web.stanford.edu/~cantwell/AA283_Course_Material/AA283_Course_Notes/
    """

    def __defaults__(self):
        """This sets the default values for the component to function.

        Assumptions:
        None

        Source:
        N/A

        Inputs:
        None

        Outputs:
        None

        Properties Used:
        None
        """
        # setting the default values
        self.tag = 'pitot_inlet'
        self.A0                              = 0.0
        self.A_capture                       = 0.0
        self.A_engineface                    = 0.0
        self.inputs.stagnation_temperature   = np.array([0.0])
        self.inputs.stagnation_pressure      = np.array([0.0])
        self.outputs.stagnation_temperature  = np.array([0.0])
        self.outputs.stagnation_pressure     = np.array([0.0])
        self.outputs.stagnation_enthalpy     = np.array([0.0])

    def compute(self):
        """ This computes the output values from the input values according to
        equations from the source.

        Assumptions:
        Constant polytropic efficiency and pressure ratio
        Adiabatic

        Source:
        https://web.stanford.edu/~cantwell/AA283_Course_Material/AA283_Course_Notes/

        Inputs:
        conditions.freestream.
          isentropic_expansion_factor         [-]
          specific_heat_at_constant_pressure  [J/(kg K)]
          pressure                            [Pa]
          gas_specific_constant               [J/(kg K)]
        self.inputs.
          stagnation_temperature              [K]
          stagnation_pressure                 [Pa]

        Outputs:
        self.outputs.
          stagnation_temperature              [K]
          stagnation_pressure                 [Pa]
          stagnation_enthalpy                 [J/kg]
          mach_number                         [-]
          static_temperature                  [K]
          static_enthalpy                     [J/kg]
          velocity                            [m/s]

        Properties Used:
        self.
          pressure_ratio                      [-]
          polytropic_efficiency               [-]
          pressure_recovery                   [-]
        """

        # unpack from conditions
        gamma = 1.4#onditions.freestream.isentropic_expansion_factor
        Cp = 1004.5  #conditions.freestream.specific_heat_at_constant_pressure
        Po = 101325 #conditions.freestream.pressure
        Mo = np.array([0.1, 1.3, 0.7])#conditions.freestream.mach_number
        R = 287 #conditions.freestream.gas_specific_constant

        # unpack from inpust
        Tt_in = self.inputs.stagnation_temperature
        Pt_in = self.inputs.stagnation_pressure

        # unpack from self
        A0 = self.A0
        AC = self.A_capture
        AE = self.A_engineface

        # First evaluate whether it is possible that there are shocks for any of the subsonic cases
        f_Mo            = Isentropic.isentropic_relations(Mo, gamma)[-1]
        f_Me_isentropic = (f_Mo * A0)/AE
        i_sub           = np.bitwise_and(f_Me_isentropic <= 1.0, f_Mo <= 1.0)
        i_sup           = (f_Me_isentropic > 1.0)
        print(i_sub)
        print(i_sup)
        
        
        # This 
        if len(Pt_in) == 1:
            Pt_in = Pt_in[0]*np.ones_like(Mo)
        if len(Tt_in) == 1:
            Tt_in = Tt_in[0]*np.ones_like(Mo)
        # initializing the arrays
        Tt_out  = Tt_in
        ht_out  = Cp*Tt_in
        Pt_out  = np.ones_like(Pt_in)
        Mach    = np.ones_like(Pt_in)
        T_out   = np.ones_like(Pt_in)
        f_Me    = np.ones_like(Pt_in)

        # Conservation of mass properties to evaluate subsonic case
        Pt_out[i_sub]   = Pt_in[i_sub]
        f_Me[i_sub]     = f_Me_isentropic[i_sub]
        Mach[i_sub]     = Isentropic.get_m(f_Me[i_sub], gamma, 1)
        T_out[i_sub]    = Isentropic.isentropic_relations(Mach[i_sub], gamma)[0]*Tt_out[i_sub]

        # Analysis of shocks for the supersonic case
        Mc      = np.ones_like(Pt_in)
        Pr_c    = np.ones_like(Pt_in)
        Tr_c    = np.ones_like(Pt_in)
        Ptr_c   = np.ones_like(Pt_in)
        f_Mc    = np.ones_like(Pt_in)
        
        Mc[i_sup], Pr_c[i_sup], Tr_c[i_sup], Ptr_c[i_sup] = Oblique_Shock.oblique_shock_relations(Mo[i_sup],gamma,0,90)
        Pt_out[i_sup] = Ptr_c[i_sup]*Pt_in[i_sup]
        f_Mc[i_sup] = Isentropic.isentropic_relations(Mc[i_sup], gamma)[-1]
        f_Me[i_sup] = f_Mc[i_sup]*AC/AE
        
        Mach[i_sup] = Isentropic.get_m(f_Me[i_sup], gamma, 1)
        T_out[i_sup] = Isentropic.isentropic_relations(Mach[i_sup], gamma)[0]*Tt_out[i_sup]
        
        # -- Compute exit velocity and enthalpy
        h_out = Cp * T_out
        u_out = np.sqrt(2. * (ht_out - h_out))

        # pack computed quantities into outputs
        self.outputs.stagnation_temperature = Tt_out
        self.outputs.stagnation_pressure = Pt_out
        self.outputs.stagnation_enthalpy = ht_out
        self.outputs.mach_number = Mach
        self.outputs.static_temperature = T_out
        self.outputs.static_enthalpy = h_out
        self.outputs.velocity = u_out
    
    
if __name__ == "__main__":
    inlet_nozzle = Pitot_Inlet()
    inlet_nozzle.tag = 'inlet nozzle'
    inlet_nozzle.A0 = np.array([2, 3, 0.5])
    inlet_nozzle.A_capture = 1.0
    inlet_nozzle.A_engineface = 2.0
    inlet_nozzle.compute()
    inlet_nozzle.inputs.stagnation_temperature = 500
    inlet_nozzle.inputs.stagnation_pressure = 200000
    

    
