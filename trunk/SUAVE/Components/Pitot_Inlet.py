## @ingroup Components-Inlets
# Pitot_Inlet.py
# 
# Created:  Apr 2019, M. Dethy

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

import SUAVE
from SUAVE.Core import Data
from SUAVE.Components import Component

# ------------------------------------------------------------
#   Pitot Inlet
# ------------------------------------------------------------

## @ingroup Components-Pitot Inlet
class Pitot_Inlet(Component):
    """This class defines the pitot inlet in SUAVE

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
        """This sets the default values of a pitot inlet defined in SUAVE.
    
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

        self.tag                       = 'pitot_inlet'
        self.mass_properties           = Mass_Properties()
        self.origin                    = [[0.0,0.0,0.0]]
        self.aerodynamic_center        = [0.0,0.0,0.0]

        self.areas = Data()
        self.areas.front_projected     = 0.0
        self.areas.side_projected      = 0.0
        self.areas.wetted              = 0.0

        self.diameter                  = 0.0

        self.lengths = Data()
        self.lengths.total             = 0.0
        self.lengths.entrance          = 0.0

