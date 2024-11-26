import random
from algorithms.algorithms import a_star
from composants.passenger import Passenger

window_x = 1400
window_y = 740
cell_size = 10

class Taxi:
    def __init__(self, position, destination, obstacles=None, taxi_stops=None):
        self.position = position
        self.destination = destination
        self.obstacles = obstacles if obstacles is not None else []
        self.passenger = None  # Initially, no passenger
        self.path = a_star(tuple(position), tuple(destination), self.obstacles)
        self.taxi_stops = taxi_stops if taxi_stops else []  # Store taxi stops

    def move(self):
        """
        Move towards the destination, avoiding obstacles.
        Pick up a passenger if at the taxi stop.
        """
        if self.passenger is None:
            self.pick_up_passenger()  # Pick up a passenger if available

        if self.path:
            next_pos = self.path[0]
            # Check if next position is safe
            if not any(obstacle.collides_with_point(next_pos) for obstacle in self.obstacles):
                self.position = list(self.path.pop(0))
            else:
                # Recalculate path if blocked
                self.path = a_star(tuple(self.position), tuple(self.destination), self.obstacles)

    def pick_up_passenger(self):
        """
        Check if the taxi is at a taxi stop and pick up a passenger.
        """
        if self.passenger is None:
            # Check if the taxi is at a taxi stop (close enough)
            for stop in self.taxi_stops:
                if self.is_at_taxi_stop(stop):
                    self.passenger = stop.pick_up_passenger()
                    break

    def is_at_taxi_stop(self, stop):
        """
        Check if the taxi is close to a taxi stop.
        """
        return abs(self.position[0] - stop.position[0]) < cell_size and abs(self.position[1] - stop.position[1]) < cell_size

    def drop_off_passenger(self):
        """
        Drop off the passenger at the destination.
        """
        if self.position == self.destination:
            self.passenger = None  # Passenger is dropped off
            self.update_destination()

    def update_destination(self):
        """
        Assign next destination and calculate path avoiding obstacles.
        """
        max_attempts = 100
        attempt = 0
        
        while attempt < max_attempts:
            new_destination = [
                random.randrange(1, (window_x // cell_size)) * cell_size,
                random.randrange(1, (window_y // cell_size)) * cell_size
            ]
            
            # Check if destination is not inside an obstacle
            if not any(obstacle.collides_with_point(new_destination) for obstacle in self.obstacles):
                if new_destination != self.destination:
                    self.destination = new_destination
                    self.path = a_star(tuple(self.position), tuple(self.destination), self.obstacles)
                    if self.path:  # Only accept if a valid path exists
                        break
            
            attempt += 1
