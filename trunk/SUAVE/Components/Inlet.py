## @ingroup Components-Inlets
# Inlet.py
# 
# Created:  Apr 2019, M. Dethy

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

import SUAVE
from SUAVE.Core import Data
from SUAVE.Components import Component

# ------------------------------------------------------------
#   Inlet
# ------------------------------------------------------------

## @ingroup Components-Inlet
class Inlet(Component):
    """This class defines the inlet in SUAVE

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
        """This sets the default values of a inlet defined in SUAVE.
    
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

        self.tag             = 'inlet'
        self.mass_properties = Mass_Properties()
        self.origin          = [[0.0,0.0,0.0]]
        
        self.symmetric                 = True
        self.vertical                  = False
        self.t_tail                    = False
        self.taper                     = 0.0
        self.dihedral                  = 0.0
        self.aspect_ratio              = 0.0
        self.thickness_to_chord        = 0.0
        self.span_efficiency           = 0.9
        self.aerodynamic_center        = [0.0,0.0,0.0]
        self.exposed_root_chord_offset = 0.0

        self.spans = Data()
        self.spans.projected = 0.0
        
        self.areas = Data()
        self.areas.reference = 0.0
        self.areas.exposed   = 0.0
        self.areas.affected  = 0.0
        self.areas.wetted    = 0.0

        self.chords = Data()
        self.chords.mean_aerodynamic = 0.0
        self.chords.mean_geometric   = 0.0
        self.chords.root             = 0.0
        self.chords.tip              = 0.0
        
        self.sweeps               = Data()
        self.sweeps.quarter_chord = 0.0
        self.sweeps.leading_edge  = 0.0
        self.sweeps.half_chord    = 0.0        

        self.twists = Data()
        self.twists.root = 0.0
        self.twists.tip  = 0.0

        self.control_surfaces = Data()
        self.flaps = Data()
        self.flaps.chord      = 0.0
        self.flaps.angle      = 0.0
        self.flaps.span_start = 0.0
        self.flaps.span_end   = 0.0
        self.flaps.type       = None
        self.flaps.area       = 0.0

        self.slats = Data()
        self.slats.chord      = 0.0
        self.slats.angle      = 0.0
        self.slats.span_start = 0.0
        self.slats.span_end   = 0.0
        self.slats.type       = None

        self.high_lift     = False
        self.high_mach     = False
        self.vortex_lift   = False

        self.transition_x_upper = 0.0
        self.transition_x_lower = 0.0
        
        self.Airfoil            = Data()
        self.Segments           = SUAVE.Core.ContainerOrdered()
        self.Fuel_Tanks         = SUAVE.Core.Container()