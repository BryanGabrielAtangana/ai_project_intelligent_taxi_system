class ControlCenter:
    def __init__(self, taxis, taxi_stops):
        self.taxis = taxis  # List of taxis
        self.taxi_stops = taxi_stops  # List of taxi stops
        self.passengers = []  # List of passengers that need to be picked up

    def add_passenger(self, passenger):
        """Add a passenger to the list."""
        self.passengers.append(passenger)

    def get_next_passenger(self):
        """Return the next available passenger."""
        if self.passengers:
            return self.passengers.pop(0)
        return None

    def has_available_passenger(self):
        """Check if there are any passengers to assign."""
        return len(self.passengers) > 0

    def update(self):
        """Update the control center, managing taxis and passengers."""
        for taxi in self.taxis:
            taxi.move()

        # Drop off passenger at destination
            taxi.drop_off_passenger()
