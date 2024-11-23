class CentraleTaxi:
    def __init__(self, taxis, stops):
        self.taxis = taxis  
        self.stops = stops 
        self.waiting_passengers = []

    def assign_passenger_to_taxi(self, passenger):
        """Assign the nearest available taxi to a waiting passenger"""
        available_taxis = [taxi for taxi in self.taxis if taxi.status == "free"]
        if available_taxis:
            nearest_taxi = min(available_taxis, 
                               key=lambda t: abs(t.position[0] - passenger.origin[0]) + 
                                             abs(t.position[1] - passenger.origin[1]))
            nearest_taxi.destination = passenger.origin
            nearest_taxi.status = "occupied"
            nearest_taxi.passengers.append(passenger)

    def manage_taxi_recharging(self):
        """Send taxis to the nearest charging stop when needed"""
        for taxi in self.taxis:
            if taxi.battery < 20 and taxi.status == "free":
                nearest_stop = min(self.stops, 
                                   key=lambda s: abs(taxi.position[0] - s.position[0]) + 
                                                 abs(taxi.position[1] - s.position[1]))
                if nearest_stop.can_accept_taxi():
                    taxi.destination = nearest_stop.position
                    taxi.status = "recharging"
