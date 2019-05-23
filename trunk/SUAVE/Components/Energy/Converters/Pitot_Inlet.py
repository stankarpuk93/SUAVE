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

    Assumptions:
    Pressure ratio and efficiency do not change with varying conditions.
    Subsonic or choked output.

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
        self.polytropic_efficiency           = 1.0
        self.A0                              = 0.0
        self.AC                              = 0.0
        self.A1                              = 0.0
        self.inputs.stagnation_temperature   = 0.0
        self.inputs.stagnation_pressure      = 0.0
        self.outputs.stagnation_temperature  = 0.0
        self.outputs.stagnation_pressure     = 0.0
        self.outputs.stagnation_enthalpy     = 0.0

    def compute(self, conditions):
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
        gamma = conditions.freestream.isentropic_expansion_factor
        Cp = conditions.freestream.specific_heat_at_constant_pressure
        Po = conditions.freestream.pressure
        Mo = conditions.freestream.mach_number
        R = conditions.freestream.gas_specific_constant

        # unpack from inpust
        Tt_in = self.inputs.stagnation_temperature
        Pt_in = self.inputs.stagnation_pressure

        # unpack from self
        A0 = self.A0
        AC = self.AC
        A1 = self.A1

        f_Mo = Isentropic.isentropic_relations(Mo, gamma)[-1]

        # First evaluate whether it is possible that there are shocks for any of the subsonic cases
        i_sub = f_Mo*A0/AE <= 1.0
        i_sup = f_Mo*A0/AE > 1.0

        # initializing the arrays
        Mach = np.ones_like(Pt_in)
        T_out = np.ones_like(Pt_in)
        Mo = Mo * np.ones_like(Pt_in)
        Pt_out = np.ones_like(Pt_in)
        P_out = np.ones_like(Pt_in)




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

    __call__ = compute
