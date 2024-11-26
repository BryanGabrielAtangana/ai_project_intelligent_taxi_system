"""composants.taxi.py"""
import random
from ai_project.algorithms import a_star

window_x = 1400
window_y = 740
cell_size = 10

class Taxi:
    def __init__(self, position, destination, obstacles=None):
        self.position = position
        self.destination = destination
        self.obstacles = obstacles if obstacles is not None else []
        self.path = a_star(tuple(position), tuple(destination), self.obstacles)

    def move(self):
        """
        Move towards the destination, avoiding obstacles
        """
        if self.path:
            next_pos = self.path[0]
            # Check if next position is safe
            if not any(obstacle.collides_with_point(next_pos) for obstacle in self.obstacles):
                self.position = list(self.path.pop(0))
            else:
                # Recalculate path if blocked
                self.path = a_star(tuple(self.position), tuple(self.destination), self.obstacles)

    def update_destination(self):
        """
        Assign next destination and calculate path avoiding obstacles
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