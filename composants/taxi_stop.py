class TaxiStop:
    def __init__(self, position):
        """
        Initialize a taxi stop with a location and a passenger queue.
        Args:
            position: List [x, y] of the stop's coordinates.
        """
        self.position = position
        self.passenger_queue = []

    def add_passenger(self, passenger):
        """Add a passenger to the queue."""
        self.passenger_queue.append(passenger)

    def remove_passenger(self):
        """Remove and return the first passenger in the queue."""
        return self.passenger_queue.pop(0) if self.passenger_queue else None

    def has_passengers(self):
        """Check if the stop has waiting passengers."""
        return bool(self.passenger_queue)
