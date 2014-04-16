
# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

from SUAVE.Structure import Data

# ----------------------------------------------------------------------
#  Runway
# ----------------------------------------------------------------------
    
class Runway(Data):
    """ SUAVE.Attributes.Airport.Runway
    """
    def __defaults__(self):
        self.tag = 'Runway'