## @ingroup Components-Inlets
# Axisym_Inlet.py
# 
# Created:  Apr 2019, M. Dethy

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

import SUAVE
from SUAVE.Core import Data
from SUAVE.Components import Component

# ------------------------------------------------------------
#   Axisymmetric Inlet
# ------------------------------------------------------------

## @ingroup Components-Axisymmetric Inlet
class 2D_Inlet(Component):
    """This class defines the axisymmetric inlet in SUAVE

    Assumptions:
    None

    Source:
    N/A

    Inputs:
    None

    Outputs:
    None

    Properties Used:
    N/A
    """      
    def __defaults__(self):
        """This sets the default values of a axisymmetric inlet defined in SUAVE.
    
        Assumptions:
        None

        Source:
        N/A

        Inputs:
        None

        Outputs:
        None

        Properties Used:
        N/A
        """         

        self.tag                       = '2d_inlet'
        self.mass_properties           = Mass_Properties()
        self.origin                    = [[0.0,0.0,0.0]]
        self.aerodynamic_center        = [0.0,0.0,0.0]

        self.areas = Data()
        self.areas.front_projected     = 0.0
        self.areas.side_projected      = 0.0
        self.areas.wetted              = 0.0

        self.angle                     = 0.0

        self.diameters = Data()
        self.diameters.start           = 0.0
        self.diameters.max             = 0.0

        self.lengths = Data()
        self.lengths.total             = 0.0
        self.lengths.LC                = 0.0
        self.lengths.CE                = 0.0
