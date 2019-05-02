## @ingroup Attributes-Routes
# Route.py

# Created:  April, 2019, M. Dethy

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

from SUAVE.Core import Data

# ----------------------------------------------------------------------
#  Route Data Class
# ----------------------------------------------------------------------

## @ingroup Attributes-Routes
class Route(Data):
    """A basic route.
    
    Assumptions:
    None
    
    Source:
    None
    """
    
    def __defaults__(self):
        """This sets the default values.
    
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
        
        self.tag                        = 'Route'
        self.airports                   = []
        self.distance                   = 0.0
        self.annual_pax_sub_and_super   = 0.0
        self.max_load_factor            = 0.0
        self.flights_per_day            = 0.0
        self.growth_rate                = 0.0
        self.ticket_fare.               = 0.0

    def compute_revenue(self, ratio_pax_super, n_pax)
        total_traffic = n_flights * self.max_load_factor * vehicle.n_pax
        return total_traffic * self.ticket_fare

    def compute_cost(self, ops_cost, compute_mission, n_pax)
        n_flights = self.flights_per_day * ops_cost.operating_days
        fuel_burn, block_time, flight_time = compute_mission(self.distance)

        fuel_cost                = ops_cost.fuel_price * n_flights * fuel_burn
        maintainence_cost        = ops_cost.maintainence_cost * n_flights * flight_time
        pilot_cost               = ops_cost.pilot_cost * n_flights * block_time
        passenger_cost           = ops_cost.passenger_cost * n_flights * self.max_load_factor * n_pax
        airport_cost             = ops_cost.airport_cost * n_flights
        other_labor_cost         = ops_cost.other_labor_cost * n_flights * n_pax * self.distance
        other_operating_cost     = ops_cost.other_operating_cost * n_flights * n_pax * self.distance
        
        return fuel_cost + maintainence_cost + pilot_cost + passenger_cost + airport_cost + other_labor_cost + other_operating_cost
        
    
    def compute_profit(self, ratio_pax_super, ops_cost, compute_mission)
        total_cost = self.compute_cost(ops_cost, compute_mission, n_pax)
        total_revenue = self.compute_revenue(ratio_pax_super, n_pax)
        total_profit = self.total_revenue - self.total_cost
        return total_profit
