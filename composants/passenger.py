class Passenger:
    def __init__(self, origin, destination):
        """
        Initialize a passenger with a pickup and drop-off location.
        Args:
            origin: List [x, y] of pickup location.
            destination: List [x, y] of drop-off location.
        """
        self.origin = origin
        self.destination = destination
        self.in_taxi = False

    def pickup(self):
        """Mark the passenger as picked up."""
        self.in_taxi = True

    def drop_off(self):
        """Mark the passenger as dropped off."""
        self.in_taxi = False
